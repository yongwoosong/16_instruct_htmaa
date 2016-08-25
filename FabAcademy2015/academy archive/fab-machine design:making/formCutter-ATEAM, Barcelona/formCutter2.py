#!/usr/bin/python
# coding: UTF-8
# the part of converter from g code to the stepper format was written by Taichi Hisatsune.
# Also the GUI was designed and programmed by Taichi
# 25/05/2015
#------IMPORTS-------
from pygestalt import nodes
from pygestalt import interfaces
from pygestalt import machines
from pygestalt import functions
from pygestalt.machines import elements
from pygestalt.machines import kinematics
from pygestalt.machines import state
from pygestalt.utilities import notice
from pygestalt.publish import rpc	#remote procedure call dispatcher
import time
import io
import csv
import wx


#------VIRTUAL MACHINE------
class virtualMachine(machines.virtualMachine):
	
	def initInterfaces(self):
		if self.providedInterface: self.fabnet = self.providedInterface		#providedInterface is defined in the virtualMachine class.
		else: self.fabnet = interfaces.gestaltInterface('FABNET', interfaces.serialInterface(baudRate = 115200, interfaceType = 'ftdi', portName = '/dev/tty.usbserial-FTXW4FTE'))
		
	def initControllers(self):
		self.xAxisNode = nodes.networkedGestaltNode('X Axis', self.fabnet, filename = '086-005a.py', persistence = self.persistence)
		self.yAxisNode = nodes.networkedGestaltNode('Y Axis', self.fabnet, filename = '086-005a.py', persistence = self.persistence)

		self.xyNode = nodes.compoundNode(self.xAxisNode, self.yAxisNode)

	def initCoordinates(self):
		self.position = state.coordinate(['mm', 'mm'])
	
	def initKinematics(self):
		self.xAxis = elements.elementChain.forward([elements.microstep.forward(4), elements.stepper.forward(1.8), elements.leadscrew.forward(8), elements.invert.forward(True)])
		self.yAxis = elements.elementChain.forward([elements.microstep.forward(4), elements.stepper.forward(1.8), elements.leadscrew.forward(8), elements.invert.forward(False)])		
		self.stageKinematics = kinematics.direct(2)	#direct drive on all axes
	
	def initFunctions(self):
		self.move = functions.move(virtualMachine = self, virtualNode = self.xyNode, axes = [self.xAxis, self.yAxis], kinematics = self.stageKinematics, machinePosition = self.position,planner = 'null')
		self.jog = functions.jog(self.move)	#an incremental wrapper for the move function
		pass
		
	def initLast(self):
		#self.machineControl.setMotorCurrents(aCurrent = 0.8, bCurrent = 0.8, cCurrent = 0.8)
		#self.xNode.setVelocityRequest(0)	#clear velocity on nodes. Eventually this will be put in the motion planner on initialization to match state.
		pass
	
	def publish(self):
		#self.publisher.addNodes(self.machineControl)
		pass
	
	def getPosition(self):
		return {'position':self.position.future()}
	
	def setPosition(self, position  = [None]):
		self.position.future.set(position)

	def setSpindleSpeed(self, speedFraction):
		#self.machineControl.pwmRequest(speedFraction)
		pass

class FoamCutter(wx.Frame):
	pathName = ''
	listXY = []
	listXonly = []
	booleanListXY = [] # for detecting painting it or not
	maxX = 0
	maxY = 0
	scale = 100
	isFirst = False;
	def __init__(self,parent,title):
		wx.Frame.__init__(
			self,
			parent,
			title=title,
			size=(500,600))
		#panel=wx.Panel(self)
		panel = wx.Panel(self,wx.ID_ANY,pos=(0,0),size=(500,70))
		#menu : just for credit and exit
		menu_file = wx.Menu()
		menu_file.Append(1,"Credits")
		menu_file.AppendSeparator()
		menu_file.Append(2,"Load G code")
		menu_file.Append(3,"Calcuration")
		menu_file.Append(4,"Start cutting")
		menu_bar = wx.MenuBar()
		menu_bar.Append(menu_file,"FormCutter")
		self.SetMenuBar(menu_bar)
		self.Bind(wx.EVT_MENU, self.showCredits, id=1)
		self.Bind(wx.EVT_MENU, self.loadbutton, id=2)
		self.Bind(wx.EVT_MENU, self.calcbutton, id=3)
		self.Bind(wx.EVT_MENU, self.startbutton, id=4)

		button2=wx.Button(panel,label="load G code",pos=(50,0),size=(100,60))
		button3=wx.Button(panel,label="Calculation",pos=(350,0),size=(100,60))
		self.text_scale = wx.TextCtrl(panel,wx.ID_ANY,"100",pos =(250,28),size=(60,20))
		self.s_text_2 = wx.StaticText(panel,wx.ID_ANY,"set scale",pos=(250,5))
		self.Bind(wx.EVT_BUTTON, self.loadbutton, button2)
		self.Bind(wx.EVT_BUTTON, self.calcbutton, button3)

		#drawing panel
		self.panel2 = wx.Panel(self,wx.ID_ANY,pos=(0,70),size=(500,300))
		self.panel2.SetBackgroundColour('WHITE')
		self.panel2.Bind(wx.EVT_PAINT,self.OnPaint)

		#text panel
		self.panel3 = wx.Panel(self,wx.ID_ANY,pos=(0,370),size=(500,150))
		button4=wx.Button(self.panel3,label="Start",pos=(50,100),size=(60,60))
		button5=wx.Button(self.panel3,label="Home",pos=(200,50),size=(60,60))
		button6=wx.Button(self.panel3,label="Go to first point",pos=(50,50),size=(120,60))

		self.text_speed = wx.TextCtrl(self.panel3,wx.ID_ANY,"8",pos =(350,28),size=(60,20))
		self.s_text_4 = wx.StaticText(self.panel3,wx.ID_ANY,"set Speed",pos=(350,0))

		self.Bind(wx.EVT_BUTTON, self.startbutton, button4)
		self.Bind(wx.EVT_BUTTON, self.homebutton, button5)
		self.Bind(wx.EVT_BUTTON, self.gotofirstbutton, button6)

		self.s_text_1 = wx.StaticText(self.panel3,wx.ID_ANY,"             Cutting sizes  X: %s mm Y: %s mm (maybe)" % (self.maxX,self.maxY))
		self.s_text_3 = wx.StaticText(self.panel3,wx.ID_ANY,"             Control machine",pos=(0,50))

		self.layout3 = wx.BoxSizer(wx.HORIZONTAL)
		self.layout3.Add(self.s_text_1)

		self.panel3.SetSizer(self.layout3)

		self.Fit()

	def showCredits(self,event):
		wx.MessageBox('Form Cutter by Mery, Lina, Jani and Taichi. FabAcademy 2015 16th week assignmnet @ FabLab Barcelona','Credits')

	def loadbutton(self,event):
		self.dirname = ''
		filename = wx.FileDialog(self,"select G code .nc", self.dirname,
		 						"","*.nc",wx.OPEN)
		if filename.ShowModal() == wx.ID_OK:
			file_name = filename.GetFilename()
			dir_name = filename.GetDirectory()
		filename.Destroy()
		self.pathName = 'codes/' + file_name

	def calcbutton(self,event):
		#get Scale value from input
		self.scale = int(self.text_scale.GetValue())

		f = open(self.pathName,'rb')
		data1 = csv.reader(f)  #
		isAfterG0 = 0
		list1 = []
		for row in data1:
			for row2 in row:
				if row2.startswith('G00'):
					isAfterG0 = 1
				if row2.startswith('G01X'):
					if isAfterG0 == 0:
						list1.append(row2)
					isAfterG0 = 0

		#print list1
		# 今list1は G01X~~Y~~Z~~のリスト構造
		listX = []
		listY = []
		for rowDataX in list1:
			listX.append(int(float(rowDataX[4:10])*self.scale))
		for rowDataY in list1:
			listY.append(int(float(rowDataY[11:17])*self.scale))

		
		count = 0
		for rowX in listX:
			smXY = []
			smXY.append(rowX)
			#for painting
			for n in range(len(listX)):
				self.booleanListXY.append(0)
			#to here

			smXY.append(listY[count])

			#for finding max vaules
			if self.maxX < rowX:
				self.maxX = rowX
			if self.maxY < listY[count]:
				self.maxY = listY[count]
			self.s_text_1.SetLabel("Cutting sizes  X: %s mm Y: %s mm (should not over 270mm)" % (self.maxX * 13/10,self.maxY * 13/10))
			#

			count = count + 1
			#print smXY
			self.listXY.append(smXY)
		lastXY = [0,0]
		#self.listXY.append(lastXY)
		print self.listXY
		self.Refresh()


	def startbutton(self,event):
		if self.isFirst == False:
			self.definemachine()
		moves = self.listXY # for XY nodes
		#move = self.listXonly # for only X node
		countMove = 0
		for move in moves:
				self.stages.move(move, 0)

				self.booleanListXY[countMove] = 1 # for drawing
				countMove = countMove + 1 # for drawing
				self.status = self.stages.xAxisNode.spinStatusRequest()
				self.Refresh()
				# This checks to see if the move is done.
				while self.status['stepsRemaining'] > 0:
					time.sleep(0.001)
					self.status = self.stages.xAxisNode.spinStatusRequest()	
					#self.Refresh()
		print "Finish cutting"

	def homebutton(self,event):
		if self.isFirst == False:
			self.definemachine()
		moves = [[0,0]]
		for move in moves:
				self.stages.move(move, 0)
				self.status = self.stages.xAxisNode.spinStatusRequest()
				while self.status['stepsRemaining'] > 0:
					time.sleep(0.001)
					self.status = self.stages.xAxisNode.spinStatusRequest()

	def gotofirstbutton(self,event):
		if self.isFirst == False:
			self.definemachine()
		firstlistXY = []
		firstlistXY.append(self.listXY[0])
		moves = firstlistXY
		for move in moves:
				self.stages.move(move, 0)
				self.status = self.stages.xAxisNode.spinStatusRequest()
				while self.status['stepsRemaining'] > 0:
					time.sleep(0.001)
					self.status = self.stages.xAxisNode.spinStatusRequest()
		#self.isFirst = True

	def definemachine(self):
		self.machinespeed = int(self.text_speed.GetValue())
		self.stages = virtualMachine(persistenceFile = "test.vmp")
		self.stages.xyNode.setVelocityRequest(self.machinespeed)	
		self.isFirst = True

	def OnPaint(self,event):
		dc = wx.PaintDC(self.panel2)
		dc.SetBackground(wx.Brush("WHITE"))
		dc.Clear()
		dc.SetPen(wx.Pen('GREEN'))
		dc.DrawLine(10,10,260,10)
		dc.DrawLine(10,10,10,260)
		dc.DrawLine(260,10,260,260)
		dc.DrawLine(10,260,260,260)
		dc.SetPen(wx.Pen('RED'))
		dc.DrawLine(10,10,50,10)
		dc.SetPen(wx.Pen('BLUE'))
		dc.DrawLine(10,10,10,50)

		dc.SetPen(wx.Pen('BLACK'))
		# drawing
		#test

		dots = self.listXY
		x1 = 0
		y1 = 0
		num = 0
		offset = 10
		for dot in dots:
			i = 0
			x2 = x1
			y2 = y1
			for value in dot:
				if i == 0:
					x1 = value
					i = i+1
				if i == 1:
					y1 = value
			if self.booleanListXY[num] == 0:
				dc.SetPen(wx.Pen('BLACK'))
				dc.DrawLine(x1+offset,y1+offset,x2+offset,y2+offset)
			if self.booleanListXY[num] == 1:
				dc.SetPen(wx.Pen('RED'))
				dc.DrawLine(x1+offset,y1+offset,x2+offset,y2+offset)
			num = num + 1

#------IF RUN DIRECTLY FROM TERMINAL------
if __name__ == '__main__':

	app = wx.App(False)
	frame = FoamCutter(None, 'FoamCutter')
	frame.Show(True)
	app.MainLoop()



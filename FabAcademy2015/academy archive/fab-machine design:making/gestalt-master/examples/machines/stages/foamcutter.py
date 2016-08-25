# Forked from DFUnitVM Oct 2013
# set portname
# set location of hex file for bootloader
#

#------IMPORTS-------
from gestalt import nodes
from gestalt import interfaces
from gestalt import machines
from gestalt import functions
from gestalt.machines import elements
from gestalt.machines import kinematics
from gestalt.machines import state
from gestalt.utilities import notice
from gestalt.publish import rpc	#remote procedure call dispatcher
import time
import io


#------VIRTUAL MACHINE------
class virtualMachine(machines.virtualMachine):
	
	def initInterfaces(self):
		if self.providedInterface: self.fabnet = self.providedInterface		#providedInterface is defined in the virtualMachine class.
		else: self.fabnet = interfaces.gestaltInterface('FABNET', interfaces.serialInterface(baudRate = 115200, interfaceType = 'ftdi', portName = '/dev/ttyUSB0'))
		
	def initControllers(self):
		self.xAxisNode = nodes.networkedGestaltNode('X Axis', self.fabnet, filename = '086-005a.py', persistence = self.persistence)
		self.yAxisNode = nodes.networkedGestaltNode('Y Axis', self.fabnet, filename = '086-005a.py', persistence = self.persistence)
		self.uAxisNode = nodes.networkedGestaltNode('U Axis', self.fabnet, filename = '086-005a.py', persistence = self.persistence)
		self.vAxisNode = nodes.networkedGestaltNode('V Axis', self.fabnet, filename = '086-005a.py', persistence = self.persistence)

		#self.xyNode = nodes.compoundNode(self.xAxisNode, self.yAxisNode)
		#self.uvNode = nodes.compoundNode(self.uAxisNode, self.vAxisNode)
		
		self.xyuvNode = nodes.compoundNode(self.xAxisNode, self.yAxisNode, self.uAxisNode, self.vAxisNode)

	def initCoordinates(self):
		self.position = state.coordinate(['mm','mm','mm', 'mm'])
	
	def initKinematics(self):
		self.xAxis = elements.elementChain.forward([elements.microstep.forward(4), elements.stepper.forward(1.8), elements.leadscrew.forward(6.096), elements.invert.forward(True)])
		self.yAxis = elements.elementChain.forward([elements.microstep.forward(4), elements.stepper.forward(1.8), elements.leadscrew.forward(6.096), elements.invert.forward(False)])
		self.uAxis = elements.elementChain.forward([elements.microstep.forward(4), elements.stepper.forward(1.8), elements.leadscrew.forward(6.096), elements.invert.forward(True)])
		self.vAxis = elements.elementChain.forward([elements.microstep.forward(4), elements.stepper.forward(1.8), elements.leadscrew.forward(6.096), elements.invert.forward(False)])

		self.stageKinematics = kinematics.direct(4)	#direct drive on all axes
	
	def initFunctions(self):
		self.move = functions.move(virtualMachine = self, virtualNode = self.xyuvNode, axes = [self.xAxis, self.yAxis, self.uAxis, self.vAxis], kinematics = self.stageKinematics, machinePosition = self.position,planner = 'null')
		self.jog = functions.jog(self.move)	#an incremental wrapper for the move function
		pass
		
	def initLast(self):
#		self.machineControl.setMotorCurrents(aCurrent = 0.8, bCurrent = 0.8, cCurrent = 0.8)
#		self.xyzNode.setVelocityRequest(0)	#clear velocity on nodes. Eventually this will be put in the motion planner on initialization to match state.
		pass
	
	def publish(self):
#		self.publisher.addNodes(self.machineControl)
		pass
	
	def getPosition(self):
		return {'position':self.position.future()}
	
	def setPosition(self, position  = [None, None, None]):
		self.position.future.set(position)

	def setSpindleSpeed(self, speedFraction):
#		self.machineControl.pwmRequest(speedFraction)
		pass

#------IF RUN DIRECTLY FROM TERMINAL------
if __name__ == '__main__':
	stages = virtualMachine(persistenceFile = "test.vmp")
#	stages.xyuvNode.setMotorCurrent(1.2)
#	stages.xyNode.setMotorCurrent(.8)
#	stages.uvNode.setMotorCurrent(.8)
#	stages.xyNode.loadProgram('../../../086-005/086-005a.hex')
#	stages.uvNode.loadProgram('../../../086-005/086-005a.hex')
	#stages.xyNode.setVelocityRequest(8)
	#stages.uvNode.setVelocityRequest(8)
	stages.xyuvNode.setVelocityRequest(1)	
	
	f = open('nadyafoil.csv','r')
	circcoords = []
	for line in f.readlines():
		xy = line.split(',')
		coord = []
		for num in xy:
			try:
				nr = float(num)
				coord.append(nr)
			except:
				pass
		circcoords.append(coord)

	#for coord in circcoords:
	#	coord[1] = coord[1]-98.0
	#	coord[3] = coord[3]-98.0
	circcoords.append([0,0,0,0])

	print circcoords

	doublecoords = []
	for coord in circcoords:
		try:
			temp = [coord[0], coord[1], coord[0], coord[1]]
			doublecoords.append(temp)
		except:
			pass


	f = open('test.csv', 'r')
	
	airfoil = []

	for line in f.readlines():
		xy = line.split(' ')
		coor = []
		for num in xy:
			coor.append(float(num)*100)
		airfoil.append(coor)
	
	airfoil2 = airfoil[0:70]
	airfoil1 = airfoil[70:]

	airfoilmoves = []
	for coord in airfoil1:
		airfoilmoves.append([coord[0], coord[1], coord[0], coord[1]])
	for coord in airfoil2:
		airfoilmoves.append([coord[0], coord[1], coord[0], coord[1]])
	airfoilmoves.append([0,0,0,0])

#	valentines moves
	f = open('happyvalentinesNadya4.csv', 'r')
	moves = []

	for line in f.readlines():
		xyuv = line.split(',')
		coor = []
		for num in xyuv:
			try:
				coor.append(float(num))
			except:
				pass
		moves.append(coor)

	moves = moves[2:] #first two wahtever

	turn = []
	i = 0
	while i<len(moves):
		first10moves = moves[i:i+9]
		next10moves = moves[i+10:i+19]

		for move in first10moves:
			turn.append(move)
		next10moves.reverse()

		for move in next10moves:
			turn.append(move)
		i= i+19
	#print turn	

	square = []
	square.append([80,0,80,0])
	square.append([0,0,0,0])
	square.append([0,80,0,80])
	square.append([0,0,0,0])

	fun =[]
	fuile = open('VC.csv', 'r')

	for line in fuile.readlines():
		xyuv = line.split(',')
		coor = []		
		for num in xyuv:
			try:
				coor.append(float(num))
			except:
				pass
		fun.append(coor)

	fun = fun[2:] #first two whatever


	double=[]
	dfile=open('roof2.csv','r')
	for line in dfile.readlines():
		coords = line.split(',')
		coor = []
		for num in coords:
			try:
				coor.append(float(num))
			except:
				pass
		double.append(coor)
	
	
	back = []
	back.append([0,0,0,0])
	#back.append([-52,-42,-55,-130])
	#back.append([-20,-30,-60,-60])	
	#nadya idjit they are absolute

	for coords in circcoords:
		stages.move(coords, 0)
		status = stages.xAxisNode.spinStatusRequest()
		while status['stepsRemaining'] > 0:
			time.sleep(0.001)
			status = stages.xAxisNode.spinStatusRequest()	
	



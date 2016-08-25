  import processing.serial.*;
  
  Serial myPort;  // Create object from Serial class
  int val;      // Data received from the serial port
  int sensorData; // Data received from the serial port with 1,2,3,4 framing numbers filtered out
  int on_low=0;
  int on_high=0;
  int off_low=0;
  int off_high=0;
  int on_value=0;
  int off_value=0;
  int diff_value=0;
 int byte1 = 0;
 int byte2 = 0;
 int byte3 = 0;
 int byte4 = 0;

 
 
 void setup()
 {
   size(1000, 1000);
  smooth();
  fill(0);
   println(Serial.list());
   myPort = new Serial(this, "/dev/ttyUSB0", 9600);
  frameRate(60);
   background(255);
 
 }
 
 void draw()
 {
   while (myPort.available() > 0) {    // If data is available
     byte1 = byte2;
     byte2 = byte3;
     byte3 = byte4;
     byte4 = on_low;
     on_low = on_high;
     on_high = off_low;
     off_low = off_high;
     off_high = myPort.read();
 
     if ((byte1 == 1) & (byte2 == 2) & (byte3 == 3) & (byte4 == 4)){                // Filter out the framing numbers: 1,2,3,4
        on_value = ((256*on_high) + on_low);
        off_value = ((256*off_high) + off_low);
        diff_value = on_value - off_value;
 
        println("THE ON VALUE IS " + on_value); 
         println("THE OFF VALUE IS " + off_value); 
         println("THE DIFFERENCE VALUE IS " + diff_value); 
        
        //print to the screen
     }}

  
  if (mousePressed == true) {
         float  x1 = map(diff_value, -700, 2000, 1, 50);
         strokeWeight(x1);
        line(pmouseX, pmouseY, mouseX, mouseY);

       println("A VALUE IS " + x1); 
    
 
                


   
   
 
   }
 }

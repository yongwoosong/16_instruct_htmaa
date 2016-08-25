 /*
 LED Off Until Button Pressed 
 
 Blinks a light emitting diode(LED) connected to digital  
 pin 7, when pressing a pushbutton attached to pin 3. 
 
 
 The circuit:
 * LED attached from pin 7 to ground 
 * pushbutton attached to pin 3 from +5V
 * 10K resistor attached to pin 3 to +5V 
 * 10K resistor pulls pin 3 and the button to HIGH by default
 
 created 2005
 by DojoDave 
 modified 30 Aug 2011
 by Tom Igoe
 modified for Hello Button + LED Board - 19 Mar 2012
 by Anna Kaziunas France
 Tried for Fab Academy2015 
 by Yongwoo Song
 
 */

// constants won't change. 
// They're used here to set pin numbers:
const int buttonPin = 3;     // the number of the pushbutton pin
const int ledPin =  7;      // the number of the LED pin

// initialize variables:
int buttonState = 0;         // variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);    
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);     
}

void loop(){
  // read the state of the pin the pushbutton is connected to:
  buttonState = digitalRead(buttonPin);

  // is the push button pressed?
  // if not pressed - the button state is HIGH 
  // the pull up resistor the button / pin 3 makes the button state HIGH by default.
  if (buttonState == HIGH) {
    digitalWrite(ledPin, HIGH); // sets the LED on
    delay(50); // waits for a second 
    digitalWrite(ledPin, LOW); // sets the LED off
    delay(50);     
    // turn LED off (LED is off by default) 
    digitalWrite(ledPin, LOW); 
  } 
  //otherwise.....
  // button is pressed
  else {
    // turn LED off:
    digitalWrite(ledPin, LOW); 
  }
}

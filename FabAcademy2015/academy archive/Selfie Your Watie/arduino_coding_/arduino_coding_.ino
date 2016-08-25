#include <SoftwareSerial.h>
SoftwareSerial serial(0, 1);


int motorPin1 = 2;
int motorPin2 = 3;
int motorPin3 = 5;
int motorPin4 = 6;

int motorPin5 = 8;
int motorPin6 = 9;
int motorPin7 = 11;
int motorPin8 = 12;

int delayTime = 10000;
int waterTime = 8000;

int waterPump = A0; // humidity sensor one 
int sensorValue = 0;  // variable to store value coming 


void setup()
{
  serial.begin(9600);
  pinMode(A0, OUTPUT);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);  
  
   
}

void loop()
{
  for(int i=0; i<40; i++){
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     digitalWrite(motorPin5, LOW);
     digitalWrite(motorPin6, HIGH);
     digitalWrite(motorPin7, HIGH);
     digitalWrite(motorPin8, LOW);
     delayMicroseconds(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, LOW);
     digitalWrite(motorPin4, HIGH);
     digitalWrite(motorPin5, LOW);
      digitalWrite(motorPin6, HIGH);
      digitalWrite(motorPin7, LOW);
      digitalWrite(motorPin8, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      digitalWrite(motorPin5, HIGH);
      digitalWrite(motorPin6, LOW);
      digitalWrite(motorPin7, LOW);
      digitalWrite(motorPin8, HIGH);

      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      digitalWrite(motorPin5, HIGH);
      digitalWrite(motorPin6, LOW);
      digitalWrite(motorPin7, HIGH);
      digitalWrite(motorPin8, LOW);
      delayMicroseconds(delayTime);
      digitalWrite(A0, HIGH);
      delay(waterTime);
      digitalWrite(A0, LOW);
   }
   for(int i=0; i<20; i++){
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      digitalWrite(motorPin5, HIGH);
      digitalWrite(motorPin6, LOW);
      digitalWrite(motorPin7, HIGH);
      digitalWrite(motorPin8, LOW);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      digitalWrite(motorPin5, HIGH);
      digitalWrite(motorPin6, LOW);
      digitalWrite(motorPin7, LOW);
      digitalWrite(motorPin8, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      digitalWrite(motorPin5, LOW);
     digitalWrite(motorPin6, HIGH);
      digitalWrite(motorPin7, LOW);
      digitalWrite(motorPin8, HIGH);
      delayMicroseconds(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     digitalWrite(motorPin5, LOW);
     digitalWrite(motorPin6, HIGH);
     digitalWrite(motorPin7, HIGH);
     digitalWrite(motorPin8, LOW);
     delayMicroseconds(delayTime);
     digitalWrite(A0, HIGH);
     delay(waterTime);
     digitalWrite(A0, LOW);
    
   }

   for(int i=0; i<15; i++){
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      digitalWrite(motorPin5, HIGH);
      digitalWrite(motorPin6, LOW);
      digitalWrite(motorPin7, HIGH);
      digitalWrite(motorPin8, LOW);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      digitalWrite(motorPin5, HIGH);
      digitalWrite(motorPin6, LOW);
      digitalWrite(motorPin7, LOW);
      digitalWrite(motorPin8, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, LOW);
      digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      digitalWrite(motorPin5, LOW);
     digitalWrite(motorPin6, HIGH);
      digitalWrite(motorPin7, LOW);
      digitalWrite(motorPin8, HIGH);
      delayMicroseconds(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     digitalWrite(motorPin5, LOW);
     digitalWrite(motorPin6, HIGH);
     digitalWrite(motorPin7, HIGH);
     digitalWrite(motorPin8, LOW);
     delayMicroseconds(delayTime);
     digitalWrite(A0, HIGH);
     delay(waterTime);
     digitalWrite(A0, LOW);
    
   }
}
 /*turn the ledPin on 
 if (1){
   for(int i=0; i<50; i++){
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     delay(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delay(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delay(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      delay(delayTime);
   }
   for(int i=0; i<10; i++){
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     delay(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delay(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delay(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      delay(delayTime);
   }

    for(int i=0; i<50; i++){
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      delay(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delay(delayTime);
      digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delay(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     delay(delayTime); 
   }
      
 
}
}

*/



#include <SoftwareSerial.h>
SoftwareSerial serial(0, 1);

int motorPin1 = 2;
int motorPin2 = 3;
int motorPin3 = 5;
int motorPin4 = 6;

//int motorPin5 = 8;
//int motorPin6 = 9;
//int motorPin7 = 11;
//int motorPin8 = 12;

int delayTime = 10000;
int waterTime = 1;

int sensorPin = A0; // humidity sensor one 
int humidwater = 13; // the water pump pin   (ledPin = 13);
int sensorValue = 0;  // variable to store value coming 

void setup()
{
  serial.begin(9600);
  pinMode(humidwater, OUTPUT);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
  
  
   
}

void loop()
{
  /*
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     delayMicroseconds(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      delayMicroseconds(delayTime);
      */

 if (1){
   for(int i=0; i<150; i++){
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     delayMicroseconds(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      delayMicroseconds(delayTime);
   }
   for(int i=0; i<100; i++){
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     delayMicroseconds(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      delayMicroseconds(delayTime);
   }
 digitalWrite (humidwater, HIGH);
 delay(waterTime);
 digitalWrite (humidwater, LOW);
    for(int i=0; i<50; i++){
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, HIGH);
      digitalWrite(motorPin4, LOW);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, HIGH);
      digitalWrite(motorPin2, LOW);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delayMicroseconds(delayTime);
      digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
      digitalWrite(motorPin3, LOW);
      digitalWrite(motorPin4, HIGH);
      delayMicroseconds(delayTime);
     digitalWrite(motorPin1, LOW);
     digitalWrite(motorPin2, HIGH);
     digitalWrite(motorPin3, HIGH);
     digitalWrite(motorPin4, LOW);
     delayMicroseconds(delayTime); 
   }
      
 //얗
}
else{
}

}

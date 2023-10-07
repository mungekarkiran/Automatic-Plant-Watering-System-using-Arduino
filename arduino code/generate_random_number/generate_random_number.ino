long randNumber;  

void setup() {
  
  // initialize the serial port
  Serial.begin(9600);
  // initialize the pseudo-random number generator
//  randomSeed(analogRead(0));

}

void loop() {
   randNumber = random(0, 255);                                              // generate a random number
  Serial.println(randNumber);                                               // send the random number to the serial port
//  analogWrite(analogOutPin, randNumber);                                    // vary the brightness of the LED according to the random number
  delay(500);

}

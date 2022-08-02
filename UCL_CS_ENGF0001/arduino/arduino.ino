#define SLAVE_ADDR 9
#define I2C_SDA 21
#include <Wire.h>
#include <Arduino.h>
typedef unsigned long ul;
union Buffer
{
  unsigned long longNumber;
  byte longBytes[4];
}buffer;

float targetTemp;
int targetRpm;
float currentTemp = 13.34;
int currentRpm = 1314;
ul encode(float temp,int rpm){
  ul msg = ((ul)rpm<<16)+(ul)round(temp*100);
  return msg;
}
void decode(ul msg){
  targetTemp = (msg & 0xFFFF)/100.0;
  targetRpm = (msg >>16)&0xFFFF;
}
void sendData() 
{    
  buffer.longNumber = encode(currentTemp,currentRpm);
  Wire.write(buffer.longBytes,4);
}
void receiveData(int a)                                                          
{
  if(Wire.available()){
    for(int i=0;i<4;i++)
      buffer.longBytes[i] = Wire.read();
    decode(buffer.longNumber);
  }
}
void setup() 
{
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDR); 
  Wire.onRequest(sendData);
  Wire.onReceive(receiveData);
}
void loop() {

}

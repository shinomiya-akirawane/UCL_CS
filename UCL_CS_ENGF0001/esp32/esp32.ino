#include <Wire.h>
#include <Arduino.h>
// Define Slave I2C Address. All slaves must be allocated a // unique number.
#define SLAVE_ADDR 9
// Define the pins used for SDA and SCL. This is important because // there is a problem with the TTGO and I2C will not work properly // unless you do.
#define I2C_SDA 21
#define I2C_SCL 22
typedef unsigned long ul;

union Buffer
{
   unsigned long longNumber;
   byte longBytes[4];
};

Buffer buffer;

float targetTemp = 2.00;
int targetRpm = 100;
float currentTemp=0.00;
int currentRpm=0;

ul encode(float temp, int rpm)
{
  ul msg = ((ul)rpm << 16) + (ul)round(temp * 100);
  return msg;
}

void decode(ul msg)
{
  currentTemp = (msg & 0xFFFF) / 100.0;
  currentRpm = (msg >> 16) & 0xFFFF;
}

void send()
{
  buffer.longNumber = encode(targetTemp, targetRpm);
  Wire.beginTransmission(SLAVE_ADDR);
  Wire.write(buffer.longBytes, 4);
  Wire.endTransmission();
  
}
void requestevent()
{
  if(Wire.available())
  {
    for(int i = 0; i < 4; i++) {
      buffer.longBytes[i] = Wire.read();
    }
  }
  decode(buffer.longNumber);
  Serial.print("Temp: ");
  Serial.println(currentTemp);
  Serial.print("RPM: ");
  Serial.println(currentRpm);
}
void setup()
{
  Wire.begin();
  Serial.begin(115200);
}

void loop()
{
  send();
  Wire.requestFrom(SLAVE_ADDR, 4);
  requestevent();
  delay(500);
}

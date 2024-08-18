#include <Servo.h>

Servo servoVer; 
Servo servoHor;

int x;
int y;

int prevX;
int prevY;


double Kp = 0.1; 
double Ki = 0.01; 
double Kd = 0.05; 

double integralX, integralY;
double prevErrorX, prevErrorY;

void setup()
{
  Serial.begin(9600);
  servoVer.attach(9); 
  servoHor.attach(7); 
  servoVer.write(90);
  servoHor.write(90);
}

void Pos()
{
  if (prevX != x || prevY != y)
  {
    double errorX = x - 250; 
    double errorY = y - 250; 

    integralX += errorX;
    integralY += errorY;

    double derivativeX = errorX - prevErrorX;
    double derivativeY = errorY - prevErrorY;

    double outputX = Kp * errorX + Ki * integralX + Kd * derivativeX;
    double outputY = Kp * errorY + Ki * integralY + Kd * derivativeY;

    int servoX = constrain(90 + outputX, 0, 179); 
    int servoY = constrain(90 - outputY, 0, 179); 

    servoHor.write(servoX);
    servoVer.write(servoY);

    prevErrorX = errorX;
    prevErrorY = errorY;
  }
}

void loop()
{
  if (Serial.available() > 0)
  {
    if (Serial.read() == 'X')
    {
      x = Serial.parseInt();
      if (Serial.read() == 'Y')
      {
        y = Serial.parseInt();
        Pos();
      }
    }
    while (Serial.available() > 0)
    {
      Serial.read();
    }
  }
}

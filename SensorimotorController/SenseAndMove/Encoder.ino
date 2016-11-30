/* I dont have more pins so I need to use the pins available from 
 *  this arduino to decode the encoder information.
 */

int pinA = 9;  // Connected to CLK on KY-040
int pinB = 10;  // Connected to DT on KY-040
int encoderPosCount;
int pinALast;
int aVal;
boolean bCW;

void setupEncoder() {
  pinMode (pinA, INPUT);
  pinMode (pinB, INPUT);
  encoderPosCount = 0;
  /* Read Pin A
    Whatever state it's in will reflect the last position
  */
  pinALast = digitalRead(pinA);
  //Serial.begin (9600);
}

void updateEncoder() {
  aVal = digitalRead(pinA);
  if (aVal != pinALast) { // Means the knob is rotating
    // if the knob is rotating, we need to determine direction
    // We do that by reading pin B.
    if (digitalRead(pinB) != aVal) {  // Means pin A Changed first - We're Rotating Clockwise
      encoderPosCount ++;
      bCW = true;
    } else {// Otherwise B changed first and we're moving CCW
      bCW = false;
      encoderPosCount--;
    }
    Serial.print ("Rotated: ");
    if (bCW) {
      Serial.println ("clockwise");
    } else {
      Serial.println("counterclockwise");
    }
    Serial.print("Encoder Position: ");
    Serial.println(encoderPosCount);

  }
  pinALast = aVal;
}

int getEncoderPos()
{
  return encoderPosCount;
}

void resetEncoderPos()
{
  encoderPosCount=0;
}


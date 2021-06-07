int ledPin = 13;
int py_byte;

void setup()
{
    pinMode(ledPin, OUTPUT);
    Serial.begin(115200);
}

void loop(){
  if(Serial.available() > 0) {
    py_byte = Serial.read();
    
    if(py_byte == 'H') {
      digitalWrite(ledPin, HIGH);
      Serial.write("LED On");
    }

    if(py_byte == 'L') {
      digitalWrite(ledPin, LOW);
      Serial.write("LED Off");
    }
  }
}

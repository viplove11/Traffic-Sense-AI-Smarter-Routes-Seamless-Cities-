int red = 10;
int yellow = 11;
int green = 12;

void setup() {
  Serial.begin(9600);
  pinMode(red, OUTPUT);
  pinMode(yellow, OUTPUT);
  pinMode(green, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    int receivedVal = Serial.parseInt();
    Serial.print(receivedVal);
    // int receivedVal = 1;
    if (receivedVal == 1) {
       digitalWrite(red, HIGH);
       delay(3000);
      digitalWrite(yellow, LOW);
      digitalWrite(green, LOW);

    } else if (receivedVal == 2) {
      digitalWrite(red, LOW);
      digitalWrite(yellow, HIGH);
       delay(3000);
      digitalWrite(green, LOW);

    } else if (receivedVal == 3) {
      digitalWrite(red, LOW);
      digitalWrite(yellow, LOW);
      digitalWrite(green, HIGH);
       delay(5000);
    }
  }
}
#include <Arduino.h>
#include "LED_button.h"

//헤더에서는 클래스와 메소드를 선언하고 C++에서는 정의를 해준다.

Led::Led(int button_Pin, int led_Pin){
    buttonPin = button_Pin; // 멤버 변수 정의2 
    ledPin = led_Pin; // 멤버 변수 정의2
}

void Led::onLed(){
    digitalWrite(ledPin, High);
}

void Led::offLed(){
    digitalWrite(ledPin, Low);
}

void Led::isPush(){
    return digitalRead(buttonPin);
}
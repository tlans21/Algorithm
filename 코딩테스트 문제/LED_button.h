//1819054 천시문

//헤더에 클래스 선언과 메소드 프로토타입을 만듭니다.
class Led{
    public:
        Led(int buttonPin, int ledPin);
        int isPush();
        void onLed();
        void offLed();
    private:
        int ledPin;
        int buttonPin;
};
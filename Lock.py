import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Lock:
    __lock=True
    __relay=18
    def __init__(self,pin):
        self.__relay=pin
        GPIO.setup(self.__relay,GPIO.OUT)
        GPIO.output(self.__relay,GPIO.HIGH)
        
        
    
    
    def setLock(self):
        self.__lock=True
        GPIO.output(self.__relay,GPIO.HIGH)
        
        
    def unsetLock(self):
        self.__lock=False
        GPIO.output(self.__relay,GPIO.LOW)
        
    def getStatus(self):
        if self.__lock:
            return "Locked"
        return "Unlocked"

"""l=Lock(18)
while True:
    ch=input("enter L to lock U to unlock:")
    if ch=='L':
        l.setLock()
        print(l.getStatus())
    elif ch=='U:
        l.unsetLock()
        print(l.getStatus())
    else:
        print("invalid")"""
        

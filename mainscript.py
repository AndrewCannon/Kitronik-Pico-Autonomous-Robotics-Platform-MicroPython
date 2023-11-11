from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from motioncontrol import MotionControl
from time import sleep
from machine import Timer

buggy = KitronikPicoRobotBuggy()
run = False
buttonState = 0
            
DegreesPerSecond = (13/5)*360

picoLED = machine.Pin(25,machine.Pin.OUT)
picoLED.value(1)
    
def ButtonIRQHandler(pin):
    buggy.beepHorn()
    
def checkButton(p):
    global buttonState
    global run
    
    buttonState = buttonState <<1 | buggy.button.value() |0xE000
    buttonState &= 0xEFFF
    if buttonState == 0xEFFF:
        if run == True:
            run = False
            MotionControl.Stop(buggy)
        else:
            run = True
            
            
def distanceaslightcolor(distance):
    if(distance < 1):
        red_channel = 0
        green_channel = 0
        blue_channel = 0
        buggy.beepHorn()
    elif(distance < 51): #0-50
        red_channel = 255
        green_channel = 5*distance
        blue_channel = 0
    elif(distance < 101): #51-100
        red_channel = 255-(5*(distance-51))
        green_channel = 255
        blue_channel = 0
    elif(distance < 150): #101 - 150
        red_channel = 0
        green_channel = 255
        blue_channel = (5*(distance-101))
    elif(distance < 201): #151-200
        red_channel = 0
        green_channel = 255-(5*(distance-151))
        blue_channel = 255
    else: #over 200
        red_channel = 0
        green_channel = 0
        blue_channel =255

    buggy.setLED(0,(int(red_channel),int(green_channel),int(blue_channel)))
    buggy.setLED(1,(int(red_channel),int(green_channel),int(blue_channel)))
    buggy.setLED(2,(int(red_channel),int(green_channel),int(blue_channel)))
    buggy.setLED(3,(int(red_channel),int(green_channel),int(blue_channel)))
    buggy.show()
    
debouceTimer = Timer(-1)
debouceTimer.init(period=2, mode=Timer.PERIODIC, callback=checkButton)

brightness = 90
sleep(2)

while True:
    sleep(0.1)
    distance = buggy.getDistance("f")
    print(distance)
    distanceaslightcolor(distance)
    MotionControl.Forwards(buggy,70) 
    if distance > 30 :
        MotionControl.Forwards(buggy,70) 
    elif distance > 20:
        MotionControl.Forwards(buggy,20)
    else: 
        sleep(0.2)
        MotionControl.Stop(buggy)
        MotionControl.Reverse(buggy)
        sleep(0.1)
        MotionControl.TurnRight(buggy,30)
        sleep(0.2)



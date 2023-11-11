from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep
from machine import Timer

class MotionControl:
    
    def Forwards(obj,speed):
        obj.motorOn("l","f",speed+5)
        obj.motorOn("r","f",speed)
        
    def ForwardsVar(obj,speed):
        obj.motorOn("l","f",speed+5)
        obj.motorOn("r","f",speed)
        
    def Reverse(obj):
        obj.motorOn("l","r",70)
        obj.motorOn("r","r",75)
        
    def Stop(obj):
        obj.motorOff("r")
        obj.motorOff("l")

    def Spin(obj):
        obj.motorOn("l","f",80)
        obj.motorOn("r","r",80)
            
    def TurnLeft(obj,howfar):
        DegreesPerSecond = (13/5)*360
        obj.motorOn("l","r",80)
        obj.motorOn("r","f",80)
        sleep(howfar/DegreesPerSecond)
        MotionControl.Stop(obj)

    def TurnRight(obj,howfar):
        DegreesPerSecond = (13/5)*360
        obj.motorOn("l","f",80)
        obj.motorOn("r","r",80)
        sleep(howfar/DegreesPerSecond)
        MotionControl.Stop(obj)


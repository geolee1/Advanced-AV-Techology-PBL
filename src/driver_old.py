"""driver.py"""
'''1. 출발(직진후 정지)
   2. 주차시작
   3. 후방 평행주차
   4. 주차완료(대기)
   5. 출차시작
   6. 출차완료(대기)
   7. 주행시작
   8. 주행완료(정지)'''
import time
from pop import Pilot

Car = Pilot.AutoCar()
centerAngle = 0

''' power 16.2
    left-1 <= steering <= 1
    forward(20<=speed<=99)
    backward(20<=speed<=99)'''

def setSteering(angle):
    print("setSteering")
    Car.steering = angle

def goForward(speed, angle = centerAngle):
    print("goForward")
    setSteering(angle)
    Car.forward(speed)

def goBackward(speed, angle = centerAngle):
    print("goBackward")
    setSteering(angle)
    Car.backward(speed)

def stop():
    print("stop")
    Car.stop()
    setSteering(centerAngle)

def driveForward(speed, t, angle=centerAngle):
    goForward(speed, angle)
    time.sleep(t)
    stop()

def driveBackward(speed, t, angle=centerAngle):
    goBackward(speed, angle)
    time.sleep(t)
    stop()

def main():
    driveForward(50,3)

    driveBackward(50, 1, -1)
    driveBackward(50, 0.8, 0)
    driveBackward(50, 0.8, 1)

    driveForward(50, 0.8, 1)
    driveForward(50, 0.8, 0)
    driveForward(50, 1, -1)

    driveForward(50,3.5)
    return

if __name__ == "__main__":
    main()
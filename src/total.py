# module import가 안되는 문제 해결
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import audio
import driver
import time

def main(*argv, **kwargv):
    d = driver.Driver()
    m = audio.Musicplayer()

    m.play("start")
    m.play("car moving", blocking=False)
    d.driveForward(50,3)

    m.play("now parking")
    d.driveBackward(50, 1, -1)
    d.driveBackward(50, 0.8, 0)
    d.driveBackward(50, 0.8, 1)
    m.play("complete parking")

    time.sleep(5)

    m.play("leave parking")
    m.play("car moving", blocking=False)
    d.driveForward(50, 0.8, 1)
    d.driveForward(50, 0.8, 0)
    d.driveForward(50, 1, -1)
    m.play("complete leaving")

    time.sleep(5)

    m.play("car moving", blocking=False)
    d.driveForward(50,3.5)
    m.play("car stop")
    m.play("finish", blocking=False)
    return

if __name__ == '__main__':
    main(*sys.argv[1:])
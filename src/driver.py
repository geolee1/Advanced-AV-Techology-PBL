import time
import multiprocessing
from pop import Pilot

class Driver:
    __centerAngle = 0
    __running = True
    __paused = False
    __current_command = None  # 현재 명령어를 기억하는 변수
    __remaining_time = 0  # 남은 시간

    def __init__(self):
        self.Car = Pilot.AutoCar()
        self.__centerAngle = 0
        self.__running = True
        self.__paused = False
        self.__current_command = None  # 현재 명령어를 기억하는 변수
        self.__remaining_time = 0  # 남은 시간

    def _setSteering(self, angle):
        print(f"[Driver] Set steering to {angle}.")
        self.Car.steering = angle

    def _goForward(self, speed, angle=__centerAngle):
        print(f"[Driver] Go forward speed {speed} to {angle}.")
        self._setSteering(angle)
        self.Car.forward(speed)

    def _goBackward(self, speed, angle=__centerAngle):
        print(f"[Driver] Go backward speed {speed} to {angle}.")
        self._setSteering(angle)
        self.Car.backward(speed)

    def _stop(self):
        print("[Driver] Car stoped.")
        self.Car.stop()
        self._setSteering(self.__centerAngle)

    def driveForward(self, speed, t, angle=__centerAngle):
        self._goForward(speed, angle)
        time.sleep(t)
        self._stop()

    def driveBackward(self, speed, t, angle=__centerAngle):
        self._goBackward(speed, angle)
        time.sleep(t)
        self._stop()

    def input_listener(self):
        while self.__running:
            command = input("명령어를 입력하세요 (stop/resume/exit): ").strip().lower()
            if command == 'stop':
                self.__paused = True
                self._stop()
                print("주행이 중지되었습니다.")
            elif command == 'resume':
                self.__paused = False
                print(f"주행을 재개합니다: {self.__current_command}, 남은 시간: {self.__remaining_time:.1f}초")
            elif command == 'exit':
                self.__running = False
                self._stop()
                print("프로그램을 종료합니다.")
                break

# main test code
def main():
    pass
    

if __name__=="__main__":
    main()
import time
from pop import Pilot
import threading

class Driver:
    __centerAngle = 0
    __running = True
    __paused = False
    __current_command = None
    __remaining_time = 0  # 남은 시간
    __start_time = 0
    drive_commands = []  # 주행 명령어 리스트

    def __init__(self):
        self.Car = Pilot.AutoCar()
        self.input_thread = threading.Thread(target=self.input_listener)  # 입력을 처리할 스레드

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
        print("[Driver] Car stopped.")
        self.Car.stop()
        self._setSteering(self.__centerAngle)

    def add_command(self, speed, duration, angle=__centerAngle, direction='forward'):
        """주행 명령을 리스트에 추가."""
        self.drive_commands.append((speed, duration, angle, direction))

    def execute_commands(self):
        """drive_commands 리스트의 명령을 순차적으로 실행."""
        for command in self.drive_commands:
            speed, duration, angle, direction = command

            # 주행 명령 실행
            self.drive(speed, duration, angle, direction)

            # 현재 명령이 완료될 때까지 update()로 상태 갱신
            while self.__current_command is not None:
                self.update()  # 주기적으로 상태를 갱신
                if not self.__running:
                    break  # 프로그램이 종료되면 루프 탈출

            if not self.__running:
                break  # 프로그램 종료 명령 시 루프 탈출
        self.drive_commands.clear()  # 모든 명령을 실행한 후 명령 리스트 초기화

    def drive(self, speed, duration, angle=__centerAngle, direction='forward'):
        self.__current_command = direction
        self.__start_time = time.time()
        self.__remaining_time = duration
        if direction == 'forward':
            self._goForward(speed, angle)
        elif direction == 'backward':
            self._goBackward(speed, angle)

    def update(self):
        """이 함수는 주기적으로 호출되어 시간을 체크하고, 주행 상태를 갱신한다."""
        if self.__current_command and not self.__paused:
            elapsed_time = time.time() - self.__start_time
            if elapsed_time >= self.__remaining_time:
                self._stop()
                self.__current_command = None
            else:
                self.__remaining_time -= elapsed_time
                self.__start_time = time.time()  # 남은 시간을 계속 갱신

    def pause(self):
        """주행을 일시정지한다."""
        if self.__current_command and not self.__paused:
            elapsed_time = time.time() - self.__start_time
            self.__remaining_time -= elapsed_time
            self._stop()
            self.__paused = True
            print(f"주행이 일시정지되었습니다. 남은 시간: {self.__remaining_time:.2f}초")

    def resume(self):
        """주행을 재개한다."""
        if self.__paused:
            self.__paused = False
            self.__start_time = time.time()
            if self.__current_command == 'forward':
                self._goForward(50, self.__centerAngle)  # 속도와 조향값을 그대로 사용
            elif self.__current_command == 'backward':
                self._goBackward(50, self.__centerAngle)
            print("주행을 재개합니다.")

    def input_listener(self):
        """사용자 입력을 대기하는 스레드."""
        while self.__running:
            command = input("명령어를 입력하세요 (stop/resume/exit): ").strip().lower()
            if command == 's':
                self.pause()
            elif command == 'r':
                self.resume()
            elif command == 'e':
                self.__running = False
                self._stop()
                print("프로그램을 종료합니다.")
                break

def main():
    driver = Driver()
    driver.input_thread.start()


    # 주행 명령을 추가
    driver.add_command(50, 3, 0, 'forward')   
    driver.execute_commands()
 
    driver.add_command(50, 1, -1, 'backward')
    driver.add_command(50, 0.8, 0, 'backward')
    driver.add_command(50, 0.8, 1, 'backward')
    driver.execute_commands()

    driver.add_command(50, 0.8, 1, 'forward')
    driver.add_command(50, 0.8, 0, 'forward')
    driver.add_command(50, 1, -1, 'forward')
    driver.execute_commands()

    driver.add_command(50, 3.5, 0, 'forward')
    driver.execute_commands()

    driver.input_thread.join()

if __name__ == "__main__":
    main()

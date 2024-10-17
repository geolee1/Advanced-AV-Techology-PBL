import time
import threading
from pop import Pilot

Car = Pilot.AutoCar()
centerAngle = 0
running = True
paused = False
current_command = None  # 현재 명령어를 기억하는 변수
remaining_time = 0  # 남은 시간

def setSteering(angle):
    print("setSteering")
    Car.steering = angle

def goForward(speed, angle=centerAngle):
    print("goForward")
    setSteering(angle)
    Car.forward(speed)

def goBackward(speed, angle=centerAngle):
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

def input_listener():
    global running, paused, current_command, remaining_time
    while running:
        command = input("명령어를 입력하세요 (stop/resume/exit): ").strip().lower()
        if command == 'stop':
            paused = True
            stop()
            print("주행이 중지되었습니다.")
        elif command == 'resume':
            paused = False
            print(f"주행을 재개합니다: {current_command}, 남은 시간: {remaining_time:.1f}초")
        elif command == 'exit':
            running = False
            stop()
            print("프로그램을 종료합니다.")
            break

def main():
    global current_command, remaining_time

    # 스레드를 시작하여 입력 감지
    listener_thread = threading.Thread(target=input_listener)
    listener_thread.start()

    # 예시 주행 명령어를 리스트로 저장
    commands = [
        ('forward', 50, 3),
        ('backward', 50, 1, -1),
        ('backward', 50, 0.8, 0),
        ('backward', 50, 0.8, 1),
        ('forward', 50, 0.8, 1),
        ('forward', 50, 0.8, 0),
        ('forward', 50, 1, -1),
        ('forward', 50, 3.5)
    ]

    for command in commands:
        if paused:  # 주행이 멈추면 루프를 종료
            break
        if command[0] == 'forward':
            current_command = command
            remaining_time = command[2]  # 남은 시간을 현재 명령의 지속 시간으로 설정
            driveForward(command[1], command[2], command[3] if len(command) > 3 else centerAngle)
        elif command[0] == 'backward':
            current_command = command
            remaining_time = command[2]  # 남은 시간을 현재 명령의 지속 시간으로 설정
            driveBackward(command[1], command[2], command[3] if len(command) > 3 else centerAngle)

    # 주행이 멈춘 상태에서 남은 시간 계산
    while running:
        while paused:
            time.sleep(0.1)  # 잠시 대기

        # 재개 후 남은 시간 동안 주행
        if remaining_time > 0:
            print(f"주행 재개: {current_command}, 남은 시간: {remaining_time:.1f}초")
            if current_command[0] == 'forward':
                driveForward(current_command[1], remaining_time, current_command[3] if len(current_command) > 3 else centerAngle)
            elif current_command[0] == 'backward':
                driveBackward(current_command[1], remaining_time, current_command[3] if len(current_command) > 3 else centerAngle)
            remaining_time = 0  # 주행 후 남은 시간을 0으로 설정

    # 스레드가 종료될 때까지 대기
    listener_thread.join()

if __name__ == "__main__":
    main()

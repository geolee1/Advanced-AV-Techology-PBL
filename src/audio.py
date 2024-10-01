import multiprocessing
from playsound import playsound
import time

# MP3 파일 이름 리스트
text = [
    "start",
    "finish",
    "pause",
    "resume",
    "parking",
    "forward",
    "backward",
    "speed",
    "stop_"
] + [f"num_{num}" for num in range(10)]

# 오디오 파일 재생 함수
def play_audio(file_name):
    try:
        playsound(f'./audios/{file_name}.mp3')
    except Exception as e:
        print(f"Error occurred while playing {file_name}.mp3: {e}")

if __name__ == "__main__":
    processes = []
    
    for t in text:
        # 새로운 프로세스를 시작
        p = multiprocessing.Process(target=play_audio, args=(t,))
        processes.append(p)
        p.start()
        
        # 0.2초 동안 프로세스 실행 후 중단
        time.sleep(0.5)
        
        if p.is_alive():
            p.terminate()  # 프로세스 중단
            p.join()  # 종료될 때까지 대기

    print("All audio files have been processed.")

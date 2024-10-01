from gtts import gTTS
import os

# audios 폴더가 없으면 생성
if not os.path.exists("audios"):
    os.makedirs("audios")

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

# 텍스트를 음성으로 변환
for x in text:
    tts = gTTS(text=f'{x}', lang='en')
    tts.save(f"./audios/{x}.mp3")
from gtts import gTTS
import os

# audios 폴더가 없으면 생성
if not os.path.exists("audios"):
    os.makedirs("audios")

# MP3 파일 이름 리스트

text = [
    "start",
    "car moving",
    "now parking",
    "complete parking",
    "leave parking",
    "complete leaving",
    "car stop",
    "finish",
]

# 텍스트를 음성으로 변환
for x in text:
    tts = gTTS(text=f'{x}', lang='en')
    tts.save(f"./audios/{x}.mp3")
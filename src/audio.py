import multiprocessing
import playsound
import time

# MP3 플레이어 클래스
class Musicplayer():
    _audio_list = [
        "start",
        "finish",
        "pause",
        "resume",
        "parking",
        "forward",
        "backward",
        "speed",
        "stop_",
        "playing"
    ] + [f"num_{num}" for num in range(10)]

    def __init__(self):
        self.__process = None

    def play(self, sound, blocking=True, terminate=True):
        if sound not in self._audio_list:
            raise ValueError(f"Invalid sound: {sound}")
        
        if self.is_playing():
            if not blocking:
                self.__process.join()
            if terminate:
                self.__process.terminate()
        
        self.__process = multiprocessing.Process(target=playsound.playsound, args=(f'./audios/{sound}.mp3',))
        self.__process.start()
    
    def is_playing(self, playsound=False):
        if (self.__process.is_alive() if self.__process is not None else False):
            if playsound: self.play("playing")
            return True
        return False
    
    def stop(self, playsound=False):
        if playsound: self.play("stop_")
        if self.is_playing(): self.__process.terminate()
    
    def get_audio_list(self):
        return self._audio_list

if __name__ == "__main__":
    processes = []
    
    musicplayer = Musicplayer()
    for sound in musicplayer.get_audio_list():
        musicplayer.play(sound)
        time.sleep(0.7)
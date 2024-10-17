import multiprocessing
import playsound
import time

# MP3 플레이어 클래스
class Musicplayer():
    __process = None
    __loop_process = None

    _now_playing = False
    _audio_list = [
        "start",
        "car moving",
        "now parking",
        "complete parking",
        "leave parking",
        "complete leaving",
        "car stop",
        "finish",
    ]

    def __init__(self):
        self.__process = None
        self.__loop_process = None
        self._now_playing = False

    def play(self, sound, blocking=True, terminate=True):
        if sound not in self._audio_list:
            raise ValueError(f"Invalid sound: {sound}")
        
        if self.is_playing():
            if not blocking:
                self.__process.join()
            if terminate:
                self.__process.terminate()
        
        self.__process = multiprocessing.Process(target=self.__playsound, args=(f'./audios/{sound}.mp3',))
        self.__process.start()
        self._now_playing = True

    def __playsound(self, sound):
        playsound.playsound(f'./audios/{sound}.mp3')
        self._now_playing = False
    
    def is_playing(self, playsound=False):
        if (self.__process.is_alive() if self.__process is not None else False) or self._now_playing:
            if playsound: self.play("playing")
            return True
        return False
    
    def stop(self, playsound=False):
        if playsound: self.play("stop_")
        if self.is_playing(): self.__process.terminate()
    
    def get_audio_list(self):
        return self._audio_list
    
    def playloop(self, sound, n=0 , blocking=True, terminate=True):
        if n < 0:
            raise ValueError(f"Invalid n: {n}")
        
        if sound not in self._audio_list:
            raise ValueError(f"Invalid sound: {sound}")
        
        if self.is_looping():
            if not blocking:
                self.__loop_process.join()
            if terminate:
                self.__loop_process.terminate()
        
        self.__loop_process = multiprocessing.Process(target=self._loop, args=(sound, n))
        self.__loop_process.start()

    def is_looping(self):
        if (self.__loop_process.is_alive() if self.__loop_process is not None else False):
            return True
        return False

    def _loop(self, sound, n):
        if n == 0:
            while True:
                self.play(sound, blocking=False)
                time.sleep(0.5)
        else:
            for _ in range(n):
                self.play(sound, blocking=False)
                time.sleep(0.5)
    
    def stoploop(self):
        self.__loop_process.terminate()
        self.stop()
        

if __name__ == "__main__":
    
    musicplayer = Musicplayer()

    musicplayer.playloop("car moving", 2)
    musicplayer.playloop("start", 5, blocking=False)
    time.sleep(5)
    musicplayer.stoploop()
    musicplayer.playloop("finish")
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
        "beep effect"
    ]

    def __init__(self):
        self.__process = None
        self.__loop_process = None
        self._now_playing = False

    def play(self, sound, terminate=True, blocking=True):
        if sound not in self._audio_list:
            raise ValueError(f"Invalid sound: {sound}")
        
        if self.is_playing():
            if terminate:
                self.__process.terminate()
            elif blocking:
                self.__process.join()
        
        self.__process = multiprocessing.Process(target=self._playsound, args=(sound,))
        self.__process.start()
        self._now_playing = True
        print(f"[MusicPlayer] Playing {sound}...")

    def _playsound(self, sound):
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
        
        if self.is_playing():
            if terminate:
                self.__process.terminate()
            elif blocking:
                self.__process.join()

        if self.is_looping():
            if terminate:
                self.__loop_process.terminate()
            elif blocking:
                self.__loop_process.join()
        
        self.__loop_process = multiprocessing.Process(target=self._playloop, args=(sound, n))
        self.__loop_process.start()

    def is_looping(self):
        if (self.__loop_process.is_alive() if self.__loop_process is not None else False):
            return True
        return False

    def _playloop(self, sound, n):
        if n == 0:
            while True:
                self.play(sound, terminate=False)
                time.sleep(0.5)
        else:
            for _ in range(n):
                self.play(sound, terminate=False)
                time.sleep(0.5)
    
    def stoploop(self):
        self.__loop_process.terminate()
        self.stop()
        

if __name__ == "__main__":
    
    m = Musicplayer()

    m.play("start")
    m.play("car moving", terminate=False)
    # d.driveForward(50,3)
    time.sleep(3)

    m.play("now parking")
    # m.playloop("beep effect", terminate=False)
    # d.driveBackward(50, 1, -1)
    time.sleep(1)
    # d.driveBackward(50, 0.8, 0)
    time.sleep(0.8)
    # d.driveBackward(50, 0.8, 1)
    time.sleep(0.8)
    m.play("complete parking")

    time.sleep(5)

    m.play("leave parking")
    m.play("car moving", terminate=False)
    # d.driveForward(50, 0.8, 1)
    time.sleep(0.8)
    # d.driveForward(50, 0.8, 0)
    time.sleep(0.8)
    # d.driveForward(50, 1, -1)
    time.sleep(1)
    m.play("complete leaving")

    time.sleep(5)

    m.play("car moving", terminate=False)
    # d.driveForward(50,3.5)
    time.sleep(3.5)
    m.play("car stop")
    m.play("finish", terminate=False)
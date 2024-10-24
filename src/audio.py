import multiprocessing
import playsound
import time

# MP3 플레이어 클래스
class Musicplayer():
    __process = None
    __is_playing = False
    __is_looping = False

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
        pass

    def wait_finish(self):
        if not self.is_playing():
            return
        print("[MusicPlayer] Waiting for the end of the music...")
        if self.__process is not None:
            self.__process.join()
        print("[MusicPlayer] Music end.")

    def play(self, sound, repeat=1, terminate=True):
        if sound not in self._audio_list:
            raise ValueError(f"Invalid sound: {sound}")
        
        if self.is_playing():
            if terminate:
                if self.__is_looping: 
                    self.stoploop()
                else: 
                    self.stop()
            else:
                self.__process.join()

        self.__process = multiprocessing.Process(target=self._playsound, args=(sound, repeat))
        self.__process.start()
        self.__is_playing = True
        print(f"[MusicPlayer] Playing {sound}...")

    def _playsound(self, sound, repeat):
        self.__is_looping = True
        for _ in range(repeat):
            if not self.__is_looping: break
            playsound.playsound(f'./audios/{sound}.mp3')
        self.__is_playing = False
    
    def is_playing(self, playsound=False):
        if (self.__process.is_alive() if self.__process is not None else False) or self.__is_playing:
            if playsound: self.play("playing")
            return True
        return False
    
    def stop(self, playsound=False):
        if playsound: self.play("stop_")
        if self.is_playing(): self.__process.terminate()
        self.__is_playing = False
    
    def get_audio_list(self):
        return self._audio_list
    
    def stoploop(self):
        self.__is_looping = False
        self.stop()
        

if __name__ == "__main__":
    
    m = Musicplayer()

    m.play("start")
    m.play("car moving", terminate=False)
    m.wait_finish()
    # d.driveForward(50,3)
    time.sleep(3)

    m.play("now parking")
    m.wait_finish()
    m.play("beep effect", repeat=100, terminate=False)
    time.sleep(10)
    # d.driveBackward(50, 1, -1)
    time.sleep(1)
    # d.driveBackward(50, 0.8, 0)
    time.sleep(0.8)
    # d.driveBackward(50, 0.8, 1)
    time.sleep(0.8)
    m.stoploop()
    m.play("complete parking")
    m.wait_finish()

    time.sleep(1)

    m.play("leave parking")
    m.play("car moving", terminate=False)
    m.wait_finish()
    # d.driveForward(50, 0.8, 1)
    time.sleep(0.8)
    # d.driveForward(50, 0.8, 0)
    time.sleep(0.8)
    # d.driveForward(50, 1, -1)
    time.sleep(1)
    m.play("complete leaving")
    m.wait_finish()

    time.sleep(1)

    m.play("car moving", terminate=False)
    m.wait_finish()
    # d.driveForward(50,3.5)
    time.sleep(3.5)
    m.play("car stop")
    m.play("finish", terminate=False)
    m.wait_finish()
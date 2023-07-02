import pvporcupine
import pyaudio
import struct
PICOVOIVCE_API_KEY = "71Ux51hT6FvYKa4fNS02K7OkgFuqhG1CyBtVQnTl7WSq1YSqXTnzxQ=="
keyword_path='/Users/minyue/Desktop/xiangmu/Orator/assets/hei-cherry_en_mac_v2_2_0/hei-cherry_en_mac_v2_2_0.ppn'


#pyaudio (用电脑的麦克风来录入声音)
class PicoWakeWord:
    def __init__(self, PICOVOIVCE_API_KEY, keyword_path):
        self.PICOVOIVCE_API_KEY = PICOVOIVCE_API_KEY
        self.keyword_path = keyword_path

        self.porcupine = pvporcupine.create(
        access_key= self.PICOVOIVCE_API_KEY,
        keyword_paths=[self.keyword_path]
        )

        self.myaudio = pyaudio.PyAudio()
        self.stream = self.myaudio.open(
            input_device_index=0,
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )
    def detect_wake_word(self):
        audio_obj = self.stream.read(self.porcupine.frame_length, exception_on_overflow=False)
        audio_obj_unpacked = struct.unpack_from('h' * self.porcupine.frame_length, audio_obj)
        keyword_index = self.porcupine.process(audio_obj_unpacked)
        return keyword_index

if __name__ == '__main__':
    picowakeword = PicoWakeWord(PICOVOIVCE_API_KEY, keyword_path)
    while True:
        keyword_idx = picowakeword.detect_wake_word()
        if keyword_idx >= 0:
            print("I can hear you!!")
        
        

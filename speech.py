import pyaudio
import numpy as np
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import threading

# Parameters for audio recording
FORMAT = pyaudio.paInt16  # 16-bit resolution
CHANNELS = 1             # Mono audio
RATE = 16000             # 16kHz sampling rate (required by Whisper)
CHUNK = 1024             # 1024 samples per frame     # Duration of recording


class Whisper:
    def __init__(self):
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-base")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-base")
        

    def transcribe(self, frames):
        audio = np.frombuffer(b''.join(frames), dtype=np.int16).astype(np.float32) / 32768.0
        input_features = self.processor(audio, sampling_rate=RATE, return_tensors="pt").input_features
        forced_decoder_ids = self.processor.get_decoder_prompt_ids(language="en", task="transcribe")

        predicted_ids = self.model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)
        return transcription[0]
    
class Speech2Text:
    def __init__(self):
        self.whisper = Whisper()
        self.audio = pyaudio.PyAudio()

        self.stream = self.audio.open(format=FORMAT, channels=CHANNELS,
                                      rate=RATE, input=True,
                                      frames_per_buffer=CHUNK)

        self.stream.stop_stream()
        self.frames = []
        self.stop = True
        self.thread = None

    def recording(self):
        def __recording():
            self.stop = False
            self.frames = []
            self.stream.start_stream()
            while not self.stop:
                data = self.stream.read(CHUNK)
                self.frames.append(data)
            self.stream.stop_stream()
        self.thread = threading.Thread(target=__recording).start()
    
    def stop_recording(self):
        if self.stop:
            return False
        self.stop = True
        if self.thread:
            self.thread.join()
        return self.stop
        

    def terminate(self):
        try:
            self.stream.stop_stream()
        except:
            print("\nStream is stopped\n")
        self.stream.close()
        self.audio.terminate()

    def get_text(self):
        return self.whisper.transcribe(self.frames)


    
if __name__ == "__main__":
    whisper = Whisper()
    # Test the Whisper class
    test_frames = [b'\x00' * CHUNK] * 10  # Simulate 10 chunks of silent audio
    transcription = whisper.transcribe(test_frames)
    print("Transcription:", transcription)
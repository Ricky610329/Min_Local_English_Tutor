from kokoro import KPipeline
import soundfile as sf
from playsound import playsound

pipeline = KPipeline(lang_code='a')

def generate_sound(text):
    generator = pipeline(text, voice='af_heart', speed=1)
    for gs, ps, audio in generator:
        sf.write(f'output.wav', audio, 24000)
        playsound('output.wav')

import sounddevice as sd  # pip install sounddevice
import vosk  # pip install vosk
import queue
import json
from pydub import AudioSegment

q = queue.Queue()
model = vosk.Model('vosk_model')
device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])
def callback(indata, frames, time, status):
    q.put(bytes(indata))


def voice_func():
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                            channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                text = json.loads(rec.Result())['text']
                if len(text)>1:
                    return text

def record_voice_tg(file_name):
    rec = vosk.KaldiRecognizer(model, 16000)
    rec.SetWords(True)
    mp3 = AudioSegment.from_mp3(file_name)
    mp3 = mp3.set_channels(1)
    mp3 = mp3.set_frame_rate(16000)
    rec.AcceptWaveform(mp3.raw_data)
    result = rec.Result()
    text = json.loads(result)["text"]
    return text
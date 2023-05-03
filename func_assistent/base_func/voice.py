from func_assistent.base_func.speech import model_speech
from pydub import AudioSegment
from pydub.playback import play




def speaker(text):
	'''Озвучка текста'''
	model_speech(text)
	dialog_file = AudioSegment.from_file(file="test.wav", format="wav")
	play(dialog_file)

import torch


device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'
model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
model.to(device)



def model_speech(text):

    example_text = text
    sample_rate = 48000
    speaker='baya'

    audio_paths = model.save_wav(text=example_text,
                                 speaker=speaker,
                                 sample_rate=sample_rate)

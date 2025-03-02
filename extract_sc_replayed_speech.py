# coding: utf-8
import librosa
import librosa.display
import soundfile
import os


def extract_single_channel_wav(fpath, fname):
    y, sr = librosa.load(f"{fpath}/{fname}.wav", sr=16000, mono=False)
    if not os.path.exists(f"{fpath}/rvb-only"):
        os.makedirs(f"{fpath}/mixture")
        os.makedirs(f"{fpath}/clean")
        os.makedirs(f"{fpath}/rvb-only")
    soundfile.write(f"{fpath}/clean/{fname}.wav", y[15, :], sr)
    soundfile.write(f"{fpath}/rvb-only/{fname}.wav", y[16, :], sr)
    soundfile.write(f"{fpath}/mixture/{fname}.wav", y[0, :], sr)


path = "mixture_clean/eval"
name = "6343252661930009508-00020"
extract_single_channel_wav(path, name)

path = "mixture_clean/eval"
name = "6354369755148493407-00048"
extract_single_channel_wav(path, name)

path = "mixture_clean/eval"
name = "6364327207327548190-00036"
extract_single_channel_wav(path, name)

path = "mixture_clean/eval"
name = "6367813861908922495-00004"
extract_single_channel_wav(path, name)

path = "mixture_clean/eval"
name = "6368177216011755289-00003"
extract_single_channel_wav(path, name)

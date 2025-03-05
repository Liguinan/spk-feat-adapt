# coding: utf-8
import librosa
import librosa.display
import soundfile
import os


def extract_single_channel_wav(fpath, fname):
    y, sr = librosa.load(f"{fpath}/{fname}.wav", sr=16000, mono=False)
    if not os.path.exists(f"{fpath}/clean"):
        os.makedirs(f"{fpath}/clean")
        os.makedirs(f"{fpath}/rvb-only")
        os.makedirs(f"{fpath}/mixture")
    soundfile.write(f"{fpath}/clean/{fname}.wav", y[15, :], sr)
    soundfile.write(f"{fpath}/rvb-only/{fname}.wav", y[16, :], sr)
    soundfile.write(f"{fpath}/mixture/{fname}.wav", y[0, :], sr)


# dataset = "ECAPA"
# path = f"mixture_clean/dev/{dataset}"
# name = "LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# extract_single_channel_wav(path, name)
#
# dataset = "ECAPA"
# path = f"mixture_clean/dev/{dataset}"
# name = "LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# extract_single_channel_wav(path, name)
#
# dataset = "ECAPA"
# path = f"mixture_clean/dev/{dataset}"
# name = "LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# extract_single_channel_wav(path, name)


dataset = "xvector"
path = f"mixture_clean/dev/{dataset}"
name = "LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
extract_single_channel_wav(path, name)

dataset = "xvector"
path = f"mixture_clean/dev/{dataset}"
name = "LRS3XX-01903-TEDXXXXX-XXXXXX-ih_10000015_0000002_0000605"
extract_single_channel_wav(path, name)

dataset = "xvector"
path = f"mixture_clean/dev/{dataset}"
name = "LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
extract_single_channel_wav(path, name)

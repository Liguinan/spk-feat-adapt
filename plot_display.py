# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import matplotlib.pyplot as plt


def print_figure(name):
    y, sr = librosa.load(f"{name}.wav", sr=16000, mono=False)
    # fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig, ax = plt.subplots()
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=512, hop_length=256)), ref=np.max)
    img = librosa.display.specshow(D, y_axis='linear', x_axis='s', hop_length=256, sr=sr, ax=ax)
    # ax.set(title='Linear-frequency power spectrogram')
    # ax.label_outer()
    plt.savefig(f"{name}.png")
    # plt.show()

#################### ECAPA #################
# data_type="ECAPA"
# data_mixture="clean"
# name1 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)

# data_mixture = "rvb-only"
# name1 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)

# data_mixture = "mixture"
# name1 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)

# name1 = f"Enrolment-free/{data_type}/dev/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"Enrolment-free/{data_type}/dev/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"Enrolment-free/{data_type}/dev/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)

# name1 = f"Enrolment-free/{data_type}/av-dev/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"Enrolment-free/{data_type}/av-dev/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"Enrolment-free/{data_type}/av-dev/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)
#
# data_quantity = "1utt"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)
#
# data_quantity = "10%"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)
#
# data_quantity = "25%"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)
#
# data_quantity = "50%"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)
#
# data_quantity = "75%"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)
#
# data_quantity = "100%"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)


# name1 = f"SI/dev/{data_type}/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"SI/dev/{data_type}/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"SI/dev/{data_type}/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)

# name1 = f"SI/av-dev/{data_type}/rev1-LRS3XX-01096-TEDXXXXX-XXXXXX-ih_10000015_0000223_0000597"
# print_figure(name1)
# name2 = f"SI/av-dev/{data_type}/rev1-LRS3XX-01344-TEDXXXXX-XXXXXX-ih_10000021_0000000_0000298"
# print_figure(name2)
# name3 = f"SI/av-dev/{data_type}/rev2-LRS3XX-02221-TEDXXXXX-XXXXXX-ih_10000046_0000000_0000457"
# print_figure(name3)


#################### xvector #################
# clean xvector
# data_type = "xvector"
# data_mixture = "clean"
# name1 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)

# data_mixture = "rvb-only"
# name1 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)
#
# data_mixture = "mixture"
# name1 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"mixture_clean/dev/{data_type}/{data_mixture}/LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)

# name1 = f"Enrolment-free/{data_type}/dev/rev1-LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"Enrolment-free/{data_type}/dev/rev1-LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"Enrolment-free/{data_type}/dev/rev4-LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)
#
# data_quantity = "1utt"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev4-LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)
#
# data_quantity = "10"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev4-LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)
#
# data_quantity = "25"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev4-LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)
#
# data_quantity = "50"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev4-LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)
#
# data_quantity = "75"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev4-LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)
#
# data_quantity = "100"
# name1 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev1-LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"Enrolment-based/{data_type}/dev/{data_quantity}/rev4-LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)

# name1 = f"SI/dev/{data_type}/rev1-LRS3XX-00203-TEDXXXXX-XXXXXX-ih_10000018_0000001_0000349"
# print_figure(name1)
# name2 = f"SI/dev/{data_type}/rev1-LRS3XX-01060-TEDXXXXX-XXXXXX-ih_10000002_0000466_0000861"
# print_figure(name2)
# name3 = f"SI/dev/{data_type}/rev4-LRS3XX-05072-TEDXXXXX-XXXXXX-ih_00050009_0000000_0000592"
# print_figure(name3)


#################### Replay #################
data_type = "eval"
data_mixture = "clean"
# name1 = f"mixture_clean/{data_type}/{data_mixture}/6367813861908922495-00004"
# print_figure(name1)
name2 = f"mixture_clean/{data_type}/{data_mixture}/6364327207327548190-00036"
print_figure(name2)
name3 = f"mixture_clean/{data_type}/{data_mixture}/6368177216011755289-00003"
print_figure(name3)
#
data_mixture = "rvb-only"
# name1 = f"mixture_clean/{data_type}/{data_mixture}/6367813861908922495-00004"
# print_figure(name1)
name2 = f"mixture_clean/{data_type}/{data_mixture}/6364327207327548190-00036"
print_figure(name2)
name3 = f"mixture_clean/{data_type}/{data_mixture}/6368177216011755289-00003"
print_figure(name3)
#
data_mixture = "mixture"
# name1 = f"mixture_clean/{data_type}/{data_mixture}/6367813861908922495-00004"
# print_figure(name1)
name2 = f"mixture_clean/{data_type}/{data_mixture}/6364327207327548190-00036"
print_figure(name2)
name3 = f"mixture_clean/{data_type}/{data_mixture}/6368177216011755289-00003"
print_figure(name3)
#
# name1 = f"SI/{data_type}/rev1-6367813861908922495-00004"
# print_figure(name1)
name2 = f"SI/{data_type}/rev1-6364327207327548190-00036"
print_figure(name2)
name3 = f"SI/{data_type}/rev1-6368177216011755289-00003"
print_figure(name3)
#
# name1 = f"SI/av-{data_type}/rev1-6367813861908922495-00004"
# print_figure(name1)
name2 = f"SI/av-{data_type}/rev1-6364327207327548190-00036"
print_figure(name2)
name3 = f"SI/av-{data_type}/rev1-6368177216011755289-00003"
print_figure(name3)
#
# name1 = f"Enrolment-free/ECAPA/{data_type}/rev1-6367813861908922495-00004"
# print_figure(name1)
name2 = f"Enrolment-free/ECAPA/{data_type}/rev1-6364327207327548190-00036"
print_figure(name2)
name3 = f"Enrolment-free/ECAPA/{data_type}/rev1-6368177216011755289-00003"
print_figure(name3)
#
#
# name1 = f"Enrolment-free/ECAPA/av-{data_type}/rev1-6367813861908922495-00004"
# print_figure(name1)
name2 = f"Enrolment-free/ECAPA/av-{data_type}/rev1-6364327207327548190-00036"
print_figure(name2)
name3 = f"Enrolment-free/ECAPA/av-{data_type}/rev1-6368177216011755289-00003"
print_figure(name3)

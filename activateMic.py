import sounddevice as sd
from scipy.io.wavfile import write

def micStart():
    print('start recording....')
    fs = 44100  # Sample rate
    seconds = 7  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('mp3/recording.wav', fs, myrecording)  # Save as WAV file 
    print('ended recording and wrote out!')


if __name__ == '__main__':
    micStart()

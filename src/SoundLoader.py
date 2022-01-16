import os
import sys
import wave

from openal import al


# load and store a wav file into an openal buffer
class SoundLoader:
    def __init__(self, filename):
        self.name = filename
        # load/set wav file
        if len(sys.argv) < 2:
            dirname = os.path.dirname(os.path.realpath(__file__)) + '/../resources'
            f_name = os.path.join(dirname, filename)
        else:
            f_name = sys.argv[1]

        wave_fp = wave.open(f_name)
        channels = wave_fp.getnchannels()
        bitrate = wave_fp.getsampwidth() * 8
        samplerate = wave_fp.getframerate()
        wave_buffer = wave_fp.readframes(wave_fp.getnframes())
        self.duration = (len(wave_buffer) / float(samplerate)) / 2
        self.length = len(wave_buffer)
        format_map = {
            (1, 8): al.AL_FORMAT_MONO8,
            (2, 8): al.AL_FORMAT_STEREO8,
            (1, 16): al.AL_FORMAT_MONO16,
            (2, 16): al.AL_FORMAT_STEREO16,
        }
        al_format = format_map[(channels, bitrate)]

        self.buffer = al.ALuint(0)
        al.alGenBuffers(1, self.buffer)
        # allocate buffer space to: buffer, format, data, len(data), and samplerate
        al.alBufferData(self.buffer, al_format, wave_buffer, len(wave_buffer), samplerate)

    # delete loaded sound
    def delete(self):
        al.alDeleteBuffers(1, self.buf)

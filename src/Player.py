from openal import al


# load sound buffers into an openal source player to play them
class Player:
    # load default settings
    def __init__(self):
        # load source player
        self.source = al.ALuint(0)
        al.alGenSources(1, self.source)
        # disable rolloff factor by default
        al.alSourcef(self.source, al.AL_ROLLOFF_FACTOR, 0)
        # disable source relative by default
        al.alSourcei(self.source, al.AL_SOURCE_RELATIVE, 0)
        # capture player state buffer
        self.state = al.ALint(0)
        # set internal variable tracking
        self._volume = 1.0
        self._pitch = 1.0
        self._position = [0, 0, 0]
        self._rolloff = 1.0
        self._loop = False
        self.queue = []

    # set rolloff factor, determines volume based on distance from listener
    def _set_rolloff(self, value):
        self._rolloff = value
        al.alSourcef(self.source, al.AL_ROLLOFF_FACTOR, value)

    def _get_rolloff(self):
        return self._rolloff

    # set whether looping or not - true/false 1/0
    def _set_loop(self, lo):
        self._loop = lo
        al.alSourcei(self.source, al.AL_LOOPING, lo)

    def _get_loop(self):
        return self._loop

    # set player position
    def _set_position(self, pos):
        self._position = pos
        x, y, z = map(int, pos)
        al.alSource3f(self.source, al.AL_POSITION, x, y, z)

    def _get_position(self):
        return self._position

    # set pitch - 1.5-0.5 float range only
    def _set_pitch(self, pit):
        self._pitch = pit
        al.alSourcef(self.source, al.AL_PITCH, pit)

    def _get_pitch(self):
        return self._pitch

    # set volume - 1.0 float range only
    def _set_volume(self, vol):
        self._volume = vol
        al.alSourcef(self.source, al.AL_GAIN, vol)

    def _get_volume(self):
        return self._volume

    # queue a sound buffer
    def add(self, sound):
        al.alSourceQueueBuffers(self.source, 1, sound.buffer)  # self.buf
        self.queue.append(sound)

    # remove a sound from the queue (detach & unqueue to properly remove)
    def remove(self):
        if len(self.queue) > 0:
            al.alSourceUnqueueBuffers(self.source, 1, self.queue[0].buffer)  # self.buf
            al.alSourcei(self.source, al.AL_BUFFER, 0)
            self.queue.pop(0)

    # play sound source
    def play(self):
        al.alSourcePlay(self.source)

    # get current playing state
    def playing(self):
        al.alGetSourcei(self.source, al.AL_SOURCE_STATE, self.state)
        if self.state.value == al.AL_PLAYING:
            return True
        else:
            return False

    # stop playing sound
    def stop(self):
        al.alSourceStop(self.source)

    # rewind player
    def rewind(self):
        al.alSourceRewind(self.source)

    # pause player
    def pause(self):
        al.alSourcePause(self.source)

    # delete sound source
    def delete(self):
        al.alDeleteSources(1, self.source)

    # Go straight to a set point in the sound file
    def _set_seek(self, offset):  # float 0.0-1.0
        al.alSourcei(self.source, al.AL_BYTE_OFFSET, int(self.queue[0].length * offset))

    # returns current buffer length position (IE: 21000), so divide by the buffers self.length
    def _get_seek(self):  # returns float 0.0-1.0
        al.alGetSourcei(self.source, al.AL_BYTE_OFFSET, self.state)
        return float(self.state.value) / float(self.queue[0].length)

    rolloff = property(_get_rolloff, _set_rolloff, doc="""get/set rolloff factor""")
    volume = property(_get_volume, _set_volume, doc="""get/set volume""")
    pitch = property(_get_pitch, _set_pitch, doc="""get/set pitch""")
    loop = property(_get_loop, _set_loop, doc="""get/set loop state""")
    position = property(_get_position, _set_position, doc="""get/set position""")
    seek = property(_get_seek, _set_seek, doc="""get/set the current play position""")
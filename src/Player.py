from openal import al


# load sound buffers into an openal source player to play them
class Player:
    # load default settings
    def __init__(self):

    # set rolloff factor, determines volume based on distance from listener
    def _set_rolloff(self, value):

    def _get_rolloff(self):

    # set whether looping or not - true/false 1/0
    def _set_loop(self, lo):

    def _get_loop(self):

    # set player position
    def _set_position(self, pos):

    def _get_position(self):

    # set pitch - 1.5-0.5 float range only
    def _set_pitch(self, pit):

    def _get_pitch(self):

    # set volume - 1.0 float range only
    def _set_volume(self, vol):

    def _get_volume(self):

    # queue a sound buffer
    def add(self, sound):

    # remove a sound from the queue (detach & unqueue to properly remove)
    def remove(self):

    # play sound source
    def play(self):
        al.alSourcePlay(self.source)

    # get current playing state
    def playing(self):

    # stop playing sound
    def stop(self):

    # rewind player
    def rewind(self):

    # pause player
    def pause(self):

    # delete sound source
    def delete(self):

    # Go straight to a set point in the sound file
    def _set_seek(self, offset):  # float 0.0-1.0

    # returns current buffer length position (IE: 21000), so divide by the buffers self.length
    def _get_seek(self):  # returns float 0.0-1.0

    rolloff = property(_get_rolloff, _set_rolloff, doc="""get/set rolloff factor""")
    volume = property(_get_volume, _set_volume, doc="""get/set volume""")
    pitch = property(_get_pitch, _set_pitch, doc="""get/set pitch""")
    loop = property(_get_loop, _set_loop, doc="""get/set loop state""")
    position = property(_get_position, _set_position, doc="""get/set position""")
    seek = property(_get_seek, _set_seek, doc="""get/set the current play position""")
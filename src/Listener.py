from openal import al, alc


# load a listener to load and play sounds.
class Listener:
    def __init__(self):

    # list number of available hrtf tables
    def _hrtf_tables(self):

    # assign hrtf table to device and soft reboot to take effect
    def _set_hrtf(self, num):

    # confirm hrtf has been loaded and is enabled
    def _get_hrtf(self):

    # set player position
    def _set_position(self, pos):

    def _get_position(self):

    # delete current listener
    def delete(self):

    position = property(_get_position, _set_position, doc="""get/set position""")
    hrtf = property(_get_hrtf, _set_hrtf, doc="""get status/set hrtf""")
    hrtf_tables = property(_hrtf_tables, None, doc="""get number of hrtf tables""")

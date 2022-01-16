from openal import al, alc


# load a listener to load and play sounds.
class Listener:
    def __init__(self):
        # load device/context/listener
        self.device = alc.alcOpenDevice(None)
        self.context = alc.alcCreateContext(self.device, None)
        alc.alcMakeContextCurrent(self.context)

        # get list of available htrf tables
        self.hrtf_buffers = [alc.ALCint(), alc.ALCint * 4, alc.ALCint()]
        alc.alcGetIntegerv(self.device, alc.ALC_NUM_HRTF_SPECIFIERS_SOFT, 1, self.hrtf_buffers[0])

        # attributes for device to set specified hrtf table
        self.hrtf_select = self.hrtf_buffers[1](alc.ALC_HRTF_SOFT, alc.ALC_TRUE, alc.ALC_HRTF_ID_SOFT, 1)

    # list number of available hrtf tables
    def _hrtf_tables(self):
        return self.hrtf_buffers[0].value

    # assign hrtf table to device and soft reboot to take effect
    def _set_hrtf(self, num):
        if num is None:
            alc.alcResetDeviceSOFT(self.device, None)
        elif 0 <= num <= self.hrtf_buffers[0].value:
            self.hrtf_select[3] = num
            # reset the device so the new hrtf settings take effect
            alc.alcResetDeviceSOFT(self.device, self.hrtf_select)

    # confirm hrtf has been loaded and is enabled
    def _get_hrtf(self):
        alc.alcGetIntegerv(self.device, alc.ALC_HRTF_SOFT, 1, self.hrtf_buffers[2])
        if self.hrtf_buffers[2].value == alc.ALC_HRTF_DISABLED_SOFT:
            return False
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_ENABLED_SOFT:
            return True
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_DENIED_SOFT:
            return False
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_REQUIRED_SOFT:
            return True
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_HEADPHONES_DETECTED_SOFT:
            return True
        elif self.hrtf_buffers[2].value == alc.ALC_HRTF_UNSUPPORTED_FORMAT_SOFT:
            return False

    # set player position
    def _set_position(self, pos):
        self._position = pos
        x, y, z = map(int, pos)
        al.alListener3f(al.AL_POSITION, x, y, z)

    def _get_position(self):
        return self._position

    # delete current listener
    def delete(self):
        alc.alcDestroyContext(self.context)
        alc.alcCloseDevice(self.device)

    position = property(_get_position, _set_position, doc="""get/set position""")
    hrtf = property(_get_hrtf, _set_hrtf, doc="""get status/set hrtf""")
    hrtf_tables = property(_hrtf_tables, None, doc="""get number of hrtf tables""")

import os
import sys

from Listener import Listener
from Player import Player
from SoundLoader import SoundLoader

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))


if __name__ == '__main__':
    # load listener
    listener = Listener()
    # initialize sound
    sound = SoundLoader('tone5.wav')
    # load sound player
    player = Player()

    # set listener position
    listener.position = (0, 0, 0)
    # set player position
    player.position = (-200, 0, 300)

    # load sound into player
    player.add(sound)
    # enable loop sound so it plays forever
    player.loop = True
    # set rolloff factor
    player.rolloff = 0.01

    # enable hrtf default_44100 table
    listener.hrtf = 1

    # play sound
    player.play()
    exit_loop = False
    while not exit_loop:
        print('Listener position is: ' + str(listener.position))
        print('Sound is playing from: ' + str(player.position))
        print('Enter a position or quit with "q" or "Q": ')
        
        key = input()
        if key == 'q' or key == 'Q':
            exit_loop = True
        else:
            arr = key.split(' ')
            if len(arr) == 3:
                player.position = (int(arr[0]), int(arr[1]), int(arr[2]))
            else:
                print('Enter valid position or quit with "q" or "Q".')

    # stop player
    player.stop()

    # clean up resources
    player.delete()
    sound.delete()
    listener.delete()

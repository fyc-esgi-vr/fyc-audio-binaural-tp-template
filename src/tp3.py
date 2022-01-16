import os
import sys
import time

from Listener import Listener
from Player import Player
from SoundLoader import SoundLoader

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))


def get_position_input():
    while True:
        print('Enter a position or quit with "q" or "Q": ')
        
        key = input()
        if key == 'q' or key == 'Q':
            return None
        else:
            arr = key.split(' ')
            if len(arr) == 3:
                return (int(arr[0]), int(arr[1]), int(arr[2]))
            else:
                print('Enter valid position or quit with "q" or "Q".')


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

    destination = (200, 0, 300)

    # load sound into player
    player.add(sound)
    # enable loop sound so it plays forever
    player.loop = True
    # set rolloff factor
    player.rolloff = 0.01

    # enable hrtf default_44100 table
    listener.hrtf = 1

    # play sound
    # player.play()
    
    player.position = get_position_input()
    destination = get_position_input()

    if player.position is not None and destination is not None:
        player.play()
        steps = 10

        dX = destination[0] - player.position[0]
        dY = destination[1] - player.position[1]
        dZ = destination[2] - player.position[2]

        for step in range(steps):
            time.sleep(1)
            factor = step / steps

            x = player.position[0] + dX * factor
            y = player.position[1] + dY * factor
            z = player.position[2] + dZ * factor

            player.position = (x, y, z)
            

    # stop player
    player.stop()

    # clean up resources
    player.delete()
    sound.delete()
    listener.delete()
import win32api as wapi
import os
import cv2
from grabscreen import grab_screen
import numpy as np


def key_press():
    if wapi.GetAsyncKeyState(32):
        return 1
    else:
        return 0


file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('Loading file')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    training_data = []

if __name__ == '__main__':
    while True:

        img = grab_screen(region=(500, 200, 1000, 380))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (50, 18))

        key = key_press()

        training_data.append([img, key])
        if len(training_data) % 600 == 0:
            np.save(file_name, training_data[120:-180])

import os
from random_words import RandomWords
import string
import random
import pyautogui
rw = RandomWords()

userprofile = str(os.environ['USERPROFILE'])

x = int(input('How many things to search: ')) # Number of times to search
a = 0


try:
    while(a<x):
        search_term = rw.random_word(random.choice(string.ascii_lowercase))
        os.system("start microsoft-edge:"+search_term)
        a += 1
        os.system("TIMEOUT /t 5")
        if(a>=x):
            print('Closing Tabs...')
            for i in range(x):
                pyautogui.keyDown('ctrl')
                pyautogui.press('w')
                pyautogui.keyUp('ctrl')
                print('Closed ' + str(i + 1) + ' tab')
            exit()
except Exception as e:
    print("Broke with " + e)
    os.system("pause")
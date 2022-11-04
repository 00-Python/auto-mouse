# x, y = pg.locateCenterOnScreen('button.png', confidence=0.5)
# print(x, y)
# pg.moveTo(x, y, duration=0.5)
'''This is a script to make random movements with the mouse using pyautogui'''
import pyautogui
import random
import human
from human import curve
import os


if __name__ == '__main__':
    try:
        # disable fail safe
        pyautogui.FAILSAFE = False
        # Disable pyautogui pauses (from DJV's answer)
        pyautogui.MINIMUM_DURATION = 0
        pyautogui.MINIMUM_SLEEP = 0
        pyautogui.PAUSE = 0
        while True:
            os.system('cls')
            inp = input('What do you want to do? (1) Counted , (2) Infinite , (3) Exit: \n')
            # Get the screen size
            width, height = pyautogui.size()
            if inp == '1':
                # clear the screen 
                os.system('cls')
                inp = input('Enter the amount:\n')
                os.system('cls')
                print('Working...')
                if inp != '':  
                    try:
                        for i in range(int(inp)):
                            # Get the current mouse position
                            x, y = pyautogui.position()
                            # Move the mouse to a random position with curve
                            curve((x, y), (random.randint(0, width), random.randint(0, height)), (random.randint(0, width), random.randint(0, height)), (random.randint(0, width), random.randint(0, height)), 100, 1)
                    except KeyboardInterrupt:
                        print('Exiting...')
                    os.system('cls')
                    
            elif inp == '2':
                try:
                    os.system('cls')
                    print('Working...')
                    print("Open this window and press CTRL+C to exit")
                    while True:
                        # print open window and press ctrl+c to exit
                        #start position
                        start = pyautogui.position()
                        # add random coordinates to end point
                        end = (start[0] + random.randrange(-500, 500, 55), start[1] + random.randrange(-500, 500, 45))
                        
                        # add random coordinates to control points
                        control1 = (start[0] + random.randrange(-500, 500, 75), start[1] + random.randrange(-500, 500, 65))
                        control2 = (start[0] + random.randrange(-500, 500, 65), start[1] + random.randrange(-500, 500, 75))
                        
                        # duration of movement
                        duration = random.randrange(1, 7, 2)
                        
                        # number of steps in curve
                        curve_steps = random.randint(50, 200)
                        
                        # call curve function
                        curve(start, end, control1, control2, curve_steps, duration)
                except KeyboardInterrupt:
                    print('Exiting...')
            elif inp == '3':
                break
            else:
                os.system('cls')
                print('Invalid input')
    except KeyboardInterrupt:
        print('Exiting...')
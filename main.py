# x, y = pg.locateCenterOnScreen('button.png', confidence=0.5)
# print(x, y)
# pg.moveTo(x, y, duration=0.5)
'''This is a script to make random movements with the mouse using pyautogui'''
import pyautogui
import random
import human
from human import curve
import os

def download(url):
    # Download image from imgur with requests
    import requests
    r = requests.get(url, allow_redirects=True)
    # get filename from url
    filename = url.split('/')[-1]
    # write to file
    open(filename, 'wb').write(r.content)
    return filename
    
def delete(filename):
    # Delete file
    os.remove(filename)

def negativeNumber(x):
    neg = x * (-1)
    return neg


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
            inp = input('What do you want to do? (1) Counted , (2) Infinite , (3) Object from Image, (E) Exit: \n')
            # Get the screen size
            width, height = pyautogui.size()
            neg_width = negativeNumber(width)
            neg_height = negativeNumber(height)
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
                try:
                    os.system('cls')
                    inp = input('(1) Single (2) Chain\n')
                    if inp == '1':
                    # clear the screen
                        os.system('cls')
                        inp = input('(1) Local, (2) Online \n')
                        if inp == '1':
                            # clear the screen
                            os.system('cls')
                            inp = input('Enter the path of the image: \n')
                            # get the center of the image
                            x, y = pyautogui.locateCenterOnScreen(inp, confidence=0.9)
                            # move to the center of the image
                            rand_x = random.randrange(neg_width/2, width/2, x)
                            rand_y = random.randrange(neg_height/2, height/2, y)
                            curve(pyautogui.position(), (x, y), (rand_x/21,rand_y/24), (rand_x/24,rand_y/21), 100, 1)
                            
                        elif inp == '2':
                            # clear the screen
                            os.system('cls')
                            inp = input('Enter the url of the image: \n')
                            # download the image
                            filename = download(inp)
                            # get the center of the image
                            x, y = pyautogui.locateCenterOnScreen(filename, confidence=0.9)
                            # random number between half og neg_width and half of width
                            rand_x = random.randrange(neg_width/2, width/2, x)
                            rand_y = random.randrange(neg_height/2, height/2, y)
                            curve(pyautogui.position(), (x, y), (rand_x/21,rand_y/24), (rand_x/24,rand_y/21), 100, 1)
                            # delete the file
                            delete(filename)
                    elif inp == '2':
                        inp = input('(1) Local, (2) Online \n')
                        if inp == '1':
                            inp = int(input('Enter the steps: \n'))
                            
                        
                except KeyboardInterrupt:
                    os.system('cls')
                    print('Exiting...')
            elif inp == 'E' or inp == 'e':
                break
            else:
                os.system('cls')
                print('Invalid input')
    except KeyboardInterrupt:
        os.system('cls')
        print('Exiting...')
import pyautogui
import human
import random
import os
t1 = int(input("Min Time 'secs': "))
t2 = int(input("Max Time 'secs': "))
clicks = int(input("Number of clicks each movement: "))
pyautogui.FAILSAFE = False
# get screen size
width, height = pyautogui.size()

while True:
    try:
        os.system("cls")
        # get position of mouse
        x, y = pyautogui.position()
        
        #get random time between t1 and t2
        time = random.randint(t1, t2)

        ## sleep for 2 minutes
        pyautogui.sleep(time)

        # get new position of mouse in different variables
        x2, y2 = pyautogui.position()

        #if the mouse has not moved, then move mouse with curve
        
        if x == x2 and y == y2:
            ## move mouse with curve to random position
            human.curve((x, y), (random.randint(80, 1634), random.randint(0, 40)), (random.randint(0, width), random.randint(0, height)), (random.randint(0, width), random.randint(0, height)), 100, 2)
            if clicks != "" or clicks != "0":
                # get new position of mouse
                x3, y3 = pyautogui.position()
                for click in range(clicks):
                    print(click)
                    if x3 > 80 and x3 < 1634 and y3 < 40: 
                        pyautogui.click()

    except KeyboardInterrupt:
        print('Done.')
        break
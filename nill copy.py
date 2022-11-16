import pyautogui
import human
import random
import os
import threading

def nill():
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
                human.curve((x, y), (random.randint(80, 1634), random.randint(0, 5)), (random.randint(0, width), random.randint(0, height)), (random.randint(0, width), random.randint(0, height)), 100, 2)
                if clicks != "" or clicks != "0":
                    # get new position of mouse
                    x3, y3 = pyautogui.position()
                    for click in range(clicks):
                        print(click)
                        if x3 > 80 and x3 < 1634 and y3 < 40: 
                            pyautogui.click()
        except KeyboardInterrupt:
            break
def open_rnd():
    urls = ['https://www.elevatema.com.au/', 'https://www.gforcema.com/', 'https://www.smafoxford.com/', 'https://www.martialarts4u.co.uk/', 'https://www.ikigai-dojo.org/', 'https://www.senjokaikarate.co.uk/', 'https://www.dynamixhinckley.com/', 'https://www.eagle-institute.com/', 'https://www.lanarkshirekarateacademy.co.uk/', 'https://www.tsxmartialarts.com/', 'https://www.pmaleeds.com/', 'https://www.nptkd.co.uk/', 'https://www.immortal365.co.uk/', 'https://www.wmac.eu/', 'https://www.oxfordkarateacademy.com/', 'https://www.southcoastckd.com/', 'https://www.sengoku.co.uk/', 'https://www.okamima.com/', 'https://www.kaijuma.co.uk/', 'https://www.urbanmartialartsfitness.com/', 'https://www.thekaratedojo.co.uk/', 'https://www.graciebarrahuddersfield.co.uk/', 'https://www.fsma.co.uk/', 'https://www.kravmagasomerset.co.uk/', 'https://www.ellismartialarts.com/', 'https://www.shudokan.co.uk/', 'https://www.missionfitnessmartialarts.co.uk/', 'https://www.pmachelmsford.com/', 'https://www.dojovanrel.com/', 'https://www.pmaabergele.com/']
    try:
        while True:
            for url in urls:
                # new tab
                pyautogui.hotkey('ctrl', 't')
                # pause 40 seconds
                pyautogui.sleep(40)
                # go to url
                # select url bar
                pyautogui.hotkey('ctrl', 'l')
                
                pyautogui.typewrite(url)
                # wait 20 seconds
                pyautogui.sleep(20)
                # select search bar
                pyautogui.hotkey('ctrl', 'l')
                # press enter
                pyautogui.press('enter')
                # wait 5 minutes
                pyautogui.sleep(300)
                for i in range(3):
                    # locate center of screen
                    pyautogui.moveTo(width/2, height/2)
                    
                    pyautogui.click()
                    
                    # scroll down random amount
                    pyautogui.scroll(random.randint(100, 400))
                    # wait 2 minutes
                    pyautogui.sleep(120)
                    # scrol down random amount
                    pyautogui.scroll(random.randint(100, 1000))
                    # wait 2 minutes
                    pyautogui.sleep(120)
                    # scroll up random amount
                    pyautogui.scroll(random.randint(-100, -1000))
                    # wait 1 minutes
                    pyautogui.sleep(60)
                    # scroll up random amount
                    pyautogui.scroll(random.randint(-100, -400))
                # close tab
                pyautogui.hotkey('ctrl', 'w')
            # wait 5 minutes
            pyautogui.sleep(300)
    except KeyboardInterrupt:
        pass
    
t1 = int(input("Min Time 'secs': "))
t2 = int(input("Max Time 'secs': "))
clicks = int(input("Number of clicks each movement: "))
pyautogui.FAILSAFE = False
# get screen size
width, height = pyautogui.size()



try:
    #  run nill in thread 1
    thread1 = threading.Thread(target=nill)
    thread2 = threading.Thread(target=open_rnd)
    
    
    thread1.start()
    thread2.start()
except KeyboardInterrupt:
    print('Done.')

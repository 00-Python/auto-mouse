# This is Go - The Auto Mouse
## What can it do?
Creates random amount or Specified amout of mouse movements with a more human like curve using the bezier library. So far it can do 3 things:

    1. Make a specified number of random movements with human-like curvature 
    2. Infinitley move around the screen to random positions with human-like curvature
    3. Locate Image/s on Screen and and move mouse to them with human-like curvature 
If  you are using the image feature you can specify a local image on your machine or you can specify a weblink such as: https://i.imgur.com/g756vf6hd.png

The script will download the image or images move around and click around, then it will delete them from your system.

## What is nill.py?
Nill is a anti idling script. You execute the script with `python nill.py` then you enter a time frame in seconds and if you want it to click or not. 
The script then starts a infinite loop, gets your mouse position, then, it picks a random number between your given timeframe and waits the selected amount of time and finally it checks the mouse position again and compares it to the original. If you have not moved the mouse it will create a human like curb to a random area between x = 80-1634 and y = 0-40, and click if specified.

## Install
    1. clone this repository
    2. cd in to the cloned repo
    3. pip install -r requirements.txt
    4. then run the Go.py or nill.py file
## Usage

1. Run
2. Follow on Screen Instructions
3. Enjoy!




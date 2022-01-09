import pyautogui as pg
import sys
#sys.path.append('./venv/lib/python3.8/site-packages/pywhatkit_custom/')
import pywhatkit as kit
from datetime import datetime

today= datetime.now()

kit.sendwhatmsg('+918591640066', str(today) + ' Hi There: From Swapnil!',15,37)


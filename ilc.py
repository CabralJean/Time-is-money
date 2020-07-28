import os
import pyautogui
from datetime import date

dthj = date.today()
day = 1 #dthj.weekday()

os.chdir("C:\Program Files\IBM\BMS\ILC")
os.startfile("ilcnew.bat")
pyautogui.sleep(3)
pyautogui.write('MandragoraParanaens')
pyautogui.press('enter')
pyautogui.sleep(5)

#Lanca as horas do dia
if day == 0:   #Segunda
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\icons\awi.png',
                                   grayscale=True, confidence=.5)
    pyautogui.sleep(2)
    pyautogui.click(loc)

    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('BZE38M')

    pyautogui.sleep(1)

    pyautogui.press('enter')
    pyautogui.sleep(0.2)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    pyautogui.press('enter')
    pyautogui.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('enter')
    # Insercao das horas
    lanc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\weekdays\mon.png',
                                    grayscale=True, confidence=.9)
    pyautogui.sleep(0.5)
    lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
    #pyautogui.click(lanc)
    pyautogui.doubleClick(lanc)
    pyautogui.write("8")
    pyautogui.press("enter")

    pyautogui.sleep(0.5)
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\icons\save.png',
                                   grayscale=True, confidence=.5)
    pyautogui.sleep(0.5)
    pyautogui.click(loc)
elif day == 1: #Terca
    pyautogui.sleep(2)
    lanc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\weekdays\tue.png',
                                    grayscale=True, confidence=.9)
    print(lanc)
    pyautogui.sleep(0.5)
    lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
    pyautogui.doubleClick(lanc)
    pyautogui.write("8")
    pyautogui.press("enter")

    pyautogui.sleep(0.5)
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\icons\save.png',
                                   grayscale=True, confidence=.5)
    pyautogui.sleep(0.5)
    pyautogui.click(loc)
elif day == 2: #Quarta
    pyautogui.sleep(2)
    lanc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\weekdays\wed.png',
                                    grayscale=True, confidence=.9)
    pyautogui.sleep(0.5)
    lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
    pyautogui.click(lanc)
    pyautogui.write("8")
    pyautogui.press("enter")

    pyautogui.sleep(0.5)
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\icons\save.png',
                                   grayscale=True, confidence=.5)
    pyautogui.sleep(0.5)
    pyautogui.click(loc)
elif day == 4: #Quinta
    pyautogui.sleep(2)
    lanc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\weekdays\thu.png',
                                    grayscale=True, confidence=.9)
    pyautogui.sleep(0.5)
    lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
    pyautogui.click(lanc)
    pyautogui.write("8")
    pyautogui.press("enter")

    pyautogui.sleep(0.5)
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\icons\save.png',
                                   grayscale=True, confidence=.5)
    pyautogui.sleep(0.5)
    pyautogui.click(loc)
elif day == 5: #Sexta
    pyautogui.sleep(2)
    lanc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\weekdays\fri.png',
                                    grayscale=True, confidence=.9)
    pyautogui.sleep(0.5)
    lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
    pyautogui.click(lanc)
    pyautogui.write("8")
    pyautogui.press("enter")

    pyautogui.sleep(0.5)
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\icons\save.png',
                                   grayscale=True, confidence=.5)
    pyautogui.sleep(0.5)
    pyautogui.click(loc)
elif day == 6: #Sabado
    lanc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\weekdays\sat.png',
                                    grayscale=True, confidence=.9)
    pyautogui.sleep(0.5)
    lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
    pyautogui.click(lanc)
    pyautogui.write("8")
    pyautogui.press("enter")

    pyautogui.sleep(0.5)
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\icons\save.png',
                                   grayscale=True, confidence=.5)
    pyautogui.sleep(0.5)
    pyautogui.click(loc)
elif day == 6: #Domingo
    lanc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\weekdays\sun.png',
                                    grayscale=True, confidence=.9)
    pyautogui.sleep(0.5)
    lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
    pyautogui.click(lanc)
    pyautogui.write("8")
    pyautogui.press("enter")

    pyautogui.sleep(0.5)
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\TimeIsMoney\icons\save.png',
                                   grayscale=True, confidence=.5)
    pyautogui.sleep(0.5)
    pyautogui.click(loc)

#print(pyautogui.position())# 1152 342 72 37
#print(pos.x, pos.y)


#os.chdir("C:\Program Files\IBM\BMS\ILC")
#os.startfile("ilcnew.bat")

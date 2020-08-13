import pyautogui
import subprocess
import win32api

program = 'C:\Program Files (x86)\CERTPONTO\Repv.exe'
subprocess.Popen(program)
#shell = win32com.client.Dispatch("WScript.Shell")
pyautogui.sleep(5)
cca = True
while cca:
    lanc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\qui.png',
            grayscale=True, confidence=.9)
    if cca != None:
        cca = False
    pyautogui.sleep(0.5)
    print(lanc)

pyautogui.write("075040")
pyautogui.press("enter")



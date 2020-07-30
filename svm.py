from selenium import webdriver
import pyautogui
from datetime import date

dthj = date.today()
day = dthj.weekday()
#browse = webdriver.Firefox(executable_path = r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\FirefoxDriver\geckodriver.exe')
browse = webdriver.Chrome(executable_path= r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\ChromeDriver84\chromedriver.exe')
browse.get("http://")

loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\isc.png',
                               grayscale=True, confidence=.5)
loc = (loc.left, loc.top + 65, loc.width, loc.height)
pyautogui.click(loc)
pyautogui.write('')
pyautogui.press('tab')
pyautogui.write('')
pyautogui.press('enter')

adh = True
while adh:
    loc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\adh.png',
                                   grayscale=True, confidence=.5)
    if loc != None:
        adh = False
    pyautogui.sleep(0.5)
#(TO DO) - Acrescentar um timeout
pyautogui.click(loc)

if day == 0:   #Segunda
    print("Seg")
elif day == 1:  # Terca
    print("Ter")
elif day == 2:  # Quarta
    qua = True
    while qua:
        lanc = pyautogui.locateOnScreen(r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\qua.png',
                                        grayscale=True, confidence=.9)
        if lanc != None:
            qua = False
        pyautogui.sleep(0.5)

    lanc = (lanc.left, lanc.top + 100, lanc.width, lanc.height)
    pyautogui.click(lanc)
    pyautogui.write("8")
    pyautogui.press("tab")
    pyautogui.press("enter")
elif day == 4:  # Quinta
    print()
elif day == 5:  # Sexta
    print()
elif day == 6: #Sabado
    print()
elif day == 6:  # Domingo
    print()



#response = requests.get('http://')

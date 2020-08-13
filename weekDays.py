import pyautogui


class DaysWeek:

    def monday(self):
        loc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\awi.png',
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
        lanc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\mon.png',
            grayscale=True, confidence=.9)
        pyautogui.sleep(0.5)
        lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
        # pyautogui.click(lanc)
        pyautogui.doubleClick(lanc)
        pyautogui.write("8")
        pyautogui.press("enter")

        pyautogui.sleep(0.5)
        loc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\save.png',
            grayscale=True, confidence=.5)
        pyautogui.sleep(0.5)
        pyautogui.click(loc)

        return True

    def tuesday(self):
        pyautogui.sleep(2)
        lanc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\tue.png',
            grayscale=True, confidence=.9)
        pyautogui.sleep(0.5)
        lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
        pyautogui.doubleClick(lanc)
        pyautogui.write("8")
        pyautogui.press("enter")

        pyautogui.sleep(0.5)
        loc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\save.png',
            grayscale=True, confidence=.5)
        pyautogui.sleep(0.5)
        pyautogui.click(loc)

        return True

    def wednesday(self):
        pyautogui.sleep(2)
        lanc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\wed.png',
            grayscale=True, confidence=.9)
        pyautogui.sleep(0.5)
        lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
        pyautogui.click(lanc)
        pyautogui.write("8")
        pyautogui.press("enter")

        pyautogui.sleep(0.5)
        loc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\save.png',
            grayscale=True, confidence=.5)
        pyautogui.sleep(0.5)
        pyautogui.click(loc)

        return True

    def thursday(self):
        pyautogui.sleep(2)
        lanc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\thu.png',
            grayscale=True, confidence=.9)
        print(lanc)
        pyautogui.sleep(0.5)
        lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
        pyautogui.click(lanc)
        pyautogui.write("8")
        pyautogui.press("enter")

        pyautogui.sleep(0.5)
        loc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\save.png',
            grayscale=True, confidence=.5)
        pyautogui.sleep(0.5)
        pyautogui.click(loc)

        return True

    def friday(self):
        pyautogui.sleep(2)
        lanc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\fri.png',
            grayscale=True, confidence=.9)
        pyautogui.sleep(0.5)
        lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
        pyautogui.click(lanc)
        pyautogui.write("8")
        pyautogui.press("enter")

        pyautogui.sleep(0.5)
        loc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\save.png',
            grayscale=True, confidence=.5)
        pyautogui.sleep(0.5)
        pyautogui.click(loc)

        return True

    def saturday(self):
        lanc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\sat.png',
            grayscale=True, confidence=.9)
        pyautogui.sleep(0.5)
        lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
        pyautogui.click(lanc)
        pyautogui.write("8")
        pyautogui.press("enter")

        pyautogui.sleep(0.5)
        loc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\save.png',
            grayscale=True, confidence=.5)
        pyautogui.sleep(0.5)
        pyautogui.click(loc)

        return True

    def sunday(self):
        lanc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\weekdays\sun.png',
            grayscale=True, confidence=.9)
        pyautogui.sleep(0.5)
        lanc = (lanc.left, lanc.top + 25, lanc.width, lanc.height)
        pyautogui.click(lanc)
        pyautogui.write("8")
        pyautogui.press("enter")

        pyautogui.sleep(0.5)
        loc = pyautogui.locateOnScreen(
            r'C:\Users\JeanMichelMarquesCab\Desktop\TimeIsMoney\Time-is-money\icons\save.png',
            grayscale=True, confidence=.5)
        pyautogui.sleep(0.5)
        pyautogui.click(loc)

        return True
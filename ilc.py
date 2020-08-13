import os
import pyautogui
from datetime import date
from weekDays import DaysWeek


class Claimer:

    def claim(self):

        dthj = date.today()
        day = dthj.weekday()
        dWeek = DaysWeek()

        os.chdir("C:\Program Files\IBM\BMS\ILC")
        os.startfile("ilcnew.bat")
        pyautogui.sleep(3)
        pyautogui.write('MandragoraParanaens')
        pyautogui.press('enter')
        pyautogui.sleep(5)
        print(day)
        # Lanca as horas do dia
        if day == 0:  # Segunda
            ret = dWeek.monday()
            print(ret)
        elif day == 1:  # Terca
            ret = dWeek.tuesday()
            print(ret)
        elif day == 2:  # Quarta
            ret = dWeek.wednesday()
            print(ret)
        elif day == 3:  # Quinta
            print("Start Thursday...")
            ret = dWeek.thursday()
            print(ret)
        elif day == 4:  # Sexta
            ret = dWeek.friday()
            print(ret)
        elif day == 5:  # Sabado
            ret = dWeek.saturday()
            print(ret)
        elif day == 6:  # Domingo
            ret = dWeek.sunday()
            print(ret)

        return True


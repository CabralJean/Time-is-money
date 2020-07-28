import win32com
import subprocess
import win32api
import win32com.client as win


program = 'C:\Program Files (x86)\CERTPONTO\Repv.exe'
subprocess.Popen(program)
shell = win32com.client.Dispatch("WScript.Shell")
win32api.Sleep(20000)
shell.SendKeys("075000")
shell.SendKeys("{ENTER}")

#app = application.Application()
#appl.start("C:\Program Files (x86)\CERTPONTO\Repv.exe")
import subprocess
import pyfiglet

text = pyfiglet.figlet_format("Wifi  Pass")
print(text)
subprocess.call("netsh wlan show profile ")

print("Enter The Name Of A WIFI")
i = input()

subprocess.call("netsh wlan show profile key=clear "+ i ,shell=True )

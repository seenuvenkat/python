
import datetime

alarmH = int(input("What hour do u want the alarm? "))
alarmM = int(input("What minute do you want the alarm? "))
amPm = str(input("am or pm? "))

print("Waiting for alarm",alarmH,alarmM,amPm)
if (amPm == "pm"):
        alarmH = alarmH + 12
while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute) :
        print("Hy Lazy boy.. Plz wake up..You didn't complete your project ")
      
        break
print("exited")
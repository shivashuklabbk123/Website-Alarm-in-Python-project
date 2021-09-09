import time
import webbrowser
set_alarm = input("Setn the alarm as H:M:S-")
url = "https://github.com/shivashuklabbk123"
Actual_time = time.strftime("%H:%M:%S")
while(Actual_time!=set_alarm):
    print("The time is"+Actual_time)
    Actual_time = time.strftime("%I:%M:%S")
    time.sleep(1)
if(Actual_time == set_alarm):
    print("You should see your webpage now :-)")
    webbrowser.open(url)    
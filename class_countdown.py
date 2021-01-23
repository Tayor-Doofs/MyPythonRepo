import winsound
import time
seconds = int(input('please enter number of seconds'))

hours = seconds//(60*60)
mins = (seconds//60)%60 
second = seconds%60

#print (hours, mins, second)

end = 0
interval = -1

while True:
    while True:
        while True:

            if second == end:
                break

            second += interval
            print(hours, "hours ;", mins, "mins :", second, "secs")
            time.sleep(0.01)
        
        second = 60
        if mins == end:
            break
        mins += interval

    mins = 60
    if hours == end:
        break

    hours += interval

winsound.Beep(1000, 500)
time.sleep(0.01)
winsound.Beep(1000, 500)
time.sleep(0.01)
winsound.Beep(1000, 500)
time.sleep(0.01)
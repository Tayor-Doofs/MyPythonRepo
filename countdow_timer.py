import time
minute = int(input("Enter minute"))
secs = int(input("Enter seconds"))
interval = 1
end = 0

while True:
    
    while True:
        secs -= interval
        print(minute, "mins :", secs, "secs")
        time.sleep(1)
        if secs == end:
            break
    secs = 60
    if minute == end:
            break
    
    minute -= interval
    while True:
        
        while True:
            secs -= interval
            print(minute, "mins :", secs, "secs")
            time.sleep(1)
            if secs == end:
                break
        secs = 60
        if minute == end:
                break
        
        minute -= interval
     
# start = 0
# end = 5
# interval = 1

# while True:
#     start += interval
#     print(start)

#     if start == end:
#         break

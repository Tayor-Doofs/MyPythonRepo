# word = "i am a boy"

# for index, i in enumerate(word):
#     print(index,"-", i)



# import time

# seconds = int(input('please enter number of seconds'))

# hours = seconds//(60*60)
# mins = (seconds//60)%60 
# seconds = seconds%60

# for i in reversed(range(hours + 1)):
#     for j in reversed(range(mins + 1)):
#         for k in reversed(range(seconds)):
#             print(i, "hour", j, "min", k, "secs")
#             time.sleep(1)
#         seconds = 60
#     minute = 60


import time

seconds = int(input('please enter number of seconds'))

hours = seconds//(60*60)
mins = (seconds//60)%60 
seconds = seconds%60

for i in reversed(range(hours + 1)):
    for j in reversed(range(mins + 1)):
        for k in reversed(range(seconds+1)):
            print(i, "hour", j, "min", k, "secs", end = "")
            time.sleep(1)
            print("\r", end = "")
        seconds = 60
    minute = 60

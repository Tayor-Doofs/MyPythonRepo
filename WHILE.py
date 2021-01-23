#WHILELOOPS

start = 0
end = 5
interval = 1

while True:
    start += interval
    print(start)

    if start == end:
        break


#forloops

word = "colloqual"
target = "a"

for i in word:
    if i == target:
        print(f'Found letter {target}.')
        break
    else:
        print("Not found")

else:
    print("All values were tested and target was not found")


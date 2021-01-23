racers = ['mario', 'luigi', 'stone']

swapped_racers = []
i = -1
while i >= -(len(racers)):
    swapped_racers.append(racers[i])
    i += -1
print(swapped_racers)

print(racers.index('mario'))
# racers[0],racers[1],racers[2] = racers[-1],racers[-2],racers[-3]

# print(racers)
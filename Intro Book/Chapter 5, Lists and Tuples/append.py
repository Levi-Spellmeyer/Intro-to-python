list = []
for i in range(6):
    list += [i] # The brackets allow us to append a 1 item list which in this case is index i
    i+=1

print(list)

# IF instead of [i] we used a string 'string' the list would then become ['s', 't', 'r', 'i', 'n', 'g']
# if a tuple is on the right side of a += then its elements will also be added to the list
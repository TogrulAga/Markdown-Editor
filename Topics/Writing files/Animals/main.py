# read animals.txt
with open('animals.txt', 'r') as file:
    lines = file.readlines()
    lines = list(map(lambda x: x.rstrip('\n') + ' ', lines))
# and write animals_new.txt
with open('animals_new.txt', 'w') as file:
    file.writelines(lines)

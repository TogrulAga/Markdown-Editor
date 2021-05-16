# create the planets.txt
file = open("planets.txt", 'w', encoding='utf-8')
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets = list(map(lambda x: x + '\n', planets))
file.writelines(planets)
file.close()

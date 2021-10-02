
class Planet:

    def __init__(self, name):
        self.name = name
        self.direct_orbit = None
        self.orbits = []
        planets[self.name] = self


tot = 0
orbits = []
f = open("day6_input.txt", "r")
for line in f:
    orbits.append(line.strip().split(")"))
planets = {}
for system in orbits:
    if system[0] in planets:
        center = planets[system[0]]
    else:
        center = Planet(system[0])
    if system[1] in planets:
        satellite = planets[system[1]]
    else:
        satellite = Planet(system[1])
    satellite.direct_orbit = center
    satellite.orbits.append(center)
changed = True
while changed:
    changed = False
    for planet_name in planets:
        planet = planets[planet_name]
        if planet.direct_orbit is not None:
            new_orbits = [planet.direct_orbit] + planet.direct_orbit.orbits
            if new_orbits != planet.orbits:
                planet.orbits = new_orbits
                changed = True
san = planets["SAN"]
you = planets["YOU"]
distances = []
for x in range(len(you.orbits)):
    for y in range(len(san.orbits)):
        if you.orbits[x] == san.orbits[y]:
            distances.append(x + y)
print(sorted(distances)[0])


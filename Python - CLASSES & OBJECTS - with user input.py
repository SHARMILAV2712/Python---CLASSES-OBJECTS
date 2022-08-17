#with user input
#In this code, the user can give input and can know whatever they need
#BY: SHARMILA.V_SIST
a = int(input("Enter the position of the planet to know about it:"))
class Solarsystem:
    def __init__(self,planetname,distance,mass,satellite,moons,nature):
        self.planetname = planetname
        self.distance = distance
        self.mass = mass
        self.satellite = satellite
        self.moons = moons
        self.nature = nature
    def features(self):
        planet = f"Planet Name:{self.planetname}\nDiastance:{self.distance}\nMass:{self.mass}\
        \nFamousSatellite:{self.satellite}\nMoons:{self.moons}\nNature of the Planet:{self.nature}"
        return planet
if a==1:
    planet1 = Solarsystem('Mercury','0.387AU','3.285x10^23 kg','Messenger','no moons','Solid and smallest planet of our SolarSystem')
    print(planet1.features())
elif a==2:
    planet2 = Solarsystem('Venus','0.722AU','4.867x10^24 kg','Mariner-10','no moons','Solid and the hottest planet also called as Earth twin and The morning star')
    print(planet2.features())
elif a==3:
     planet3 = Solarsystem('Earth','1AU','5.97x10^24 kg','There are numerous satellites that are orbitting the Earth','The Moon','The only planet that supports life')
     print(planet3.features())
elif a==4:
     planet4 = Solarsystem('Mars','1.52AU','6.39x10^23 kg','Mangalyaan','Phobos and Deimos','Red planet and the planet which humans will colonize in future ')
     print(planet4.features())
elif a==5:
     planet5 = Solarsystem('Jupiter','5.2AU','1.89X10^27 kg','Voyager 1','It has 79 moons in which Europa is the largest','The largest planet in our Solar system and Gaseous giant')
     print(planet5.features())
elif a==6:
     planet6 = Solarsystem('Saturn','9.58AU','5.6x10^26 kg','Cassini','It has 82 moons in which titan is the largest','Gaseous and well known for its beautiful rings')
     print(planet6.features())
elif a==7:
     planet7 = Solarsystem('Uranus','19.2AU','8.6x10^25 kg','Voyager 2','It has 27 moons','Gaseous methane filled and rolls in its orbit')
     print(planet7.features())
elif a==8:
     planet8 = Solarsystem('Neptune','30.1AU','1.24x10^26 kg','Voyager 2','It has 14 moons','Blue gaseous planet and the coldest in our Solar system')
     print(planet8.features())
else:
    print("No Planet in this position")
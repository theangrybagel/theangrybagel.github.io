import Lib, random


def GetThruster():
	names1 = "death pan bee coal bag weasle sea dirt floor sand space nail cream wealth knife cannon beef police train".split(" ")
	names2 = "blaster booster jetter equalizer finisher driver swimmer propeller skipper weaver mover runner walker".split(" ")
	name = random.choice(names1) + random.choice(names2)
	types = ["High level thrusters", "Low level thrusters"]
	units = ["Yorks per unit", "Microyorks per unit"]
	speedunits = ["YPM", "MPM"]
	speedranges = [[1, 6], [10, 80]]
	costs = [[40000, 100000], [10000, 40000]]
	fuelranges = [[.1, 6], [50, 2000]]
	tp = random.choice([0, 1])
	yorksperunit = random.randrange(1, 1000)/1000
	speed = random.randrange(1, 1000)/1000
	cost = costs[tp][0] + (costs[tp][1] - costs[tp][0])*.4 * yorksperunit + .5*(speed*(1+speed))*(costs[tp][1] - costs[tp][0])
	costvariation = 1 + random.randrange(-300, 300)/1000
	cost = cost * costvariation
	print("Name:", name)
	print("Type:", types[tp])
	print(units[tp]+":", yorksperunit*(fuelranges[tp][1]-fuelranges[tp][0])+fuelranges[tp][0])
	print("Speed: ", (speedranges[tp][1]-speedranges[tp][0])*speed+speedranges[tp][0], speedunits[tp])
	print("Cost: ", cost, "CR")

for x in range(10):
	GetThruster()
	print('\n')
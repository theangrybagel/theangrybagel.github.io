import Lib, random, Thruster
from Lib import StrDict
from Lore import Lore
from math import sqrt

def OneLineFormat(d):
	txt = "("
	if "name" in d:
		txt = d["name"] + " ("
	for x in d:
		if x not in "name":
			txt += x + ": " + str(d[x]) + ", "
	return txt[:-2] + ")"
def LifeSupportModule():
	o = []
	o.append({"name": "Gas Dispenser", "description": "Dispenses a gas of your choice when you want it to. It comes with a canister of low grade tear gas. ", "cost": 8000})
	o.append({"name": "Poison Detector", "description": "Detects hazardous fumes.", "cost": 9000})
	o.append({"name": "Air Conditioner I", "description": "Controls the temperature.", "cost": 3000})
	o.append({"name": "Air Conditioner II", "description": "Controls temperature and humidity.", "cost": 7000})
	o.append({"name": "Air Conditioner III", "description": "Can simulate a wide variety of climates. Acid rain included in this package.", "cost": 32000})
	o.append({"name": "Diverse Gas Supply II", "description": "Provides a wider variety of gas than the Diverse Gas Supply I", "cost": 5000})
	o.append({"name": "Fuel Leakage Detector", "description": "Alerts the captain if there is a fuel leak of some kind. ", "cost": 12000})
	o.append({"name": "Gamma Filter", "description": "Filters out gamma radiation coming through the ship's windows. ", "cost": 19000})
	o.append({"name": "Cyrogenic Time Module", "description": "Can be used to freeze everyone and everything for a desired amount of time. Good for drifting slowly through space when you've run out of fuel and have nothing else to do. ", "cost": 80000})
	return random.choice(o)
def LifeSupport():
	names1 = "saftey free air life water sun day".split(" ")
	names2 = "breather infuser emitter giver maker smeller sniffer".split(" ")
	name = random.choice(names1) + random.choice(names2)
	slots = random.randrange(4, 12)
	thing = {"name": name.title(), "module Slots": str(slots)}
	moduleefficiency = random.randrange(20, 100)/100
	thing["module efficiency"] = moduleefficiency
	thing["module 1"] = "Basic Gravitational Control Module"
	thing["module 2"] = "Diverse Gas Supply I"
	modules = []
	cost = 25000
	for x in range(slots-2):
		if random.choice([True, False, False, False]):
			m = LifeSupportModule()
			modules.append(m)
			thing["module {}".format(x+3)] = m['name'] + " - " + m["description"]
			cost += m['cost'] + 1000 * moduleefficiency
		else:
			thing["module {}".format(x+3)] = "Empty"
			cost += 4000 * moduleefficiency
	thing["cost"] = cost
	return thing
def GetThruster(t):
	th = None
	while th == None:
		a = Thruster.GetThruster()
		if a["type"] == t:
			th = a
	return th

def ShipWeapon():
	names1 = "death star planet dust gas juice pan bee coal fire bag weasle sea dirt floor sand space nail cream wealth knife cannon beef police train wack face life bag rain snow frisbee coal".split(" ")
	names2 = "killer shooter ruiner spewer fighter knotter gun blaster launcher sender maker vaporizer zapper".split(" ")
	name = (random.choice(names1) + random.choice(names2)).title()
	weaponclass = random.choice("B F C R W".split(" "))
	damage = random.randrange(3, 30)
	cost = 0
	cost += damage*200
	firerate = random.randrange(1, 900)/100
	cost *= firerate
	mass = random.randrange(50, 200)
	thing = {"name": name, "class": weaponclass, "damage": damage, "firerate": firerate, "mass": mass}
	return thing
def NavSystem():
	commdist = random.range(10, 100)
	return
def FuelBay(targetsize, t):
	typelist = Lore.Fuels.low
	if t.upper().startswith("H"):
		typelist = Lore.Fuels.high
	supportedTypes = [random.choice(typelist)["name"]]
	for x in range(random.randrange(0, 3)):
		ft = random.choice(typelist)['name']
		if ft not in supportedTypes:
			supportedTypes.append(ft)
	thing = {"capacity": targetsize, "supported fuel": ""}
	for x in supportedTypes:
		thing["supported fuel"] += x + " "
	return thing
def GetShipWeapon(t):
	wpn = None
	while wpn == None:
		a = ShipWeapon()
		if a['class'] == t:
			wpn = a
	return wpn

def ShipGenerator():
	n1 = "death star planet sour dust gas juice pan bee coal bag weasle sea dirt floor sand space nail cream wealth knife cannon beef police train fire wack face life bag rain snow frisbee coal".split(" ")
	n2 = "speeder fighter eagle parrot genguin sparrow goose fisher duck bird jet skimmer glider ship wing yacht boat lugger vessel sailer mobile falcon".split(" ")
	ship = {"name": random.choice(n1).title() + random.choice(n2)}
	hthrusters = GetThruster("High level thrusters")
	lthrusters = GetThruster("Low level thrusters")
	plating = random.choice(Lore.Materials.shiparmor)
	lowlevelspeed = 0
	highlevelspeed = 0
	body = random.choice(Lore.bodies)
	mass = body["mass"] + plating["mass"]*body["plating"]
	ship["body"] = body["name"]
	ship["plating"] = plating["name"]
	ship["weapons class"] = body["wc"]
	lifesupport = LifeSupport()
	cost = body["cost"] + lifesupport["cost"]
	lowlevelspeed += lthrusters["speed"]*body['llt']
	highlevelspeed += hthrusters["speed"]*body['hlt']
	mass += lthrusters["mass"]*body['llt'] + hthrusters["mass"]*body['hlt']
	ship["low level speed"] = lowlevelspeed / sqrt(.0005*mass)
	ship["high level speed"] = highlevelspeed / sqrt(.0005*mass)
	cost += hthrusters["cost"] * body["hlt"]
	cost += lthrusters["cost"] * body["llt"]
	cost += ship["low level speed"]*100 + ship["high level speed"]*100
	ship["micro yorks per low level unit"] = lthrusters['distance per unit']*body['llt']
	ship["yorks per high level unit"] = hthrusters['distance per unit']*body['hlt']
	wpns = {"B":0, "F":0, "C":0, "R":0, "W":0}
	for x in body['wc']:
		wpns[x] += 1
		wpn = GetShipWeapon(x)
		mass += wpn["mass"]
		ship["Weapon {} {}".format(x, wpns[x])] = "\n"+StrDict(wpn, tb="    ")
	ship["low level fuel bay"] = FuelBay(random.randrange(int(body["fc"]*.25*100), int(body["fc"]*.75*100))/100, "Low Level")
	ship["high level fuel bay"] = StrDict(FuelBay(body["fc"]-ship["low level fuel bay"]["capacity"], "High Level"), tb="    ")
	ship["low level fuel bay"] = StrDict(ship["low level fuel bay"], tb="    ")
	ship["total mass"] = mass
	ship["total cost"] = cost

	ship["life support"] = "\n"+StrDict(lifesupport, tb="    ")
	ship["high level thrusters"] = "\n"+StrDict(hthrusters, tb="    ")
	ship["low level thrusters"] = "\n"+StrDict(lthrusters, tb="    ")
	return ship



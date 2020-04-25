#for editing the python code that goes into store.html
#LIB
import random
def StrDict(d, tb=""):
	txt = ""
	for x in d:
		txt += tb+(x.title() + ": " + str(d[x])) + "\n"
	txt += ("\n")
	return txt
def GetHTML(d, nl="", dv="div"):

	txt = "<{}>".format(dv)
	tab = ""
	for x in d:
		if x not in "name":
			txt += "{nl}{tab}<br>{nl}{tab}{x}: {dx}".format(nl=nl, x=x.title(), dx=d[x], tab=tab).replace("\n", "<br>")
		else:
			txt += "{nl}{tab}<br>{nl}{tab}<h3>{dx}</h3>".format(nl=nl, x=x, dx=d[x], tab=tab)
	txt += "{nl}</{}>".format(dv, nl=nl)
	txt = txt.replace("<br><br>", "<br>").replace("<br></p>", "</p>").replace("<br><p>", "<p>")
	return txt
#--------------
#Others.py
from math import sqrt

def OneLineFormat(d):
	txt = d["name"] + " ("
	for x in d:
		if x not in "name":
			txt += x + ": " + d[x] + ", "
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
	thing = {"name": name, "module Slots": str(slots)}
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
def GetSpecificThruster(t):
	th = None
	while th == None:
		a = GetThruster()
		if a["type"] == t:
			th = a
	return th

def ShipWeapon():
	names1 = "death star planet dust gas juice pan bee coal fire bag weasle sea dirt floor sand space nail cream wealth knife cannon beef police train wack face life bag rain snow frisbee coal".split(" ")
	names2 = "killer shooter ruiner spewer fighter knotter gun blaster launcher sender maker vaporizer zapper".split(" ")
	name = random.choice(names1) + random.choice(names2)
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
	hthrusters = GetSpecificThruster("High level thrusters")
	lthrusters = GetSpecificThruster("Low level thrusters")
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
	ship["high level fuel bay"] = FuelBay(body["fc"]-ship["low level fuel bay"]["capacity"], "High Level")
	ship["total mass"] = mass
	ship["total cost"] = cost

	ship["life support"] = "\n"+StrDict(lifesupport, tb="    ")
	ship["high level thrusters"] = "\n"+StrDict(hthrusters, tb="    ")
	ship["low level thrusters"] = "\n"+StrDict(lthrusters, tb="    ")
	return ship
#--------------
def Round(num):
	return int(num*100)/100

def GetThruster():
	names1 = "death star planet dust gas juice pan bee coal bag weasle sea dirt floor sand space nail cream wealth knife cannon beef police train".split(" ")
	names2 = "blaster thruster passer ranger speeder booster jetter equalizer finisher driver swimmer propeller skipper weaver mover runner walker".split(" ")
	name = random.choice(names1) + random.choice(names2)
	types = ["High level thrusters", "Low level thrusters"]
	speedranges = [[.1, 2.7], [5, 40]]
	costs = [[40000, 100000], [10000, 40000]]
	fuelranges = [[.3, 6], [50, 300]]
	mass = random.randrange(40, 200)
	tp = random.choice([0, 1])
	distanceperunit = random.randrange(1, 1000)/1000
	speed = random.randrange(1, 1000)/1000
	cost = costs[tp][0] + (costs[tp][1] - costs[tp][0])*.4 * distanceperunit + .5*(speed*(1+speed))*(costs[tp][1] - costs[tp][0]) + max(10000-mass*30, 0)
	costvariation = 1 + random.randrange(-300, 300)/1000
	cost = cost * costvariation
	thing = {"name": name, "type": types[tp], "distance per unit": distanceperunit*(fuelranges[tp][1]-fuelranges[tp][0])+fuelranges[tp][0]}
	thing["speed"] = (speedranges[tp][1]-speedranges[tp][0])*speed+speedranges[tp][0]
	thing["cost"] = Round(cost)
	thing['mass'] = mass
	return thing
#------------
#LORE
#Libary for obtaining lore in python dictonaries.

class Lore:
	bodies = []#ship bodies
	class Fuels:
		fueltypes = []
		low = []
		high = []
	class Materials:#catalogue of materials used in WPLTS
		shiparmor = []
		allmats = []


#lore builder
class LB:
	#material. strength is on a scale of 0 - 100. Most things range in the 20-50 range.
	def Fuel(name, symbol, cost, efficiency):
		fid = "FT-" + symbol.upper() + name[:1].upper() + "L"
		thing = {"name": name, "id": fid, "cost": cost, "efficiency": efficiency}
		Lore.Fuels.fueltypes.append(thing)
		if name.startswith("L"):
			Lore.Fuels.low.append(thing)
		if name.startswith("H"):
			Lore.Fuels.high.append(thing)
		return thing
	def Mat(name, cost, mass, strength, data=[]):
		thing = {"name": name, "cost": cost, "strength": strength, "notes": data, "mass": mass}
		Lore.Materials.allmats.append(thing)
		return thing
	def ShipBody(name, mass, cost, FC, ICC, clss, WC, plating, HLT=2, LLT=2, GT=8):
		return {"name": name, "mass": mass, "cost": cost, "fc": FC, "icc": ICC, "class": clss, "wc": WC, "hlt": HLT, "llt":LLT, "gt":GT, "plating": plating}
	def Build():
		Lore.Materials.shiparmor.append(LB.Mat("Chengerthium plating", 2500, 280, 20))
		Lore.Materials.shiparmor.append(LB.Mat("Bungorian Steel Plating", 472000, 400, 80, data=["Discontinued", "Resistant to high velocity impacts."]))
		Lore.Materials.shiparmor.append(LB.Mat("Altamanium Steel", 70000, 360, 50))
		Lore.bodies.append(LB.ShipBody("FK-23", 3900, 897000, 12, 4.75, "A", "WWB", 3.75))
		Lore.bodies.append(LB.ShipBody("HAT-46", 5400, 324000, 14, 6.5, "B", "FFWW", 5))
		Lore.bodies.append(LB.ShipBody("VX-92", 4300, 468000, 11, 4, "D", "WWWW", 4.25, LLT=4, GT=10))
		Lore.bodies.append(LB.ShipBody("PCF-97", 8500, 233000, 10, 5, "R", "FFWW",5., HLT=4))
		LB.Fuel("Low Level PLutonium Fuel", "P", 920, 9)
		LB.Fuel("Low Level Uranium Fuel", "U", 460, 6)
		LB.Fuel("High Level Plutogen Fuel", "PH", 7370, 7)
		LB.Fuel("High Level Hylutogen Fuel", "HP", 13260, 10)
		LB.Fuel("High Level Neptunium Fuel", "NPT", 8800, 8)

LB.Build()
#----------
from browser import document
def Generate():
	sources = {'thruster':GetThruster, 'lifesupport': LifeSupport, 'ship': ShipGenerator, 'shipweapon': ShipWeapon}
	sourceskeys = []
	for x in sources:
		sourceskeys.append(x)
	source = random.choice(sourceskeys)
	if source in sources:
		print(source.upper()+"\n")	
		generated = sources[source]()
		document.getElementById("Ships").innerHTML += ("<br><br><br>" + (GetHTML(generated).replace("    ", "&emsp;")))
	else:
		print('Invalid generator source')


Generate()
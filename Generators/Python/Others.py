import Lib, random, Thruster
from Lib import StrDict

def OneLineFormat(d):
	txt = d["Name"] + " ("
	for x in d:
		if x not in "Name":
			txt += x + ": " + d[x] + ", "
	return txt[:-2] + ")"
def LifeSupportModule():
	o = []
	o.append({"Name": "Gas Dispenser", "Description": "Dispenses a gas of your choice when you want it to. It comes with a canister of low grade tear gas. ", "Price": 8000})
	o.append({"Name": "Poison Detector", "Description": "Detects hazardous fumes.", "Price": 9000})
	o.append({"Name": "Air Conditioner I", "Description": "Controls the temperature.", "Price": 3000})
	o.append({"Name": "Air Conditioner II", "Description": "Controls temperature and humidity.", "Price": 7000})
	o.append({"Name": "Air Conditioner III", "Description": "Can simulate a wide variety of climates. Acid rain included in this package.", "Price": 32000})
	o.append({"Name": "Diverse Gas Supply II", "Description": "Provides a wider variety of gas than the Diverse Gas Supply I", "Price": 5000})
	o.append({"Name": "Fuel Leakage Detector", "Description": "Alerts the captain if there is a fuel leak of some kind. ", "Price": 12000})
	o.append({"Name": "Gamma Filter", "Description": "Filters out gamma radiation coming through the ship's windows. ", "Price": 19000})
	o.append({"Name": "Cyrogenic Time Module", "Description": "Can be used to freeze everyone and everything for a desired amount of time. Good for drifting slowly through space when you've run out of fuel and have nothing else to do. ", "Price": 80000})
	return random.choice(o)
def LifeSupport():
	names1 = "saftey free air life water sun day".split(" ")
	names2 = "breather infuser emitter giver maker smeller sniffer".split(" ")
	name = random.choice(names1) + random.choice(names2)
	slots = random.randrange(4, 12)
	thing = {"Name": name, "Module Slots": str(slots)}
	thing["Module 1"] = "Basic Gravitational Control Module"
	thing["Module 2"] = "Diverse Gas Supply I"
	modules = []
	moduleefficiency = random.randrange(20, 100)/100
	thing["Module Efficiency"] = moduleefficiency
	cost = 25000
	for x in range(slots-2):
		if random.choice([True, False, False, False]):
			m = LifeSupportModule()
			modules.append(m)
			thing["Module {}".format(x+3)] = m['Name'] + " - " + m["Description"]
			cost += m['Price'] + 1000 * moduleefficiency
		else:
			thing["Module {}".format(x+3)] = "Empty"
			cost += 4000 * moduleefficiency
	thing["Cost"] = cost
	return thing
def GetThruster(t):
	th = None
	while th == None:
		a = Thruster.GetThruster()
		if a["Type"] == t:
			th = a
	return th
def ShipBody(name, mass, cost, FC, ICC, clss, WC, HLT=2, LLT=2, GT=8):
	return {"Name": name, "Mass": mass, "Cost": cost, "FC": FC, "ICC": ICC, "Class": clss, "WC": WC, "HLT": HLT, "LLT":LLT, "GT":GT}
def ShipWeapon():
	names1 = "death star planet dust gas juice pan bee coal fire bag weasle sea dirt floor sand space nail cream wealth knife cannon beef police train wack face life bag rain snow frisbee coal".split(" ")
	names2 = "killer shooter ruiner spewer fighter gun blaster launcher sender maker vaporizer zapper".split(" ")
	name = random.choice(names1) + random.choice(names2)
	thing = {"Name": name}
	return thing
def ShipPlating():
	return
def NavSystem():
	return
def FuelBay():
	return

def ShipGenerator():
	bodies = []
	bodies.append(ShipBody("FK-23", 3900, 897000, 12, 4.75, "A", "WWB"))
	bodies.append(ShipBody("HAT-46", 5400, 324000, 14, 6.5, "B", "FFWW"))
	bodies.append(ShipBody("VX-92", 4300, 468000, 11, 4, "D", "WWWW", LLT=4, GT=10))
	bodies.append(ShipBody("PCF-97", 8500, 233000, 10, 5, "R", "FFWW", HLT=4))
	ship = {}
	body = random.choice(bodies)
	ship["Body"] = body["Name"]
	lifesupport = LifeSupport()
	ship["Life Support"] = StrDict(lifesupport)
	cost = body["Cost"] + lifesupport["Cost"]
	hthrusters = GetThruster("High level thrusters")
	lthrusters = GetThruster("Low level thrusters")
	for x in range(body["HLT"]):
		ship["High Level Thruster {}".format(x+1)] = StrDict(hthrusters)
		cost += hthrusters["Cost"]
	for x in range(body["LLT"]):
		ship["Low Level Thruster {}".format(x+1)] = StrDict(lthrusters)
		cost += lthrusters["Cost"]
	ship["Cost"] = cost
	return ship



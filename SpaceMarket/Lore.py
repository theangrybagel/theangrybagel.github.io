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
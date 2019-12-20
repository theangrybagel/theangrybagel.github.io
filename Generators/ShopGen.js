AddEditorCategory("Shop")

var Items = []
var Weapons = []
var Gear = []
var Tools = []
var profitmultiplier = random.range(1, 500) / 300;
function AddItem(dta)
{
	Items.push(dta);
}
function AddWeapon(name, cost)
{
	Weapons.push([name, cost]);
	AddItem([name, cost, "Weapons"]);
}
function AddTool(name, cost)
{
	Tools.push([name, cost]);
	AddItem([name, cost, "Tools"]);
}
function AddGear(name, cost){
	Gear.push([name, cost]);
	AddItem([name, cost, "Gear"]);
}
function AddFood(name, cost)
{
	AddItem([name, cost, "Food"]);
}
function AddOther(name, cost)
{
	AddItem([name, cost, "other"]);
}
AddWeapon("Anopium Knives", 6250)
AddWeapon("FTX-9", 13540)
AddWeapon("Melverth Lightcaster", 32500)
AddWeapon("VZFF-37", 9000)
AddWeapon("High Power Zapcaster", 22000)
AddWeapon("Feverdriver", 35000)
AddWeapon("Nitrogenic Hyperemitter", 42000)
AddGear("CT-12", 121000)
AddGear("CT-16", 765000)
AddGear("NB-73", 3250)
AddGear("FMI-67", 12000)
AddTool("Thermal Tracker Visor", 15000)
AddTool("Atmospheric Radiator", 12000)
AddTool("Circut Scrubber", 2000)
AddTool("YIP", 12000)
AddTool("YIP-MAX", 22000)
AddTool("BWRD", 9875)
AddFood("Yolcorg", 25)
AddFood("Gorn", 15)
AddFood("Gruffalo Burger", 45)
AddFood("Lydracane", 890)
AddFood("Lydracane-X", 3250)
var txt = ""
for(var i = 0; i < random.range(3, 12); i++)
{
	var v = random.choice(Items)
	SetEditorData("Shop", v[0], Math.round(v[1]*profitmultiplier) + "CR")
	//txt += v[0] + " - " + v[1] + "CR<br>"
}
//SetEditorData("Shop", txt, "");
Display()
document.getElementById("content").style="text-align: left;"

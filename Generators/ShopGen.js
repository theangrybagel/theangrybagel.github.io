AddEditorCategory("Shop")

var Items = []
var Weapons = []
var Gear = []
var Tools = []
var profitmultiplier = random.range(1, 500) * .01;
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
	Gear.push([name, cost])
	AddItem([name, cost, "Gear"])
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
var txt = ""
for(var i = 0; i < random.range(1, 12); i++)
{
	var v = random.choice(Items)
	txt += v[0] + " - " + v[1] + "CR<br>"
}
SetEditorData("Shop", txt);
Display()
document.getElementById("content").style="text-align: left;"

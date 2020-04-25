import Thruster, Others, random
from Lib import GetHTML, StrDict


from browser import document
def Generate():
	sources = {'thruster':Thruster.GetThruster, 'lifesupport': Others.LifeSupport, 'ship': Others.ShipGenerator, 'shipweapon': Others.ShipWeapon}
	sourceskeys = []
	for x in sources:
		sourceskeys.append(x)
	source = random.choice(sourceskeys)
	if source in sources:
		print(source.upper()+"\n")	
		generated = sources[source]()
		document.getElementById("Ships").innerHTML += ("<br><br><br><h2>Tag: "+source.title()+"</h2>" + (GetHTML(generated).replace("    ", "&emsp;")))
	else:
		print('Invalid generator source')

for x in range(30):
	Generate()
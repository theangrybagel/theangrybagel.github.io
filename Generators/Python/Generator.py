import Thruster, Others, random
from Cmd import Run, Command, Param, O
from Lib import GetHTML, StrDict



def Generate(args):
	source = "random"
	if args['source'] != None:
		source = args['source']
	sources = {'thruster':Thruster.GetThruster, 'lifesupport': Others.LifeSupport, 'ship': Others.ShipGenerator, 'shipweapon': Others.ShipWeapon}
	sourceskeys = []
	for x in sources:
		sourceskeys.append(x)
	if source == "random":
		source = random.choice(sourceskeys)
	if args['l']:
		print("Available generators: ")
		for x in sources:
			print(x)
		return
	if source in sources:
		print(source.upper()+"\n")	
		for x in range(args['times']):
			generated = sources[source]()
			if args['h']:
				print(GetHTML(generated))
			else:
				print(StrDict(generated))

	else:
		print('Invalid generator source')





commands = []
commands.append(Command("generate", Generate, aliases=['gen'], parameters=[Param("times", "int", 1, desc="The amount of times you wish to generate something")], args=[Param("source", 'string', 'thruster', required=False)], options=[O("l", "lists all available generators"), O("h", "outputs HTML format")]))
Run(commands)
import Thruster
from Cmd import Run, Command, Param



def Generate(args):
	sources = {'thruster':Thruster.GetThruster}
	if args['source'] in sources:
		for x in range(args['times']):
			sources[args['source']]()
	else:
		print('Invalid generator')





commands = []
commands.append(Command("generate", Generate, aliases=['gen'], parameters=[Param("times", "int", 1), Param("source", 'string', 'thruster')]))
Run(commands)
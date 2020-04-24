import shlex, os, sys
try:
	import tabulate
except ImportError:
	print("Module tabulate not found. Installing it now. ")
	os.system("python -m pip install tabulate")
import tabulate
class CommandStuff:
	#--argname="argvalue" -o
	#^ the -- indicates setting a value, the -o indicates enabling an option. 
	def ArgParse(args, cmd):
		#split the arguments
		a = shlex.split(args)
		arguments = {}
		for x in cmd.options:
			arguments[x] = False
		for x in cmd.parameters:
			arguments[x] = cmd.parameters[x].defaultvalue
		for x in cmd.arguments:
			arguments[x.name] = None
		argumentIndex = -1 #set to -1 because the first argument found is going to be the actual command being called.

		for x in a:
			if x.startswith("--"):
				arg = x.split("=")[0].replace('--', '')
				if arg in cmd.parameters:
					arguments[arg] = cmd.parameters[arg].Get(x.replace(x.split('=')[0]+"=", ""))
				else:
					print(arg, "does not exist as a valid parameter")
			else:
				if x.startswith("-"):
					for letter in x:
						if letter in cmd.options:
							arguments[letter] = True
				else:
					#we assume that it is a required argument
					if argumentIndex >= 0 and argumentIndex < len(cmd.arguments):
						arguments[cmd.arguments[argumentIndex].name] = cmd.arguments[argumentIndex].Get(x) 
					argumentIndex += 1

		return arguments
	def TryNum(value):
		a = value
		try:
			a = float(value)
			if a - int(a) == 0:
				a = int(value)
		except:
			return a
		return a


class Command:
	#options (optional) - single letter options in the form of O(). Called like command -abC. Each option is set to false unless it is toggled when running the command.
	#aliases - alternative list names the command can be called with
	#parameters (optional) - complex options in the form of a Param(). Called like this: command --option="some value". 
	#desc - description of the command
	#args (required when running the command) - required arguments to pass through. Used like this: command 30 "some thing". The first argument is a number, the second one is a string. The args are in Param() form.
	def __init__(self, name, functionref, aliases=[], options=[], parameters=[], desc="No description", args=[]):
		self.name = name
		self.functionref = functionref
		self.aliases = aliases
		self.options = []
		self.optiondata = options
		for x in options:
			self.options.append(x.letter)
		self.parameters = {}
		self.arguments = args
		self.desc = desc
		for x in parameters:
			self.parameters[x.name] = x
	def Call(self, args):
		arguments = CommandStuff.ArgParse(args, self)
		for x in arguments:
			if arguments[x] == "FAIL_COMMAND":
				print("Command aborted. ")
				return
		for x in self.arguments:
			if arguments[x.name] == None and x.required:
				print("Invalid syntax. Missing argument \"" + x.name + "\"")
				print("Command aborted. ")
				return
		self.functionref(arguments)
class Param:
	#ptype can be either ['int', 'num', 'string', 'any']
	#setting to 'any' is not recommended unless your program can handle mutliple types of a single parameter.
	#default value does not apply for arguments
	#set required to false to make an argument optional. This is only recommended if you have a single argument. 
	def __init__(self, name, ptype, defaultvalue, required=True, desc=""):
		self.name = name
		self.ptype = ptype
		self.required = required
		self.desc = desc
		self.defaultvalue = defaultvalue
	#gets the outcome of this parameter. if the parameter is supposed to be a string, but comes in as a number, this will prevent your code from breaking.
	def Get(self, valuegiven):
		if self.ptype == "string":
			return str(valuegiven)
		val = valuegiven
		if self.ptype in ['num', 'int']:
			val = CommandStuff.TryNum(val)
			if val == valuegiven:
				print("Error: parameter " + self.name + " must be type a number. The command will not be run. ")
				return "FAIL_COMMAND"
			if self.ptype == 'num':
				return val
		if self.ptype == 'int':
			val = int(val)
			return val
class O:#for single letter options (giving them descriptions and names)
	def __init__(self, letter, desc=""):
		self.letter = letter
		self.desc = desc







class Run:
	def Help(self, args):
		#print(args)
		if args['command'] == None:
			table = []
			for x in self.commands:
				table.append([x.name, x.desc, str(x.aliases).replace("[", "").replace("]","").replace("'", "")])
			print(tabulate.tabulate(table, headers=["Command", "Description", "Aliases"]))
			print("\nUse ? [command name] to get more detailed help. ")
			return
		if args['command'] in self.cmddict:
			cmd = self.cmddict[args['command']]
			name = cmd.name
			for x in cmd.arguments:
				name += " ["+x.name+"]"

			print(name)
			print(cmd.desc)
			print("Aliases:", str(cmd.aliases).replace("[", "").replace("]","").replace("'", ""))
			print("Options:")
			options = []
			for x in cmd.parameters:
				options.append(["--"+cmd.parameters[x].name, cmd.parameters[x].desc, cmd.parameters[x].defaultvalue])
			for x in cmd.optiondata:
				options.append(["-"+x.letter, x.desc, "False"])
			print(tabulate.tabulate(options, headers=["Option", "Description", "Default"]))
	def GetInput(self):
		a = ""
		while True:
			a = input("> ")
			if a == "":
				continue
			print("\n")
			if a in self.history:
				self.history.remove(a)
			self.history.append(a)
			break
		return a

	def __init__(self, commands):
		commands.append(Command("help", self.Help, aliases=["?", "h"], args=[Param("command", "string", "", required=False)], desc="Provides helpful info on particular commands"))
		commands.append(Command("exit", sys.exit, aliases=["q", "quit", "stop"], desc="Stops the program dead in its tracks. "))
		self.commands = commands
		self.cmddict = {}
		self.history = []
		for x in commands:
			self.cmddict[x.name] = x
			for a in x.aliases:
				self.cmddict[a] = x
		while True:
			a = self.GetInput()
			
			if a.lower() in ["exit", "quit", "stop"]:
				break
			cmd = a.split(" ")[0]
			if cmd in self.cmddict:
				self.cmddict[cmd].Call(a)




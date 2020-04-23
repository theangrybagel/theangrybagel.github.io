import shlex

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
		for x in a:
			if "--" in x:
				arg = x.split("=")[0].replace('--', '')
				if arg in cmd.parameters:
					arguments[arg] = cmd.parameters[arg].Get(x.replace(x.split('=')[0]+"=", ""))
				else:
					print(arg, "does not exist as a valid parameter")
			else:
				if "-" in x:
					for letter in x:
						if letter in cmd.options:
							arguments[letter] = True
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
	def __init__(self, name, functionref, documentation, aliases=[], options=[], parameters=[]):
		self.name = name
		self.functionref = functionref
		self.documentation = documentation
		self.aliases = aliases
		self.options = options
		self.parameters = {}
		for x in parameters:
			self.parameters[x.name] = x
	def Call(self, args):
		arguments = CommandStuff.ArgParse(args, self)
		for x in arguments:
			if arguments[x] == "FAIL_COMMAND":
				print("Command aborted. ")
				return
		self.functionref(arguments)
class Param:
	#ptype can be either ['int', 'num', 'string', 'any']
	#setting to 'any' is not recommended unless your program can handle mutliple types of a single parameter.
	def __init__(self, name, ptype, defaultvalue):
		self.name = name
		self.ptype = ptype
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



class Run:
	def __init__(self, commands):
		cmddict = {}
		for x in commands:
			cmddict[x.name] = x
			for a in x.aliases:
				cmddict[a] = x

		while True:
			a = input("> ").strip()
			if a == "":
				continue
			if a.lower() in ["exit", "quit", "stop"]:
				break
			cmd = a.split(" ")[0]
			if cmd in cmddict:
				cmddict[cmd].Call(a)




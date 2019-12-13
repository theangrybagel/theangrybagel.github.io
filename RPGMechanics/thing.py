things = []
while True:
	x = input("...")
	if "GO" not in x:
		things.append(x)
	else:
		print("BREAK")
		break
txt = ""
for x in things:
	txt += "<br>" + x + ":___"
print(txt)
import os, time
print("HELLO ")
time.sleep(.5)
total = 0
cd = os.curdir
replace = [["WPTLS", "WPLTS"]]
#replace = [["['The Divine Oligarchy']", "The Divine Oligarchy"], ["['The Torgians']", "The Torgians"], ["['The Galactic Federation']", "The Galactic Federation"], ["['Rebel Peasants']", "Rebel Peasants"]]
for root, dirs, files in os.walk(cd):
	for file in files:
		if "About" in file and file.endswith(".html"):
			pth = os.path.join(root, file)
			print(pth)
			total += 1
			'''f = open(pth, "r")
			text = f.read()
			f.close()
			f2 = open(pth, "w")
			for x in replace:
				text = text.replace(x[0], x[1])
			f2.write(text)
			f2.close()'''
print(total)
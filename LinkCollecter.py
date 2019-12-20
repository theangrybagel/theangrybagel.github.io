import os
cd = os.curdir
txt = "function StartNav(){\n"
for root, dirs, files in os.walk(cd):
	for file in files:
		if "About" not in file and file.endswith(".html"):
			pth = os.path.join(root, file)
			print(pth)
			f = open(pth, "r")
			title = f.read()
			if "<title>" in title:
				title = title.split("<title>")[1].split("</title>")[0]
			if "WPLTS - " in title:
				print(title)
				title = title.split("WPLTS - ")[1]
				print(title)
			if len(title) < 40:
				newtxt = "AddLink('" + title + "', '" + pth + "');"
				txt += newtxt
				print(newtxt)
			f.close()

txt += "\n}"
f = open("addlinks.txt", "w")
f.write(txt)
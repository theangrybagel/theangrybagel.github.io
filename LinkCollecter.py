import os
cd = os.curdir
txt = "function StartNav(){\n"
for root, dirs, files in os.walk(cd):
	for file in files:
		if file.endswith(".html"):
			pth = os.path.join(root, file)
			print(pth)
			f = open(pth, "r")
			title = f.read().split("<title>")[1].split("</title>")[0]
			if "WPLTS -" in title:
				title = title.split("WPLTS -")[0]
			txt += "AddLink('" + title + "', '" + pth + "');"
			f.close()

txt += "\n}"
f = open("addlinks.txt", "w")
f.write(txt)
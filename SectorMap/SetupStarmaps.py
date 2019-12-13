import os

sectors = []
for x in range(100):
	sectors.append("Sector " + str(x))
for x in sectors:
	if ".html" not in x and ".py" not in x:
		print(x)
		#go through that directory
		stars = os.listdir("./" + x)
		print(stars)
		for s in stars:
			if ".html" not in s:
				thing = '</script><script src="../../../planetcode.js"></script>'
				htmlfile = "./" + x + "/" + s + "/"  + "About.html"
				print(htmlfile)
				planets = []
				for p in os.listdir("./" + x + "/" + s):
					if ".html" not in p:
						f = open("./" + x + "/" + s + "/" + p + "/About.html", "r")
						c = f.read()
						stdist = float(c.split("Distance From Star: ")[1].split("Y")[0])
						typ = c.split("Enviroment: ")[1].split("<br>")[0]
						size = c.split("Size: ")[1].split("MY")[0]
						planets.append([p, stdist, size, typ])
						f.close()
				print(str(planets))
				f = open(htmlfile, "r")
				c = f.read()
				f.close()
				if len(c) > 1:
					f = open(htmlfile, "w")
					f1 = c.split("StartNav();</script>")[0] + "StartNav();</script>"
					f2 = "<script>planets="+str(planets)+thing
					f3 = "</head>" + c.split("</head>")[1]
					f.write(f1 + f2 + f3)
					f.close()

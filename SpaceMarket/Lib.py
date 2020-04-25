def StrDict(d, tb=""):
	txt = ""
	for x in d:
		txt += tb+(x.title() + ": " + str(d[x])) + "\n"
	txt += ("\n")
	return txt
def GetHTML(d, nl="", dv="div"):

	txt = "<{}>".format(dv)
	tab = ""
	for x in d:
		if x not in "name":
			txt += "{nl}{tab}<br>{nl}{tab}{x}: {dx}".format(nl=nl, x=x.title(), dx=RoundIfNeeded(d[x]), tab=tab).replace("\n", "<br>")
	txt += "{nl}</{}>".format(dv, nl=nl)
	txt = txt.replace("<br><br>", "<br>").replace("<br></p>", "</p>").replace("<br><p>", "<p>")
	return txt.replace("'", "\\'")
def RoundIfNeeded(txt):
	try:
		float(txt)
	except:
		return txt
	return int(float(txt)*100)/100

def GetHTMLStars(stars):
	txt = ""
	for x in range(5):
		chk = " checked"
		if x > stars-1:
			chk = ""
		txt += "<span class=\"fa fa-star{}\"></span>".format(chk)
	return txt
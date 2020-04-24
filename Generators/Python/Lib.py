def StrDict(d):
	txt = ""
	for x in d:
		txt += (x + ": " + str(d[x])) + "\n"
	txt += ("\n")
	return txt
def GetHTML(d, nl="", dv="div"):

	txt = "<{}>".format(dv)
	tab = ""
	for x in d:
		if x not in "Name":
			txt += "{nl}{tab}<br>{nl}{tab}<p>{x}: {dx}</p>".format(nl=nl, x=x, dx=d[x], tab=tab).replace("\n", "<br>")
		else:
			txt += "{nl}{tab}<br>{nl}{tab}<h3>{dx}</h3>".format(nl=nl, x=x, dx=d[x], tab=tab)
	txt += "{nl}</{}>".format(dv, nl=nl)
	txt = txt.replace("<br><br>", "<br>").replace("<br></p>", "</p>").replace("<br><p>", "<p>")
	return txt
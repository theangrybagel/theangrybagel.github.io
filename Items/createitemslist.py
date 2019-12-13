filetouse = "weapons.txt"
pagedesc = "Here you will find many weapons used in space."

txt = ""
txt += "<div id='content'><p>" + pagedesc + "</p><div>"
f = open(filetouse, "r")
g = f.readlines()
ontitle = True
for x in g:
	if ontitle:
		txt += "\n<div><h3 style='text-align: left;'>" + x + "</h3>"
	if not ontitle:
		txt += "<p>" + x + "</p></div>\n"
	ontitle = not ontitle

txt += "</div></div>"

f.close()
f2 = open("newhtml.txt", "w")
f2.write(txt)
f2.close()
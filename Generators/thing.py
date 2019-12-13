
txt = "Hacking | Lockpicking | Spacecraft Operation | Planetary Vehicle Operation | Luck"
'''
Brain
Spaceship Engineering | Politics | Persuasion | Weapon Engineering | Galactic Knowledge | Instant Judgement | Situational Awareness
Physical
Evasion | Running | Stealth | Climbing | Flexibility
Misc
Hacking | Lockpicking | Spacecraft Operation | Planetary Vehicle Operation | Luck | 
"
'''
t = ""
txt2 = "Misc"
for x in txt.split("|"):
	t += "SetEditorData2(" + "'Skills','" + txt2 + "','" + x.strip() + "'," + str(2)+");\n"
f = open("thingtxt.txt", "w")
f.write(t)
f.close()
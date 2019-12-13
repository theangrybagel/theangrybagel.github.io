function RollForStat(m)
{
	if(m == null)
		m = 1
	s = 0
	d20 = D20(1, 5)
	if(d20 > 18)
	{
		s += D20(1, 5);
	}
	return Math.round((s + d20)/4)*m;
}
AddEditorCategory("Stats")
AddEditorCategory("Skills")
AddEditorSubcategory("Skills", "Combat")
AddEditorSubcategory("Skills", "Brain")
AddEditorSubcategory("Skills", "Physical")
AddEditorSubcategory("Skills", "Misc")
AddEditorCategory("Equipment")
SetEditorData("Stats", "Strength", RollForStat())
SetEditorData("Stats", "Perception", RollForStat())
SetEditorData("Stats", "Awareness", RollForStat())
SetEditorData("Stats", "Intelligence", RollForStat())
SetEditorData("Stats", "Reputation", RollForStat())
SetEditorData("Stats", "Endurance", RollForStat())
SetEditorData("Stats", "Max Health", RollForStat(10))
SetEditorData2('Skills','Combat','Small Weapons',0);
SetEditorData2('Skills','Combat','Large Weapons',0);
SetEditorData2('Skills','Combat','Melee',0);
SetEditorData2('Skills','Combat','Ranged Weapons',0);
SetEditorData2('Skills','Combat','Improvised Weapons',0);
SetEditorData2('Skills','Brain','Spaceship Engineering',0);
SetEditorData2('Skills','Brain','Politics',0);
SetEditorData2('Skills','Brain','Persuasion',0);
SetEditorData2('Skills','Brain','Weapon Engineering',0);
SetEditorData2('Skills','Brain','Galactic Knowledge',0);
SetEditorData2('Skills','Brain','Instant Judgement',0);
SetEditorData2('Skills','Brain','Situational Awareness',0);
SetEditorData2('Skills','Physical','Evasion',0);
SetEditorData2('Skills','Physical','Running',0);
SetEditorData2('Skills','Physical','Stealth',0);
SetEditorData2('Skills','Physical','Climbing',0);
SetEditorData2('Skills','Physical','Flexibility',0);
SetEditorData2('Skills','Misc','Hacking',0);
SetEditorData2('Skills','Misc','Lockpicking',0);
SetEditorData2('Skills','Misc','Spacecraft Operation',0);
SetEditorData2('Skills','Misc','Planetary Vehicle Operation',0);
SetEditorData2('Skills','Misc','Luck',0);
weapons = ["Melverth Lightcaster", "FTX-9", "None"]
weapons2 = ["None", "Anopium Knives"]
armor = ["CT-12", "CT-16", "NB-73"]
SetEditorData("Equipment", "Weapon", random.choice(weapons))
SetEditorData("Equipment", "Secondary Weapon", random.choice(weapons2))
SetEditorData("Equipment", "Armor", random.choice(armor))
SetEditorData("Equipment", "Balance", random.range(10, 270) + "CR")
skillpoints = 20 + D10(1, 1)
//Randomly assign skill points. (Requires array of skills)
skills = []
for(var i = 0; i < Object.keys(data.Skills).length; i++)
{
	var catn = Object.keys(data.Skills)[i];
	for(y = 0; y < Object.keys(data.Skills[catn]).length; y++)
	{
		var yy = Object.keys(data.Skills[catn])[y];
		skills.push(catn + "_" + yy)
	}
}
function GetSkill(s)
{
	return data.Skills[s.split("_")[0]][s.split("_")[1]]
}
while(skillpoints > 1)
{
	//random amount
	amt = Math.round(D6(2)/3)
	skill = random.choice(skills)
	if(skillpoints - amt < 0)
		amt = skillpoints
	skillpoints -= amt
	data.Skills[skill.split("_")[0]][skill.split("_")[1]] += amt
}
Display()
document.getElementById("content").style="text-align: left;"
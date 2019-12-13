var random = {}
var data = {}
random.range = function(min, max){
	//find amt between min/max, multiply it by random, add min
	return Math.round((max-min)*Math.random()+min);
}
random.choice = function(arr){
	indx = Math.round(random.range(0, arr.length - 1))
	return arr[indx]
}
function SetEditorData2(category, subcategory, dataid, dta)
{
	data[category][subcategory][dataid] = dta;
}
function SetEditorData(category, dataid, dta)
{
	data[category][dataid] = dta;
}
function AddEditorCategory(category){
	data[category] = {"usesubcategory": false}
}
function AddEditorSubcategory(category, subcategory)
{
	data[category][subcategory] = {}
	data[category].usesubcategory = true
}
function Display()
{
	txt = ""
	for(var c = 0; c < Object.keys(data).length; c++)
	{
		//check if subcategories exist
		var cc = Object.keys(data)[c]
		txt += "<h2>" + cc + "</h2>"
		if(data[cc].usesubcategory == true)
		{
			for(var s = 0; s < Object.keys(data[cc]).length; s++)
			{
				ss = Object.keys(data[cc])[s]
				if(ss != "usesubcategory")
					txt += "<h3>" + ss + "</h3>"
				if(ss != "usesubcategory")
				for(var x = 0; x < Object.keys(data[cc][ss]).length; x++)
				{
					xx = Object.keys(data[cc][ss])[x]
					txt += xx + ": " + data[cc][ss][xx] + "&nbsp;&nbsp;&nbsp;&nbsp;"
					console.log(cc, ss, x, xx)
				}
			}
		}
		else{
			for(var x = 0; x < Object.keys(data[cc]).length; x++)
			{
				xx = Object.keys(data[cc])[x]
				if(xx != "usesubcategory")
					txt += "<h4>"+xx +": "  + data[cc][xx]  +"</h4>"
			}
		}
	}
	document.getElementById("content").innerHTML = txt;
}
function D6(amt)
{
	if(amt == null)
	{
		amt = 1
	} 
	total = 0
	for(var i = 0; i < amt; i++)
	{
		total += random.range(1, 6);
		console.log(total);
	}
	return total;
}
function D20(amt, min)
{
	if(amt == null)
	{
		amt = 1
	}
	total = 0
	for(var i = 0; i < amt; i++)
	{
		r = random.range(1, 20);
		if(r < min)
		{
			r = 0;
			i -= 1;
		}
		total += r
		console.log(total);
	}
	return total;
}
function D10(amt, min)
{
	if(amt == null)
	{
		amt = 1
	}
	total = 0
	for(var i = 0; i < amt; i++)
	{
		r = random.range(1, 10);
		if(r < min)
		{
			r = 0;
			i -= 1;
		}
		total += r
		console.log(total);
	}
	return total;
}
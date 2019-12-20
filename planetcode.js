function insertAfter(el, referenceNode) {
	    referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);
	}
function toDegrees (angle) {
  return angle * (180 / Math.PI);
}
function toRadians (angle) {
  return angle * (Math.PI / 180);
}
function Clamp(v, mini, maxi){
	return Math.max(Math.min(v, maxi), mini)
}
function Wrap(value, wrapval){
	return value - Math.round(Clamp(value, 1, 1000000)/wrapval) * wrapval
}
objs = []
planetangles = []

var smass = 0
function setupstarmap()
{
	p = document.getElementsByTagName("p")[0]
	newEl = document.createElement("div")
	newEl.id = "planetcanvas"
	selectTag = ""
	indx = 0
	planets.forEach(function(element){
		element.push(indx)
		selectTag += "<option value='" + element[4] + "'>" + element[0] + "</option>"
		indx += 1
	});
	selectTag += "</select>"
	newEl.innerHTML += "<canvas id='planetcanv' width='800' height='500'></canvas><br><div class='slidercontainer'><input type='range' min='-50' max='50' value='1' class='slider' id='slider1'></input></div><br><select id='select0'>" + selectTag + "<br><select id='select1'>" + selectTag + "<br><p id='dist'></p><p id='year'></p>"
	insertAfter(newEl, p)
	c = document.getElementsByTagName("canvas")[0]
	ctx = c.getContext('2d')
	ctx.beginPath()
	smass = document.getElementsByTagName("p")[0].innerHTML.split("Solar Mass: ")[1].split("<br>")[0]
	ctx.fillStyle = 'black'
	ctx.fillRect(0, 0, 800, 500)
	ctx.ellipse(350, 250, Clamp(smass * 14, 5, 20), Clamp(smass * 14, 5, 20), 0, 0, 360)
	ctx.strokeStyle = 'white'
	ctx.fillStyle = 'white'
	ctx.fill()
	ctx.stroke()
	planets.forEach(function(element){
		ctx.beginPath()
		ctx.ellipse(350, 250, element[1]*15, element[1]*15, 0, 0, 360)
		ctx.stroke()
		ctx.beginPath()
		//random point on circle would be nice
		r = element[1]*15
		angle = (Wrap(element[0].length, 6)+Wrap(element[2], 30))*360/36
		planetangles.push(angle)
		x = r*Math.sin(toRadians(angle))
		y = r*Math.cos(toRadians(angle))
		ctx.ellipse(350+x, 250+y, Math.min(Math.max(element[2]/100, 3), 10), Math.min(Math.max(element[2]/100, 3), 10), 0, 0, 360)
		ctx.fill()
		ctx.font = "14px Arial"
		ctx.fillText(element[0], 350+x, 250+y-Math.max(element[2]/100, 3))
	});
	setInterval(UpdateThing, 10)
}
o = 0
year = 63454
function UpdateThing()
{
	var c = document.getElementsByTagName("canvas")[0]
	var ctx = c.getContext('2d')
	ctx.beginPath()
	ctx.fillStyle = 'black'
	ctx.fillRect(0, 0, 800, 500)
	ctx.ellipse(350, 250, Clamp(smass * 14, 5, 20), Clamp(smass * 14, 5, 20), 0, 0, 360)
	ctx.strokeStyle = 'white'
	ctx.fillStyle = 'white'
	ctx.fill()
	ctx.stroke()
	var d1 = document.getElementById("select0").value;
	var d2 = document.getElementById("select1").value;
	var plan1 = planets[d1];
	var plan2 = planets[d2];
	var p1p = GetPos(plan1)
	var p2p = GetPos(plan2)
	//console.log(p1p, p2p);
	var dis = Distance(p1p[0], p1p[1], p2p[0], p2p[1]);
	document.getElementById("dist").innerHTML = "Distance: " + dis;
	i = 0
	speed = document.getElementById("slider1").value
	year += speed/10000;
	document.getElementById("year").innerHTML = "Year: " + Math.round(year * 1000)/1000 + " AGF."
	planets.forEach(function(element){
		c = "white"
		if(element[3] === "Volcanic")
			c = "red";
		if(element[3] === "Forest")
			c = "green";
		if(element[3].includes("Ocean"))
			c = "blue";
		if(element[3] === "Tagia")
			c = "gray"
		if(element[3].includes("Gas"))
			c = "purple"
		if(element[3] === "Desert")
			c = "orange"

		ctx.fillStyle = c
		ctx.strokeStyle = c
		ctx.beginPath()
		ctx.ellipse(350, 250, element[1]*15, element[1]*15, 0, 0, 360)
		ctx.stroke()
		ctx.beginPath()
		if(element[3] === "Goth")
		{
			c = "black"
			ctx.fillStyle = c
			ctx.strokeStyle = c
		}
		//random point on circle would be nice
		var r = element[1]*15
		var angle = planetangles[i] + 1/(element[2])
		planetangles[i] += 1/(element[1]*element[1]*element[1]/16)*5*(speed*Math.abs(speed)/100)
		var x = r*Math.sin(toRadians(angle))
		var y = r*Math.cos(toRadians(angle))
		ctx.ellipse(350+x, 250+y, Math.min(Math.max(element[2]/100, 3), 10), Math.min(Math.max(element[2]/100, 3), 10), 0, 0, 360)
		ctx.fill()
		if(element[3] === "Goth")
		{
			ctx.strokeStyle = "white"
			ctx.stroke()
		}
		ctx.fillStyle = "white"
		ctx.font = "14px Arial"
		ctx.fillText(element[0], 350+x, 250+y-Math.max(element[2]/100, 3))
		i+=1
	});
}
function Distance(x1, y1, x2, y2)
{
	return Math.sqrt(Math.abs(x1 - x2) + Math.abs(y1 - y2))
}
function GetPos(planet)
{
	var element = planet;
	var r = element[1]*15
	var angle = planetangles[planet[4]] + 1/(element[2])
	var x = r*Math.sin(toRadians(angle))
	var y = r*Math.cos(toRadians(angle))
	return [x, y]
}
setTimeout(setupstarmap, 100)
//planet stuff [0] = name, [1] = dist from star, [2] = size (my), [3] = enviroment, [4] = index
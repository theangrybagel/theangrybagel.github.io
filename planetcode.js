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
	newEl.innerHTML += "<canvas id='planetcanv' width='800' height='500' />"
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
function UpdateThing()
{
	c = document.getElementsByTagName("canvas")[0]
	ctx = c.getContext('2d')
	ctx.beginPath()
	ctx.fillStyle = 'black'
	ctx.fillRect(0, 0, 800, 500)
	ctx.ellipse(350, 250, Clamp(smass * 14, 5, 20), Clamp(smass * 14, 5, 20), 0, 0, 360)
	ctx.strokeStyle = 'white'
	ctx.fillStyle = 'white'
	ctx.fill()
	ctx.stroke()
	i = 0
	planets.forEach(function(element){
		ctx.beginPath()
		ctx.ellipse(350, 250, element[1]*15, element[1]*15, 0, 0, 360)
		ctx.stroke()
		ctx.beginPath()
		//random point on circle would be nice
		r = element[1]*15
		angle = planetangles[i] + 1/(element[2])
		planetangles[i] += 1/(element[1]*element[1]*element[1]/16)*5
		x = r*Math.sin(toRadians(angle))
		y = r*Math.cos(toRadians(angle))
		ctx.ellipse(350+x, 250+y, Math.min(Math.max(element[2]/100, 3), 10), Math.min(Math.max(element[2]/100, 3), 10), 0, 0, 360)
		ctx.fill()
		ctx.font = "14px Arial"
		ctx.fillText(element[0], 350+x, 250+y-Math.max(element[2]/100, 3))
		i+=1
	});
}
setTimeout(setupstarmap, 100)
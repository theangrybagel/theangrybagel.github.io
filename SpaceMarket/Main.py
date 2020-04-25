import Thruster, Others, random
from datetime import datetime
from Lib import GetHTML, StrDict, GetHTMLStars
from operator import itemgetter
import time
now = datetime.now()

random.seed(a=int(now.isocalendar()[1]*now.year))
from browser import document, timer


catalogue = []
def DisplayAsHTML(generated, ID, rating=5):
	txt = "<br><br><br><h2>{}</h2><button class='button' style='border: none;' id='buttonfor{}' onclick=\"ViewDiv('{}', '{}')\">Click here to view</button>".format(generated["name"], ID, generated["name"], (GetHTML(generated).replace("    ", "&emsp;"))) + "<span>" + GetHTMLStars(rating) + "</span>" + "<div id='{}'>".format(ID) + "</div>"
	return (txt)

def Generate():
	sources = {'thruster':Thruster.GetThruster, 'lifesupport': Others.LifeSupport, 'ship': Others.ShipGenerator, 'shipweapon': Others.ShipWeapon}
	sourceskeys = []
	for x in sources:
		sourceskeys.append(x)
	source = random.choice(sourceskeys)
	if source in sources:
		generated = sources[source]()
		#DisplayGenerated(generated)
		catalogue.append({"data": generated, "rating": random.randrange(1, 5), "trending": random.randrange(100, 200), "tag": source})
	else:
		print('Invalid generator source')

for x in range(60):
	Generate()



def AddNews(news):
	document.getElementById("announc").innerHTML += "&emsp;"*8+ news


document.getElementById("title").innerHTML = "The Galactic Market"
document.getElementById("Store").innerHTML = "<h2>Finding trending items... Please wait...</h2>"
#Get trending
def SetupTrendView():
	trending = sorted(catalogue, key=itemgetter('trending'))
	trendingShips = []
	for x in trending:
		if x['tag'] == "ship":
			trendingShips.append(x)
	document.getElementById("Store").innerHTML = "<div id='trending'><h2>Trending Now</h2></div>"
	for x, i in zip(trendingShips, range(len(trendingShips))):
		if i >= 5 or x == None:
			break
		document.getElementById("trending").innerHTML += DisplayAsHTML(x["data"], x["data"]["name"], rating=x["rating"])
	return

def AlterTrends():
	alterations = ((datetime.weekday(now)) * 24*4) + now.hour*4 + int(now.minute/15)
	for x in range(alterations):
		#find some items and adjust their trends
		for y in catalogue:
			y["trending"] += random.randrange(-3, 3)

AlterTrends()
SetupTrendView()
random.seed(now.second*now.minute*now.year)
#add advertisements
from Ads import ads, news
for a in range(4):
	ad = random.choice(ads)
	document.getElementById("Ads").innerHTML += ad + "<br>"*15


for x in range(4):
	AddNews(random.choice(news))

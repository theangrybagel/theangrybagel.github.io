import Thruster, Others, random
from datetime import datetime
from Lib import GetHTML, StrDict
from operator import itemgetter
import time
random.seed(a=int(datetime.today().month*datetime.today().year+(int(datetime.today().day)/4)))
from browser import document, timer


catalogue = []

def DisplayAsHTML(generated):
	return ("<br><br><br>" + (GetHTML(generated).replace("    ", "&emsp;")))
def Generate():
	sources = {'thruster':Thruster.GetThruster, 'lifesupport': Others.LifeSupport, 'ship': Others.ShipGenerator, 'shipweapon': Others.ShipWeapon}
	sourceskeys = []
	for x in sources:
		sourceskeys.append(x)
	source = random.choice(sourceskeys)
	if source in sources:
		print(source.upper()+"\n")	
		generated = sources[source]()
		#DisplayGenerated(generated)
		catalogue.append({"data": generated, "rating": random.randrange(1, 5), "trending": random.randrange(0, 1000), "tag": source})
	else:
		print('Invalid generator source')

for x in range(60):
	Generate()



def AddNews(news):
	document.getElementById("announc").innerHTML += "&emsp;"*8+ news


document.getElementById("title").innerHTML = "The Galactic Market"
#Get trending
def SetupTrendView():
	trending = sorted(catalogue, key=itemgetter('trending'))
	trendingShips = []
	for x in trending:
		if x['tag'] == "ship":
			trendingShips.append(x['data'])
	document.getElementById("Store").innerHTML = "<div id='trending'><h2>Trending Now</h2></div>"
	for x, i in zip(trendingShips, range(len(trendingShips))):
		if i >= 5 or x == None:
			break
		print(x)
		document.getElementById("trending").innerHTML += DisplayAsHTML(x)
	return



SetupTrendView()

random.seed(datetime.now().second*datetime.now().minute*datetime.now().year)
#add advertisements
from Ads import ads, news
for a in range(4):
	ad = random.choice(ads)
	document.getElementById("Ads").innerHTML += ad + "<br>"*15


for x in range(4):
	AddNews(random.choice(news))

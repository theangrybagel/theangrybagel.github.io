ads = ["""
<div style='background-color: #d1a000; color: #140013;'>
	<h3 class='c'>Introducing the YIP-MAX 2.0. Incubate your eggs like never before, no dead yolcorgs guaranteed!</h3>
	<br>
	<h2 class='c'>ORDER NOW! STARTING FROM ONLY 1600CR</h2>
	<p class='c'><i>Carton Industries</i></p> 
</div>
""",
"""
<div style='background-color: #520c00; color: #ccffe5;'>
	<h3 class='c'>Hungry?</h3>
	<br>
	<h3 class='c'><i>Poor?</i></h3>
	<br><br>
	<h2 class='c'>Order McRonalds. </h2>
	<p class='c'><i>You won't be disappointed.</i></p> 
</div>
""",
"""
<div style='background-color: #60afb5; color: #140013;'>
	<h3 class='c'>Do you like seeing through things? Seeing through the profit that we as a company are making off of you absent minded fools? Then you'll love the STC's new product!</h3>
	<h3 class='c'>Introducing the all new <b>See Through Window Mk. II</b>! This window is so transparent that it not only lets light through, but it also lets anything physical through as well! It's like it's not even there!</h3>
	<h3 class='c'>Order today, starting from 3000CR per window!</h3>
	<p class='r'>See Through Industries Inc. All rights reserved.</p>
</div>
""",
"""
<div style='background-color: #3c02c4; color: #72f542;'>
	<marquee style="top: 0; width: 100%; height: 30px;">Goopwazzer was delicous!&emsp;&emsp; Goopwazzer was great!</marquee>
	<h3 class='c'>Don't you miss Goopwazzer? We do. </h3><br>
	<h3 class='c b'>Help bring Goopwazzer back today!</h3>
	<br>
	<p class='c'>#revivegoopwazzer</p>
</div>
""",
]


import random
from Lore import Lore
news = ["Announcement from Sector 41: Whoever left their ship in the path of our incredibly important cargo carrier, please move it. If you do not comply, we will have no choice but to vaporize your spaceship.",
"Propaganda propaganda propaganda! Boy do I love that propaganda!", "Did you know that drinking ship fuel doesn't kill everyone? I got myself and some friends hooked on the stuff! Only two of my friends died from it."]
colors = ["red", "blue", "yellow", "pink", "green", "orange", "striped", "black", "white", "silver", "poka dotted", "extremely dirty"]
news.append("Announcement from Sector " + str(random.randrange(2, 99)) + ": Whoever owns the " + random.choice(colors) + " " + random.choice(Lore.bodies)["name"] + " out in the middle of space, please move it or we will have it destroyed. ")
news.append("Announcement from Sector " + str(random.randrange(2, 99)) + ": Whoever owns the " + random.choice(colors) + " " + random.choice(Lore.bodies)["name"] + " out in the middle of space, please move it or we will have it destroyed. ")

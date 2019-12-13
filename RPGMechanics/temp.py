from math import sqrt
import math
sy = -5
ay = -9.8
uy = 0
ty = (sqrt(2*ay*sy))/-9.8
ux = 15
ax = 0
sx = ux*ty
print(ty, sx)
xaccel = 0
yaccel = -9.8
xm = 0
ym = 0
timestamp = 0
cxv = 0
cyv = 0
cposx = 0
cposy = 0
def velat(time):
	global timestamp
	global cxv
	global cyv
	#assuming you've got inital pos = 0, dont know new position, ux/uy (xm/ym), accelX(0), accelY(-9.8)
	timestamp = time
	cxv = xm + xaccel * time
	cyv = ym + yaccel*time
	print("Without Ground", cxv, cyv)
	cposx = xm * time + .5*xaccel*(time*time)
	cposy = ym * time + .5*yaccel*(time*time)
	print("Position", cposx, cposy)
	if cposy < 0:
		cxv = 0
		cyv = 0
	print("Velocity with ground", cxv, cyv)
def magfromang(a, mag):
	global xm
	global ym
	ang = a * math.pi / 180
	xm = math.cos(a) * mag
	ym = math.sin(a) * mag
	print("X:", xm, " --- ", "Y: ", ym)
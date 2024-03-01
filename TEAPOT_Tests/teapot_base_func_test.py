#===========================================
# Test of TEAPOT functions for tracking and
# possible memory leaks.
#===========================================

import posix

from orbit import teapot
from bunch import Bunch
from orbit.teapot import teapot

print "Start."

b_init = Bunch()
syncPart = b_init.getSyncParticle()
#energy in GeV
energy = 1.0                          
syncPart.kinEnergy(energy)

nParts = 100000
for i in xrange(nParts):
	b_init.addParticle(0.1+i,0.2+i,0.3+i,0.4+i,0.5+i,0.6+i)

print "n parts.  =",nParts
print "mass[GeV] = ",b_init.mass()
print "charge    = ",b_init.charge()
print "======== Start Tracking ========="

count = 0
while(1< 2):
	b = Bunch()
	b_init.copyBunchTo(b)
	ring_length = 100.
	b.ringwrap(ring_length)
	#------------------------------------
	teapot.TPB.rotatexy(b, 0.5)
	#------------------------------------
	teapot.TPB.drift(b,1.1)
	#------------------------------------
	teapot.TPB.multp(b,2,0.8,5)
	#------------------------------------
	teapot.TPB.multpfringeIN(b,1,0.9,0)
	#------------------------------------
	teapot.TPB.multpfringeOUT(b,1,0.9,0)
	#------------------------------------
	teapot.TPB.kick(b,1.0e-10,2.0e-10,2.0e-10,)
	#------------------------------------
	teapot.TPB.quad1(b,1.0,2.0)
	#------------------------------------
	teapot.TPB.quad2(b,1.0)
	#------------------------------------
	teapot.TPB.quadfringeIN(b,2.0)
	#------------------------------------
	teapot.TPB.quadfringeOUT(b,2.0)
	#------------------------------------
	teapot.TPB.wedgerotate(b,0.5,1)
	#------------------------------------
	teapot.TPB.wedgedrift(b,0.5,2)
	#------------------------------------
	teapot.TPB.wedgebend(b,0.5,1,2.0,1)
	#------------------------------------
	teapot.TPB.bend1(b,1.0,2.0)
	#------------------------------------
	teapot.TPB.bend2(b,1.0)
	#------------------------------------
	teapot.TPB.bend3(b,1.0)
	#------------------------------------
	teapot.TPB.bend4(b,1.0)
	#------------------------------------
	teapot.TPB.bendfringeIN(b,0.5)
	#------------------------------------
	teapot.TPB.bendfringeOUT(b,0.5)
	#------------------------------------
	teapot.TPB.soln(b,0.5,0.66)
	#------------------------------------
	e = 0.1
	inout = 1
	rho = 0.2
	vecnum = 3
	poleV = [1,2,3]
	klV = [0.4,0.5,0.6]
	skewV = [4,5,6]
	nsteps = 10
	teapot.TPB.wedgebendCF(b,e,inout,rho,vecnum,poleV,klV,skewV,nsteps)
	#------------------------------------
	count += 1
	if(count % 1 == 0):
		print "i=",count," time= %6.3f "%(posix.times()[0]/count)

print "Stop."

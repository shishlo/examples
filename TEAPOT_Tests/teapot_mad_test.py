#===========================================
# Test TEAPOT tracking through SNS Ring
# for protons (default) and arbitrary heavy 
# ions. The results should be the same.
#===========================================

import sys

from orbit.teapot import teapot
from orbit.lattice import AccLattice, AccNode, AccActionsContainer
from bunch import Bunch

print "Start."

b_init = Bunch()
b_init.addParticle(1.0e-3,0.0,0.0,0.0,0.0,0.0)
b_init.addParticle(0.0,1.0e-3,0.0,0.0,0.0,0.0)
b_init.addParticle(0.0,0.0,1.0e-3,0.0,0.0,0.0)
b_init.addParticle(0.0,0.0,0.0,1.0e-3,0.0,0.0)
b_init.addParticle(0.0,0.0,0.0,0.0,1.0e-3,0.0)
b_init.addParticle(0.0,0.0,0.0,0.0,0.0,1.0e-3)
b_init.compress()

syncPart = b_init.getSyncParticle()
#energy in GeV
energy = 1.0                          
syncPart.kinEnergy(energy)

mass = b_init.mass()
charge = b_init.charge()
momentum = syncPart.momentum()

#---------------------------------------------------
#---- Let's build TEAPOT lattice for SNS Ring
#---------------------------------------------------
teapot_latt = teapot.TEAPOT_Lattice()
teapot_latt.readMAD("sext_623_620_00.mad","RNG")
print "Lattice=",teapot_latt.getName()," length [m] =",teapot_latt.getLength()

#------------------------------------------------------------
#---- Now let's track bunch, keeping the initial bunch
#-----------------------------------------------------------
b = Bunch()
b_init.copyBunchTo(b)
teapot_latt.trackBunch(b)
print "=============Results of tracking # 1 ===================="
for ind in range(b.getSize()):
	(x,xp,y,yp,z,dE) = (b.x(ind),b.xp(ind),b.y(ind),b.yp(ind),b.z(ind),b.dE(ind))
	st = "%d2  %+15.7e  %+15.7e   %+15.7e  %+15.7e  %+15.7e  %+15.7e "
	print st%(ind,x,xp,y,yp,z,dE)
print "========================================================="

#------------------------------------------------------------
#---- define a new heavy ion
#----------------------------------------------------------

b = Bunch()
b_init.copyBunchTo(b)

b.mass(10.)
b.charge(5.0)
syncPart = b.getSyncParticle()
momentum_new = (b.charge()/charge)*momentum
syncPart.momentum(momentum_new)

#------------------------------------------------------------------------
# TEAPOT used k1 = (dB/dr)/(momentum/charge)) in magnets (quads)
# where momentum/charge = B*rho
# So, tracking should give the same results for all particles
# except the last one.
# The last line is different because the 1 MeV change in the energy will
# result in different velocity change for particles with different mass.
#-------------------------------------------------------------------------

teapot_latt.trackBunch(b)
print "=============Results of tracking # 2 ===================="
for ind in range(b.getSize()):
	(x,xp,y,yp,z,dE) = (b.x(ind),b.xp(ind),b.y(ind),b.yp(ind),b.z(ind),b.dE(ind))
	st = "%d2  %+15.7e  %+15.7e   %+15.7e  %+15.7e  %+15.7e  %+15.7e "
	print st%(ind,x,xp,y,yp,z,dE)
print "========================================================="

"""
#---------------Results to compare -----------------------------
Lattice= RNG  length [m] = 248.0
=============Results of tracking # 1 ====================
02   +9.6526633e-04   -5.4566491e-05    +0.0000000e+00   +0.0000000e+00   -2.0623633e-05   +0.0000000e+00 
12   +1.5595394e-04   +1.0274038e-03    +0.0000000e+00   +0.0000000e+00   -5.6233120e-05   +0.0000000e+00 
22   +4.2191444e-10   +4.9129255e-10    -1.1433267e-03   +1.9585874e-04   -2.7585546e-06   +0.0000000e+00 
32   -3.5852008e-08   +1.2032839e-07    -2.5935129e-02   +3.5800768e-03   -7.4353838e-04   +0.0000000e+00 
42   +0.0000000e+00   +0.0000000e+00    +0.0000000e+00   +0.0000000e+00   +1.0000000e-03   +0.0000000e+00 
52   +2.3315706e-07   +1.3078068e-07    +0.0000000e+00   +0.0000000e+00   +3.3000219e-02   +1.0000000e-03 
=========================================================
=============Results of tracking # 2 ====================
02   +9.6526633e-04   -5.4566491e-05    +0.0000000e+00   +0.0000000e+00   -2.0623633e-05   +0.0000000e+00 
12   +1.5595394e-04   +1.0274038e-03    +0.0000000e+00   +0.0000000e+00   -5.6233120e-05   +0.0000000e+00 
22   +4.2191444e-10   +4.9129255e-10    -1.1433267e-03   +1.9585874e-04   -2.7585546e-06   +0.0000000e+00 
32   -3.5852008e-08   +1.2032839e-07    -2.5935129e-02   +3.5800768e-03   -7.4353838e-04   +0.0000000e+00 
42   +0.0000000e+00   +0.0000000e+00    +0.0000000e+00   +0.0000000e+00   +1.0000000e-03   +0.0000000e+00 
52   +9.1527677e-08   +5.0482833e-08    +0.0000000e+00   +0.0000000e+00   +2.4641415e-02   +1.0000000e-03

#-----------------------------------------
# The last line is different because the 1 MeV change in the energy will
# result in different 
"""

sys.exit(0)

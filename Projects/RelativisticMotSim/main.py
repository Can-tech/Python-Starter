# Student ID  : 2423341
# Project Name: 1-D Relativistic Motion
# Project ID  : S-KIN-1D_Rel_Motion
# Description : This code is used to simulate the relativistic motion of a particle in 1-D space and compare it with classical mechanics.

import math
import matplotlib.pyplot as plt

m=1
F=1000
#1.67e-26
a=round(F/m,2)
rel_acc_instant=0
rel_vel_instant=0
rel_mom_instant=0
classic_acc_instant=a
classic_vel_instant=0
c= 299792458
dt=1000
N=700

def gamma(vel):
    return 1/(math.sqrt(1-(vel**2/c**2)))

def rel_acc(vel):
    return a/((gamma(vel))**3)
def rel_mom(vel):
    return (m*vel)*gamma(vel)
def rel_tot_energy(momentum):
    return math.sqrt(((momentum*c)**2)+((m*c)**2))

time_list=[i*dt for i in range(N)]
classic_acc_list=[a for i in range(N)]
classic_vel_list=[]
classic_energy_list=[]
j=0
while j<N:
    print(classic_vel_instant, (1/2)*m*(classic_vel_instant**2))
    classic_vel_list.append(classic_vel_instant/c)
    classic_vel_instant+=classic_acc_instant*dt
    classic_energy_list.append((1/2)*m*(classic_vel_instant**2))
    j+=1

i=0
rel_acc_list=[]
rel_vel_list=[]
rel_mom_list=[]
rel_tot_eng_list=[]
while i<N:
    # print(rel_acc_instant,rel_vel_instant,rel_mom_instant,rel_tot_eng_instant)  
    rel_acc_instant=rel_acc(rel_vel_instant)
    rel_acc_list.append(rel_acc_instant)
    rel_vel_instant+=(rel_acc_instant*dt)
    rel_vel_list.append((rel_vel_instant)/c)
    rel_mom_instant=rel_mom(rel_vel_instant)
    rel_mom_list.append(rel_mom_instant)
    rel_tot_eng_list.append(rel_tot_energy(rel_mom_instant))

    i+=1

#Time vs Velocity Graph
plt.xlabel("Time(s)")
plt.ylabel("Velocity(V/c)(unitless)")
plt.plot(time_list,rel_vel_list)
plt.plot(time_list,classic_vel_list)
plt.axhline(1, linestyle='--', color="black")
plt.legend(["Relativistic","Classic"])
plt.show()
#Time vs Acceleration Graph
plt.xlabel("Time(s)")
plt.ylabel("Acceleration(m/s²)")
plt.plot(time_list,rel_acc_list)
plt.plot(time_list,classic_acc_list)
plt.legend(["Relativistic","Classic"])
plt.axhline(0, linestyle='--', color="black")
plt.show()

#Energy vs Time Graph
plt.plot(rel_vel_list,rel_tot_eng_list)
plt.plot(classic_vel_list,classic_energy_list)

plt.axvline(1, linestyle='--', color="black")
plt.xlabel("Velocity(v/c)")
plt.ylabel("Energy(Work)(Joule)")
plt.legend(["Relativistic","Classic"])
plt.show()


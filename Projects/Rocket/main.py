# Student ID  : 2423341
# Project Name: Rocket
# Project ID  : S-KIN-Rocket
# Description : This code calculates the acceleration, velocity, distance between rocket to the center of the earth and gravity force on the rocket until it reaches the escape speed of the earth. 

import math
import matplotlib.pyplot as plt

##Falcon 9
ROCKET_INITIAL_MASS_kg=549054
ROCKET_DIAMETER_m=3.7
ROCKET_HEIGHT_m=70
ROCKET_PROPELLANT_MASS_FIRST_STAGE_kg=395700
ROCKET_FUELL_CONSUPTION_kg_PER_sec=550
ROCKET_THRUST_newton=7607*(10**3)
ROCKET_CENTER_OF_MASS_LOCATION_m=(2*ROCKET_HEIGHT_m/5)

##Earth
EARTH_MASS_kg=5.98*(10**(24))
EARTH_RADIOUS_m=6371*10**3
G_CONST=6.673*(10**(-11))
ESCAPE_VEL_m_PER_sec=11200
ALTITUDE=0

#Time seconds
dt=1

acc=0
vel=0
gravity_force=9.81*ROCKET_INITIAL_MASS_kg
time=0
rocket_position=ROCKET_CENTER_OF_MASS_LOCATION_m
distance_rocket_to_center_of_earth=EARTH_RADIOUS_m+ROCKET_CENTER_OF_MASS_LOCATION_m+ALTITUDE
remaining_rocket_propellant=ROCKET_PROPELLANT_MASS_FIRST_STAGE_kg
rocket_mass=ROCKET_INITIAL_MASS_kg

acc_list=[]
vel_list=[]
time_list=[]
gravity_list=[]
distance_rocket_to_center_of_earth_list=[]

def calculate_g(distance):
 return G_CONST*EARTH_MASS_kg/(distance**2)

#UNTIL THE ROCKET REACHES THE ESCAPE SPEED 11200
while vel<11200:
    acc_list.append(acc)
    vel_list.append(vel)
    time_list.append(time)
    gravity_list.append(gravity_force)
    distance_rocket_to_center_of_earth_list.append(distance_rocket_to_center_of_earth)
    instant_net_force=(ROCKET_THRUST_newton-(rocket_mass*calculate_g(distance_rocket_to_center_of_earth)))
    acc=instant_net_force/rocket_mass
    vel+=acc*dt
    rocket_mass-=ROCKET_FUELL_CONSUPTION_kg_PER_sec*dt
    remaining_rocket_propellant-=ROCKET_FUELL_CONSUPTION_kg_PER_sec*dt
    distance_rocket_to_center_of_earth+=(vel*dt)+((1/2)*acc*(dt**2))
    gravity_force=(rocket_mass*calculate_g(distance_rocket_to_center_of_earth))
    time+=dt

plt.xlabel("time(s)")
plt.ylabel("acceleration(m/s²)")
plt.plot(time_list,acc_list)
plt.show()

plt.xlabel("time(s)")
plt.ylabel("velocity(m/s)")
plt.plot(time_list,vel_list)
plt.show()

plt.xlabel("Distance Rocket to Center of the Earth(m)")
plt.ylabel("Gravity(N)")
plt.plot(distance_rocket_to_center_of_earth_list,gravity_list)
plt.show()

plt.xlabel("Time(seconds)")
plt.ylabel("Distance Rocket to Center of the Earth(m)")
plt.plot(time_list,distance_rocket_to_center_of_earth_list)
plt.show()








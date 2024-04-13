import statistics;

values_of_radious_first_ring=[[1.27,1.45,1.3], [1.3925,1.2975,1.42], [1.14,1.405,1.1925], [1.3525,1.085], [1.2575,0.96]];
values_of_radious_second_ring=[[2.19, 2.2125, 2.235], [2.18, 2.01, 2.24], [1.97, 2.1375, 1.9225], [2.04, 1.8425], [2.04, 1.7625]];
mean_values_of_radious_first_ring=[1.340,1.370,1.245,1.218,1.108]
mean_values_of_radious_second_ring=[2.212,2.143,2.009,1.941,1.900]
Standard_Deviation=[]

for i in values_of_radious_second_ring:
    print(statistics.stdev(i));
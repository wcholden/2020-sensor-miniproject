Will Holden & Stephanie Pellicane 

TASK 0

The greeting string issued by the server to the client upon first connecting is as follows:

	ECE Senior Capstone IoT simulator




TASK 1

After running sp_iotsim.server and sp_iotsim.client in the terminal, the following outputs are printed:

	{"class1": {"time": "2020-09-16T15:44:44.313231", "temperature": [26.925777244795224], "occupancy": [23], "co2": [21.812608763922334]}}
	{"lab1": {"time": "2020-09-16T15:44:44.534277", "temperature": [21.43359063763903], "occupancy": [6], "co2": [10.796119559568975]}}
	{"office": {"time": "2020-09-16T15:44:45.192890", "temperature": [24.272252243324147], "occupancy": [4], "co2": [5.48999873247679]}}
	{"office": {"time": "2020-09-16T15:44:46.292582", "temperature": [21.788908732340992], "occupancy": [2], "co2": [3.1046936855824043]}}
	{"lab1": {"time": "2020-09-16T15:44:47.610804", "temperature": [20.998294759694662], "occupancy": [5], "co2": [13.86296162661886]}}



TASK 2

After running analyze.py in the terminal, the following outputs are printed:

	median temperature: 
	lab1      21.002071
	class1    27.018662
	office    23.008560
	dtype: float64 

	median occupancy: 
	lab1       5.0
	class1    19.0
	office     2.0
	dtype: float64 

	median co2: 
	lab1       9.485641
	class1    29.291713
	office     4.619367
	dtype: float64 

	temperature variance: 
	lab1        7.098741
	class1    126.840789
	office    184.235808
	dtype: float64 

	occupancy variance: 
	lab1       4.677633
	class1    18.058467
	office     1.947494
	dtype: float64 

	co2 variance: 
	lab1       9.578181
	class1    30.963790
	office     5.446523
	dtype: float64 

	mean interval: 
	0    1.036616
	dtype: float64 

	interval variance: 
	0    1.378764
	dtype: float64 

From this we can extrapolate that the median of the temperature data in the lab is about 21.00 degrees Celcius 


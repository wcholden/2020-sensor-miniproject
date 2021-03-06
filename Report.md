Will Holden & Stephanie Pellicane 

TASK 0

1. The greeting string issued by the server to the client upon first connecting is as follows:

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

1. From this data we can extrapolate that the median of the temperature data in the lab is about 21.00 degrees Celcius, and the variance is about 7.10.

2. We can also extrapolate that the median of the occupancy data in the lab is about 5.00, and the variance is about 4.68.

3. The probability density functions of each of the sensor types can be found by following the links below:

temperature: https://drive.google.com/file/d/1w3t552Pa64eC8ymP9X3lqkQAtCqPk8-M/view?usp=sharing

occupancy: https://drive.google.com/file/d/1_Jg4zSDsX_OFwl_RXxzGZZ-CBA2ucBEq/view?usp=sharing

co2: https://drive.google.com/file/d/109TIqA39hV6FFJvPFR9-2-A-eZXxeP0v/view?usp=sharing

4. The mean of the time interval of the sensor readings is about 1.04 seconds, and the variance is about 1.38.
The PDF of the time intervals can be found by following the link below:

time intervals: https://drive.google.com/file/d/1mwL2Rg3X3VM-U8W28gcPUHj9_zWVmdLM/view?usp=sharing

This resembles a chi squared distribution, in that it starts our with a steep rise followed by a more gradual fall. 




TASK 3

After running our code task3.py (based on analyze.py) in the terminal, the following outputs are printed:

	mean temperature: 
	 lab1      20.886339
	class1    26.518707
	office    23.474051
	dtype: float64 

	temperature variance: 
	 lab1        7.098741
	class1    126.840789
	office    184.235808
	dtype: float64 

	lab min:  15.557646966121329 
	lab max:  26.215031763863802 
	 class min:  3.99398384118458 
	class max:  49.04343022251838 
	 office min:  -3.6726468728146493 
	office max:  50.620749864370495 

	0.759493670886076  percent of lab data points were bad
	1.243781094527363  percent of class data points were bad
	0.49875311720698257  percent of office data points were bad 

	new median temperature: 
	 0    21.00206
	dtype: float64 

	new temperature variance: 
	 0    0.415759
	dtype: float64 

1. From this data we may extrapolate that about 0.76% of lab temperature data points are bad, 1.24% of class temperature data points are bad, 
and 0.50% of office temperature data points are bad. Our method for determining which points are "bad" is fairly straight forward. First
take the square root of each room's temperature variance to get the standard deviation. A data point is considered "bad" if it is over or
under two standard deviations from the mean temperature of each room. 

With the "bad" data points discarded the median temperature of the lab is still 21.00 degrees, but the variance decreased from 7.10 to 0.42. 
This illustrates the drastic effect the ouliers have on the variance of the data. 

2. A persistant change in temperature does not necessarily indicate a failed sensor. A temperatuer fluxuation could be caused by a faulty HVAC
system or human interference (lighting candles, bringing in hot food, etc.)

3. In order to accurately judge the temperature bounds of each room, a zoomed-in PDF of the temperature data is observed (link below)

https://drive.google.com/file/d/1HZpzggfWYeLce8bO8XOA1RRVjlYz88e6/view?usp=sharing

The temperature in the lab is usually between 18 degrees Celcius and 23 degrees Celcius (64 degrees Fahrenheit and 73 degrees Fahrenheit).
The temperature in the office is usually between 15 degrees Celcius and 33 degrees Celcius (59 degrees Fahrenheit and 91 degrees Fahrenheit).
the temperature in the class is usually between 20 degrees Celcius and 35 degrees Celcius (68 degrees Fahrenheit and 95 degrees Fahrenheit).




TASK 4 

1. Websockets allow for softwares to send and receive data without experiencing delay. This can be used for ride sharing applications, multiplayer games, and messaging applications.

2. One can imagine how a web-time out or connectivity issue could cause software problems and data collection issues, and is something that is not accounted for in this program. 

3. We initially had some problems getting my websockets server and client running - when typing the command to connect to the server, there was no message diplaying that the IoT simulator began running. This problem was only solved after a computer reboot and python re-download. Once connected, however, there no issues at all. I'm assuming I had previous python packages installed that were interfering with my software, and I can  In the past I've used websockes with C++, and was required to perform more steps as opposed to two simple one line commands initializing the IoT Simulator. It appears Python is more suited for simple websocket integration.

4. We predict it would be better to have the sensors reach out to the server when they have the data to prevent a backup of information. However, information polled directly from the sensor to the server can be more up-to-date than data collected and then sent to the server. It will depend on the application.































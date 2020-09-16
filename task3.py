import pandas as pd
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np
import math


def load_data(file: Path) -> T.Dict[str, pd.DataFrame]:

    temperature = {}
    occupancy = {}
    co2 = {}

    with open(file, "r") as f:
        for line in f:
            r = json.loads(line)
            room = list(r.keys())[0]
            time = datetime.fromisoformat(r[room]["time"])

            temperature[time] = {room: r[room]["temperature"][0]}
            occupancy[time] = {room: r[room]["occupancy"][0]}
            co2[time] = {room: r[room]["co2"][0]}

    data = {
        "temperature": pd.DataFrame.from_dict(temperature, "index").sort_index(),
        "occupancy": pd.DataFrame.from_dict(occupancy, "index").sort_index(),
        "co2": pd.DataFrame.from_dict(co2, "index").sort_index(),
    }

    return data


def datetime_to_float(d):
    return d.timestamp()





if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

    temp = pd.DataFrame(data['temperature'])

    num_items = temp.count()

    mean_temp = temp.mean(axis = 0)
    print("mean temperature: \n" , mean_temp , "\n")

    var_temp = temp.var()
    print("temperature variance: \n" , var_temp , "\n")
 

    lab_bad = 0
    class_bad = 0
    office_bad = 0


    var_coeff = 2

    max_lab = mean_temp.lab1 + (var_coeff * math.sqrt(var_temp.lab1))
    min_lab = mean_temp.lab1 - (var_coeff * math.sqrt(var_temp.lab1))

    max_class = mean_temp.class1 + (var_coeff * math.sqrt(var_temp.class1))
    min_class = mean_temp.class1 - (var_coeff * math.sqrt(var_temp.class1))

    max_office = mean_temp.office + (var_coeff * math.sqrt(var_temp.office))
    min_office = mean_temp.office - (var_coeff * math.sqrt(var_temp.office))



    print("lab min: " , min_lab , "\nlab max: " , max_lab, "\n" , "class min: " , min_class , "\nclass max: " , max_class, "\n" , "office min: " , min_office , "\noffice max: " , max_office, "\n")

    temp_rev_lab = {}

    for k in range(0, 1198):
        if temp.lab1[k] > max_lab:
            lab_bad = lab_bad + 1
        elif temp.lab1[k] < min_lab:
            lab_bad = lab_bad + 1
        else:
            temp_rev_lab[k] = temp.lab1[k]


    for k in range(0, 1198):
        if temp.class1[k] > max_class:
            class_bad = class_bad + 1
        elif temp.class1[k] < min_class:
            class_bad = class_bad + 1


    for k in range(0, 1198):
        if temp.office[k] > max_office:
            office_bad = office_bad + 1
        elif temp.office[k] < min_office:
            office_bad = office_bad + 1


    print((100*lab_bad/num_items.lab1) , " percent of lab data points were bad")
    print((100*class_bad/num_items.class1) , " percent of class data points were bad")
    print((100*office_bad/num_items.office) , " percent of office data points were bad \n")

    temp_rev = {"temp": pd.DataFrame.from_dict(temp_rev_lab, "index").sort_index()}
    tempz = pd.DataFrame(temp_rev['temp'])

    new_med_temp = tempz.median(axis = 0)
    print("new median temperature: \n" , new_med_temp , "\n")

    new_var_temp = tempz.var()
    print("new temperature variance: \n" , new_var_temp , "\n")

























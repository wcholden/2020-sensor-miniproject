#!/usr/bin/env python3
"""
This example assumes the JSON data is saved one line per timestamp (message from server).

It shows how to read and process a text file line-by-line in Python, converting JSON fragments
to per-sensor dictionaries indexed by time.
These dictionaries are immediately put into Pandas DataFrames for easier processing.

Feel free to save your data in a better format--I was just showing what one might do quickly.
"""
import pandas as pd
from pathlib import Path
import argparse
import json
from datetime import datetime
import typing as T
import matplotlib.pyplot as plt
import numpy as np


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


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="load and analyse IoT JSON data")
    p.add_argument("file", help="path to JSON data file")
    P = p.parse_args()

    file = Path(P.file).expanduser()

    data = load_data(file)

    temp = pd.DataFrame(data['temperature'])
    occ = pd.DataFrame(data['occupancy'])
    co2 = pd.DataFrame(data['co2'])

    ax_temp = temp.plot.kde()
    ax_occ = occ.plot.kde()
    ax_co2 = co2.plot.kde()

    med_temp = temp.median(axis = 0)
    print("median temperature: \n" , med_temp , "\n")
    med_occ = occ.median(axis = 0)
    print("median occupancy: \n" , med_occ , "\n")
    med_co2 = co2.median(axis = 0)
    print("median co2: \n" , med_co2 , "\n")

    var_temp = temp.var()
    print("temperature variance: \n" , var_temp , "\n")
    var_occ = occ.var()
    print("occupancy variance: \n" , var_occ , "\n")
    var_co2 = co2.var()
    print("co2 variance: \n" , var_co2 , "\n")




    for k in data:
        # data[k].plot()
        time = data[k].index
        data[k].hist()
        plt.figure()
        plt.hist(np.diff(time.values).astype(np.int64) // 1000000000)
        plt.xlabel("Time (seconds)")

    plt.show()

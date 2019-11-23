#!/usr/bin/env python

import tkinter
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import os


def graphRawFX():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)
    data_path = os.path.join(dir_path, '../TestData/GBPUSD1d.txt')
    print(data_path)
    date,bid,ask = np.loadtxt(data_path, unpack=True, 
                    delimiter=','#,
                    #converters={0:mdates.datestr2num('%Y%m%d%H%M%S')}
                    )
    fig = plt.figure(figsize=(10,7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)

    ax1.plot(date,bid)
    ax1.plot(date,ask)

    #ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    graphRawFX()
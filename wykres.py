import pyseries.LoadingData as loading
import pyseries.Preprocessing as prep
import pyseries.Analysis as analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

paths = ['/home/az/Desktop/Nagrania EEG/rest/Agnieszka_03_06_16/', '/home/az/Desktop/Nagrania EEG/rest/Agnieszka_07_21_16/', \
 '/home/az/Desktop/Nagrania EEG/rest/Aleksandra_07_15_16/', '/home/az/Desktop/Nagrania EEG/rest/Aleksandra_07_21_16/', \
 '/home/az/Desktop/Nagrania EEG/rest/Ania_14_06_16/', '/home/az/Desktop/Nagrania EEG/rest/Karen_14_06_16/', \
 '/home/az/Desktop/Nagrania EEG/rest/Kuba_14_06_16/', '/home/az/Desktop/Nagrania EEG/rest/Rysiek_03_06_16/', \
 '/home/az/Desktop/Nagrania EEG/rest/Rysiek_07_21_16/']

recording_list = []
def read(signal):
#reads the whole info about eeg for all paths   
    for single_path in paths:
        recording = loading.Read_edf.Combine_EDF_XML(single_path, 3, 70)
        recording_list.append(recording)
    return recording_list
    
read(paths)



first_entry = recording_list[0]
fig, axes = plt.subplots(1)
axes.plot(first_entry['timestamp'], first_entry['EEG C3'])   
      
events0 = first_entry['events']

times = np.array(events0['trial'].index.values, dtype ='datetime64[ms]')
x1 =times[0]
x2 =times[1]
axes.axvline(x1, color='k', linestyle='dashed')
axes.axvline(x2, color='k', linestyle='dashed')

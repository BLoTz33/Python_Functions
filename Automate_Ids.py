import pandas as pd

def Retrive_ids(dataset, col):
    url_array = dataset.iloc[:,col].values
    i = 0
    while i < len(url_array):
        start_string = 'spotify:track:'
        url_array[i] = url_array[i].replace(start_string,'')
        i += 1
    return url_array
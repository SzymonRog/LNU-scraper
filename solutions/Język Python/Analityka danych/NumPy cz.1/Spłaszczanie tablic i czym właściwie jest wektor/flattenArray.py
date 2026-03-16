from superSecretModule import join_tables


def flatten_data(sensor_data_list):
    flattened_list = []  
    for arr in sensor_data_list:  
        flattened_list.append(arr.flatten())  
    return join_tables(flattened_list) 


import copy
def correct_time(data_storage, time):
    inna_lista = copy.deepcopy(data_storage)
    inna_lista.time = time
    return inna_lista
import fitness
def clientBmi( clientsData, clientId ):
    data = clientsData[clientId][4:]
    return fitness.bmi(*data)
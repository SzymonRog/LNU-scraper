import datetime
def englishBreakfast(x):
    odp = []
    temp = []
    today = datetime.datetime.today().strftime('%Y%m%d')
    todayY = int(today[0:4]) #Rok

    if int(today[4]) == 0:
        todayM = int(today[5:6])
    else:
        todayM = int(today[4:6])

    if int(today[6]) == 0:
        todayD = int(today[7:])
    else:
        todayD = int(today[6:])
    koniec = datetime.date(todayY, todayM, todayD)
    
    
    for i in x:
        temp.append(str(i[0]))
        agentY = int(i[1][0:4])
        if int(i[1][4]) == 0:
            agentM = int(i[1][5:6])
        else:
            agentM = int(i[1][4:6])
            
        if int(i[1][6]) == 0:
            agentD = int(i[1][7:])
        else:
            agentD = int(i[1][6:])
            
        początek = datetime.date(agentY, agentM, agentD)
        dni = int((koniec - początek).days)
        temp.append(dni)
        odp.append(temp)
        temp = []
    return odp
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#2020.01.30
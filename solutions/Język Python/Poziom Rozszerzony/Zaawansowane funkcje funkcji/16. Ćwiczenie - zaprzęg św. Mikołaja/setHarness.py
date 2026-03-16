#place for your code
def setHarness(minRP, **renifery, ):
    reniferowie = sorted(renifery, key= renifery.get, reverse = True)
    total_power = 0 
    wybrani = []
    zaprzęg = {'Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph'}
    for renifer in reniferowie:
        if renifer in zaprzęg:
            total_power += renifery[renifer]
            wybrani.append(renifer)
            
        if total_power >= minRP:
            break 
    
    return sorted(wybrani, reverse = False)
def cargoSpace(area = 240, business = 0, premium = 0, economy = 0):
    print("Available space:", round( area - business*2 - premium*1.6 - economy*1.2, 2))
    
    
cargoSpace(area = 240, premium = 12, economy = 145)
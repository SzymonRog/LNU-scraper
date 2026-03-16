#write your code here
def finalPrice(price,/, tax = 23, discount = 0):
    final_price = price + (price * tax/100) 
    if discount:
        return round(final_price - (final_price * discount/100), 2 )
    else:
        return round(final_price,2)
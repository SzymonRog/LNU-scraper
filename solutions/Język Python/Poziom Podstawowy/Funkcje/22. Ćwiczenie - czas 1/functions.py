#your codede
def to_time(x,y,z):

   if y < 10:

       y = f'0{y}'

   if x < 10:

       x = f'0{x}'

   return int(f'{z}{y}{x}')


def crimes(crimesList):
   return[[ str(i[0]) , sum(i[2:7])] for i in crimesList ]
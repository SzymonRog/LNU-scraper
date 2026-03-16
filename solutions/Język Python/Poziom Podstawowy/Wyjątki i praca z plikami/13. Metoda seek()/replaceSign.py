def replaceSign(x, y):
  f = open("data.txt", "r+")
  f.seek( x - 1 )
  f.write( y )
  f.close()
   
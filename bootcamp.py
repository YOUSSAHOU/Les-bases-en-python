
def decision(python, numpy, pandas, matplotlib, abscence,niveau):
  a=int(python)
  b=int(numpy)
  c=int(pandas)
  d=int(matplotlib)
  e=int(abscence)
  g=int(niveau)
  moyenne= (a*3 + b*4 + c*7 + d*5)/19
  if e > 0:
    moyenne*=(1 - e*0.05)
  
  if e == 0:
    moyenne*=(1 + e*0.1)
  
  if g == 5:
      if moyenne >= 17:
          return "Oui"
      else:
          return "Non"
  elif g == 4:
      if moyenne >= 15:
          return "Oui"
      else:
          return "Non"
  elif g == 3:
      if moyenne >= 14:
          return "Oui"
      else:
          return "Non"
  elif g == 2:
      if moyenne >= 13.5:
          return "Oui"
      else:
          return "Non"
  elif g == 1:
      if moyenne >= 12:
          return "Oui"
      else:
          return "Non"
  else:
   return "Non"
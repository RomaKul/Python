def func(a,b):
  if(a<0 or b<0):
    raise NameError("NegativeNuber")
  return True if a%b==0 else False
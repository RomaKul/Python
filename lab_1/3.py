def sec_func(a,b):
  if type(a)is not int or type(b)is not int:
    raise NameError("NoSimpleDigits")
  if a>b:
    a,b=b,a
  return [i for i in range(a,b+1)]
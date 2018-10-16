mas=['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
Array=[]
def list_writer(arr):
  global Array
  if isinstance(arr, list):
    for item in arr:  
      list_writer(item)
  else:
    Array.append(arr)
    return arr

list_writer(mas)
print(Array)
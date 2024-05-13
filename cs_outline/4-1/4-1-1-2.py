def list_upper(xs):
  result = []
  for x in xs:
    result.append(x.upper())
  return result

print(list_upper(["sakamoto", "soya"]))
#実行結果　　['SAKAMOTO', 'SOYA']

def list_upper(xs):
  result = []
  for x in xs:
    x.upper()
    result = result.append(x)
  return result

print(list_uppee(["sakamoto", "soya"]))

x = "iniad"
print(x.upper())
#実行結果---INIAD
n = 6
totn = 0
for c in range(n, 1, -1):
  if c == n:
    print(f'{n} x {c-1} = {n*(c-1)}')
    totn = n*(c-1)
  else:
    print(f'{totn} x {c-1} = {totn*(c-1)}')     
    totn *= c-1
if totn == 0:
  totn =1 

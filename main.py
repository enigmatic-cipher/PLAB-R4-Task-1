"""
Given n as input. Print following pattern using For loop.
Input-> 5
Output->
5 
54 
543 
5432 
54321
"""

n = 5
st = ""
for i in range(n,0,-1):
  st = st + str(i)
  print(st)

minnum = int(input("Die minimale Zahl: "))
maxnum = int(input("Die maximale Zahl: "))
nums = []

for i in range(minnum, maxnum):
  nums.append(i)
  
if minnum == 1:
  nums.remove(1)
for i in nums:
  index = i
  for l in nums:
    if (l % index == 0 and l != index):
      nums.remove(l)
    
for i in nums:
  print(i)
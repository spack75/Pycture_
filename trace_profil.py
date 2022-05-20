import matplotlib.pyplot as plt


Xtot=[]
htot=[]

for i in range(1):
  x = [] 
  h = []
  f=open(f"out/coord{i}.txt","r")
  for j in f:
    temp = j.split()
    x.append(float(temp[0]))
    h.append(float(temp[1]))
  Xtot.append(x)
  htot.append(h)

plt.figure()
l=len(Xtot)
for i in range():
  plt.plot(Xtot[i],htot[i])
plt.show()
import random
import numpy
import array
import math

x = [0.0] * 20
y = [0.0] * 20
actual = [0.0] * 20
e = [0.0] * 20
i = 0
while i < 20:
    #Generating inputs
    if i == 0:
        x[i] = 0.05
        i = i + 1
    else:
        x[i] = x[i-1] + 0.05
        i = i + 1
#Calculating desired output
i = 0
while i < 20:
    y[i] = (1+ 0.6 * math.sin(2*math.pi*(x[i]/0.7))+ 0.3 * math.sin(2*math.pi*x[i]))/2
    i = i + 1
#c and r parameters and initial w1,w2,w0
c1 = 0.35
c2 = 0.5
r1 = 2
r2 = 1.87
w1 = random.uniform(0,1)
w2 = random.uniform(0,1)
w0 = random.uniform(0,1)
#Calculating RBF
i = 0
while i < 20:
    F1 = math.exp(((-1)*(x[i]-c1)**2)/(2*r1**2))
    F2 = math.exp(((-1)*(x[i]-c2)**2)/(2*r2**2))
    actual[i] = F1*w1+F2*w2+w0
    #error
    e[i] = y[i] - actual[i]
    i = i + 1

e_total = sum(e)

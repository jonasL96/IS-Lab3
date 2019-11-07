import random
import numpy
import array
import math
import time

x = [0.0] * 20
y = [0.0] * 20
actual = [0.0] * 20
e = [0.0] * 20
F1 = [0.0] * 20
F2 = [0.0] * 20
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
r1 = 0.5
r2 = 0.4
w1 = random.uniform(0,1)
w2 = random.uniform(0,1)
w0 = random.uniform(0,1)
#Calculating RBF
i = 0
while i < 20:
    F1[i] = math.exp(((-1)*(x[i]-c1)**2)/(2*r1**2))
    F2[i] = math.exp(((-1)*(x[i]-c2)**2)/(2*r2**2))
    actual[i] = F1[i]*w1+F2[i]*w2+w0
    #error
    e[i] = y[i] - actual[i]
    i = i + 1

e_total = sum(e)
eta = 0.1
iterations = 1000
executions = 0
i = 0
k = 0
while e_total != 0:
    executions = executions + 1
    while k < 20:
        #weight update
        w1 = w1 + eta*e_total*F1[k]
        w2 = w2 + eta*e_total*F2[k]
        w0 = w0 + eta*e_total
        e_total = 0
        #trying updated weights
        while i < 20:
            F1[i] = math.exp(((-1) * (x[i] - c1) ** 2) / (2 * r1 ** 2))
            F2[i] = math.exp(((-1) * (x[i] - c2) ** 2) / (2 * r2 ** 2))
            actual[i] = F1[i] * w1 + F2[i] * w2 + w0
            e[i] = y[i] - actual[i]
            e_total = e_total + e[i]
            i = i + 1
        if i == 20:
            i = 0
        e_total = round(e_total,2)
        k = k + 1
    if k == 20:
        k = 0
    if e_total == 0:
        print("Learning algorithm succeeded in eliminating errors. Amount of executions: ",executions)
        break
    if executions == iterations:
        print("Maximum amount of executions reached")
        break


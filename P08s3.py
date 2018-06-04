
v0 = 20
g = 9.81
from numpy import linspace,array
t = linspace(0,11,11)
y = v0*t-(g*t**2)/2

from matplotlib import pyplot as p
p.plot(t,y,color="#ff0000", label="trajektorija")
p.legend()
p.show()

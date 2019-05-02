"""import matplotlib.pyplot as plt
from math import sin, cos
function =
for i in range(0, 100)"""

import numpy as np
import matplotlib.pyplot as plt



for x in range(0, 1000):
    f = x * np.sin(x)
#    g = (x+1) * np.cos(x)
    plt.plot(x, f, 'ro')
#    plt.plot(g)


plt.show()

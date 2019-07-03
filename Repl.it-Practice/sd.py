from scipy.integrate import quad

import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

#---------------------------------------

x_min = 0.5
x_max = 2.0

mean = 1.0
std = 2

x = np.linspace(x_min, x_max, 100)

y = scipy.stats.norm.pdf(x,mean,std)

plt.plot(x,y, color='black')

#----------------------------------------
#integration between x1 and x1

import numpy as np
import matplotlib.pyplot as plt

dis = np.random.normal(5, 2, 1000)
def h(x):
    return x**3
xval = np.linspace(0, 10, 100)
yval = h(xval)

fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.hist(dis, bins = 30, color='lightskyblue', label='Sample distribution (mean of 5, deviation of 2)')
ax1.legend()
ax2 = ax1.twinx()
ax2.plot(xval, yval, color='salmon', label='Plot h=x^3 (range 0 to 10)')
ax1.set_title('Sample Normal Distribution of 1000 Values', fontweight='bold')
ax1.set_xlabel('Bins')
ax1.set_ylabel('Frequency')
ax2.set_ylabel('Value')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

fig.savefig('/workspaces/pands-weekly-tasks/assignments/week_8')
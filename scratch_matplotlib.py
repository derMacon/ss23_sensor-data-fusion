import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

fig, ax = plt.subplots()

# Plotting the data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
ax.plot(x, y, 'b-')

# Defining the interval
start = 2.5
end = 4.5

# Creating the curly brace
# brace = mpatches.FancyArrowPatch((start, min(y)), (end, min(y)),
#                                  connectionstyle="arc3,rad=-0.5",
#                                  arrowstyle='->, head_width=0.5, head_length=1',
#                                  color='red', lw=2)
# ax.add_patch(brace)

# ax.text((start+end)/2, min(y) - 1.5, 'Interval', color='red',
#         ha='center', va='bottom')

ax.fill_between(np.arange(2, 4), *ax.get_ylim(), facecolor='red', alpha=.2)

# Set plot title and axis labels
ax.set_title('Curly Braces in Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

plt.show()
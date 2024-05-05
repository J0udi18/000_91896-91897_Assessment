# program of midpoint formula
import numpy as np
import matplotlib.pyplot as plt

print('-----------------------------------------------')
print('                 Gradient formula')
print('-----------------------------------------------')
print('             m = rise / run = y1-y2/x2-x1')
print('-----------------------------------------------')
# Example data
x = [0, 1, 2, 3, 4]
y = [1, 2, 5, 8, 1]
x = np.array(x)
y = np.array(y)

# Fit line
slope, intercept = np.polyfit(x, y, 1)

# Plot
plt.figure()
plt.scatter(x, y)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='k')
plt.show()

print(slope)

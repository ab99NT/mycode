#!/usr/bin/env/ python3

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Andrew', 'Julia', 'Dave', 'Kurt', 'Alex', 'Marlon', 'Seth', 'Tim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()

# SAVE the graph locally
plt.savefig("/home/student/mycode/graphing/classhorizontalbar.png")
# Save to "~/static"
plt.savefig("/home/student/static/classhorizontalbar.png")
print("Graph created.")

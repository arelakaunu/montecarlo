# Monte Carlo method to calculate pi
# MonteCarlo.py
import math
import random
import matplotlib.pyplot as plt
import numpy as np

N = 10000
print("Parameter : N =", str(N))
# Array of iterations.
iterations = []
# Array of results
results = []

x_point = []
y_point = []

count_in = 0
for i in range(N):
	# random.random retuns a random floating number in range 0-1.
	x = random.random()
	y = random.random()
	x_point.append(x)
	y_point.append(y)
	# Condition checks if the random point falls in the inscribed circle.
	cond = x**2 + y**2
	outcome = 1 if cond <= 1 else 0
	count_in += outcome
	# Percentage of how many times it did fall into the circle.
	# Analytically, this equals Ac/As = pi/4.
	fraction_in = count_in/(i+1)

	# Store the results into the array.
	results.append(4.0 * fraction_in)
	# Store iteration into the array.
	iterations.append(i+1)

	# Print the results - the last printed number should converge to pi.
	print ("Location: " + str(outcome) + "\t" + str(x)
		+ "\t" + str(y) + "\t" + str(count_in) + "\t"
		+ str(i) + "\t" + str(4.0 * fraction_in))

angle = np.linspace(0,2*np.pi,150)

radius = 1

x_circ = radius * np.cos(angle)
y_circ = radius * np.sin(angle)

figure, axes = plt.subplots(1)

plt.plot(x_point[0:N], y_point[0:N], 'o', color='g', markersize=1)

axes.plot (x_circ,y_circ)
axes.set_aspect(1)

plt.show()	


# Plot the results using pyplot
fig = plt.figure()
plt.plot(iterations, results, "k-", label="numerical pi")
plt.plot([0, iterations[-1]], [math.pi, math.pi], "r-", label="pi")

plt.grid(True)
plt.legend()
plt.ylabel("Result [-]")cd 
plt.xlabel("Iteration [-]")
plt.savefig("piconvergence.pdf")
plt.show()
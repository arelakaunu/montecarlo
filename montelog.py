# montelog.py
# Monte Carlo method to calculate ln(2)

import math
import random
import matplotlib.pyplot as plt
import numpy as np

N = 100
print("Parameter : N =", str(N))
# Array of iterations.
iterations = []
# Array of results
results = []

x_point = []
y_point = []

count_in = 0
for i in range(N):
	# returns random floating point between 1 and 2 for x and random floating point between 0 and 1 for y
	x = random.uniform(1,2)
	y = random.random()
	x_point.append(x)
	y_point.append(y)
	# Condition checks if the random point falls below the line y=1/x
	cond = y - 1/x
	outcome = 1 if cond <= 0 else 0
	count_in += outcome
	# Percentage of how many times it did fall below the line y=1/x
	# Analytically, this equals to ln(2)
	fraction_in = count_in/(i+1)

	# Store the results into the array.
	results.append(fraction_in)
	# Store iteration into the array.
	iterations.append(i+1)

	# Print the results - the last printed number should converge to pi.
	print ("Location: " + str(outcome) + "\t" + str(x)
		+ "\t" + str(y) + "\t" + str(count_in) + "\t"
		+ str(i) + "\t" + str(fraction_in))

x_1 = np.linspace(1,2,1000)
y_1 = 1 / x_1

# Plots graph of y=1/x and the randomly generated points

plt.plot(x_point[0:N], y_point[0:N], 'o', color='r', markersize=1, label="Random points")
plt.plot(x_1, y_1, label="y = 1/x")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("random-points.pdf")

plt.show()


# Plot the results using pyplot
fig = plt.figure()
plt.plot(iterations, results, "k-", label="numerical ln(2)")
plt.plot([0, iterations[-1]], [np.log(2), np.log(2)], "r-", label="ln(2)")

plt.grid(True)
plt.legend()
plt.ylabel("Result [-]")
plt.xlabel("Iteration [-]")
plt.savefig("ln-2-convergence.pdf")
plt.show()
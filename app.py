import matplotlib.pyplot as plot

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plot.plot(input_values, squares, linewidth=5)
plot.title("Square Numbers", fontsize=24)
plot.xlabel("Value", fontsize=14)
plot.ylabel("Square of Value", fontsize=14)
plot.tick_params(axis='both', labelsize=14)
plot.scatter(2, 4)
plot.show()
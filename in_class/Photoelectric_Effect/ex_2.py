import matplotlib.pyplot as plt

# Plot Graph-1 (example)
x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y_values = [x**2 for x in x_values]

plt.plot(x_values, y_values, label='Graph-1')

# Define the rectangular region coordinates
rect_x = (-2, 0)
rect_y = (-2, 2)

# Set x and y-axis limits to the rectangular region
plt.xlim(rect_x)
plt.ylim(rect_y)

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph-1 in a Rectangular Region')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
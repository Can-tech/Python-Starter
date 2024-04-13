import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Plot Graph-1 (example)
x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y_values = [x**2 for x in x_values]

plt.plot(x_values, y_values, label='Graph-1')

# Define the rectangular region coordinates
rect_x = (-2, 0)
rect_y = (-2, 2)

# Create a rectangle patch
rectangle = patches.Rectangle((rect_x[0], rect_y[0]), rect_x[1] - rect_x[0], rect_y[1] - rect_y[0],
                              linewidth=1, edgecolor='r', facecolor='none', label='Rectangle Region')

# Add the rectangle to the plot
plt.gca().add_patch(rectangle)

# Set plot limits
plt.xlim(-2, 0)
plt.ylim(-2, 0)

# Add labels and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph-1 with Rectangle Region')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the vertices of the triangle
triangle = np.array([[0, 1], [-1, -1], [1, -1], [0, 1]])

# Function to rotate the triangle
def rotate(triangle, angle):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    return np.dot(triangle, rotation_matrix)

# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
line, = ax.plot([], [], 'b-')

# Animation function
def animate(i):
    angle = np.radians(i)
    rotated_triangle = rotate(triangle, angle)
    line.set_data(rotated_triangle[:, 0], rotated_triangle[:, 1])
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=360, interval=20, blit=True)

# Show the plot
plt.show()
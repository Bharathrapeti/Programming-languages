import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Function to draw a cylinder (cake layer)
def draw_cylinder(ax, center, radius, height, color):
    x0, y0, z0 = center
    z = np.linspace(z0, z0 + height, 30)
    theta = np.linspace(0, 2 * np.pi, 30)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = x0 + radius * np.cos(theta_grid)
    y_grid = y0 + radius * np.sin(theta_grid)
    ax.plot_surface(x_grid, y_grid, z_grid, color=color, alpha=0.9, linewidth=0)

# Function to draw candles
def draw_candle(ax, x, y, base_height, height):
    # Candle body
    z = [base_height, base_height + height]
    ax.plot([x, x], [y, y], z, color='red', linewidth=3)

    # Flame (a small yellow sphere)
    u, v = np.mgrid[0:2*np.pi:10j, 0:np.pi:10j]
    r = 0.2
    xs = x + r*np.cos(u)*np.sin(v)
    ys = y + r*np.sin(u)*np.sin(v)
    zs = base_height + height + r*np.cos(v)
    ax.plot_surface(xs, ys, zs, color='yellow', alpha=0.9)

# Set up the 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])  # Equal aspect ratio

# Cake layers (bottom to top)
layers = [
    (0, 0, 0, 3.5, 2, '#D2691E'),  # Bottom layer (brown)
    (0, 0, 2, 2.5, 2, '#FF69B4'),  # Middle layer (pink)
    (0, 0, 4, 1.5, 2, '#FFD700'),  # Top layer (yellow)
]

for x, y, z, r, h, color in layers:
    draw_cylinder(ax, (x, y, z), r, h, color)

# Candles on top layer
candle_positions = [
    (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5), (0.5, -0.5), (0, 0)
]
for x, y in candle_positions:
    draw_candle(ax, x, y, base_height=6, height=1)

# Hide grid and axes
ax.axis('off')
plt.title("🎂 3D Cake with Candles", fontsize=15)
plt.show()

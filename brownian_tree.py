import random
from PIL import Image

# settings
size = 300
particles = 5000
max_steps = 5000
img = Image.new("RGB", (size, size), "black")
pixels = img.load()

center = (size // 2, size // 2)
cluster = {center}
pixels[center] = (255, 255, 255)
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

for _ in range(particles):
    # start somewhere near the border
    angle = random.random() * 2 * 3.14159
    r = size // 2 - 2
    x = int(center[0] + r * random.choice([-1, 1]) * random.random())
    y = int(center[1] + r * random.choice([-1, 1]) * random.random())

    for _ in range(max_steps):
        dx, dy = random.choice(dirs)
        x = (x + dx) % size
        y = (y + dy) % size

        if any((x+dx, y+dy) in cluster for dx, dy in dirs):
            cluster.add((x, y))
            pixels[x, y] = (255, 255, 255)
            break

img.save("brownian_tree.png")
print("Saved brownian_tree.png")

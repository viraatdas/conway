import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_grid(N):
    return np.random.choice([0, 1], size=(N, N))

def update(grid):
    N = grid.shape[0]
    new_grid = grid.copy()
    

def animate_life(N, generations):
    grid = create_grid(N)
    print(grid)
    fig, ax = plt.subplots()
    
    def update_frame(*args):
        nonlocal grid
        # grid = update(grid)
        ax.clear()
        ax.imshow(grid, cmap='binary')
        return ax
    
    ani = animation.FuncAnimation(fig, update_frame, frames=generations, interval=200)
    plt.show()

# Parameters: Grid size and number of generations
animate_life(N=50, generations=100)
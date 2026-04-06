import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from matplotlib.colors import ListedColormap

# ── Maze ────────────────────────────────────────────────
MAZE = [
"#########################",
"#.    #       #        E#",
"# ### # ##### # ###### ##",
"# #   #     # #      #  #",
"# # ####### # ###### # ##",
"# #       # #        #  #",
"# ####### # ########## #",
"#       # #            #",
"####### # ############ #",
"#     # #              #",
"# ### # ############## #",
"#   # #                #",
"### # ################ #",
"#   #                  #",
"########################"
]

# ✅ FIX: samakan panjang baris
max_len = max(len(r) for r in MAZE)
MAZE = [r.ljust(max_len, '#') for r in MAZE]

# ── Konversi grid ───────────────────────────────────────
def build_grid(maze):
    h, w = len(maze), len(maze[0])
    grid = np.zeros((h, w))

    start = end = None

    for r in range(h):
        for c in range(w):
            ch = maze[r][c]

            if ch == "#":
                grid[r, c] = 0
            elif ch == ".":
                grid[r, c] = 4
                start = (r, c)
            elif ch == "E":
                grid[r, c] = 5
                end = (r, c)
            else:
                grid[r, c] = 1

    return grid, start, end

# ── BFS ─────────────────────────────────────────────────
def bfs_steps(grid, start, end):
    q = deque([start])
    visited = {start}
    parent = {}

    while q:
        node = q.popleft()
        yield ("visit", node)

        if node == end:
            break

        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = node[0]+dr, node[1]+dc

            if (0 <= nr < grid.shape[0] and
                0 <= nc < grid.shape[1] and
                grid[nr, nc] != 0 and
                (nr, nc) not in visited):

                visited.add((nr, nc))
                parent[(nr, nc)] = node
                q.append((nr, nc))

    # rekonstruksi path
    path = []
    cur = end
    while cur in parent:
        path.append(cur)
        cur = parent[cur]

    path.append(start)
    path.reverse()

    for p in path:
        yield ("path", p)

# ── Animasi ─────────────────────────────────────────────
def run():
    grid, start, end = build_grid(MAZE)

    if start is None or end is None:
        print("❌ Start atau End tidak ditemukan!")
        return

    cmap = ListedColormap([
        "#0b2545",  # wall
        "#ffffff",  # open
        "#90ee90",  # visited
        "#ffd966",  # path
        "#00c853",  # start
        "#ff9800",  # end
        "#00e5ff"   # current
    ])

    fig, ax = plt.subplots(figsize=(8,6))
    im = ax.imshow(grid, cmap=cmap, vmin=0, vmax=6)

    # grid garis
    ax.set_xticks(np.arange(-.5, grid.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-.5, grid.shape[0], 1), minor=True)
    ax.grid(which="minor", color="#1b3a5c", linewidth=0.5)

    ax.set_xticks([])
    ax.set_yticks([])

    plt.ion()

    for action, pos in bfs_steps(grid, start, end):
        r, c = pos

        if action == "visit":
            if pos != start and pos != end:
                grid[r, c] = 6

        elif action == "path":
            if pos != start and pos != end:
                grid[r, c] = 3

        im.set_data(grid)
        plt.pause(0.03)

    plt.ioff()
    plt.show()

# ── RUN ────────────────────────────────────────────────
if __name__ == "__main__":
    run()
labrinth = [
    ["E", " ", "#"],
    ["#", " ", "#"],
    ["#", " ", " "],
    ["#", "#", "#"]
]

def dfs(row, col, grid):
    stack = [(row, col)]
    while stack:
        i, j = stack.pop()
        if grid[i][j] == "E":
            print(i, j)
        for dy in [-1, 0, 1]:
            if i + dy < 0 or i + dy >= len(grid): continue
            for dx in [-1, 0, 1]:
                if dx + j < 0 or dx + j >= len(grid[i + dy]): continue
                if grid[i + dy][j + dx] == "-":
                    continue
                stack.append((i + dy, j + dx))
        grid[i][j] = "-"

dfs(0,1,labrinth)

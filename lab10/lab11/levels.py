GRID_SIZE = 20
WIDTH, HEIGHT = 600, 400

def get_speed_for_level(level):
    return 10 + (level - 1) * 2

def get_walls_for_level(level):
    walls = []
    if level >= 2:
        for x in range(100, 500, GRID_SIZE):
            walls.append((x, HEIGHT // 2))
    if level >= 3:
        for y in range(0, HEIGHT, GRID_SIZE):
            walls.append((WIDTH // 3, y))
    return walls

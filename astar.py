import pygame
import heapq

# Pygame setup
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 30, 30  # Grid size
CELL_SIZE = WIDTH // COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
PURPLE = (128, 0, 128)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("A* Pathfinding Visualization")

# Grid setup
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
start, end = None, None

# Directions for movement (up, down, left, right)
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Node:
    def __init__(self, row, col, g=0, h=0):
        self.row = row
        self.col = col
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

# Manhattan distance heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def a_star(start, end):
    open_set = []
    closed_set = set()
    start_node = Node(*start, g=0, h=heuristic(start, end))
    heapq.heappush(open_set, start_node)
    came_from = {}

    while open_set:
        current = heapq.heappop(open_set)
        
        if (current.row, current.col) == end:
            path = []
            while current:
                path.append((current.row, current.col))
                current = came_from.get((current.row, current.col))
            return path[::-1]  # Reverse path
        
        closed_set.add((current.row, current.col))
        
        for dr, dc in DIRECTIONS:
            neighbor = (current.row + dr, current.col + dc)
            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS and neighbor not in closed_set:
                if grid[neighbor[0]][neighbor[1]] == 1:  # Obstacle check
                    continue

                new_g = current.g + 1
                new_node = Node(neighbor[0], neighbor[1], g=new_g, h=heuristic(neighbor, end))
                new_node.parent = current

                if neighbor not in came_from or new_g < came_from[neighbor].g:
                    heapq.heappush(open_set, new_node)
                    came_from[neighbor] = current

    return None  # No path found

# Draw grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE
            if grid[row][col] == 1:
                color = BLACK  # Obstacle
            elif (row, col) == start:
                color = GREEN  # Start point
            elif (row, col) == end:
                color = RED  # End point
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))

# Main loop
running = True
while running:
    screen.fill(GRAY)
    draw_grid()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:  # Left click to add obstacles
            x, y = pygame.mouse.get_pos()
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if (row, col) != start and (row, col) != end:
                grid[row][col] = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Set Start position
                x, y = pygame.mouse.get_pos()
                start = (y // CELL_SIZE, x // CELL_SIZE)

            if event.key == pygame.K_e:  # Set End position
                x, y = pygame.mouse.get_pos()
                end = (y // CELL_SIZE, x // CELL_SIZE)

            if event.key == pygame.K_SPACE and start and end:  # Run A* when Space is pressed
                path = a_star(start, end)
                if path:
                    for r, c in path:
                        pygame.draw.rect(screen, PURPLE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))
                    pygame.display.update()
                    pygame.time.delay(1000)  # Pause to see path

    pygame.display.update()

pygame.quit()

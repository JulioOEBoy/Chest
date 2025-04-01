import pygame
import random

# Configurações da tela
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
PINK = (255, 105, 180)

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]   # J
]

SHAPES_COLORS = [CYAN, YELLOW, PURPLE, GREEN, RED, BLUE, PINK]

# Função para desenhar a grade
def draw_grid(surface):
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(surface, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(surface, WHITE, (0, y), (SCREEN_WIDTH, y))

# Função para desenhar as peças
def draw_piece(surface, piece, position, color):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(surface, color, (position[0] + j * BLOCK_SIZE, position[1] + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Função para verificar colisão
def check_collision(grid, piece, position):
    for i, row in enumerate(piece):
        for j, cell in enumerate(row):
            if cell:
                x = position[0] + j
                y = position[1] + i
                if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT or grid[y][x]:
                    return True
    return False

# Função para girar a peça
def rotate_piece(piece):
    return [list(row) for row in zip(*piece[::-1])]

# Função para limpar linhas completas
def clear_lines(grid):
    new_grid = [row for row in grid if any(cell == 0 for cell in row)]
    lines_cleared = GRID_HEIGHT - len(new_grid)
    return [[0] * GRID_WIDTH] * lines_cleared + new_grid, lines_cleared

# Função principal do jogo
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    current_piece = random.choice(SHAPES)
    current_color = random.choice(SHAPES_COLORS)
    piece_position = [GRID_WIDTH // 2 - len(current_piece[0]) // 2, 0]

    score = 0
    game_over = False
    fall_time = 0

    while not game_over:
        screen.fill(BLACK)
        draw_grid(screen)
        draw_piece(screen, current_piece, (piece_position[0] * BLOCK_SIZE, piece_position[1] * BLOCK_SIZE), current_color)

        # Verificando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_position = [piece_position[0] - 1, piece_position[1]]
                    if not check_collision(grid, current_piece, new_position):
                        piece_position = new_position
                elif event.key == pygame.K_RIGHT:
                    new_position = [piece_position[0] + 1, piece_position[1]]
                    if not check_collision(grid, current_piece, new_position):
                        piece_position = new_position
                elif event.key == pygame.K_DOWN:
                    new_position = [piece_position[0], piece_position[1] + 1]
                    if not check_collision(grid, current_piece, new_position):
                        piece_position = new_position
                    else:
                        # Se a peça não pode descer, fixar ela na grade
                        for i, row in enumerate(current_piece):
                            for j, cell in enumerate(row):
                                if cell:
                                    grid[piece_position[1] + i][piece_position[0] + j] = 1
                        grid, cleared_lines = clear_lines(grid)
                        score += cleared_lines
                        current_piece = random.choice(SHAPES)
                        current_color = random.choice(SHAPES_COLORS)
                        piece_position = [GRID_WIDTH // 2 - len(current_piece[0]) // 2, 0]

                elif event.key == pygame.K_UP:
                    rotated_piece = rotate_piece(current_piece)
                    if not check_collision(grid, rotated_piece, piece_position):
                        current_piece = rotated_piece

        # Movimento automático para baixo
        fall_time += clock.get_rawtime()
        if fall_time > 1000:  # 1 segundo por cada movimento
            piece_position[1] += 1
            if check_collision(grid, current_piece, piece_position):
                piece_position[1] -= 1
                # Fixar peça na grade
                for i, row in enumerate(current_piece):
                    for j, cell in enumerate(row):
                        if cell:
                            grid[piece_position[1] + i][piece_position[0] + j] = 1
                grid, cleared_lines = clear_lines(grid)
                score += cleared_lines
                current_piece = random.choice(SHAPES)
                current_color = random.choice(SHAPES_COLORS)
                piece_position = [GRID_WIDTH // 2 - len(current_piece[0]) // 2, 0]
            fall_time = 0

        # Atualizando o jogo
        pygame.display.flip()

        clock.tick(10)  # A velocidade do jogo

    pygame.quit()

if __name__ == "__main__":
    run_game()

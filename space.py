import pygame
import sys
import random


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Man")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BROWN = (165, 42, 42)
GOLD = (255, 215, 0)
RED = (255, 0, 0)

GRAVITY = 0.8
PLAYER_JUMP_STRENGTH = -15


player_width, player_height = 40, 60
player_x, player_y = WIDTH // 2, HEIGHT - player_height - 50
player_velocity_y = 0
player_speed = 5
on_ground = False

platforms = [
    pygame.Rect(100, HEIGHT - 100, 200, 20),
    pygame.Rect(400, HEIGHT - 150, 200, 20),
    pygame.Rect(150, HEIGHT - 300, 200, 20),
    pygame.Rect(500, HEIGHT - 350, 200, 20),
    pygame.Rect(200, HEIGHT - 450, 200, 20),
    pygame.Rect(600, HEIGHT - 500, 200, 20),

]

ground = pygame.Rect(0, HEIGHT - 20, WIDTH, 20)


player = pygame.Rect(player_x, player_y, player_width, player_height)


gold_sprite = pygame.Rect(random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 100), 20, 20)
red_sprite = pygame.Rect(random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 100), 20, 20)

score = 0
lives = 3


running = True
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    if keys[pygame.K_SPACE] and on_ground:
        player_velocity_y = PLAYER_JUMP_STRENGTH
        on_ground = False

    player_velocity_y += GRAVITY
    player.y += player_velocity_y

    on_ground = False

    if player.colliderect(ground):
        player.y = ground.y - player_height
        player_velocity_y = 0
        on_ground = True

    for platform in platforms:
        if player.colliderect(platform) and player_velocity_y > 0:
            player.y = platform.y - player_height
            player_velocity_y = 0
            on_ground = True

    if player.x < 0:
        player.x = 0
    if player.x + player_width > WIDTH:
        player.x = WIDTH - player_width
    if player.y > HEIGHT:
        player.y = HEIGHT - player_height
        on_ground = True

    if player.colliderect(gold_sprite):
        score += 1

        gold_sprite.x = random.randint(0, WIDTH - 20)
        gold_sprite.y = random.randint(0, HEIGHT - 100)

    if player.colliderect(red_sprite):
        lives -= 1

        red_sprite.x = random.randint(0, WIDTH - 20)
        red_sprite.y = random.randint(0, HEIGHT - 100)

    if lives <= 0:
        running = False

    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, GREEN, ground)

    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)

    pygame.draw.rect(screen, GOLD, gold_sprite)
    pygame.draw.rect(screen, RED, red_sprite)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    lives_text = font.render(f"Lives: {lives}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    pygame.display.flip()


screen.fill(WHITE)
game_over_text = font.render("Game Over", True, (255, 0, 0))
final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2))
pygame.display.flip()
pygame.time.wait(3000)


pygame.quit()

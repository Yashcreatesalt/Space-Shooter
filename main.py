import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 80, 80)
GREEN = (80, 255, 120)
BLACK = (0, 0, 0)

player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 70, 50, 50)
player_speed = 6

bullets = []
enemies = []

bullet_speed = 8
enemy_speed = 4

score = 0
font = pygame.font.SysFont(None, 36)

spawn_timer = 0

running = True
while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(
                    pygame.Rect(player.centerx - 5, player.top, 10, 20)
                )

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    spawn_timer += 1
    if spawn_timer > 40:
        enemies.append(
            pygame.Rect(random.randint(0, WIDTH-40), -40, 40, 40)
        )
        spawn_timer = 0

    for enemy in enemies[:]:
        enemy.y += enemy_speed

        if enemy.colliderect(player):
            print("Game Over!")
            pygame.quit()
            sys.exit()

        if enemy.top > HEIGHT:
            enemies.remove(enemy)

    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 1
                break

    pygame.draw.rect(screen, GREEN, player)

    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()

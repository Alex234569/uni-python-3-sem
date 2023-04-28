import pygame
import random
from player import Player
from rocket import Rocket
from asteroid import Asteroid
from explosion import Explosion


# Функция перерисовки окна
def update_game_window():
    player.update_offscreen_location()
    window.blit(background_surf, (0, 0))
    player.draw()
    for rocket in rockets:
        rocket.draw()
    for asteroid in asteroids:
        asteroid.draw()
    for explosion in explosions:
        explosion.draw()

    livesText = font.render('Lives: ' + str(lives), True, '#FFFFFF')
    scoreText = font.render('Score: ' + str(score), True, '#FFFFFF')

    if gameover:
        window.blit(background_surf, (0, 0))
        window.blit(gameoverText, (screenWidth // 2 - gameoverText.get_width() // 2, screenHeight // 2 - gameoverText.get_height() // 2))

    window.blit(scoreText, (screenWidth - scoreText.get_width() - 25, 25))
    window.blit(livesText, (25, 25))
    pygame.display.update()


# Настройка окна
pygame.init()
screenWidth = 1200
screenHeight = 900
FPS = 60
pygame.display.set_caption('Asteroids')
window = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

# Экран приветствия игрока
background_surf = pygame.image.load('textures/background.png')
window.blit(background_surf, (0, 0))
font = pygame.font.SysFont(None, 50)
welcomeText = font.render('Press MOUSE1 to start the game!', True, '#FFFFFF')
window.blit(welcomeText, (screenWidth // 2 - welcomeText.get_width() // 2, screenHeight // 2 - welcomeText.get_height() // 2))

run = True # Активно ли окно
startScreen = True # Активен ли начальный экран

while run and startScreen:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            startScreen = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    
    pygame.display.update()

# Игровые переменные
lives = 3
score = 0
rockets = [] # Массив всех "живых" ракет
asteroids = [] # Массив всех "живых" астероидов
asteroid_count = 0 # Счётчик, по которому появляются астероиды
ASTEROID_SPAWN_RATE = 60 # Частота появления астероидов
invincibility_count = 0 # Показывает, сколько тиков осталось до завершения неуязвимости
INVINCIBILITY_DURATION = 120 # Длительность неуязвимости в тиках
gameover = False # Флаг завершения игры

explosions = [] # Список всех взрывов

livesText = font.render('Lives: ' + str(lives), True, '#FFFFFF')
scoreText = font.render('Score: ' + str(score), True, '#FFFFFF')
gameoverText = font.render('Press ENTER to play again', True, '#FFFFFF')

player = Player(screenWidth, screenHeight, window)

while run:
    clock.tick(FPS)
    asteroid_count += 1
    if invincibility_count > 0:
        player.invincibility = True
        invincibility_count -= 1
    else:
        player.invincibility = False
    if not gameover:
        #Астероид появляется каждые ASTEROID_SPAWN_RATE тиков
        if asteroid_count % ASTEROID_SPAWN_RATE == 0:
            rank = random.choice([1, 1, 1, 1, 2, 2, 3])
            asteroids.append(Asteroid(screenWidth, screenHeight, rank, window))
        player.update_offscreen_location()
        for explosion in explosions:
            if explosion.check_out_of_time():
                explosions.pop(explosions.index(explosion))
        for rocket in rockets:
            if rocket.check_offscreen():
                rockets.pop(rockets.index(rocket))
            rocket.move()
        for asteroid in asteroids:
            if asteroid.check_offscreen():
                asteroids.pop(asteroids.index(asteroid))
            asteroid.move()
            # Столкновение игрока с астероидом
            # При уничтожении астероида нового астероида не появляется
            # Игрок получает INVINCIBILITY_DURATION тиков неуязвимости
            if pygame.Rect.colliderect(player.rotatedPlayerRect, asteroid.asteroidRect) and not player.invincibility:
                explosions.append(Explosion(player.x, player.y, window))
                lives -= 1
                invincibility_count += INVINCIBILITY_DURATION
                asteroids.pop(asteroids.index(asteroid))
                player.move_to_center()
            for rocket in rockets:
                # Столкновение ракеты с астероидом
                # При уничтожении астероида ракетой появляется более маленький астероид
                if pygame.Rect.colliderect(asteroid.asteroidRect, rocket.rotatedRocketRect):
                    explosions.append(Explosion(rocket.x, rocket.y, window))
                    #explosionSurf = pygame.image.load('textures/explosion.png')
                    #window.blit(explosionSurf, (rocket.x, rocket.y))
                    if asteroid.rank == 3:
                        score += 3
                        newAsteroid = Asteroid(screenWidth, screenHeight, 2, window)
                        newAsteroid.x = asteroid.x
                        newAsteroid.y = asteroid.y
                        asteroids.append(newAsteroid)
                    elif asteroid.rank == 2:
                        score += 2
                        newAsteroid = Asteroid(screenWidth, screenHeight, 1, window)
                        newAsteroid.x = asteroid.x
                        newAsteroid.y = asteroid.y
                        asteroids.append(newAsteroid)
                    else:
                        score += 1
                    asteroids.pop(asteroids.index(asteroid))
                    rockets.pop(rockets.index(rocket))
        if lives <= 0:
            gameover = True
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.turn_left()
        if keys[pygame.K_RIGHT]:
            player.turn_right()
        if keys[pygame.K_UP]:
            player.move_forvard()
        else:
            player.set_idle_sprite()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rockets.append(Rocket(player, screenWidth, screenHeight, window))
            if event.key == pygame.K_RETURN:
                gameover = False
                lives = 3
                score = 0
                asteroids.clear()
                rockets.clear()
                explosions.clear()
                asteroid_count = 0
                invincibility_count = 0
                player.move_to_center()
            if event.key == pygame.K_ESCAPE:
                run = False

    update_game_window()

pygame.quit()

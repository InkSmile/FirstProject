import pygame
import sys
import time
import random
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()
score = 0
font_score = pygame.font.SysFont('Arial', 22, bold = True)
display_width = 640
display_height = 480
win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Snaky')
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150,150,150)
greenColour = pygame.Color(50,255,10)

game_is_running = True
while game_is_running:
        snakePos = [0,0]
        snakeSegments = [[100,100],[80,100],[60,100]]
        applePos = [300,300]
        appleSpawn = 0
        direction = 'right'
        changeDirection = direction
        fps = 10


        def message_to_screen(msg, color, y_displace=0, size="small"):
            textSurf, textRect = text_objects(msg, color, size)
            textRect.center = (display_width / 2), (display_height / 2) + y_displace
            gameDisplay.blit(textSurf, textRect)

        def pause():
            paused = True

            message_to_screen("Paused", whiteColour, -100, size="large")

            message_to_screen("Press C to continue or Q to quit", whiteColour, 25)

            pygame.display.update()
            while paused:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            paused = False
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            quit()

                # gameDisplay.fill(white)

                clock.tick(5)

        snake_is_alive = True
        while snake_is_alive:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT or event.key == ord('d'):
                        changeDirection = 'right'
                    if event.key == K_LEFT or event.key == ord('a'):
                        changeDirection = 'left'
                    if event.key == K_UP or event.key == ord('w'):
                        changeDirection = 'up'
                    if event.key == K_DOWN or event.key == ord('s'):
                        changeDirection = 'down'
                    if event.key == K_ESCAPE:
                        pygame.event.post(pygame.event.Event(QUIT))
                    if event.key == K_1:
                        fps = 10
                    if event.key == K_2:
                        fps = 20
                    if event.key == K_3:
                        fps = 30
                    if event.key == K_4:
                        fps = 40
                    if event.key == K_5:
                        fps = 50
                    if event.key == K_r:
                        snake_is_alive = False

            if changeDirection == 'right' and not direction == 'left':
                direction = changeDirection
            if changeDirection == 'left' and not direction == 'right':
                direction = changeDirection
            if changeDirection == 'up' and not direction == 'down':
                direction = changeDirection
            if changeDirection == 'down' and not direction == 'up':
                direction = changeDirection
            if direction == 'right':
                snakePos[0] += 20
            if direction == 'left':
                snakePos[0] -= 20
            if direction == 'up':
                snakePos[1] -= 20
            if direction == 'down':
                snakePos[1] += 20
            snakeSegments.insert(0,list(snakePos))
            if snakePos[0] == applePos[0] and snakePos[1] == applePos[1]:
                appleSpawn = 0
                score += 1
            else:
                snakeSegments.pop()
            if appleSpawn == 0:
                x = random.randrange(1,32)
                y = random.randrange(1,24)
                applePos = [int(x*20),int(y*20)]
            appleSpawn = 1
            win.fill(blackColour)
            for position in snakeSegments:
                pygame.draw.rect(win,redColour,Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(win,greenColour,Rect(applePos[0], applePos[1], 20, 20))
            pygame.display.flip()
            if snakePos[0] > 620 or snakePos[0] < 0:
                snake_is_alive = False
            if snakePos[1] > 460 or snakePos[1] < 0:
                snake_is_alive = False
            for snakeBody in snakeSegments[1:]:
                if snakePos[0] == snakeBody[0] and snakePos[1] == snakeBody[1]:
                    snake_is_alive = False

            fpsClock.tick(fps)

            render_score = font_score.render(f'score: {score}', 1, greyColour)
            win.blit(render_score, (5, 5))


        gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
        gameOverSurf = gameOverFont.render('Game Over', True, greyColour)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (320, 10)
        win.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()
        time.sleep(3)

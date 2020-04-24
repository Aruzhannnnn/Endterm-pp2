import pygame
import random
 
pygame.init()

size = [800,600]
screen = pygame.display.set_mode(size)
rect_x = 200
rect_y = 500
 
circle = []
def rect(x, y):
    pygame.draw.rect(screen, (45, 100, 34), (rect_x,rect_y, 50, 60))

for i in range(5):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    circle.append([x, y])


 
clock = pygame.time.Clock()
game_over = False 
score = 0
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


    screen.fill((0 , 0 , 0))

 
    for i in range(len(circle)):
 
        pygame.draw.circle(screen, [25 , 100 , 120], circle[i], 10)
 
        circle[i][1] += 3

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: rect_x -= 10
        if pressed[pygame.K_RIGHT]: rect_x += 10
         
        if rect_x > 600  :
            rect_x = rect_x % 800
        if rect_x < 0 :
            rect_x = rect_x % 800
       
        if circle[i][0] in range(rect_x, rect_x + 51)  and circle[i][1] in range(rect_y, rect_y + 61):
            score += 1
            y = random.randrange(0, 100)
            circle[i][1] = y
            x = random.randrange(0, 800)
            circle[i][0] = x
 
        if circle[i][1] > 600:
           font = pygame.font.SysFont("Arial", 36)
           text = font.render("Game over", 1, (255, 255, 255))
           place = text.get_rect(center=(800 // 2, 600 // 2 - 20))
           font2 = pygame.font.SysFont("Arial", 18)
           text2 = font2.render('Score: {}'.format(score), 1, (255, 255, 255))
           place2 = text2.get_rect(center=(800 // 2, 600 // 2 + 10))
           screen.blit(text, place)
           screen.blit(text2, place2)
           pygame.display.flip()
           game_over = True
           pygame.time.delay(2000)
           continue

    rect(rect_x , rect_y)
    pygame.display.flip()
    clock.tick(20)

 
pygame.quit()
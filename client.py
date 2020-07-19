import pygame

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

class player:
    def __init__(self,x,y,width,height,colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (self.x,self.y,self.width,self.height)
        self.x_vel = 3
        self.y_vel = 3


    def draw(self,win):
        pygame.draw.rect(win, self.colour, self.rect)

    def move(self):
        global run

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.x_vel
        
        if keys[pygame.K_RIGHT]:
            self.x += self.x_vel

        if keys[pygame.K_UP]:
            self.y -= self.y_vel

        if keys[pygame.K_DOWN]:
            self.y += self.y_vel

        if keys[pygame.K_h]:
            self.x = width // 2
            self.y = height // 2
        
        if keys[pygame.K_q] and keys[pygame.K_LSHIFT]:
            run = False
            pygame.quit()

        self.rect = (self.x,self.y,self.width,self.height)


def redrawWin(win, player1):
    win.fill((255,255,255))
    player1.draw(win)
    pygame.display.update()

def main():
    run = True
    p1 = player(50,50,100,100,(0,255,0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p1.move()
        redrawWin(win, p1)

main()
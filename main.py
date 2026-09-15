from sys import exit
import pygame

pygame.init()

SCREEN_WIDTH=850
SCREEN_HEIGHT=650
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill("white")
clock=pygame.time.Clock()

player_size=25
player_surfaces=[]
player_rects=[]
player_surfaces.append(pygame.surface.Surface((25,25)))
player_rects.append(player_surfaces[0].get_rect(center=(SCREEN_WIDTH/2,3*SCREEN_HEIGHT/4+50)))
player_surfaces[0].fill("blue")

player_surfaces.append(pygame.surface.Surface((25,25)))
player_rects.append(player_surfaces[1].get_rect(center=(player_rects[0].centerx+player_size*2,player_rects[0].centery)))
player_surfaces[0].fill("blue")
directionx=0
speed=5

def render():

    for index,player_surface in enumerate(player_surfaces):
        screen.blit(player_surface,player_rects[index])
        player_rects[index].x+=directionx*speed



while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:directionx=1
            elif event.key==pygame.K_a:directionx=-1
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_d or event.key==pygame.K_a:directionx=0

    screen.fill("white")
    render()

    pygame.display.update()
    clock.tick(60)
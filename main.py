from sys import exit
import pygame

pygame.init()

SCREEN_WIDTH=850
SCREEN_HEIGHT=650
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill("white")
clock=pygame.time.Clock()

player_size=25
spacing=10
player_surfaces=[]
player_rects=[]
player_surfaces.append([pygame.surface.Surface((25,25))])
player_rects.append([player_surfaces[0][0].get_rect(center=(SCREEN_WIDTH/2,3*SCREEN_HEIGHT/4))])
player_surfaces[0][0].fill("blue")


# player_surfaces[0].append(pygame.surface.Surface((25,25)))
# player_rects[0].append(player_surfaces[0][1].get_rect(center=(player_rects[0][0].centerx+player_size +spacing,player_rects[0][0].centery)))
# player_surfaces[0][1].fill("blue")
directionx=0
speed=8
current_x,current_y=1,1
def render():

    pygame.draw.line(screen,"black",(3*SCREEN_WIDTH/4,0),(3*SCREEN_WIDTH/4,SCREEN_HEIGHT/2+100),10)
    for index_row,player_surface_row in enumerate(player_surfaces):
        for index,player_surface in enumerate(player_surface_row):
            screen.blit(player_surface,player_rects[index_row][index])
            player_rects[index_row][index].x+=directionx*speed

def spawn_new_player():
    global player_surfaces,player_rects,current_x,current_y,spacing
    
    for index,row in enumerate(player_surfaces):
        if len(row)==len(player_surfaces) and index==len(player_surfaces)-1:
            if current_y>0:
                current_y*=-1
                spacing=-10
            else:
                current_y*=-1
                current_y+=1
                spacing=10
            
            player_surfaces.append([pygame.surface.Surface((25,25))])
            player_rects.append([player_surfaces[-1][0].get_rect(center=(SCREEN_WIDTH/2,3*SCREEN_HEIGHT/4+player_size*current_y+spacing))])
            player_surfaces[0][0].fill("blue")
            print("new list")
            break

        elif len(row)<len(player_surfaces):
            if current_x>0:
                current_x*=-1
                spacing=-10
            elif current_x<0:
                current_x*=-1
                current_x+=1
                spacing=10
            current_y=index
            player_surfaces[index].append(pygame.surface.Surface((25,25)))
            player_rects[index].append(player_surfaces[index][-1].get_rect(center=(SCREEN_WIDTH/2+player_size*current_x+spacing,3*SCREEN_HEIGHT/4+player_size*current_y+spacing)))
            print(f"added player to {index}")
            break
    print(len(player_rects))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:directionx=1
            elif event.key==pygame.K_a:directionx=-1
        elif event.type==pygame.MOUSEBUTTONDOWN:spawn_new_player()
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_d or event.key==pygame.K_a:directionx=0

    screen.fill("white")
    render()

    pygame.display.update()
    clock.tick(60)
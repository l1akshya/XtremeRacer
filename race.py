import pygame
import math
import random
from pygame import mixer

def main():
    pygame.init()
    from pygame import mixer
    screen_width = 1168
    screen_height = 648
    player_car_x=584
    player_car_y=648
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("XTREME RACER")#game title
    icon=pygame.image.load("carz.png")#game title
    player_win=pygame.image.load("player_win.png")
    Ai_win=pygame.image.load("ai_win.png")
    test_background=pygame.image.load("test_background.png")
    pygame.display.set_icon(icon)
    clock=pygame.time.Clock()
    screenz=pygame.image.load("home_screenz.png")
    start_playing=pygame.image.load("resume.png").convert_alpha()#play button for start screen
    exit_playing=pygame.image.load("quit.png").convert_alpha()#exit button for start screen
    nfs=mixer.music.load(r"C:\Users\LAKSHYA\Desktop\XtremeRacer\nfs.mp3")
    mixer.music.play(-1)    

    class button():
        def __init__(self,x,y,image):
            self.image=image
            self.rect=self.image.get_rect()
            self.rect.topleft=(x,y)
            self.clicked=False
        def draw(self):
            action=False
            position_mouse=pygame.mouse.get_pos()
            if self.rect.collidepoint(position_mouse):
                if pygame.mouse.get_pressed()[0]==1 and self.clicked==False :
                    self.clicked=True
                    action=True
                if pygame.mouse.get_pressed()[0]==0 and self.clicked == True:
                    self.clicked=False

            screen.blit(self.image,(self.rect.x,self.rect.y))
            return action

    start_button=button(480-128-20,162+64,start_playing)
    exit_button=button(480+128+20+20+40+30,418-64,exit_playing)

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image=pygame.image.load("car1.png").convert_alpha()
            self.rect = self.image.get_rect(midbottom=(32+64,548))
            self.a=3
            self.speedy = self.a
            self.speedx = 3
            self.speedb=  1

        def update(self):
            if pressed_keys[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.x += self.speedx
            if self.rect.left<=0:
                self.rect.x+=1
            if self.rect.right>=1168:
                self.rect.x-=1
            if self.rect.right>=292-2 and self.rect.right<=292+2:
                self.rect.x-=3
            if self.rect.left>=292-2 and self.rect.left<=292+2:
                self.rect.x+=3
            if self.rect.right>=292*2-2 and self.rect.right<=292*2+2:
                self.rect.x-=3
            if self.rect.left>=292*2-2 and self.rect.left<=292*2+2:
                self.rect.x+=3
            if self.rect.right>=292*3-2 and self.rect.right<=292*3+2:
                self.rect.x-=3
            if self.rect.left>=292*3-2 and self.rect.left<=292*3+2:
                self.rect.x+=3

        def update_2(self):
            if pressed_keys[pygame.K_DOWN]:
                self.speedy=self.speedb
            if self.rect.bottom>=648 :
                self.rect.y-=1

        def update_3(self):
            self.rect.y -= self.speedy
            if self.rect.top<=-64:
                if self.rect.left>=0+292*0 and self.rect.right<=292*1:
                    self.rect.x+=292
                    self.rect.y=648+64
                elif self.rect.left>=292 and self.rect.right<=292*2:
                    self.rect.x+=292
                    self.rect.y=648+64
                elif self.rect.left>=292*2 and self.rect.right<=292*3:
                    self.rect.x+=292
                    self.rect.y=648+64
                self.rect.y+=1
                self.speedy=0
            if self.rect.top>=10:
                self.speedy=self.a
        def draw(self, screen):
            screen.blit(self.image, self.rect)

    class Ai(pygame.sprite.Sprite):
        def __init__(self,phantom_sprite_y,phantom_sprite_x):
            super().__init__()
            self.image=pygame.image.load("car2.png").convert_alpha()
            self.rect = self.image.get_rect(midbottom=(32+64+128+64*phantom_sprite_x-50,548-64*phantom_sprite_y))
            self.a=3
            self.phantom_sprite_x=phantom_sprite_x
            self.speedy = self.a
            self.speedx = 1
            self.speedb=  1

        def update(self):
            '''if pressed_keys[pygame.K_LEFT]:
                self.rect.x -= self.speedx
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.x += self.speedx'''
            if self.rect.left<=0+64*self.phantom_sprite_x:
                self.rect.x+=1
            if self.rect.right>=1168+64*self.phantom_sprite_x:
                self.rect.x-=1
            if self.rect.right>=292-2+64*self.phantom_sprite_x and self.rect.right<=292+2+64*self.phantom_sprite_x:
                self.rect.x-=3
            if self.rect.left>=292-2+64*self.phantom_sprite_x and self.rect.left<=292+2+64*self.phantom_sprite_x:
                self.rect.x+=3
            if self.rect.right>=292*2-2+64*self.phantom_sprite_x and self.rect.right<=292*2+2+64*self.phantom_sprite_x:
                self.rect.x-=3
            if self.rect.left>=292*2-2+64*self.phantom_sprite_x and self.rect.left<=292*2+2+64*self.phantom_sprite_x:
                self.rect.x+=3
            if self.rect.right>=292*3-2+64*self.phantom_sprite_x and self.rect.right<=292*3+2+64*self.phantom_sprite_x:
                self.rect.x-=3
            if self.rect.left>=292*3-2+64*self.phantom_sprite_x and self.rect.left<=292*3+2+64*self.phantom_sprite_x:
                self.rect.x+=3

        def update_2(self):
            '''if pressed_keys[pygame.K_DOWN]:
                self.speedy=self.speedb'''
            if self.rect.bottom>=648 :
                self.rect.y-=1

        def update_3(self):
            self.rect.y -= self.speedy
            if self.rect.top<=-64:
                if self.rect.left>=0+292*0+64*self.phantom_sprite_x and self.rect.right<=292*1+64*self.phantom_sprite_x:
                    self.rect.x+=292
                    self.rect.y=648+64
                elif self.rect.left>=292+64*self.phantom_sprite_x and self.rect.right<=292*2+64*self.phantom_sprite_x:
                    self.rect.x+=292
                    self.rect.y=648+64
                elif self.rect.left>=292*2+64*self.phantom_sprite_x and self.rect.right<=292*3+64*self.phantom_sprite_x:
                    self.rect.x+=292
                    self.rect.y=648+64
                self.rect.y+=1
            '''if self.rect.top>=10:
                self.speedy=self.a'''
        def draw(self, screen):
            screen.blit(self.image, self.rect)

    class Obstacle(pygame.sprite.Sprite):
        def __init__(self,k):
            super().__init__()
            type=random.choice([1,2,1])
            if type== 1:
                self.image = pygame.image.load("barrier.png")
            if type == 2:
                self.image =pygame.image.load("barrier2.png")
            self.rect = self.image.get_rect()
            for i in range(0,4):
                for j in range(0,5):
                    if  k==1+3*j+15*i:
                        x_upper=292/3+(292*i)
                        x_lower=0+(292*i)
                        y_upper=648/5+(648/5)*j
                        y_lower=0+(648/5)*j
                    if k==2+3*j+15*i:
                        x_lower=292/3+(292*i)
                        x_upper=(2*292)/3+(292*i)
                        y_upper=648/5+(648/5)*j
                        y_lower=0+(648/5)*j
                    if k==3+3*j+15*i:
                        x_lower=(292*2)/3+(292*i)
                        x_upper=(3*292)/3+(292*i)
                        y_upper=648/5+(648/5)*j
                        y_lower=0+(648/5)*j
            self.rect.x = random.uniform(x_lower,x_upper - 64)  # Random x-position
            self.rect.y = random.uniform(y_lower, y_upper - 64)  # Random y-position

        def update(self):
            # Implement any update logic for the obstacle (e.g., movement, interaction)
            pass

    def collision_sprite():
        if pygame.sprite.spritecollide(all_sprites_ai.sprite,obstacle_group,False):
                player_ai.rect.y+=10
                player_phantom_ai.rect.y+=10
                player_phantom_ai_right.rect.y+=10
                player_phantom_ai_left.rect.y+=10
                player_phantom_ai_right_2.rect.y+=10
                player_phantom_ai_left_2.rect.y+=10
        else:
            collision_phantom_sprite()

    def collision_player_sprite():
        if pygame.sprite.spritecollide(all_sprites.sprite,obstacle_group,False):
            player.rect.y+=32
        
    def collision_phantom_sprite():
        for l in range(0,4):
            if pygame.sprite.spritecollide(all_phantom_ai.sprite,obstacle_group,False):
                if collision_phantom_sprite_right():
                    turn=35
                    if player_ai.rect.left>=292*l and player_ai.rect.right<=292+292*l-64:
                        player_ai.rect.x+=turn
                        player_phantom_ai.rect.x+=turn
                        player_phantom_ai_right.rect.x+=turn
                        player_phantom_ai_left.rect.x+=turn
                        player_phantom_ai_right_2.rect.x+=turn
                        player_phantom_ai_left_2.rect.x+=turn
                if collision_phantom_sprite_left():
                    turn=-35
                    if player_ai.rect.left>=64+292*l and player_ai.rect.right<=290+292*l:
                        player_ai.rect.x+=turn
                        player_phantom_ai.rect.x+=turn
                        player_phantom_ai_right.rect.x+=turn
                        player_phantom_ai_left.rect.x+=turn
                        player_phantom_ai_right_2.rect.x+=turn
                        player_phantom_ai_left_2.rect.x+=turn

    def collision_phantom_sprite_right():
        if pygame.sprite.spritecollide(all_phantom_ai_right.sprite,obstacle_group,False) :
            return False
        else:
            return True
    def collision_phantom_sprite_left():
        if pygame.sprite.spritecollide(all_phantom_ai_left.sprite,obstacle_group,False) :
            return False
        else:
            return True
        
    def player_ai_collision():
        if pygame.sprite.spritecollide(all_sprites_ai.sprite,all_sprites,False):
            if player.rect.x>player_ai.rect.x:
                player.rect.x+=12
                player_ai.rect.x-=3
                player_phantom_ai.rect.x-=3
                player_phantom_ai_left.rect.x-=3
                player_phantom_ai_right.rect.x-=3
                player_phantom_ai_left_2.rect.x-=3
                player_phantom_ai_right_2.rect.x-=3
            elif player.rect.x<player_ai.rect.x:
                player.rect.x-=12
                player_ai.rect.x+=3
                player_phantom_ai.rect.x+=3
                player_phantom_ai_left.rect.x+=3
                player_phantom_ai_right.rect.x+=3
                player_phantom_ai_left_2.rect.x+=3
                player_phantom_ai_right_2.rect.x+=3
            
        
    def ai_update():
        player_ai.update()
        player_ai.update_2()
        player_ai.update_3()
        player_phantom_ai.update()
        player_phantom_ai.update_2()
        player_phantom_ai.update_3()
        player_phantom_ai_right.update()
        player_phantom_ai_right.update_2()
        player_phantom_ai_right.update_3()
        player_phantom_ai_left.update()
        player_phantom_ai_left.update_2()
        player_phantom_ai_left.update_3()
        player_phantom_ai_left_2.update()
        player_phantom_ai_left_2.update_2()
        player_phantom_ai_left_2.update_3()
        player_phantom_ai_right_2.update()
        player_phantom_ai_right_2.update_2()
        player_phantom_ai_right_2.update_3()

    def player_update():
        player.update()
        player.update_2()
        player.update_3()

    def ai_phantom_set_alpha():
        player_phantom_ai.image.set_alpha(0)
        player_phantom_ai_right.image.set_alpha(0)
        player_phantom_ai_left.image.set_alpha(0)
        player_phantom_ai_right_2.image.set_alpha(0)
        player_phantom_ai_left_2.image.set_alpha(0)

    def ai_draw():
        all_sprites_ai.draw(screen)
        all_phantom_ai.draw(screen)
        all_phantom_ai_right.draw(screen)
        all_phantom_ai_left.draw(screen)
        all_phantom_ai_right_2.draw(screen)
        all_phantom_ai_left_2.draw(screen)

    victory=0
    replay2=pygame.image.load("retry.png").convert_alpha()
    quit_playing2=pygame.image.load("quit_lose.png").convert_alpha()
    replay1=pygame.image.load("play_again.png").convert_alpha()
    quit_playing1=pygame.image.load("exit_win.png").convert_alpha()
    restart_button1=button(480-30,480+50,replay1)
    quit_button1=button(480+200+20,480+50,quit_playing1)
    restart_button2=button(480-30,480+50,replay2)
    quit_button2=button(480+200+20,480+50,quit_playing2)
    def decide_victory():
        if player.rect.left>292*3 and player.rect.right<292*4 and player.rect.bottom<=5:
            return 1
        elif player_ai.rect.left>292*3 and player_ai.rect.right<292*4 and player_ai.rect.bottom<=0:
            return 2
    
            
    player = Player()
    # Create a sprite group and add the player to it
    all_sprites = pygame.sprite.GroupSingle()
    all_sprites.add(player)       
    # Create the player object
    player_ai = Ai(0,0)
    player_phantom_ai=Ai(2,0)
    player_phantom_ai_right=Ai(1,1)
    player_phantom_ai_right_2=Ai(2,1)
    player_phantom_ai_left=Ai(1,-1)
    player_phantom_ai_left_2=Ai(2,-1)
    # Create a sprite group and add the player to it
    all_sprites_ai = pygame.sprite.GroupSingle()
    all_phantom_ai=pygame.sprite.GroupSingle()
    all_phantom_ai.add(player_phantom_ai)
    all_phantom_ai_right=pygame.sprite.GroupSingle()
    all_phantom_ai_right.add(player_phantom_ai_right)
    all_phantom_ai_left=pygame.sprite.GroupSingle()
    all_phantom_ai_left.add(player_phantom_ai_left)
    all_phantom_ai_right_2=pygame.sprite.GroupSingle()
    all_phantom_ai_right_2.add(player_phantom_ai_right_2)
    all_phantom_ai_left_2=pygame.sprite.GroupSingle()
    all_phantom_ai_left_2.add(player_phantom_ai_left_2)
    all_sprites_ai.add(player_ai)
    obstacle_group = pygame.sprite.Group()
            
    # Creating multiple obstacles
    def generate_obstacles(no_of_obstacles,lap_number):
        lap_number=lap_number-1
        result = []
        result.append(random.randint(1+15*lap_number, 3+15*lap_number))
        result.append(random.randint(4+15*lap_number, 5+15*lap_number))
        result.append(random.randint(6+15*lap_number, 8+15*lap_number))
        result.append(random.randint(9+15*lap_number, 12+15*lap_number))
        for _ in range(no_of_obstacles - 4):
            result.append(random.randint(1, 12))
        obstacle_generator=result
        obstacle=[]
        for o in range(0,no_of_obstacles):
            obstaclez = Obstacle(obstacle_generator[o])
            obstacle.append(obstaclez)
        obstacle_group.add(obstacle)
        obstacle_group.update()

    generate_obstacles(2,1)
    generate_obstacles(4,2)
    generate_obstacles(4,3)
    generate_obstacles(5,4)
    # Game loop
    running = True
    paused=False
    victory=0
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if paused:
                        paused = False
                    else:
                        paused = True
        if paused == False:
        
            # Get the state of all keyboard keys
            pressed_keys = pygame.key.get_pressed()
            collision_sprite()
            collision_player_sprite()
            player_ai_collision()
            player_update()
            victory=decide_victory()
            if victory==1:
                running=False
                running1=True
                while running1:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running1 = False
                        screen.fill((0, 0, 0))#preset screen colour
                        screen.blit(player_win,(0,0))#setting up the background
                        if restart_button1.draw():
                            main()
                        if quit_button1.draw():
                            pygame.quit()
                        pygame.display.flip()
                        pygame.display.update()
            elif victory==2:
                running=False
                running1=True
                while running1:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running1 = False
                        screen.fill((0, 0, 0))#preset screen colour
                        screen.blit(Ai_win,(0,0))#setting up the background
                         #setting the buttons
                        if restart_button2.draw():
                            main()
                        if quit_button2.draw():
                            pygame.quit()
                        pygame.display.flip()
                        pygame.display.update()
            # Update the player sprite
            ai_update()
            ai_phantom_set_alpha()
            # Fill the screen with black color
            screen.fill((0,0,0))
            screen.blit(test_background,(-2,-2))
            obstacle_group.draw(screen)
            ai_draw()
            all_sprites.draw(screen)
            pygame.display.flip()
            pygame.display.update()
        elif paused:
            screen.fill((0,0,0))
            screen.blit(test_background,(-2,-2))
            obstacle_group.draw(screen)
            ai_draw()
            all_sprites.draw(screen)
            screen.blit(screenz,(292,162))
            if start_button.draw():
                paused = False
                print("Start")
            if exit_button.draw():
                pygame.quit()
                print("Exit")
            pygame.display.flip()
            pygame.display.update()

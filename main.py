
import random
import pygame

import sys





class GameObject:
    def __init__(self,image, x_pos, y_pos, speed):
        self.speed = speed
        self.image = pygame.image.load(image)
        self.vel_y = 0

        self.Y_GRAVITY = 1
        self.JUMP_HEIGHT = 15
        self.Y_VELOCITY = self.JUMP_HEIGHT
        self.jumping = 0

        self.pos = self.image.get_rect().move(x_pos, y_pos)
        self.flip = 0

        self.sprites = []
        self.current_sprite = 0

        self.pnj_walk = False
        self.pnj_walk_cycle = 0
        self.pnj_side = 0



    def anim(self,path_to_anim,number_of_anim,anim_time=0.1,size=(60, 60)):
        self.sprites = []
        for i in range(1,number_of_anim+1) :
            self.sprites.append(pygame.image.load('{} ({}).png'.format(path_to_anim,i)))

        self.current_sprite += anim_time
        if self.current_sprite >= number_of_anim :
            self.current_sprite = 0


        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.image, size)
        if self.flip > 0 :
            self.image = pygame.transform.flip(self.image, 180, 0)






    def move(self,up=False, down=False, left=False, right=False):

        if right:
          self.pos.right += self.speed

        if left:
          self.pos.right -= self.speed

        #if down:
          #self.pos.top += self.speed

        if up:
            self.pos.top -= self.Y_VELOCITY
            self.Y_VELOCITY -= self.Y_GRAVITY

            if self.Y_VELOCITY < -self.JUMP_HEIGHT :
                self.Y_VELOCITY = self.JUMP_HEIGHT
                self.jumping += 1


        if self.pos.right > 1920:
          self.pos.right = 1920

        if self.pos.left < 10:
          self.pos.left = 10


def move(npc : object, path_idle : str, path_walk : str, nb_anim_idle: int, nb_anim_walk : int, anim_time : float) -> None :
    npc.anim(path_idle, nb_anim_idle)

    if not npc.pnj_walk:
        if random.randint(0, 100) < 1:
            npc.pnj_walk = True
            npc.pnj_side = random.randint(0, 1)

    if npc.pnj_walk:

        if npc.pnj_side == 1:
            npc.move(right=True)
            npc.flip = 0
            npc.anim(path_walk, nb_anim_walk, anim_time)


        elif npc.pnj_side == 0:
            npc.move(left=True)
            npc.flip += 1
            npc.anim(path_walk, nb_anim_walk, anim_time)

        npc.pnj_walk_cycle += 1
        if npc.pnj_walk_cycle > random.randint(0, 10000):
            npc.pnj_walk_cycle = 0
            npc.pnj_walk = False

    print(npc.flip)




screen = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()            #get a pygame clock object
background = pygame.image.load('./sprites/map/level_bar_with_background.png').convert_alpha()
background = pygame.transform.scale(background, (1920, 1080))




objects = []
pnjs = []

player_hand = GameObject('sprites/characters/Biker/guns/hands/one_hand/hand_ (3).png',100,1000,2)
objects.append(player_hand)

p = GameObject('./sprites/characters/Biker/idle/idle_ (1).png',960, 900, 2)          #create the player object
objects.append(p)

loading_bar = GameObject('./sprites/UI/loading_bar_test/loading_ (1).png',1000, 500, 2)
objects.append(loading_bar)

#pnjs


pnj1 = GameObject('./sprites/pnj/people/1/idle/idle_ (1).png',300, 900, 1)
pnj2 = GameObject('./sprites/pnj/people/2/idle/idle_ (1).png', 750, 900, 1)
pnj5 = GameObject('./sprites/pnj/people/5/idle/idle_ (1).png', 1700, 900, 1)
pet4 = GameObject('./sprites/pnj/animals/4/idle/idle_ (1).png', 950, 900, 1)
pet6 = GameObject('./sprites/pnj/animals/6/idle/idle_ (1).png', 1375, 900, 1)

pnjs.append(pnj1)
pnjs.append(pnj2)
pnjs.append(pnj5)
pnjs.append(pet4)
pnjs.append(pet6)



clic_gauche = 0
clic_droit = 0

cycle = 0

player_jumping = False

player_use = False
player_use_animation = 0
player_press_e = 0

player_attack = False
player_attack_animation = 0

player_attack2 = False
player_attack2_animation = 0



player_dash = False
cycle_dash = 0
cycle_dash_begin = False
player_dash_animation = 0
player_press_ctrl = 0

player_have_gun = False



player_idle_animation = 1
test = False



while True:

    #print(pygame.mouse.get_pos())

    left, middle, right = pygame.mouse.get_pressed()

    cycle+=1

    screen.blit(background,(0,0))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player_jumping = True

    if keys[pygame.K_q]:
        p.move(left=True)
        p.anim('./sprites/characters/Biker/walk/walk_', 6)
        p.flip +=1


        if keys[pygame.K_LSHIFT] :
            p.anim('./sprites/characters/Biker/run/run_', 6)
            p.speed = 5
        else :
            p.speed = 2


    elif keys[pygame.K_d]:
        p.move(right=True)
        p.anim('./sprites/characters/Biker/walk/walk_', 6)
        p.flip = 0

        if keys[pygame.K_LSHIFT] :
            p.anim('./sprites/characters/Biker/run/run_', 6)
            p.speed = 5
        else :
            p.speed = 2

    else: #IDLE
        if player_attack2 == False and player_attack == False:
            if player_have_gun :
                p.anim('./sprites/characters/Biker/guns/idle/idle_', 4)

                if keys[pygame.K_s] :
                    p.anim('./sprites/characters/Biker/crouch/crouch_', 4)

            else:
                p.anim('./sprites/characters/Biker/idle/idle_', 4)

                if keys[pygame.K_s] :
                    p.anim('./sprites/characters/Biker/crouch/crouch_', 4)



    #PLAYER DASH
    if keys[pygame.K_LCTRL]:

        player_press_ctrl+=1

        if player_press_ctrl == 1 :
            player_dash = True
            p.current_sprite = 0

    if player_dash :
        cycle_dash = 0
        cycle_dash_begin = False
        player_dash_animation += 1
        if player_dash_animation < 15 :
            p.anim('./sprites/characters/Biker/dash/dash_', 6)

            if p.flip > 0 :
                p.pos.right -= 7
            else :
                p.pos.right += 7
        else :
            player_dash = False
            player_dash_animation = 0
            cycle_dash_begin = True
            loading_bar.current_sprite = 0

    if cycle_dash_begin :

        loading_bar.anim('./sprites/UI/loading_bar_test/loading_', 32,0.32,(100,100))
        cycle_dash += 1

        if cycle_dash % 100 == 0: #CHANGER VAR '100' POUR le temps de recharge du dash
            player_press_ctrl = 0
            cycle_dash_begin = False


    #PLAYER USE
    if keys[pygame.K_e]:
        player_press_e += 1
        if player_press_e == 1 :
            player_use = True
            p.current_sprite = 0

    if player_use :
        player_use_animation += 1
        if player_use_animation < 30 :
            p.anim('./sprites/characters/Biker/use/use_', 6)
        else :
            player_use = False
            player_use_animation = 0





    #PLAYER ATTACK
    if left :
        clic_gauche += 1
        if clic_gauche == 1 :
            player_attack = True
            p.current_sprite = 0

    if player_attack : #ATTACK CLIC GAUCHE
        player_attack_animation+=1
        if player_attack_animation < 35 :

            if not keys[pygame.K_LSHIFT] and ( keys[pygame.K_d] or keys[pygame.K_q] ):
                p.anim('./sprites/characters/Biker/walk_attack/walk_attack_', 6)

            elif keys[pygame.K_LSHIFT] :
                p.anim('./sprites/characters/Biker/run_attack/run_attack_', 6)

            else :
                p.anim('./sprites/characters/Biker/attack1/attack_', 6)

        else :
            player_attack = False
            player_attack_animation = 0


    if right :
        clic_droit += 1
        if clic_droit == 1 :
            player_attack2 = True
            p.current_sprite = 0

    if player_attack2 : #ATTACK CLIC droit
        player_attack2_animation+=1

        if player_attack2_animation < 35 :
            p.anim('./sprites/characters/Biker/kick/kick_', 6, 0.2)

        else :
            player_attack2 = False
            player_attack2_animation = 0




    #PLAYER JUMPING
    if p.pos.top > 900 :
        p.pos.top = 900
    if player_jumping == True :
        p.move(up=True)
        p.anim('./sprites/characters/Biker/jump/jump_', 4, 0.0001)
    if p.jumping > 0 :
        player_jumping = False
        p.jumping = 0







    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYUP :
            if event.key == pygame.K_e :
                player_press_e = 0

        if event.type == pygame.MOUSEBUTTONUP :
            mouse_presses = pygame.mouse.get_pressed()
            clic_gauche,clic_droit = 0,0




    if player_have_gun :

        player_hand.pos.y = p.pos.y+17
        player_hand.flip = p.flip

        if player_hand.flip > 0 :
            player_hand.pos.right = p.pos.right+2
        else:
            player_hand.pos.right = p.pos.right - 8

    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)

    #PNJS

    for pnj in pnjs:
        pnj.move()
        screen.blit(pnj.image, pnj.pos)

    #PNJ 1
    move(pnj1,'./sprites/pnj/people/1/idle/idle_','./sprites/pnj/people/1/walk/walk_',10,6,0.025)

    # PNJ 2
    move(pnj2,'./sprites/pnj/people/2/idle/idle_','./sprites/pnj/people/2/walk/walk_',4,6,0.025)

    #PNJ 5
    move(pnj5,'./sprites/pnj/people/5/idle/idle_','./sprites/pnj/people/5/walk/walk_',4,6,0.025)

    # PET 4
    move(pet4,'./sprites/pnj/animals/4/idle/idle_','./sprites/pnj/animals/4/walk/walk_',4,6,0.04)

    # PET 6
    move(pet6,'./sprites/pnj/animals/6/idle/idle_','./sprites/pnj/animals/6/walk/walk_',4,4,0.04)





    pygame.display.update()
    clock.tick(60)






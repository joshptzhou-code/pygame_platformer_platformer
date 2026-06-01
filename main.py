import pygame
from sys import exit #terminate the program
import os
import random
import tile_map

#game variables
Tile_Size = 64
Row_Count = 16
Column_Count = 29
game_width = Tile_Size * Column_Count #(1856)
game_height = Tile_Size * Row_Count #(1024)
Game_Map = tile_map.OPTIMIZED_GAME_MAP1

Player_X = game_width/2
Player_Y = game_height/2
Player_width = 100
Player_height = 100
Player_Jump_Width = 100
Player_Jump_Height = 100
Player_Shoot_Width = 110 # same height as player height
Player_Jump_Shoot_Width = 110 # same height as player jump height
Player_distance = 5


Gravity = 0.5
Friction = 0.4
Player_Velocity_X = 10
Player_Velocity_Y = -15

Player_Bullet_Width = 33
Player_Bullet_Height = 6
Player_Bullet_Velocity_X = 8

Health_Width = 40
Health_Height = 10

#enemy variables
Enemy_Width = 63
Enemy_Height = 90

Enemy_Bullet_Width = 70
Enemy_Bullet_Height = 35
Enemy_Bullet_Velocity_X = 2
Enemy_Bullet_velocity_Y = Enemy_Bullet_Velocity_X

Bat_Width = 70
Bat_Height = 35
Bat_Velocity_X = 8
Bat_Velocity_Y = 4

Dragon_Width = 315
Dragon_Height = 200

Dragon_Bullet_Width = 115
Dragon_Bullet_Height = 20
Dragon_Bullet_Velocity_X = 1
Dragon_Bullet_Velocity_Y = Dragon_Bullet_Velocity_X

#item variables
Life_Energy_Width = 50
Life_Energy_Height = 50
Item_Velocity_Y = -11 # item flies up then goes down

#images
def load_image(image_name, scale=None):
    image = pygame.image.load(os.path.join("images", image_name))
    if scale is not None:
        image = pygame.transform.scale(image, scale)
    return image

background_image = load_image("forest background.jpg")#background
player_image_right = load_image("Character default right.png", (Player_width, Player_height)) #player
player_image_left = load_image("Character default left.png", (Player_width, Player_height)) #player
player_image_jump_right = load_image("Character jump right.png", (Player_Jump_Width, Player_Jump_Height))
player_image_jump_left = load_image("Character jump left.png", (Player_Jump_Width, Player_Jump_Height))
player_image_shoot_right = load_image("Character Bow Right.png",(Player_Shoot_Width, Player_height))
player_image_shoot_left = load_image("Character Bow left.png", (Player_Shoot_Width, Player_height))
player_image_jump_shoot_right = load_image("Character jump shoot right.png", (Player_Jump_Shoot_Width, Player_Jump_Height))
player_image_jump_shoot_left = load_image("Character jump shoot left.png", (Player_Jump_Shoot_Width, Player_Jump_Height))
player_image_bullet_right = load_image("Arrow Right.png",(Player_Bullet_Width, Player_Bullet_Height))


floor_tile_image = load_image("Grassy Tile platform.jpg",(Tile_Size, Tile_Size))
rock_tile1_image = load_image("rock-tile1.png", (Tile_Size, Tile_Size))
rock_tile2_image = load_image("rock-tile2.png", (Tile_Size, Tile_Size))
rock_tile3_image = load_image("rock-tile3.png", (Tile_Size, Tile_Size))
rock_tile4_image = load_image("rock-tile4.png", (Tile_Size, Tile_Size))
light_grassy_tile_image = load_image("light grassy platform.jpg", (Tile_Size, Tile_Size))
dark_grassy_tile_image = load_image("Dark wood grassy platform.jpg", (Tile_Size, Tile_Size))
final_tile_image = load_image("final part grass platform.jpg", (Tile_Size, Tile_Size))
room_tile_image = load_image("room-tile.png", (Tile_Size, Tile_Size))


enemy_image_right = load_image("Basic_enemy_idle_right.png", (Enemy_Width, Enemy_Height))
enemy_image_left = load_image("Basic_enemy_idle_left.png", (Enemy_Width, Enemy_Height))
enemy_image_defense_left = load_image("enemy defense left.png", (Enemy_Width, Enemy_Height))
enemy_image_defense_right = load_image("enemy defense right.png", (Enemy_Width, Enemy_Height))

enemy_image_bullet_right = load_image("enemy bullet right.png", (Enemy_Bullet_Width, Enemy_Bullet_Height))
enemy_image_bullet_left = load_image("enemy bullet left.png",(Enemy_Bullet_Width, Enemy_Bullet_Height))
health_image = load_image("health.png", (Health_Width, Health_Height))
life_energy_image = load_image("heart life energy.png", (Life_Energy_Width, Life_Energy_Height))
spike_image = load_image("spike.png", (Tile_Size, Tile_Size))
bat_image_right = load_image("bat right.png", (Bat_Width, Bat_Height))
bat_image_left = load_image("bat left.png", (Bat_Width, Bat_Height))
dragon_image_right = load_image("dragon left.png", (Dragon_Width, Dragon_Height))
dragon_image_left = load_image("dragon right.png", (Dragon_Width, Dragon_Height))
dragon_image_bullet_right = load_image("fireball right.png", (Dragon_Bullet_Width, Dragon_Bullet_Height))
dragon_image_bullet_left = load_image("fireball left.png", (Dragon_Bullet_Width, Dragon_Bullet_Height))


pygame.init() #intiate the program
window = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("imagine playing this game coded by the greatest person of all time")
pygame.display.set_icon(player_image_right)
clock = pygame.time.Clock() # used for frame rate
pygame.font.init()
#game_font = pygame.font.SysFont("Arial", 24)
game_font = pygame.font.Font("./HollyBerryPop.ttf", 40)
game_over = False
game_win = False
#final_tile = None

#Custom event
Invincible_End = pygame.USEREVENT + 0
Shooting_End = pygame.USEREVENT + 1

class Player(pygame.Rect):
    class Bullet(pygame.Rect):
        def __init__(self):
            if player.direction == "left":
                pygame.Rect.__init__(self, player.x, player.y + Tile_Size/2, Player_Bullet_Width, Player_Bullet_Height)

                self.velocity_x = -Player_Bullet_Velocity_X
            elif player.direction == "right":
                pygame.Rect.__init__(self, player.x + player.width, player.y + Tile_Size/2, Player_Bullet_Width, Player_Bullet_Height )

                self.velocity_x = Player_Bullet_Velocity_X
            self.image = player_image_bullet_right
            self.used = False

    def __init__(self):
        pygame.Rect.__init__(self, Player_X, Player_Y, Player_width, Player_height)
        self.image = player_image_right
        self.velocity_x = 0
        self.velocity_y = 0
        self.direction = "right"
        self.jumping = False
        self.invincible = False
        self.max_health = 28
        self.health = self.max_health
        self.shooting = False
        self.bullets = []
        self.score = 0

    def update_image(self):
        if self.jumping and self.shooting:
            if self.direction == "right":
                self.image = player_image_jump_shoot_right
            elif self.direction == "left":
                self.image = player_image_jump_shoot_left

        elif self.shooting:
            if self.direction == "right":
                self.image = player_image_shoot_right
            elif self.direction == "left":
                self.image = player_image_shoot_left

        elif self.jumping:
            if self.direction == "right":
                self.image = player_image_jump_right
            elif self.direction == "left":
                self.image = player_image_jump_left
        else:
            if self.direction == "right":
                self.image = player_image_right
            elif self.direction == "left":
                self.image = player_image_left

    def set_invincible(self, milliseconds=1000):
        self.invincible = True
        pygame.time.set_timer(Invincible_End, milliseconds, 1)

    def set_shooting(self):
        if not self.shooting:
            self.shooting = True
            self.bullets.append(Player.Bullet())
            pygame.time.set_timer(Shooting_End, 250, 1)

class Enemy(pygame.Rect):
    class Bullet(pygame.Rect):
        def __init__(self, enemy, velocity_y):
            if enemy.direction == "left":
                pygame.Rect.__init__(self, enemy.x, enemy.y + Tile_Size / 2,
                                     Enemy_Bullet_Width, Enemy_Bullet_Height)
                self.velocity_x = -Enemy_Bullet_Velocity_X
            elif enemy.direction == "right":
                pygame.Rect.__init__(self, enemy.x + enemy.width, enemy.y + Tile_Size / 2,
                                     Enemy_Bullet_Width, Enemy_Bullet_Height)
                self.velocity_x = Enemy_Bullet_Velocity_X
            self.velocity_y = velocity_y
            self.image = enemy_image_bullet_left
            self.used = False

    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, Enemy_Width, Enemy_Height)
        self.image = enemy_image_left
        self.velocity_y = 0
        self.direction = "left"
        self.jumping = False
        self.health = 1
        self.bullets = []
        self.last_fired = pygame.time.get_ticks()  # time in ms after pygame.initialize
        self.guarding = False

    def update_image(self):
        if self.direction == "right":
            if self.guarding:
                self.image = enemy_image_defense_right
            else:
                self.image = enemy_image_right
        elif self.direction == "left":
            if self.guarding:
                self.image = enemy_image_defense_left
            else:
                self.image = enemy_image_left

    def set_shooting(self):
        if abs(self.x - player.x) <= Tile_Size * 4:
            self.guarding = False
            now = pygame.time.get_ticks()
            if now - self.last_fired > 1000:
                self.last_fired = now
                self.bullets.append(Enemy.Bullet(self, -Enemy_Bullet_velocity_Y))
                self.bullets.append(Enemy.Bullet(self, 0))
                self.bullets.append(Enemy.Bullet(self, Enemy_Bullet_velocity_Y))
        else:
            self.guarding = True

class Dragon(pygame.Rect):
    class Bullet(pygame.Rect):
        def __init__(self, dragon, velocity_y):
            if dragon.direction == "left":
                pygame.Rect.__init__(self, dragon.x, dragon.y + Tile_Size / 2,
                                     Dragon_Bullet_Width, Dragon_Bullet_Height)
                self.velocity_x = -Dragon_Bullet_Velocity_X
            elif dragon.direction == "right":
                pygame.Rect.__init__(self, dragon.x + dragon.width, dragon.y + Tile_Size / 2,
                                     Dragon_Bullet_Width, Dragon_Bullet_Height)
                self.velocity_x = Dragon_Bullet_Velocity_X
            self.velocity_y = velocity_y
            self.image = dragon_image_bullet_left
            self.used = False

    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, Dragon_Width, Dragon_Height)
        self.image = dragon_image_left
        self.velocity_y = 0
        self.direction = "left"
        self.jumping = False
        self.health = 30
        self.bullets = []
        self.last_fired = pygame.time.get_ticks()  # time in ms after pygame.initialize
        self.guarding = False

    def update_image(self):
        if self.direction == "left":
            self.image = dragon_image_right
        elif self.direction == "right":
            self.image = dragon_image_left

    def set_shooting(self):
        if abs(self.x - player.x) <= Tile_Size * 9:
            now = pygame.time.get_ticks()
            if now - self.last_fired > 3000:
                self.last_fired = now
                self.bullets.append(Dragon.Bullet(self, -Dragon_Bullet_Velocity_Y))
                self.bullets.append(Dragon.Bullet(self, 0))
                self.bullets.append(Dragon.Bullet(self, Dragon_Bullet_Velocity_Y))


class Bat(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, Bat_Width, Bat_Height)
        self.image = bat_image_right
        self.direction = "right"
        self.health = 3
        self.velocity_x = Bat_Velocity_X
        self.velocity_y = Bat_Velocity_Y
        self.start_x = x
        self.start_y = y
        self.max_range_x = Tile_Size*13
        self.max_range_y = Tile_Size*4

    def update_image(self):
        if self.direction == "right":
            self.image = bat_image_right
        elif self.direction == "left":
            self.image = bat_image_left

#class Dragon(pygame.Rect):
 #   class Bullet(pygame.Rect):
       # def __init__(self, dragon, velocity_y):
          #  if dragon.direction == "left":
            #    pygame.Rect.__init__(self, dragon.x, dragon.y + Tile_Size/2, Dragon_Bullet_Width, Dragon_Bullet_Height)
           #     self.velocity_x = -Dragon_Bullet_Velocity_X
          #  elif dragon.direction == "right":
            #    pygame.Rect.__init__(self, dragon.x + dragon.width, dragon.y + Tile_Size/2, Dragon_Bullet_Width, Dragon_Bullet_Height)
            #    self.velocity_x = Dragon_Bullet_Velocity_X
          #  self.velocity_y = velocity_y
          #  self.image = dragon_image_bullet
          #  self.used = False

   # def __init__(self, x, y):
       # pygame.Rect.__init__(self, x, y, Dragon_Width, Dragon_Height)
      #  self.image = dragon_image_left
       # self.velocity_y = 0
        #self.direction = "right"
       # self.health = 20
       # self.jumping = False
        #self.guarding = False
       # self.last_fired = pygame.time.get_ticks()
       # self.bullets = []
        #self.shooting = False

   # def update_image(self):
     #   if self.direction == "right":
        #    self.image = dragon_image_right
       # elif self.direction == "left":
          #  self.image = dragon_image_left

    #def set_shooting(self):
     #   if abs(self.x - player.x) <= Tile_Size * 6:
           # now = pygame.time.get_ticks()
         #   if now - self.last_fired > 3000:
           #     self.last_fired = now
              #  self.bullets.append(Dragon.Bullet(self, -Enemy_Bullet_velocity_Y))
               # self.bullets.append(Dragon.Bullet(self, 0))
                #self.bullets.append(Dragon.Bullet(self, Enemy_Bullet_velocity_Y))


class Tile(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, Tile_Size, Tile_Size)
        self.image = image

class Item(pygame.Rect):
    def __init__(self, x, y, image):
        pygame.Rect.__init__(self, x, y, image.get_width(), image.get_height())
        self.image = image
        self.jumping = False
        self.velocity_y = Item_Velocity_Y
        self.used = False

def append_tiles(map_code, tile):
    if map_code < 0:
        background_tiles.append(tile)
    else:
        tiles.append(tile)

#CREATE THE TILES
def create_map():
    #global final_tile

    for column in range(len(Game_Map[0])):
        for row in range(len(Game_Map)):
            map_code = Game_Map[row][column]
            x = column * Tile_Size
            y = row * Tile_Size
            if map_code == 0:
                continue

            elif abs(map_code) == 1:
                append_tiles(map_code, Tile(x, y, rock_tile1_image))

            elif abs(map_code) == 2:
                append_tiles(map_code, Tile(x, y, rock_tile2_image))

            elif abs(map_code) == 3:
                append_tiles(map_code, Tile(x, y, rock_tile3_image))

            elif abs(map_code) == 4:
                append_tiles(map_code, Tile(x, y, rock_tile4_image))

            elif abs(map_code) == 5:
                append_tiles(map_code, Tile(x, y, light_grassy_tile_image))

            elif abs(map_code) == 6:
                append_tiles(map_code, Tile(x, y, dark_grassy_tile_image))

            elif map_code == 7:
                background_tiles.append(Tile(x, y, room_tile_image))

            elif map_code == 8:
                spikes.append(Tile(x, y, spike_image))

            elif map_code == 9:
                enemies.append(Enemy(x, y))

            elif map_code == 10:
                bats.append(Bat(x, y))

            elif map_code == 11:
                final_tile = Tile(x,y, final_tile_image)
                tiles.append(final_tile)


            elif map_code == 12:
                tiles.append(Tile(x, y, floor_tile_image))

            elif map_code == 13:
               dragons.append(Dragon(x, y))

def reset_game():
    global player, enemies, enemy_bullets, tiles, background_tiles, items, spikes, bats, game_over, game_win, dragons, dragon_bullets #win_tiles #final_tiles

    player = Player()
    enemies = []
    enemy_bullets = []  # keep bullets active after death
    tiles = []
    background_tiles = []
    items = []
    spikes = []
    bats = []
    dragons = []
    create_map()

    game_over = False
    game_win = False

def check_tile_collision(character):
    for tile in tiles:
        if character.colliderect(tile):
            return tile
        elif tile.x - character.x > game_width:
            return None
    return None

def check_tile_collision_x(character):
    tile = check_tile_collision(character)
    if tile is not None:
        if character.velocity_x < 0:
            character.x = tile.x + tile.width
        elif character.velocity_x > 0:
            character.x = tile.x - character.width
        character.velocity_x = 0

def check_tile_collision_y(character):
   tile = check_tile_collision(character)
   if tile is not None:
       if character.velocity_y < 0:
           character.y = tile.y + tile.height
       elif character.velocity_y > 0:
           character.y = tile.y - character.height
           character.jumping = False
       character.velocity_y = 0

def drop_item(character):
    random_number = random.randint(1, 100)
    if 0 < random_number <= 20:
        items.append(Item(character.x, character.y, life_energy_image))

#scrolling camera(everything moves with the player)
def move_player_x(velocity_x):
    move_map_x(velocity_x)
    tile = check_tile_collision(player)
    if tile is not None:
        move_map_x(-velocity_x)

def move_map_x(velocity_x):
    for tile in background_tiles:
        tile.x += velocity_x

    for tile in tiles:
        tile.x += velocity_x

    for enemy in enemies:
        enemy.x += velocity_x
        for bullet in enemy.bullets:
            bullet.x += velocity_x

    for bullet in enemy_bullets:
        bullet.x += velocity_x

    for dragon in dragons:
        dragon.x += velocity_x
        for bullet in dragon.bullets:
            bullet.x += velocity_x

    for bullet in dragon_bullets:
        bullet.x += velocity_x

    for item in items:
        item.x += velocity_x

    for spike in spikes:
        spike.x += velocity_x

    for bat in bats:
        bat.start_x += velocity_x
        bat.x += velocity_x

    #for dragon in dragons:
      #  dragon.x += velocity_x


def move():
    global enemies, items, bats, enemy_bullets, game_over, game_win, dragons, dragon_bullets #win_tiles #final_tiles
    # x movement
    # if player.direction == "left" and player.velocity_x < 0:
    #     player.velocity_x += FRICTION
    # elif player.direction == "right" and player.velocity_x > 0:
    #     player.velocity_x -= FRICTION
    # else:
    #     player.velocity_x = 0

    # player.x += player.velocity_x
    # if player.x < 0:
    #     player.x = 0
    # elif player.x + player.width > GAME_WIDTH:
    #     player.x = GAME_WIDTH - player.width

    # check_tile_collision_x(player)

    # y movement
    player.velocity_y += Gravity
    player.y += player.velocity_y
    check_tile_collision_y(player)

    for spike in spikes:
        if player.colliderect(spike):
            player.health = 0  # game over

    # bullets
    for bullet in player.bullets:
        bullet.x += bullet.velocity_x
        for enemy in enemies:
            if enemy.health > 0 and not bullet.used and bullet.colliderect(enemy):
                bullet.used = True
                if not enemy.guarding:
                    enemy.health -= 1
                    if enemy.health <= 0:
                        drop_item(enemy)
                        # enemy_bullets += enemy.bullets
                        enemy_bullets.extend(enemy.bullets)
                        player.score += 500

        for bat in bats:
            if bat.health > 0 and not bullet.used and bullet.colliderect(bat):
                bullet.used = True
                bat.health -= 1
                if bat.health <= 0:
                    drop_item(bat)
                    player.score += 2500

        for dragon in dragons:
            if dragon.health > 0 and not bullet.used and bullet.colliderect(dragon):
                bullet.used = True
                dragon.health -= 1
                if dragon.health <= 0:
                    drop_item(dragon)
                    dragon_bullets.extend(dragon.bullets)
                    player.score += 10000
                    game_win = True
    player.bullets = [bullet for bullet in player.bullets if not bullet.used \
                      and bullet.x + bullet.width > 0 and bullet.x < game_width]

    enemies = [enemy for enemy in enemies if enemy.health > 0]
    bats = [bat for bat in bats if bat.health > 0]
    dragons = [dragon for dragon in dragons if dragon.health > 0]

    # enemy y movement

    for enemy in enemies:
        if player.x < enemy.x:
            enemy.direction = "left"
        else:
            enemy.direction = "right"

        enemy.velocity_y += Gravity
        enemy.y += enemy.velocity_y
        check_tile_collision_y(enemy)

        if not player.invincible and player.colliderect(enemy):
            player.health -= 1
            player.set_invincible()

        # enemy bullets
        enemy.set_shooting()
        for bullet in enemy.bullets:
            bullet.x += bullet.velocity_x
            bullet.y += bullet.velocity_y
            if not player.invincible and player.colliderect(bullet):
                player.health -= 2
                bullet.used = True
                player.set_invincible()

        enemy.bullets = [bullet for bullet in enemy.bullets if not bullet.used \
                          and bullet.x + bullet.width > 0 and bullet.x < game_width]

    for bullet in enemy_bullets:
        bullet.x += bullet.velocity_x
        bullet.y += bullet.velocity_y
        if not player.invincible and player.colliderect(bullet):
            player.health -= 2
            bullet.used = True
            player.set_invincible()

    enemy_bullets = [bullet for bullet in enemy_bullets if not bullet.used \
                      and bullet.x + bullet.width > 0 and bullet.x < game_width]

    #dragon movement
    for dragon in dragons:
        if player.x < dragon.x:
            dragon.direction = "left"
        else:
            dragon.direction = "right"

        dragon.velocity_y += Gravity
        dragon.y += dragon.velocity_y
        check_tile_collision_y(dragon)

        if not player.invincible and player.colliderect(dragon):
            player.health -= 1
            player.set_invincible()

        # enemy bullets
        dragon.set_shooting()
        for bullet in dragon.bullets:
            bullet.x += bullet.velocity_x
            bullet.y += bullet.velocity_y
            if not player.invincible and player.colliderect(bullet):
                player.health -= 2
                bullet.used = True
                player.set_invincible()

        dragon.bullets = [bullet for bullet in dragon.bullets if not bullet.used \
                          and bullet.x + bullet.width > 0 and bullet.x < game_width]

    for bullet in dragon_bullets:
        bullet.x += bullet.velocity_x
        bullet.y += bullet.velocity_y
        if not player.invincible and player.colliderect(bullet):
            player.health -= 2
            bullet.used = True
            player.set_invincible()

    dragon_bullets = [bullet for bullet in dragon_bullets if not bullet.used \
                      and bullet.x + bullet.width > 0 and bullet.x < game_width]

    for bat in bats:
        if abs(bat.x + bat.velocity_x - bat.start_x) >= bat.max_range_x:
            bat.velocity_x *= -1
            if bat.velocity_x < 0:
                bat.direction = "left"
            elif bat.velocity_x > 0:
                bat.direction = "right"
        else:
            bat.x += bat.velocity_x

        if abs(bat.y + bat.velocity_y - bat.start_y) >= bat.max_range_y:
            bat.velocity_y *= -1
        else:
            bat.y += bat.velocity_y

        if not player.invincible and player.colliderect(bat):
            player.health -= 1
            player.set_invincible()

    for item in items:
        item.velocity_y += Gravity
        item.y += item.velocity_y
        check_tile_collision_y(item)
        if player.colliderect(item):
            item.used = True
            if item.image == life_energy_image:
                player.health = min(player.health + 2, player.max_health)

    items = [item for item in items if not item.used]

    if player.health <= 0 or player.y > game_height:
        game_over = True


def draw():
    window.fill("pink") #window color
    window.blit(background_image, (0, 20)) #place the background

    for tile in background_tiles:
        if tile.x > game_width:
            break
        window.blit(tile.image, tile)

    for tile in tiles:
        if tile.x > game_width:
            break
        window.blit(tile.image, tile)

    for spike in spikes:
        if spike.x > game_width:
            break
        window.blit(spike.image, spike)

    player.update_image()
    window.blit(player.image, player)

    for bullet in player.bullets:
        window.blit(bullet.image, bullet)

    for enemy in enemies:
        if enemy.x <= game_width:
            enemy.update_image()
            window.blit(enemy.image, enemy)
        for bullet in enemy.bullets:
            window.blit(bullet.image, bullet)

    for bullet in enemy_bullets:
        window.blit(bullet.image, bullet)

    for dragon in dragons:
        if dragon.x <= game_width:
            dragon.update_image()
            window.blit(dragon.image, dragon)
        for bullet in dragon.bullets:
            window.blit(bullet.image, bullet)

    for bullet in dragon_bullets:
        window.blit(bullet.image, bullet)

    for bat in bats:
        if bat.x > game_width:
            break
        bat.update_image()
        window.blit(bat.image, bat)

  #  for dragon in dragons:
     #   if dragon.x > game_width:
      #      break
      #  dragon.update_image()
       # window.blit(dragon.image, dragon)
       # for bullet in dragon.bullets:
        #    window.blit(bullet.image, bullet)

    for item in items:
        if item.x > game_width:
            break
        window.blit(item.image, item)

    #pygame.draw.rect(window, "red", (Tile_Size, Tile_Size, 10 * player.max_health, 10))
    #pygame.draw.rect(window, "green", (Tile_Size, Tile_Size, 10 * player.health, 10))

    pygame.draw.rect(window, "black", (Tile_Size, Tile_Size, Health_Width, Health_Height * player.max_health))
    for i in range(player.max_health - player.health, player.max_health):
        window.blit(health_image, (Tile_Size, Tile_Size + i*Health_Height, Health_Width, Health_Height))

    #score
    text_score = str(player.score)
    while len(text_score) < 7: #7 digits in score
        text_score = "0" + text_score
    text_surface = game_font.render(text_score, False, "white")
    window.blit(text_surface, (game_width/2, Tile_Size/2))

    if game_over:
        text_surface = game_font.render("GAME OVER:", False, "white")
        window.blit(text_surface, (game_width / 2, game_height / 2))
        text_surface = game_font.render("Press [Enter} to restart", False, "white")
        window.blit(text_surface, (game_width / 2, game_height / 2 + Tile_Size))

    if game_win:
        text_surface = game_font.render("OMG you actually won...:", False, "white")
        window.blit(text_surface, (game_width / 2, game_height / 2))
        text_surface = game_font.render(f"Final Score: {text_score}", False, "white")
        window.blit(text_surface, (game_width / 2, game_height / 2 + Tile_Size ))
        text_surface = game_font.render("Press [Enter} to play again", False, "white")
        window.blit(text_surface, (game_width / 2, game_height / 2 + Tile_Size*2))

   # if player.x <= Column_Count:
        #text_surface = game_font.render("You Win!", False, "white")
       # window.blit(text_surface, (game_width / 2, game_height / 2))
       # text_surface = game_font.render("Press [Enter] to play again", False, "white")
        #window.blit(text_surface, (game_width / 2, game_height / 2 + Tile_Size))
        #reset_game()

#start game
player = Player()
enemies = []
enemy_bullets = [] # keep bullets active after death
tiles = []
background_tiles = []
items = []
spikes = []
bats = []
#final_tiles = []
#win_tiles = []
dragons = []
dragon_bullets = []
create_map()

while True:#game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == Invincible_End:
            player.invincible = False
        elif event.type == Shooting_End:
            player.shooting = False

        #control keys WASD and arrows
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and game_over:
        reset_game()

    if (keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]) and game_win:
        reset_game()

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not player.jumping:
        player.velocity_y = Player_Velocity_Y
        player.jumping = True

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        #player.velocity_x = -Player_Velocity_X
        move_player_x(Player_Velocity_X)
        player.direction = "left"

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        #player.velocity_x = Player_Velocity_X
        move_player_x(-Player_Velocity_X)
        player.direction = "right"

    if keys[pygame.K_x] or keys[pygame.K_SPACE]:
        player.set_shooting()

    #Press speed movement
    keys = pygame.key.get_pressed()

    player.velocity_x = 0

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.velocity_x = -Player_Velocity_X
        player.direction = "left"

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.velocity_x = Player_Velocity_X
        player.direction = "right"

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and not player.jumping:
        player.velocity_y = Player_Velocity_Y
        player.jumping = True

    if not game_over and not game_win:
        move()

        draw()
        pygame.display.update()
        clock.tick(60) # 60 fps
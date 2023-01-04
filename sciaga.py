import pygame, random
from pygame.locals import *
import xml.etree.ElementTree
class SpriteSheet(pygame.sprite.Sprite):
    # load an atlas image
    # can also pass an associated XML file (ref. Kenney art)
    def __init__(self, img_file, data_file=None):
        super().__init__()
        self.spritesheet = pygame.image.load(img_file).convert_alpha()
        if data_file:
            tree = xml.etree.ElementTree.parse(data_file)
            self.map = {}
            for node in tree.iter():
                if node.attrib.get('name'):
                    name = node.attrib.get('name')
                    self.map[name] = {}
                    self.map[name]['x'] = int(node.attrib.get('x'))
                    self.map[name]['y'] = int(node.attrib.get('y'))
                    self.map[name]['width'] = int(node.attrib.get('width'))
                    self.map[name]['height'] = int(node.attrib.get('height'))

    def get_image_rect(self, x, y, w, h):
        rect = self.spritesheet.subsurface(pg.Rect(x, y, w, h))

        return self.spritesheet.subsurface(pg.Rect(x, y, w, h))

    def get_image_name(self, name):
        rect = pygame.Rect(self.map[name]['x'], self.map[name]['y'],self.map[name]['width'], self.map[name]['height'])
        pygame.sprite.Sprite.add(self)
        return self.spritesheet.subsurface(rect)

class Units(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = sheet_1.get_image_name("medievalUnit_07.png")
        self.rect = self.image.get_rect(center=(700, 300))
        self.mouse_movement_group = False
        self.if_collide = False
        self.x_speed = 0
        self.y_speed = 0
        self.where_to_move = ()
        self.where_to_move_x = self.rect.centerx
        self.where_to_move_y = self.rect.centery


        self.image = sheet_1.get_image_name("medievalUnit_07.png")
        self.rect = self.image.get_rect(center=(700, 300))
    def update(self):
        if pygame.sprite.spritecollide(self,mouse_group,dokill=False):
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
            if pygame.mouse.get_pressed()[2] == False:
                self.mouse_movement_group = True

        if self.mouse_movement_group == True:
            if pygame.mouse.get_pressed()[2] == True:
                self.where_to_move_x, self.where_to_move_y =  pygame.mouse.get_pos()
                self.movement = True
            if pygame.mouse.get_pressed()[0] == True:
                self.mouse_movement_group = False
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        for sprites in units_group:
            if sprites == self:
                pass
            elif pygame.sprite.collide_circle(self, sprites):
                pass






        if self.where_to_move_x != self.rect.centerx:
            if self.where_to_move_x > self.rect.centerx:
                self.x_speed = 1
            else: self.x_speed = -1
        else:self.x_speed = 0
        if self.where_to_move_y != self.rect.centery:
            if self.where_to_move_y > self.rect.centery:
                self.y_speed = 1
            else: self.y_speed = -1
        else: self.y_speed = 0


        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed

        if self.where_to_move_y == self.rect.y and self.where_to_move_x == self.rect.centerx:
            self.movement = False







class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([50,50])
        self.rect = self.image.get_rect()
    def update(self):
        self.size_rect = mouse_rect()
        if pygame.mouse.get_pressed()[0] == True:

            self.image = pygame.Surface([self.size_rect[1][0], self.size_rect[1][1]],5)
            self.rect.update(self.size_rect)
            pygame.draw.rect(screen,(255,255,255,),self.size_rect,4)
        else:

            self.rect.update((2,2),(1,1))

class UnitsSelected(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()



#Nazwa i wielkosc ekranu aplikacji
pygame.display.set_caption("siemaneczko")
screen = pygame.display.set_mode((1600, 800))

clock = pygame.time.Clock()
#Sprite Sheets
sheet_1 = SpriteSheet("graphics/Spritesheet/medievalRTS_spritesheet.png", "graphics/Spritesheet/medievalRTS_spritesheet.xml")
sheet_2 = SpriteSheet("graphics/Spritesheet/medievalRTS_spritesheet.png", "graphics/Spritesheet/medievalRTS_spritesheet.xml")


#Stałe
running = True

cord_1 = (0,0)


mouse_button = 1
camera_group = pygame.sprite.Group()
base = sheet_1.get_image_name("medievalStructure_17.png")
baserect = base.get_rect(center=(800, 400))

#sprite groups
mouse_group = pygame.sprite.GroupSingle()
mouse_group.add(Mouse())

units_group = pygame.sprite.Group()

units_group_selected = pygame.sprite.Group

def mouse_rect():
    global cord_1
    cord_2 = pygame.mouse.get_pos()

    x, y = cord_1
    x_2, y_2 = cord_2
    h = abs(y_2 - y)
    w = abs(x_2 - x)
    if y < y_2 and x < x_2:
        mouse_rect = ((x,y),(w+1,h+1))
    elif y < y_2 and x > x_2:
        mouse_rect = ((x_2,y),(w+1,h+1))

    elif  x > x_2:
        mouse_rect = ((x_2,y_2),(w+1,h+1))

    else:
        mouse_rect = ((x,y_2),(w+1,h+1))

    return mouse_rect


while running:
    screen.fill((4,255,255))
    point = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.K_SPACE:
            camera_group.draw(screen)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] ==  True:
                # dodawanie nowej jednostki
                point = pygame.mouse.get_pos()
                collide = baserect.collidepoint(point)

                if collide: units_group.add(Units())

                cord_1 = pygame.mouse.get_pos()

                mouse_button_left = 0
        if event.type == pygame.MOUSEBUTTONUP:


            mouse_button_left = 1




    screen.blit(base,baserect)




    units_group.draw(screen)
    units_group.update()




    mouse_group.update()



    pygame.display.update()
    clock.tick(60)
pygame.quit()
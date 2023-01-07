import pygame, random, math
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
        rect = self.spritesheet.subsurface(pygame.Rect(x, y, w, h))

        return self.spritesheet.subsurface(pygame.Rect(x, y, w, h))

    def get_image_name(self, name):
        rect = pygame.Rect(self.map[name]['x'], self.map[name]['y'],self.map[name]['width'], self.map[name]['height'])
        pygame.sprite.Sprite.add(self)
        return self.spritesheet.subsurface(rect)
class Resources():
    def __init__(self):
        super().__init__()
        self.wood = 10000
        self.gold = 50000
        self.iron = 0
        self.food = 10000
        self.stone = 0

class MousePropertier():
    def __init__(self):
        super().__init__()
        self.mouse_1 = 1
        self.mouse_2 = 1
        self.mouse_3 = 1
        self.mouse_rect_unit_group = ()
        self.mouse_rect_building_group =()
class Interface():
    def __init__(self):
        super().__init__()
    def recousrce_bar(self):
        recource_bar_group.add(ResourceBar("RecourceBarRect"))
        recource_bar_group.add(ResourceBar("Woodbar"))
        recource_bar_group.add(ResourceBar("Goldbar"))
        recource_bar_group.add(ResourceBar("Ironbar"))
        recource_bar_group.add(ResourceBar("Foodbar"))
        recource_bar_group.add(ResourceBar("Stonebar"))
    def base_interface(self):
        base_interface_group.add(BaseInterface("BaseInterfaceRect"))
        base_interface_group.add(BaseInterface("WorkerSpawner"))
        base_interface_group.add(BaseInterface("FarmSpawner"))
        base_interface_group.add(BaseInterface("BarrackSpawner"))

class ResourceBar(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.type = type
        if self.type == "RecourceBarRect":
            self.image = pygame.Surface((300,100))
            self.rect = self.image.get_rect(topleft=(0,0))
        if self.type == "Woodbar":
            self.image = test_font.render(f"Wood: {current_recouces.wood}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,10))
        if self.type == "Goldbar":
            self.image = test_font.render(f"Gold: {current_recouces.gold}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,30))
        if self.type == "Ironbar":
            self.image = test_font.render(f"Iron: {current_recouces.iron}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,50))
        if self.type == "Foodbar":
            self.image = test_font.render(f"Food: {current_recouces.food}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,70))
        if self.type == "Stonebar":
            self.image = test_font.render(f"Stone: {current_recouces.stone}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,90))




    def update(self):
        if self.type == "RecourceBarRect":
            pass
        if self.type == "Woodbar":
            self.image = test_font.render(f"Wood: {current_recouces.wood}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,10))
        if self.type == "Goldbar":
            self.image = test_font.render(f"Gold: {current_recouces.gold}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,30))
        if self.type == "Ironbar":
            self.image = test_font.render(f"Iron: {current_recouces.iron}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,50))
        if self.type == "Foodbar":
            self.image = test_font.render(f"Food: {current_recouces.food}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,70))
        if self.type == "Stonebar":
            self.image = test_font.render(f"Stone: {current_recouces.stone}", False, (255, 255, 255))
            self.rect = self.image.get_rect(topleft = (10,90))

class BaseInterface(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.type = type
        if self.type == "BaseInterfaceRect":
            self.image = pygame.Surface((100,400))
            self.rect = self.image.get_rect(topleft=(0,100))
        if self.type == "WorkerSpawner":
            self.image = sheet_1.get_image_name("medievalUnit_07.png")
            self.rect = self.image.get_rect(topleft=(10, 110))
        if self.type == "FarmSpawner":
            self.image = sheet_1.get_image_name("medievalStructure_14.png")
            self.image = pygame. transform. scale(self.image, (20,20))
            self.rect =self.image.get_rect(topleft =(10,142))
        if self.type == "BarrackSpawner":
            self.image = sheet_1.get_image_name("medievalStructure_05.png")
            self.image = pygame.transform.scale(self.image, (20, 20))
            self.rect = self.image.get_rect(topleft=(10, 172))

    def do_kill(self):
        interface_box = self.rect

        for i in base_interface_group:
            if i.type == "BaseInterfaceRect":
                interface_box = i.rect
                break
        if pygame.mouse.get_pressed()[0] == True and mouse_button_state.mouse_1 == 0:
            collide_with_base = False
            if collide_with_base == False:
                for buildings in buildings_group:
                    if (buildings.type == "Base" and buildings.rect.collidepoint(pygame.mouse.get_pos())) or interface_box.collidepoint(pygame.mouse.get_pos()):
                        collide_with_base = True

            if collide_with_base == False:
                self.kill()


    def update(self):
        self.do_kill()
        if self.type == "WorkerSpawner":

            if self.rect.collidepoint(pygame.mouse.get_pos())  and mouse_button_state.mouse_1 == 0 and pygame.mouse.get_pressed()[0] == True:
                mouse_button_state.mouse_1 = 1
                if current_recouces.food >= 50:
                    units_group.add(Units("Worker"))
                    current_recouces.food -= 50
        if self.type == "FarmSpawner":
            if self.rect.collidepoint(pygame.mouse.get_pos()) and mouse_button_state.mouse_1 == 0 and pygame.mouse.get_pressed()[0] == True:
                mouse_button_state.mouse_1 = 1
                if current_recouces.wood >=50:
                    buildings_group.add(Buildings(("Farm"),pygame.mouse.get_pos()))
                    current_recouces.wood -= 50
        if self.type == "BarrackSpawner":
            if self.rect.collidepoint(pygame.mouse.get_pos()) and mouse_button_state.mouse_1 == 0 and pygame.mouse.get_pressed()[0] == True:
                mouse_button_state.mouse_1 = 1
                buildings_group.add(Buildings(("Barracks"), pygame.mouse.get_pos()))


class Buildings(pygame.sprite.Sprite):
    def __init__(self,type,position):
        super().__init__()
        self.type = type
        self.animation_index = 0
        self.position = position
        self.if_placed = False
        if self.type == "Base":
            self.image = sheet_1.get_image_name("medievalStructure_17.png")
            self.rect = self.image.get_rect(center=self.position)

        if self.type == "Farm":
            self.positionx, self.positiony = self.position
            self.image = sheet_1.get_image_name("medievalStructure_19.png")

            self.rect = self.image.get_rect(center=self.position)

            wind_mill_frame1 = sheet_1.get_image_name("medievalStructure_14.png")
            wind_mill_frame2 = sheet_1.get_image_rect(382, 381, 52, 52)
            wind_mill_frame3 = sheet_1.get_image_name("medievalStructure_15.png")
            self.frames = [wind_mill_frame1, wind_mill_frame2, wind_mill_frame3]


            self.farmland_image = sheet_1.get_image_name("medievalTile_57.png")
            self.farmlands_positions = ((self.positionx - 64,self.positiony-64),(self.positionx,self.positiony-64),(self.positionx + 64,self.positiony-64),
                                        (self.positionx -64,self.positiony),(self.positionx,self.positiony),(self.positionx + 64,self.positiony),
                                        (self.positionx - 64,self.positiony+64),(self.positionx,self.positiony+64),(self.positionx+64,self.positiony+64))



            self.jobs = [0, 0, 0, 0, 0, 0, 0, 0]

        if self.type == "Barracks":
            self.positionx, self.positiony = self.position
            self.image = sheet_1.get_image_name("medievalStructure_05.png")
            self.rect = self.image.get_rect(center=self.position)

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.animation_rect = self.frames[int(self.animation_index)].get_rect(center=(self.position))
        screen.blit(self.frames[int(self.animation_index)],self.animation_rect)
    def update(self):
        if self.type == "Base":
            if self.if_placed == False:
                self.rect.center = self.position = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0] == True  and mouse_button_state.mouse_1 == 0:
                    self.if_placed = True
            else:
                if  mouse_button_state.mouse_1 == 0 and pygame.mouse.get_pressed()[0] == True:
                    if self.rect.collidepoint(pygame.mouse.get_pos()):
                       interface_draw.base_interface()
        if self.type == "Farm":
            if self.if_placed == False:
                self.position = pygame.mouse.get_pos()
                self.positionx, self.positiony = self.position
                self.farmlands_positions = ((self.positionx - 64, self.positiony - 64), (self.positionx, self.positiony - 64),(self.positionx + 64, self.positiony - 64),
                                            (self.positionx - 64, self.positiony),      (self.positionx, self.positiony),     (self.positionx + 64, self.positiony),
                                            (self.positionx - 64, self.positiony + 64), (self.positionx, self.positiony + 64),(self.positionx + 64, self.positiony + 64))
                self.rect.center = self.position
                if pygame.mouse.get_pressed()[0] == True  and mouse_button_state.mouse_1 == 0:
                    self.if_placed = True
            else:


                pass

            for farms in self.farmlands_positions:
                farm_rect = self.image.get_rect(center=(farms))
                screen.blit(self.farmland_image,farm_rect)
            screen.blit(self.image,self.rect)
            self.animation_state()
        if self.type =="Barracks":
            if self.type == "Barracks":
                if self.if_placed == False:
                    self.rect.center = self.position = pygame.mouse.get_pos()
                    self.positionx, self.positiony = self.position
                    self.rect.center = self.position
                    if pygame.mouse.get_pressed()[0] == True and mouse_button_state.mouse_1 == 0:
                        self.if_placed = True
                else:
                    pass
        if self in mouse_button_state.mouse_rect_building_group:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)




class Units(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        self.type = type
        self.image = sheet_1.get_image_name("medievalUnit_07.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mouse_movement_group = False
        self.if_collide = False
        self.x_speed = 0
        self.y_speed = 0

        self.spawn_position = (0,0)
        if self.type == "Worker":

            for building in buildings_group:
                if building.type == "Base":
                    self.spawn_position = building.rect.midbottom
            self.image = sheet_1.get_image_name("medievalUnit_07.png").convert_alpha()
            self.rect = self.image.get_rect(center = (self.spawn_position))
            self.where_to_move_x = self.rect.centerx
            self.where_to_move_y = self.rect.centery



    def update(self):
        self.unit_movement()


    #This function arranges unnits chosen by player in square formation
    def click_mouse_movement(self):

        rows = int(math.sqrt(len(mouse_button_state.mouse_rect_unit_group)))
        columns = int(len(mouse_button_state.mouse_rect_unit_group)/rows)
        which_column = 0
        where_x, where_y = pygame.mouse.get_pos()

        for sprites in mouse_button_state.mouse_rect_unit_group:
            sprites.where_to_move_x = where_x
            sprites.where_to_move_y = where_y
            where_x += 32
            which_column += 1
            if which_column == columns:
                where_x -= (32 * which_column)
                where_y += 32
                which_column = 0

            sprites.movement = True
    #Check if unit is in destination given by other functions
    #if not it moves them slowly to that posision
    def where_to_move(self):
        if self.where_to_move_y == self.rect.y and self.where_to_move_x == self.rect.centerx:
            self.movement = False
        else:
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


    def unit_movement(self):

        global move
        if self in mouse_button_state.mouse_rect_unit_group:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
            if pygame.mouse.get_pressed()[2] == False:
                self.mouse_movement_group = True

        if self.mouse_movement_group == True:
            if pygame.mouse.get_pressed()[2] == True:
                if move:
                    self.click_mouse_movement()
                    move = False
            if pygame.mouse.get_pressed()[2] == False:
                move = True
            if pygame.mouse.get_pressed()[0] == True:
                self.mouse_movement_group = False
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        self.where_to_move()


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
            mouse_button_state.mouse_rect_unit_group = pygame.sprite.spritecollide(self, units_group, dokill=False)
            mouse_button_state.mouse_rect_building_group = pygame.sprite.spritecollide(self, buildings_group, dokill=False)

        else:
            self.rect.update((2,2),(1,1))




class UnitsSelected(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()



move = True
#Nazwa i wielkosc ekranu aplikacji
pygame.init()
pygame.display.set_caption("siemaneczko")
screen = pygame.display.set_mode((1600, 800))

current_recouces = Resources()
clock = pygame.time.Clock()
#Sprite Sheets
sheet_1 = SpriteSheet("graphics/Spritesheet/medievalRTS_spritesheet.png", "graphics/Spritesheet/medievalRTS_spritesheet.xml")
sheet_2 = SpriteSheet("graphics/Spritesheet/medievalRTS_spritesheet.png", "graphics/Spritesheet/medievalRTS_spritesheet.xml")


#Stałe
running = True

cord_1 = (0,0)

camera_group = pygame.sprite.Group()

interface_draw = Interface()
mouse_button_state = MousePropertier()
#sprite groups
mouse_group = pygame.sprite.GroupSingle()
mouse_group.add(Mouse())

units_group = pygame.sprite.Group()

buildings_group = pygame.sprite.Group()
buildings_group.add(Buildings("Base",pygame.mouse.get_pos()))

test_font = pygame.font.Font('Fonts/Pixeltype.ttf',12)

recource_bar_group = pygame.sprite.Group()
interface_draw.recousrce_bar()

base_interface_group = pygame.sprite.Group()



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

                cord_1 = pygame.mouse.get_pos()
                mouse_button_state.mouse_1 = 0
            if pygame.mouse.get_pressed()[1] == True:
                mouse_button_state.mouse_2 = 0
            if pygame.mouse.get_pressed()[2] == True:
                mouse_button_state.mouse_3 = 0
        if event.type == pygame.MOUSEBUTTONUP:
            pass



    buildings_group.draw(screen)
    buildings_group.update()

    units_group.draw(screen)
    units_group.update()

    base_interface_group.draw(screen)
    base_interface_group.update()

    recource_bar_group.draw(screen)
    recource_bar_group.update()




    mouse_group.update()



    pygame.display.update()
    clock.tick(60)
pygame.quit()
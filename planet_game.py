import pygame

width = 360
height = 600
screen_size = [width, height]
screen = pygame.display.set_mode(screen_size)
#In pygame module we are calling set_mode method which is in display class
#set_mode method is for setting the size of our game ie, the dimesnions of boundaries of our game which is visible on mobile or computer screen_size
#we are using a variable screen which helps in modifying the charectes on the screen
background = pygame.image.load('background.png')
#here we have uploaded the image which would we visisble on the screen. Now to display it, we have to transfer the image as a block. Hence we call it as BLIT= BLock Image Transfer.
#This is the method that we call to diaplay the image. In order to display the image, we need 2 variables- image, starting coordinates=[0,0]

#loading planet
planets =['p_one.png','p_two.png','p_three.png']
p_index =0
planet = pygame.image.load(planets[p_index])
planet_x=140
move_direction='right'

#load spaceship
spaceship=pygame.image.load('spaceship.png')

#load bullets
bullet=pygame.image.load('bullet.png')
bullet_y = 50
fired = False

keep_alive=True
clock = pygame.time.Clock()

while keep_alive:
#calling the get_press function
#Checking for spacebar press
#when user presses space bar, user can fire the bullet
  pygame.event.get()
  keys=pygame.key.get_pressed()
  if keys[pygame.K_SPACE]== True:
    fired = True
    #print("Spacebar is pressed")

#animation of bullet
  if fired == True:
    bullet_y = bullet_y - 5
    if bullet_y == 50:
      fired = False
      bullet_y = 500

  screen.blit(background, [0, 0])
  screen.blit(bullet,[180,bullet_y])#for bullet animation
  screen.blit(spaceship,[160,500])
  
  #collision detection
  #motion direction of planet
  if move_direction =='right':
    planet_x = planet_x + 5
    if planet_x == width- 60 :
      move_direction ='left'
  else:
    planet_x = planet_x - 5
    if planet_x == 0:
      move_direction ='right'

  screen.blit(planet,[planet_x,50])#for the planet display(planet dia=60)

  if bullet_y<80 and planet_x>120 and planet_x<180:#(considering the dia of planet)
    p_index= p_index + 1
    if p_index <len(planets):
      planet = pygame.image.load(planets[p_index])
      planet_x = 10
    else:
      print("You Win")
      keep_alive=False
    print('BOOM')

  pygame.display.update()
  clock.tick(60)

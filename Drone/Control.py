import socket
from tello import Tello
import pygame, math, time, sys, os
from ast import literal_eval
import keyboard


def connectToDrone():
    global tello
    tello = Tello()
    tello.connect()
    tello.can_send_rc_control = False
    time.sleep(2)


def droneTakeoff():
    tello.takeoff()
    tello.can_send_rc_control = True


def droneLand():
    tello.land()
    tello.can_send_rc_control = False


def droneController(coords):
    #For each event in the program
    for event in pygame.event.get():

        #If the close button is pressed
        if event.type == pygame.QUIT:
            # raise SystemExit
            pass

        #When a button is pressed down
        elif event.type == pygame.KEYDOWN:
            #When l is pressed
            if event.Key == pygame.K_l:
                #Call land function here
                droneLand()


        #When a button is let go
        elif event.type == pygame.KEYUP:

            #When t is pressed
            if event.key == pygame.K_t:
                #Call take-off function here
                droneTakeoff()

            # #Rotate left
            elif event.key == pygame.K_a:
                if(rotation != -30)
                    rotation = -30
                else:
                    rotation = 0
            
            # #Rotate right
            elif event.key == pygame.K_d:
                if(rotation != 30)
                    rotation = 30
                else:
                    rotation = 0


    if tello.can_send_rc_control:
        x = coords[0]
        y = coords[1] - 450
        z = coords[2]

        tello.for_back_velocity = 0
        tello.left_right_velocity = 0
        tello.up_down_velocity = 0

        xSpeed = 0
        ySpeed = 0
        zSpeed = 0

        xzDeadzone = 150.0
        yDeadzone = 100.0

        xzDistance = int(math.sqrt(math.pow(x, 2) + math.pow(z, 2)))

        if xzDistance > xzDeadzone:
            xSpeed = int(x / 40)
            zSpeed = int(z / 40)

        if y > yDeadzone:
            ySpeed = int(y / 30)

        #Sets the tello's velocity 
        tello.left_right_velocity = xSpeed
        tello.for_back_velocity = zSpeed
        tello.up_down_velocity = ySpeed
        tello.yaw_velocity = rotation 

        #Test command to just rotate forever
        # tello.send_rc_control(0, 0, 0, 30)

        #Sends the command to control the drone to the drone
        tello.send_rc_control(tello.left_right_velocity, tello.for_back_velocity, tello.up_down_velocity, tello.yaw_velocity)




class GUI_Support:

    def initDisplay(self, dims):
        pygame.init()
        return pygame.display.set_mode(dims)

    def isQuit(self):
        pass


    #Function to draw and update GUI graphics as it receives new coordinates
    def drawGraphics(self, position, screen, dims):
        handX, handY, handZ = position
        handXVisual = handX
        handZVisual = handZ

        #Centers the X and Z coordinates
        handY = handY * -1
        handX += 400
        handZ += 400
        handY += 850
        width, height = dims
        screen.fill((175, 238, 247))

        #Creates the circles where the hand is located
        circleRadius = 20
        pygame.draw.circle(screen, (0, 0, 0), (handX, handZ), circleRadius)
        pygame.draw.circle(screen, (0, 0, 0), (1050, handY), circleRadius)

        #Draws the circle and lines across the screen
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 150, 5)

        #Vertical Line Separating the XZ and the Y planes
        pygame.draw.line(screen, (0, 0, 0), (800, 0), (800, 800))

        #Y Axis Deadzone
        pygame.draw.line(screen, (0, 0, 0), (800, 300), (1300, 300))
        pygame.draw.line(screen, (0, 0, 0), (800, 500), (1300, 500))

        # RIGHT ARROW
        pygame.draw.line(screen, (0, 0, 0), (550, 410), (620,410), 2)
        pygame.draw.line(screen, (0, 0, 0), (620,410), (620, 425), 2)
        pygame.draw.line(screen, (0, 0, 0), (620, 425), (650, 400), 2)
        pygame.draw.line(screen, (0, 0, 0), (650, 400), (620, 375), 2)
        pygame.draw.line(screen, (0, 0, 0), (620, 375), (620,390), 2)
        pygame.draw.line(screen, (0, 0, 0), (620,390), (550,390), 2)
        pygame.draw.line(screen, (0, 0, 0), (550,390), (550, 410), 2)
        wRight = arrowFont.render(f'Right', True, (0,0,0))
        screen.blit(wRight, (562, 388))

        # LEFT ARROW
        pygame.draw.line(screen, (0, 0, 0), (250, 410), (180,410), 2)
        pygame.draw.line(screen, (0, 0, 0), (180,410), (180, 425), 2)
        pygame.draw.line(screen, (0, 0, 0), (180, 425), (150, 400), 2)
        pygame.draw.line(screen, (0, 0, 0), (150, 400), (180, 375), 2)
        pygame.draw.line(screen, (0, 0, 0), (180, 375), (180,390), 2)
        pygame.draw.line(screen, (0, 0, 0), (180,390), (250,390), 2)
        pygame.draw.line(screen, (0, 0, 0), (250,390), (250, 410), 2)
        wLeft = arrowFont.render(f'Left', True, (0,0,0))
        screen.blit(wLeft, (200, 388))

        # FORWARD ARROW
        pygame.draw.line(screen, (0, 0, 0), (410, 250), (410,180), 2)
        pygame.draw.line(screen, (0, 0, 0), (410,180), (425, 180), 2)
        pygame.draw.line(screen, (0, 0, 0), (425, 180), (400, 150), 2)
        pygame.draw.line(screen, (0, 0, 0), (400, 150), (375, 180), 2)
        pygame.draw.line(screen, (0, 0, 0), (375, 180), (390,180), 2)
        pygame.draw.line(screen, (0, 0, 0), (390,180), (390,250), 2)
        pygame.draw.line(screen, (0, 0, 0), (390,250), (410, 250), 2)
        wF = arrowFont.render(f'F', True, (0,0,0))
        screen.blit(wF, (395, 157))
        wo = arrowFont.render(f'o', True, (0,0,0))
        screen.blit(wo, (395, 169))
        wr = arrowFont.render(f'r', True, (0,0,0))
        screen.blit(wr, (395, 181))
        ww = arrowFont.render(f'w', True, (0,0,0))
        screen.blit(ww, (395, 193))
        wa = arrowFont.render(f'a', True, (0,0,0))
        screen.blit(wa, (395, 205))
        wr = arrowFont.render(f'r', True, (0,0,0))
        screen.blit(wr, (395, 217))
        wd = arrowFont.render(f'd', True, (0,0,0))
        screen.blit(wd, (395, 229))

         # REVERSE ARROW
        pygame.draw.line(screen, (0, 0, 0), (410, 549), (410,620), 2)
        pygame.draw.line(screen, (0, 0, 0), (410,620), (425, 620), 2)
        pygame.draw.line(screen, (0, 0, 0), (425, 620), (400, 650), 2)
        pygame.draw.line(screen, (0, 0, 0), (400, 650), (375, 620), 2)
        pygame.draw.line(screen, (0, 0, 0), (375, 620), (390,620), 2)
        pygame.draw.line(screen, (0, 0, 0), (390,620), (390,549), 2)
        pygame.draw.line(screen, (0, 0, 0), (390,549), (410, 549), 2)
        wR = arrowFont.render(f'R', True, (0,0,0))
        screen.blit(wR, (395, 550))
        we = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(we, (395, 562))
        wv = arrowFont.render(f'v', True, (0,0,0))
        screen.blit(wv, (395, 574))
        we = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(we, (395, 586))
        wr = arrowFont.render(f'r', True, (0,0,0))
        screen.blit(wr, (395, 598))
        ws = arrowFont.render(f's', True, (0,0,0))
        screen.blit(ws, (395, 610))
        we = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(we, (395, 622))

        #DESCEND ARROW
        pygame.draw.line(screen, (0, 0, 0), (840, 505), (840,575), 2)
        pygame.draw.line(screen, (0, 0, 0), (840,575), (855, 575), 2)
        pygame.draw.line(screen, (0, 0, 0), (855, 575), (830, 605), 2)
        pygame.draw.line(screen, (0, 0, 0), (830, 605), (805, 575), 2)
        pygame.draw.line(screen, (0, 0, 0), (805, 575), (820,575), 2)
        pygame.draw.line(screen, (0, 0, 0), (820,575), (820,505), 2)
        pygame.draw.line(screen, (0, 0, 0), (820,505), (840, 505), 2)
        wDescend = arrowFont.render(f'D', True, (0,0,0))
        screen.blit(wDescend, (825, 502))
        wDescend = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(wDescend, (825, 514))
        wDescend = arrowFont.render(f's', True, (0,0,0))
        screen.blit(wDescend, (825, 526))
        wDescend = arrowFont.render(f'c', True, (0,0,0))
        screen.blit(wDescend, (825, 538))
        wDescend = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(wDescend, (825, 550))
        wDescend = arrowFont.render(f'n', True, (0,0,0))
        screen.blit(wDescend, (825, 562))
        wDescend = arrowFont.render(f'd', True, (0,0,0))
        screen.blit(wDescend, (825, 574))

        # ASCEND ARROW
        pygame.draw.line(screen, (0, 0, 0), (840, 295), (840,225), 2)
        pygame.draw.line(screen, (0, 0, 0), (840,225), (855, 225), 2)
        pygame.draw.line(screen, (0, 0, 0), (855, 225), (830, 195), 2)
        pygame.draw.line(screen, (0, 0, 0), (830, 195), (805, 225), 2)
        pygame.draw.line(screen, (0, 0, 0), (805, 225), (820,225), 2)
        pygame.draw.line(screen, (0, 0, 0), (820,225), (820,295), 2)
        pygame.draw.line(screen, (0, 0, 0), (820,295), (840, 295), 2)
        wAscend = arrowFont.render(f'A', True, (0,0,0))
        screen.blit(wAscend, (825, 210))
        wAscend = arrowFont.render(f's', True, (0,0,0))
        screen.blit(wAscend, (825, 222))
        wAscend = arrowFont.render(f'c', True, (0,0,0))
        screen.blit(wAscend, (825, 234))
        wAscend = arrowFont.render(f'e', True, (0,0,0))
        screen.blit(wAscend, (825, 246))
        wAscend = arrowFont.render(f'n', True, (0,0,0))
        screen.blit(wAscend, (825, 258))
        wAscend = arrowFont.render(f'd', True, (0,0,0))
        screen.blit(wAscend, (825, 270))

        #Take off                                _______
        takeOffVisual = myFont.render(f'Take-Off:_____T', True, (0,0,0))
        screen.blit(takeOffVisual, (12,712))

        #Land                             _____________
        landVisual = myFont.render(f'Land:________L', True, (0,0,0))
        screen.blit(landVisual, (12,731))

        # Rotate Left: a                         ___
        rotateLeft = myFont.render(f'Rotate-Left:___A', True, (0,0,0))
        screen.blit(rotateLeft, (12,750))

        # Rotate Right: d                         
        rotateRight = myFont.render(f'Rotate-Right:__D', True, (0,0,0))
        screen.blit(rotateRight, (12,772))

        #box
        pygame.draw.line(screen, (0, 0, 0), (4, 710), (4,797), 2)
        pygame.draw.line(screen, (0, 0, 0), (4, 797), (155,797), 2)
        pygame.draw.line(screen, (0, 0, 0), (155,797), (155,710), 2)
        pygame.draw.line(screen, (0, 0, 0), (155, 710), (4,710), 2)
        
        
        #XZ axis coordinate display
        showXZCoords = myFont.render(f'X,Z Coords:{handXVisual},{handZVisual}', True, (0,0,0))
        screen.blit(showXZCoords, (0, 10))

        #Y-Axis coordinate display
        handYVisual = 400 - handY
        showYCoords = myFont.render(f'Y Coords:{handYVisual}', True, (0,0,0))
        screen.blit(showYCoords, (810, 0))


    #Not sure what this does but crashes without it
    def getTextObjects(self, text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()


#Changes the screen content and updates the display
def guiDisplay(coords):
    guiSupport.drawGraphics(coords, screen, (800, 800))
    pygame.display.update()


#Initializes the socket connection with the hand sensor file and starts the main loop
def connectToSocket():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))
    main()


#Receives coordinates from web socket connection and passes them to the drone and GUI portions of the code
def main():
    try:
        while True:
            
            #Receive 1024 bits of websocket information (Is enough for our purposes)
            full_msg = ''
            msg = s.recv(1024)

            #Full message recieves a decoded string of the server data
            full_msg = msg.decode("utf-8")
            print(full_msg)

            #This is meant to clear the buffer until only one array is left if the buffer is filled too fast
            while(len(full_msg) > 20):
                count += 1

                #Re-receives 1024 bits of websocket information in order to unclog the buffer
                full_msg = ''
                msg = s.recv(1024)
                full_msg = msg.decode("utf-8")
                print(full_msg)
            

            #Turns the string array into an actual array of integers
            coordinateArr = literal_eval(full_msg)

            #Passes the GUI an array of the hand coordinates
            guiDisplay(coordinateArr)

            #Function that takes coordinates and outputs drone commands to the connected drone
            droneController(coordinateArr)



    except Exception as inst:
        print(type(inst)) 
        print(inst) 
        print("Connection closed")
        droneLand()




if __name__ == "__main__":
    #Gets current working directory to pass to the GUI
    path = os.getcwd()

    #A global rotation value that can be used by the GUI to help control the drone
    global rotation
    rotation = 0

    #Connects to the drone object
    connectToDrone()

    #Initializes the pygame GUI window
    guiSupport = GUI_Support()

    #Initializes window to 1300x800 but 800x800 is used for the X and Z portion of the display
    xWidth = 1300
    yHeight = 800
    screen = guiSupport.initDisplay((xWidth, yHeight))

    #Initializing font for coordinate display
    pygame.font.init()
    myFont = pygame.font.SysFont('Comic Sans MS', 22)
    arrowFont = pygame.font.SysFont('Comic Sans MS', 18)

    #Drone icon
    icon = pygame.image.load(path + '\Drone.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Drone Controller')

    #Connect to socket
    connectToSocket()
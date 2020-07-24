import socket
import tello
import pygame, math, time, sys, os
from ast import literal_eval

def connectToDrone():
    global tello
    tello = Tello()
    tello.connect()

def droneTakeoff():
    tello.takeoff()
    time.sleep(10)

def droneController(coords):
    x = coords[0]
    y = coords[1] - 450
    z = coords[2]

    xSpeed = 0
    ySpeed = 0
    zSpeed = 0

    xzDeadzone = 150.0
    yDeadzone = 100.0

    xzDistance = int(math.sqrt(math.pow(x, 2) + math.pow(z, 2)))

    if xzDistance > xzDeadzone:
        xSpeed = int(x / 4)
        zSpeed = int(z / 4)

    if y > yDeadzone:
        ySpeed = int(y / 3)

    tello.send_rc_control(xSpeed, zSpeed, ySpeed, 0)

class GUI_Support:

    def initDisplay(self, dims):
        pygame.init()
        return pygame.display.set_mode(dims)

    def isQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False

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
    print(coords)


#Receives coordinates from web socket connection and passes them to the drone and GUI portions of the code
def main():
    prevVal = (0, 450, 0)
    try:
        while True:
            #Receive 1024 bits of websocket information (Is enough for our purposes)
            full_msg = ''
            msg = s.recv(1024)

            #Full message recieves a decoded string of the server data
            full_msg = msg.decode("utf-8")

            #Turns the string array into an actual array of integers
            coordinateArr = literal_eval(full_msg)

            #If the current coordinates received are a duplicate of the last coordinates, don't send a repeat
            if(coordinateArr != prevVal):

                #Passes the GUI an array of the hand coordinates
                guiDisplay(coordinateArr)

                #To add: Function that takes coordinates and outputs drone commands to the connected drone
                #droneController(coordinateArr)


            prevVal = coordinateArr

    except:
        print("Connection closed")


if __name__ == "__main__":
    #Gets current working directory to pass to the GUI
    path = os.getcwd()

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
    #drone icon

    icon = pygame.image.load(path + '\Drone.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Drone Controller')

    #Initializes the socket connection with the hand sensor file
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))
    main()

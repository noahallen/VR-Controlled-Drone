import socket
import tello
import pygame, math, time, sys, os
from ast import literal_eval

def droneController(coords):
    #Testing function calls

    x = coords[0]
    y = coords[1] - 450
    z = coords[2]
    min = z

    if x < min:
        min = x
    if y < min:
        min = y

    distanceFromCenter = int(math.sqrt(math.pow(x, 2) + math.pow(z, 2) + math.pow(y, 2)))
    trackerXToDrone = int((x / min) * 20)
    trackerYToDrone = int((y / min) * 20)
    trackerZToDrone = int((z / min) * 20)
    trackerToSpeed = int((distanceFromCenter / 7.6) + 9)

    #The speed is calculated this way because the max distance from the center
    #is approximately 566 units away, and to divide it evenly to fit in
    #the tello's range of 10 - 100, every 7.6 units is converted to 1 unit of speed

    tello.go_xyz_speed(trackerXToDrone, trackerYToDrone, trackerZToDrone, trackerToSpeed)

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

        circleRadius = 20
        pygame.draw.circle(screen, (0, 0, 0), (handX, handZ), circleRadius)
        pygame.draw.circle(screen, (0, 0, 0), (1050, handY), circleRadius)

        #Draws the circle and lines across the screen
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 150, 5)

        #Vertical Line
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

        #Y axis coordinate display
        handYVisual = 400 - handY 
        showYCoords = myFont.render(f'Y Coords:{handYVisual}', True, (0,0,0))
        screen.blit(showYCoords, (810, 0))




    def getTextObjects(self, text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()




def guiDisplay(coords):
    guiSupport.drawGraphics(coords, screen, (800, 800))
    pygame.display.update()
    print(coords)


def main():
    prevVal = (0, 450, 0)
    try:
        while True:
            full_msg = ''
            msg = s.recv(1024)

            #Full message recieves a decoded string of the server data
            full_msg = msg.decode("utf-8")

            #Turns the string array into an actual array of integers
            coordinateArr = literal_eval(full_msg)
            if(coordinateArr != prevVal):
                guiDisplay(coordinateArr)
            prevVal = coordinateArr

    except:
        print("Connection closed")


if __name__ == "__main__":
    guiSupport = GUI_Support()
    #Square is 800x800 but 1300 for X for y portion to be displayed
    xWidth = 1300
    yHeight = 800
    screen = guiSupport.initDisplay((xWidth, yHeight))
    #initializing font for coordinate display
    pygame.font.init()
    myFont = pygame.font.SysFont('Comic Sans MS', 22)
    arrowFont = pygame.font.SysFont('Comic Sans MS', 18)
    #drone icon
    icon = pygame.image.load(path + '\Drone.png')
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Drone Controller')

    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))
    main()

################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time, socket


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']

    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        print ("Connected")

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print ("Disconnected")

    def on_exit(self, controller):
        print ("Exited")

    def on_frame(self, controller):

        #Slows down the speed of the output by skipping frames by changing seconds variable
        seconds = .01
        time.sleep(seconds)
        

        # Get the most recent frame and report some basic information
        frame = controller.frame()


        # Get hands
        for hand in frame.hands:

            #Checks if hand is left or right
            #handType = "Left hand" if hand.is_left else "Right hand"

            intPos = []
   
            #Limits the xyz coordinate outputs to a certain range

            #x
            intPos.append(int(hand.palm_position[0]))
            if intPos[0] > 400:
                intPos[0] = 400
            elif intPos[0] < -400:
                intPos[0] = -400

            #y
            intPos.append(int(hand.palm_position[1]))
            if intPos[1] > 850:
                intPos[1] = 850
            elif intPos[1] < 50:
                intPos[1] = 50

            #z
            intPos.append(int(hand.palm_position[2]))
            if intPos[2] > 400:
                intPos[2] = 400
            elif intPos[2] < -400:
                intPos[2] = -400


            print("Coordinates of Palm: ")
            print(intPos)

            #Send information to the connected client, if one isnt there wait for connection of another client
            try:
                clientsocket.send(str(intPos))
            except:
                waitForConnection()


        if not frame.hands.is_empty:
            print ("")

        #If no hands are detected send a zero vector to the client
        if frame.hands.is_empty:
            print("No Hands Detected")
            zeroVector = [0, 450, 0]

            #Send information to the connected client, if one isnt there wait for connection of another client
            try:
                clientsocket.send(str(zeroVector))
            except:
                waitForConnection()


#Initializes hand tracker class
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until "Enter" is pressed
    print ("Press Enter to quit...")
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


#Function to pause program until a websocket connection is made
def waitForConnection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1243))
    s.listen(5)
    print("Listening for a connection")
    global clientsocket
    global address
    clientsocket, address = s.accept()
    print("Connection found")


#Waits for a client to connect to the websocket then proceeds to send coordinates to the client when they connect
if __name__ == "__main__":
    global s
    waitForConnection()
    main()

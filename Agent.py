import turtle
import os
import time

is_paused = False
image_file_bowser = None
image_file_mario = None

class Agent:

    def __init__(self):
        self.__wumpusWorld = [
                 ['','','P',''], # Rooms [1,1] to [4,1]
                 ['','','',''], # Rooms [1,2] to [4,2] 
                 ['W','','P',''], # Rooms [1,3] to [4,3]
                 ['','P','',''],  # Rooms [1,4] to [4,4]
                ] # This is the wumpus world shown in the assignment question.
                  # A different instance of the wumpus world will be used for evaluation.
        self.__curLoc = [1,1]
        self.__isAlive = True
        self.__hasExited = False

    def __FindIndicesForLocation(self,loc):
        x,y = loc
        i,j = y-1, x-1
        return i,j

    def __CheckForPitWumpus(self):
        ww = self.__wumpusWorld
        i,j = self.__FindIndicesForLocation(self.__curLoc)
        if 'P' in ww[i][j] or 'W' in ww[i][j]:
            print(ww[i][j])
            self.__isAlive = False
            print('Agent is DEAD.')
        return self.__isAlive

    def TakeAction(self,action): # The function takes an action and returns whether the Agent is alive
                                # after taking the action.
        validActions = ['Up','Down','Left','Right']
        assert action in validActions, 'Invalid Action.'
        if self.__isAlive == False:
            print('Action cannot be performed. Agent is DEAD. Location:{0}'.format(self.__curLoc))
            return False
        if self.__hasExited == True:
            print('Action cannot be performed. Agent has exited the Wumpus world.'.format(self.__curLoc))
            return False

        index = validActions.index(action)
        validMoves = [[0,1],[0,-1],[-1,0],[1,0]]
        move = validMoves[index]
        newLoc = []
        for v, inc in zip(self.__curLoc,move):
            z = v + inc #increment location index
            z = 4 if z>4 else 1 if z<1 else z #Ensure that index is between 1 and 4
            newLoc.append(z)
        self.__curLoc = newLoc
        print('Action Taken: {0}, Current Location {1}'.format(action,self.__curLoc))
        if self.__curLoc[0]==4 and self.__curLoc[1]==4:
            self.__hasExited=True
        return self.__CheckForPitWumpus()
    
    def __FindAdjacentRooms(self):
        cLoc = self.__curLoc
        validMoves = [[0,1],[0,-1],[-1,0],[1,0]]
        adjRooms = []
        for vM in validMoves:
            room = []
            valid = True
            for v, inc in zip(cLoc,vM):
                z = v + inc
                if z<1 or z>4:
                    valid = False
                    break
                else:
                    room.append(z)
            if valid==True:
                adjRooms.append(room)
        return adjRooms
                
        
    def PerceiveCurrentLocation(self): #This function perceives the current location. 
                                        #It tells whether breeze and stench are present in the current location.
        breeze, stench = False, False
        ww = self.__wumpusWorld
        if self.__isAlive == False:
            print('Agent cannot perceive. Agent is DEAD. Location:{0}'.format(self.__curLoc))
            return [None,None]
        if self.__hasExited == True:
            print('Agent cannot perceive. Agent has exited the Wumpus World.'.format(self.__curLoc))
            return [None,None]

        adjRooms = self.__FindAdjacentRooms()
        for room in adjRooms:
            i,j = self.__FindIndicesForLocation(room)
            if 'P' in ww[i][j]:
                breeze = True
                print('Agent perceive BREEZE. Location:{0}'.format(self.__curLoc))
            if 'W' in ww[i][j]:
                stench = True
                print('Agent perceive STENCH. Location:{0}'.format(self.__curLoc))
        return [breeze,stench]
    
    def FindCurrentLocation(self):
        return self.__curLoc






def startGUI():
    global wn
    global pencil
    global is_paused    
    global image_file_bowser
    global image_file_mario

    # Get the current working directory
    cwd = os.getcwd()

    # Specify the file path of the image file
    image_file_bowser = os.path.join(cwd, "images", "bowser.gif")

    # Register the image as a shape
    turtle.register_shape(image_file_bowser)

    # Specify the file path of the image file
    image_file_mario = os.path.join(cwd, "images", "mario.gif")

    # Register the image as a shape
    turtle.register_shape(image_file_mario)



    wn = turtle.Screen()
    wn.title("Escapa al Wumpus")
    wn.bgcolor("black")

    pencil = turtle.Turtle()
    pencil.speed(0)
    pencil.color("white")
    #pencil.shape("triangle")
    pencil.penup()

    
    wn.listen()
    wn.onkeypress(flag_pause, "p")    





def drawBoard():



    # Set the starting position for drawing the chessboard
    start_x = -200
    start_y = 200
    number_rows = 4
    number_cols = 4

    # Define the size of each square on the chessboard
    square_size = 100

    # Loop to draw the chessboard
    for row in range( number_rows ):
        for col in range( number_cols ):
            x = start_x + col * square_size
            y = start_y - row * square_size
            pencil.penup()
            pencil.goto(x, y)
            pencil.pendown()
            if (row + col) % 2 == 0:
                pencil.fillcolor("white")
            else:
                pencil.fillcolor("coral")
            pencil.begin_fill()
            for i in range(4):
                pencil.forward(square_size)
                pencil.right(90)
            pencil.end_fill()

    # Hide the pencil when finished
    #pencil.hideturtle()

    # Exit on click
    #wn.exitonclick()




def flag_pause():
    global is_paused        
    if is_paused ==True:
        is_paused=False
    if is_paused ==False:
        is_paused=True




def updateHour():
        # Hide the turtle icon
    pencil.hideturtle()

    # Move the turtle to the desired position
    pencil.penup()
    pencil.goto(0, 220)

    # Set the font and size for the text
    pencil.write("Current time: " + time.strftime("%H:%M:%S"), font=("Arial", 16, "normal"))
    time.sleep(0.1)
    pencil.write("                                                                              ")



def showBowser():
    global image_file_bowser    
    pencil.shape(image_file_bowser)
    pencil.shapesize(8, 8)

    # Move the turtle around the screen
    #pencil.forward(100)
    #pencil.left(90)

    # pencil.pencolor("red")
    # pencil.pensize(3)
    # pencil.pendown()
    # pencil.shape("turtle")
    # pencil.stamp()



def showMario():
    global image_file_mario    
    # pencil.shape(image_file_mario)
    # pencil.shapesize(10,10)
    # # Move the turtle around the screen
    # pencil.backward(50)
    # pencil.right(45)




def processGUI():
    global is_paused     

    
    drawBoard()
    while True:
        updateHour()

        #showBowser()

        #showMario()


        if not is_paused:
            pencil.fd(1)
            pencil.lt(1)
        else:
            wn.update()












def main():

    startGUI()
    processGUI()

    # ag = Agent()
    # print('curLoc',ag.FindCurrentLocation())
    # print('Percept [breeze, stench] :',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Right')
    # print('Percept',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Right')
    # print('Percept',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Right')
    # print('Percept',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Up')
    # print('Percept',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Up')
    # print('Percept',ag.PerceiveCurrentLocation())
    # ag.TakeAction('Up')
    # print('Percept',ag.PerceiveCurrentLocation())


if __name__=='__main__':
    main()

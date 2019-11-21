import tkinter
import tkinter.messagebox
import sys

status = {"turn": "X", "X": 0, "O": 0}  # Int Dictionary for total no of win for both player
grid = ['', '', '', '', '', '', '', '', '']  # Grid to represent the status of board
labtext = ["Turn of Player: X", "Player X Wins: 0", "Player O Wins: 0"]
moves = []
statusbar = 0

coords = [{"X1": 0, "Y1": 0, "X2": 149, "Y2": 149}, {"X1": 150, "Y1": 0, "X2": 299, "Y2": 149},
          {"X1": 300, "Y1": 0, "X2": 450, "Y2": 149},
          {"X1": 0, "Y1": 150, "X2": 149, "Y2": 299}, {"X1": 150, "Y1": 150, "X2": 299, "Y2": 299},
          {"X1": 300, "Y1": 150, "X2": 450, "Y2": 299},
          {"X1": 0, "Y1": 300, "X2": 149, "Y2": 450}, {"X1": 150, "Y1": 300, "X2": 299, "Y2": 450},
          {"X1": 300, "Y1": 300, "X2": 450, "Y2": 450}]

top = tkinter.Tk()
C = tkinter.Canvas(top, bg="white", height=480, width=450)
# op.title = "Tic Tok Toe"

x1 = int((top.winfo_screenwidth() - 450) / 2)
y1 = int((top.winfo_screenheight() - 480) / 2)

# Positions the window in the center of the page.
top.geometry("+{}+{}".format(x1, y1))


def drawCanvas():
    # Binding On Click on canvas
    C.bind("<Button-1>", callback)

    # Creating Columns
    line = C.create_line(150, 0, 150, 485)
    line = C.create_line(300, 0, 300, 485)
    # Creating Rows
    line = C.create_line(0, 150, 450, 150)
    line = C.create_line(0, 300, 450, 300)
    # Creating Status Bar
    line = C.create_line(0, 450, 450, 450)

    showstatus()


# Checking in which cell Coordinates of mouse click lies
def callback(event):
    for num in coords:
        # Checking whether or no mouse click lies within the bounds of cell
        if (num["X1"] <= event.x <= num["X2"]) and (num["Y1"] <= event.y <= num["Y2"]):
            playermove(coords.index(num))
            break  # end the loop once cell is found


# Showing Player's Move, switch the turn, updating the status bar, and checking the win or draw conditions.
def playermove(pos):
    global statusbar
    if pos not in moves:
        color = ("Black" if status["turn"] == "X" else "Red")
        C.create_text(coords[pos]["X1"] + 75, coords[pos]["Y1"] + 75, fill=color, font="Times 90 italic bold",
                      text="" + status["turn"])

        # Maintaining the list of played moves
        moves.append(pos)

        # Updating the grid for winCheck
        grid[pos] = status["turn"]

        # Updating the players move
        if status["turn"] == "O":
            status["turn"] = "X"
        else:
            status["turn"] = "O"

        labtext[0] = "Turn of Player: " + status["turn"]
        C.delete(statusbar)
        showstatus()

        if len(moves) >= 5:
            winCheck()


def winCheck():
    win = 0
    if (grid[0] == grid[1] == grid[2] == 'X') or (
            grid[3] == grid[4] == grid[5] == 'X') or (
            grid[6] == grid[7] == grid[8] == 'X') or (
            grid[0] == grid[3] == grid[6] == 'X') or (
            grid[1] == grid[4] == grid[7] == 'X') or (
            grid[2] == grid[5] == grid[8] == 'X') or (
            grid[0] == grid[4] == grid[8] == 'X') or (
            grid[2] == grid[4] == grid[6] == 'X'):
        status['X'] += 1
        win = 'X'
    elif (grid[0] == grid[1] == grid[2] == 'O') or (
            grid[3] == grid[4] == grid[5] == 'O') or (
            grid[6] == grid[7] == grid[8] == 'O') or (
            grid[0] == grid[3] == grid[6] == 'O') or (
            grid[1] == grid[4] == grid[7] == 'O') or (
            grid[2] == grid[5] == grid[8] == 'O') or (
            grid[0] == grid[4] == grid[8] == 'O') or (
            grid[2] == grid[4] == grid[6] == 'O'):
        status['O'] += 1
        win = 'O'

    # to update the status
    C.delete(statusbar)
    showstatus()


    # Showing win dialouge box
    if win != 0:
        ans = tkinter.messagebox.askokcancel("Player " + str(win) + " Won", "Do you want to play again?")
        if ans:
            newGame()
        else:
            sys.exit()
    # In the case of Game Draw
    elif len(moves) == 9:
        ans = tkinter.messagebox.askokcancel("Game Draw", "Do you want to play again?")
        if ans:
            newGame()
        else:
            sys.exit()


def newGame():
    global status, grid, labtext, moves, statusbar
    status["turn"] = "X"
    grid = ['', '', '', '', '', '', '', '', '']  # Grid to represent the status of board
    labtext = ["Turn of Player: X", "Player X Wins: " + str(status["X"]), "Player O Wins: " + str(status["O"])]
    moves.clear()
    statusbar = 0

    # Clearing whole
    C.delete("all")

    # Re-Drawing the whole canvas
    drawCanvas()


def showstatus():
    global statusbar
    labtext[0] = "Turn of Player: " + str(status["turn"])
    labtext[1] = "Player X Wins: " + str(status["X"])
    labtext[2] = "Player O Wins: " + str(status["O"])

    statusbar = C.create_text(220, 465, fill="darkblue", font="Times 12 italic bold",
                              text="" + labtext[0] + "       " + labtext[1] + "       " + labtext[2])


# Start drawing the board and status bar
drawCanvas()

C.pack()
top.mainloop()
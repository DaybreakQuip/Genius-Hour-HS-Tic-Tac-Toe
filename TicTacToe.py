'''
Created on Apr 15, 2017

@author: Ze Hang
'''
from random import random, randint
from time import sleep

class tac:
    def __init__(self):
        self.game = [' ', ' ', ' ', ' ', ' ',' ',' ',' ',' ', ]
    def winning1(self):
        self.counter = 0;
        self.combo1 = [[0,1,2], [0,3,6],[0,4,8], [1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
        for self.x in self.combo1:
            for self.y in self.x:
                if (self.game[self.y] == 'X'):
                    self.counter+=1;
                if (self.counter == 3):
                    return True
            self.counter = 0;
        return False;
    def winning2(self):
        self.counter = 0;
        self.combo1 = [[0,1,2], [0,3,6],[0,4,8], [1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
        for self.x in self.combo1:
            for self.y in self.x:
                if (self.game[self.y] == 'O'):
                    self.counter+=1;
                if (self.counter == 3):
                    return True
            self.counter = 0;
        return False;
    def draw(self):
        for self.x in range(9):
            if (self.game[self.x] == ' '):
                return False
        return True
    def printboard(self):
        print(self.game[0],"|", self.game[1], "|", self.game[2])
        print("----------")
        print(self.game[3],"|", self.game[4], "|", self.game[5])
        print("----------")
        print(self.game[6],"|", self.game[7], "|", self.game[8])
    def chooseboard(self):
        print(1,"|", 2, "|", 3)
        print("----------")
        print(4,"|", 5, "|", 6)
        print("----------")
        print(7,"|", 8, "|", 9)
    def player1(self):
        print("Choose a spot")
        while (True):
            self.temporary = int(input())
            if self.game[self.temporary-1] == ' ':
                self.game[self.temporary-1] = 'X'
                break
            else:
                print("Try Again")
    def player2(self):
        print("Choose a spot")
        while (True):
            self.temporary = int(input())
            if self.game[self.temporary-1] == ' ':
                self.game[self.temporary-1] = 'O'
                break;
            else:
                print("Try Again")
    def computer(self):
        self.counter = 0;
        self.combo1 = [[0,1,2], [0,3,6],[0,4,8], [1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
        for self.x in range(8):
            for self.y in range(3):
                self.tempo = self.combo1[self.x][self.y]
                if (self.game[self.tempo] == "O"):
                    self.counter += 1
                if (self.counter == 2):
                    if (self.y == 2):
                        self.tempo1 = self.combo1[self.x][self.y-1]
                        self.tempo2 = self.combo1[self.x][self.y-2]
                        if (self.game[self.tempo] != "X" and self.game[self.tempo1] != "X" and self.game[self.tempo2] !="X"):
                            self.game[self.tempo1] = "O"
                            self.game[self.tempo2] = "O"
                            self.game[self.tempo] = "O"
                            return
                    elif (self.y == 1):
                        self.tempo1 = self.combo1[self.x][self.y+1]
                        self.tempo2 = self.combo1[self.x][self.y-1]
                        if (self.game[self.tempo] != "X" and self.game[self.tempo1] != "X" and self.game[self.tempo2] !="X"):
                            self.game[self.tempo1] = "O"
                            self.game[self.tempo2] = "O"
                            self.game[self.tempo] = "O"
                            return
                    elif (self.y == 0):
                        self.tempo1 = self.combo1[self.x][self.y+1]
                        self.tempo2 = self.combo1[self.x][self.y+2]
                        if (self.game[self.tempo] != "X" and self.game[self.tempo1] != "X" and self.game[self.tempo2] !="X"):
                            self.game[self.tempo1] = "O"
                            self.game[self.tempo2] = "O"
                            self.game[self.tempo] = "O"
                            return
            self.counter = 0

        self.counter = 0
        for self.x in range(8):
            for self.y in range(3):
                self.tempo = self.combo1[self.x][self.y]
                if (self.game[self.tempo] == "X"):
                    self.counter += 1
                if (self.counter == 2):
                    if (self.y == 2 or self.y == 1 or self.y == 0):
                        for self.z in range(0,3):
                            self.tempo1 = self.combo1[self.x][self.z]
                            if (self.game[self.tempo1] == ' '):
                                self.game[self.tempo1] = 'O'
                                return
            self.counter = 0
        
        self.combo2 = [0,2,6,8]
        while(True):
            self.chance = randint(0,3)
            self.picked = self.combo2[self.chance]
            if (self.game[0] != " " and self.game[2] != " " and self.game[6] != " " and self.game[8] != " "):
                break;
            elif (self.game[self.picked] == ' '):
                self.game[self.picked] = 'O'
                return
            else:
                continue
        if (self.game[5] == ' '):
            self.game[5] = 'O'
            return
        
        self.combo3 = [1,3,5,7]
        while(True):
            self.chance = randint(0,3)
            self.picked = self.combo3[self.chance]
            if (self.game[1] != " " and self.game[3] != " " and self.game[5] != " " and self.game[7] != " "):
                break;
            elif (self.game[self.picked] == ' '):
                self.game[self.picked] = 'O'
                return
            else:
                continue
        return
    def computer2(self):
        self.counter = 0;
        self.combo1 = [[0,1,2], [0,3,6],[0,4,8], [1,4,7],[2,4,6],[2,5,8],[3,4,5],[6,7,8]]
        for self.x in range(8):
            for self.y in range(3):
                self.tempo = self.combo1[self.x][self.y]
                if (self.game[self.tempo] == "X"):
                    self.counter += 1
                if (self.counter == 2):
                    if (self.y == 2):
                        self.tempo1 = self.combo1[self.x][self.y-1]
                        self.tempo2 = self.combo1[self.x][self.y-2]
                        if (self.game[self.tempo] != "O" and self.game[self.tempo1] != "O" and self.game[self.tempo2] !="O"):
                            self.game[self.tempo1] = "X"
                            self.game[self.tempo2] = "X"
                            self.game[self.tempo] = "X"
                            return
                    elif (self.y == 1):
                        self.tempo1 = self.combo1[self.x][self.y+1]
                        self.tempo2 = self.combo1[self.x][self.y-1]
                        if (self.game[self.tempo] != "O" and self.game[self.tempo1] != "O" and self.game[self.tempo2] !="O"):
                            self.game[self.tempo1] = "X"
                            self.game[self.tempo2] = "X"
                            self.game[self.tempo] = "X"
                            return
                    elif (self.y == 0):
                        self.tempo1 = self.combo1[self.x][self.y+1]
                        self.tempo2 = self.combo1[self.x][self.y+2]
                        if (self.game[self.tempo] != "O" and self.game[self.tempo1] != "O" and self.game[self.tempo2] !="O"):
                            self.game[self.tempo1] = "X"
                            self.game[self.tempo2] = "X"
                            self.game[self.tempo] = "X"
                            return
            self.counter = 0

        self.counter = 0
        for self.x in range(8):
            for self.y in range(3):
                self.tempo = self.combo1[self.x][self.y]
                if (self.game[self.tempo] == "O"):
                    self.counter += 1
                if (self.counter == 2):
                    if (self.y == 2 or self.y == 1 or self.y == 0):
                        for self.z in range(0,3):
                            self.tempo1 = self.combo1[self.x][self.z]
                            if (self.game[self.tempo1] == ' '):
                                self.game[self.tempo1] = 'X'
                                return
            self.counter = 0
        
        self.combo2 = [0,2,6,8]
        while(True):
            self.chance = randint(0,3)
            self.picked = self.combo2[self.chance]
            if (self.game[0] != " " and self.game[2] != " " and self.game[6] != " " and self.game[8] != " "):
                break;
            elif (self.game[self.picked] == ' '):
                self.game[self.picked] = 'X'
                return
            else:
                continue
        if (self.game[5] == ' '):
            self.game[5] = 'X'
            return
        
        self.combo3 = [1,3,5,7]
        while(True):
            self.chance = randint(0,3)
            self.picked = self.combo3[self.chance]
            if (self.game[1] != " " and self.game[3] != " " and self.game[5] != " " and self.game[7] != " "):
                break;
            elif (self.game[self.picked] == ' '):
                self.game[self.picked] = 'X'
                return
            else:
                continue
        return
start = randint(0,1)
game = tac()
go = True;
print ("Choose: P (Player v Player) or C (Player v Computer) or CC (Computer v Computer)")
chooseinput = input()
if (chooseinput == "P"):
    while (go):
        if (game.winning1() or game.winning2()):
            print("Winning Board:")
            game.printboard()
            if game.winning1():
                print("Player 1 Wins!")
            elif game.winning2:
                print("Player 2 Wins!")
            go = False
            break
        elif (game.draw()):
            print("Tied Board:")
            game.printboard()
            print("You Tied!")
            go = False
            break
        if (start == 0):
            print("Player 1's Turn")
            game.chooseboard()
            print()
            print()
            game.printboard()
            game.player1()
            print()
            print()
            start = 1
            continue
        elif (start == 1):
            print("Player 2's Turn")
            game.chooseboard()
            print()
            print()
            game.printboard()
            game.player2()
            print()
            print()
            start = 0
            continue
elif (chooseinput == "C"):
    while (go):
        if (game.winning1() or game.winning2()):
            print("Winning Board:")
            game.printboard()
            if game.winning1():
                print("Player 1 Wins!")
            elif game.winning2:
                print("Computer Wins!")
            go = False
            break
        elif (game.draw()):
            print("Tied Board:")
            game.printboard()
            print("You Tied!")
            go = False
            break
        if (start == 0):
            print("Your Turn")
            game.chooseboard()
            print()
            print()
            game.printboard()
            game.player1()
            print()
            print()
            start = 1
            continue
        elif (start == 1):
            print("Computer's Turn")
            game.computer()
            game.printboard()
            print()
            print()
            start = 0
            continue
elif (chooseinput == "CC"):
    while (go):
        if (game.winning1() or game.winning2()):
            print("Winning Board:")
            game.printboard()
            if game.winning1():
                print("Computer 1 Wins!")
            elif game.winning2:
                print("Computer 2 Wins!")
            go = False
            break
        elif (game.draw()):
            print("Tied Board:")
            game.printboard()
            print("They Tied!")
            go = False
            break
        if (start == 0):
            print("Computer 1's Turn")
            game.computer2()
            game.printboard()
            print()
            print()
            sleep(5)
            start = 1
            continue
        elif (start == 1):
            print("Computer 2's Turn")
            game.computer()
            game.printboard()
            print()
            print()
            sleep(5)
            start = 0
            continue
    
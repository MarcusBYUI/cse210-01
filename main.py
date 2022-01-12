from combinations import by_three, by_four
from art import logo
import time
import os
import random

class board:
    
    def __init__(self, number, character):
        """Funtion initializes with the class the needed variables"""
        self.character = character
        self.number = number
        
        self.rows = []
        self.columns = []
        self.count = 0
        
        
        self.user = []
        self.computer = []
        
        
    def layout(self):
        """The layout funtion generates a board for the user bassed on the size the user selects"""
        
        for i in range(1, self.number*self.number+1):
            self.rows.append(i)
            #rows.append("|")
            
            self.count += 1
            if self.count == self.number:
                
                self.columns.append(list(self.rows))
                self.rows = []
                self.count = 0
        
        
    def display(self):
        """The display function is used to display the current game grid to the screen"""
        #This demacates the board horizontally
        demacation = []
        for i in range(self.number *3):
            demacation.append("___")
            
        #This is to print out the board using a well spaced format to boost user experience
        for i in self.columns:
            line = f"{i[0]}".ljust(5), "|".ljust(5), f"{i[1]}".ljust(5), "|".ljust(5), f"{i[2]}"
            
            if len(i) == 4:
                line = f"{i[0]}".ljust(5), "|".ljust(5), f"{i[1]}".ljust(5), "|".ljust(5), f"{i[2]}".ljust(5), "|".ljust(5), f"{i[3]}"
            elif len(i) == 5:
                line = f"{i[0]}".ljust(5), "|".ljust(5), f"{i[1]}".ljust(5), "|".ljust(5), f"{i[2]}".ljust(5), "|".ljust(5), f"{i[3]}".ljust(5), "|".ljust(5), f"{i[4]}"
            elif len(i) == 6:
                 line = f"{i[0]}".ljust(5), "|".ljust(5), f"{i[1]}".ljust(5), "|".ljust(5), f"{i[2]}".ljust(5), "|".ljust(5), f"{i[3]}".ljust(5), "|".ljust(5), f"{i[4]}".ljust(5), "|".ljust(5), f"{i[5]}"
            
            print("".join(line))
            
            print("".join(demacation))    


    def combinations(self):
        """returns win combinations from the combination file
            Win combinations is necesary to decide a winner and also to get computer to play"""
        if self.number == 3:
            return by_three
        elif self.number == 4:
            return by_four
    
    
    def modify(self, input, character):
        """The modify function removes the particular tile the user/compiter picks and then replaces it with their character
            then it keeps the removed tile in a list for further opeartions"""
        
        for i in self.columns:
            for j in i:
                if j == input:
                    index = i.index(j)
                    i[index] = character
                    if self.character == character:
                        self.user.append(input)
                    else:
                        self.computer.append(input)

    
    def compare(self):
        """Checks the board after each turn to find a draw or a win"""
        combination_set = self.combinations() 
        count = 0
        # checks if it's draw
        if len(self.user) + len(self.computer) == (self.number * self.number):
            return "Draw"
        
        # checks if user has a complete set
        for i in combination_set:
            for j in i:
                if j in self.user:
                    count += 1
            if count == self.number:
                return "user won"
            else:
                count = 0
                    
        # checks if computer has a complete set
        count = 0
        for i in combination_set:
            for j in i:
                if j in self.computer:
                    count += 1
            if count == self.number:
                return "computer won"
            else:
                count = 0
    
    
    def comp_move(self, difficulty):
        """Function decides computer move based on difficulty choosen between easy and hard
        
            Easy Mode: returns a random number that has not been previosly played but present on the board
            
            Hard Mode: Checks if the computer has an incomplete game to win if not,
                        It checks if the user has a pending game to win then blocks the game, if not
                        It returns a random number like the easy mode"""
        combination_set = self.combinations() 
        #easy mode
        if difficulty == "easy":
            play = False
            while not play:
                move = random.randint(1, (self.number * self.number))            
                if move not in self.user and move not in self.computer:
                    play = True
                    return move
                    
        
        else:
            #i want to check if there is a game where the computer can complete and win

            if len(self.computer) >= 2:
                
                for i in combination_set:
                    new_list = set(i).intersection(self.computer)
                    if len(new_list) >= (self.number - 1):
                        check =  all(item in i for item in new_list)
                        if check is True:
                            for j in i:
                                if j not in self.computer and j not in self.user:
                                    return j
                                
            #i want to check if there is a move the user is currently making that i need to block          
            
            if len(self.user) >= 2:
                for i in combination_set:
                    new_list = set(i).intersection(self.user)
                    if len(new_list) >= (self.number - 1):
                        check =  all(item in i for item in new_list)
                        if check is True:
                            for j in i:
                                if j not in self.computer and j not in self.user:
                                    return j
            
            # Will just play a random move if there is nothing to block or win                               
            play = False
            while not play:
                move = random.randint(1, (self.number * self.number))            
                if move not in self.user and move not in self.computer:
                    play = True
                    return move     
    
    
    def verdict(self):
        """A simple funtion that takes output from the compare funtion then displays the appropriate result to the screen"""
        if self.compare() == "Draw":
            os.system('cls||clear')
            #print logo
            print(logo)
            print()    
            self.display()
            print("Its a Draw!!!")
            return True
        
        elif self.compare() == "user won": 
            os.system('cls||clear')
            #print logo
            print(logo)
            print()     
            self.display()
            print("You win!!!")
            return True

        elif self.compare() == "computer won":
            os.system('cls||clear')   
            #print logo
            print(logo)
            print()  
            self.display()
            print("You Loose!!!")
            return True
        
        else:
            os.system('cls||clear')  
            #print logo
            print(logo)
            print()  
            return False
            
    
def main():
    #print logo
    print(logo)
    print()
    
    try:
        number = int(input("Input the layout type '3 for 3x3','4 for 4x4'. Your options are 3 and 4: "))
        character = input("Which would you prefer.... 'X' or 'O' ....: ").upper()
        difficulty = input("Reply 'easy' For Easy Mode or 'hard' fo Hard Mode: ").lower()
        #input check
        while number < 3 and number > 4:
            print("Layout type is meant to be between 3 and 6")
            number = int(input("Input the layout type '3 for 3x3','4 for 4x4'. Your options are 3 through 6: "))
        #input check    
        while difficulty != "easy" and difficulty != "hard":
            os.system('cls||clear') 
            print("You have made an error")
            difficulty = input("Easy Mode or Hard?.... :").lower()
            
        if character == "X":
            comp_character = "O"
        else:
            comp_character = "X"
        
        #initiating an instance of the game class and a layout based on the user
        game = board(number, character)
        game.layout()
        
        #loop that keeps the game going till a draw or winner is found
        game_end = False
        while not game_end:
            
            game.display()
            user_input = int(input("Reply with a tile number: "))
            #input check
            while user_input < 0 or user_input > (number*number):
                print("Number is put of bounds")
                user_input = int(input("Reply with a tile number: "))
                
            #input check
            while user_input in game.user or user_input in game.computer:
                print("Number is taken")
                user_input = int(input("Reply with a tile number: "))            
                
            #modification of the board called based on inout
            game.modify(user_input, character)
            game_end = game.verdict()
            if game_end == True:
                return
            
            #computer thinks and delays for 2 sec
            print("I am thinking")
            time.sleep(2)

            #computers move based on difficulty is called from the game class
            move = game.comp_move(difficulty)
            game.modify(move, comp_character)
            game_end = game.verdict()
            if game_end == True:
                return
        
    #catch the ValueError type 
    except ValueError as value_err:
        print(type(value_err).__name__, value_err, sep=": ")
        print(f"The amount {value_err} inputed is not valid, \
            \nplease run the program again and try a valid number")    
        
    
    # catch the filenotfounderror type
    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The file  does not exist in this directory \
            \nRun the program again using a file name that exists")
        
    # catch the permissionerror type    
    except PermissionError as perm_err:
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You do not have permission to open the file \
            \nPlease run the program again and use a file within your permission rights")    
        
    
    
if __name__ == '__main__':
    main()
    
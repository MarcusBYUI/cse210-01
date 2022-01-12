from combinations import by_three, by_four
import time
import os
import random

class frame:
    
    def __init__(self, number, character):
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

    
    def compare(self,character):
        combination_set = self.combinations() 
        count = 0
        if len(self.user) + len(self.computer) == (self.number * self.number):
            return "Draw"
        
        for i in combination_set:
            for j in i:
                if j in self.user:
                    count += 1
            if count == self.number:
                return "user won"
            else:
                count = 0
                    
        
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
        combination_set = self.combinations() 
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
        if self.compare(self.character) == "Draw":
            os.system('cls||clear')    
            self.display()
            print("Its a Draw!!!")
            return True
        
        elif self.compare(self.character) == "user won": 
            os.system('cls||clear')    
            self.display()
            print("You win!!!")
            return True

        elif self.compare(self.character) == "computer won":
            os.system('cls||clear')    
            self.display()
            print("You Loose!!!")
            return True
        
        else:
            os.system('cls||clear')    
            return False
            
    
def main():
    
    try:
        number = int(input("Input the layout type '3 for 3x3','4 for 4x4'. Your options are 3 and 4: "))
        character = input("Which would you prefer.... 'X' or 'O' ....: ").upper()
        difficulty = input("Reply 'easy' For Easy Mode or 'hard' fo Hard Mode: ").lower()
        
        while number < 3 and number > 4:
            print("Layout type is meant to be between 3 and 6")
            number = int(input("Input the layout type '3 for 3x3','4 for 4x4'. Your options are 3 through 6: "))
            
        while difficulty != "easy" and difficulty != "hard":
            os.system('cls||clear') 
            print("You have made an error")
            difficulty = input("Easy Mode or Hard?.... :").lower()
            
        if character == "X":
            comp_character = "O"
        else:
            comp_character = "X"
        
        game = frame(number, character)
        game.layout()
        
        game_end = False

        while not game_end:
            
            game.display()
            user_input = int(input("Reply with a tile number: "))
            while user_input < 0 or user_input > (number*number):
                print("Number is put of bounds")
                user_input = int(input("Reply with a tile number: "))
                
            while user_input in game.user or user_input in game.computer:
                print("Number is taken")
                user_input = int(input("Reply with a tile number: "))            
                
            
            game.modify(user_input, character)
            game_end = game.verdict()
            if game_end == True:
                return
            
            
            print("I am thinking")
            time.sleep(2)

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
    
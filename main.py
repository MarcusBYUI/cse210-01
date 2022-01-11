from combinations import by_three, by_four, by_five, by_six
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
        elif self.number == 5:
            return by_five
        elif self.number == 6:
            return by_six
    
    
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
        if self.character == character:
            for i in combination_set:
                for j in i:
                    if j in self.user:
                        count += 1
                if count == self.number:
                    return "user won"
                else:
                    count = 0
                    
        else:
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
        if difficulty == "easy":
            play = False
            while not play:
                move = random.randint(1, (self.number * self.number))            
                if move not in self.user and move not in self.computer:
                    play = True
                    return move
                    
        
        else:
            pass
    
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
    number = int(input("Input the layout type '3 for 3x3','4 for 4x4'. Your options are 3 through 6: "))
    character = input("Which would you prefer.... 'X' or 'O' ....: ").upper()
    play_with = input("Reply 'M' to play with me or 'P' to play with a partner: ").lower()
    difficulty = input("Reply 'easy' For Easy Mode or 'hard' fo Hard Mode: ").lower()
    
    while number < 3 and number > 6:
        print("Layout type is meant to be between 3 and 6")
        number = int(input("Input the layout type '3 for 3x3','4 for 4x4'. Your options are 3 through 6: "))
    
    while play_with != "m" and play_with != "p":
        os.system('cls||clear') 
        print("You have made an error")
        play_with = input("Reply 'm' to play with me or 'p' to play with a partner: ").lower()
        
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
            
        
        game.modify(user_input, character)
        game_end = game.verdict()
        if game_end == True:
            return
        
        
        print("I am thinking")
        time.sleep(2)
        if play_with == "p":
            pass
            game_end = game.verdict()
            if game_end == True:
                return
            
        else:
            move = game.comp_move(difficulty)
            game.modify(move, comp_character)
            game_end = game.verdict()
            if game_end == True:
                return
        
        
        
        
        
        
    
if __name__ == '__main__':
    main()
    
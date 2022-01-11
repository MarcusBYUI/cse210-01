from combinations import by_three, by_four, by_five, by_six
import time
import os

class frame:
    
    def __init__(self):
        self.rows = []
        self.columns = []
        self.count = 0
        
        self.user = []
        self.computer = []
        
        
    def layout(self, number, character):
        """The layout funtion generates a board for the user bassed on the size the user selects"""
        self.character = character
        if number >= 3 and number <= 6:
            self.number = number
            for i in range(1, number*number+1):
                self.rows.append(i)
                #rows.append("|")
                
                self.count += 1
                if self.count == number:
                    
                    self.columns.append(list(self.rows))
                    self.rows = []
                    self.count = 0

        else:
            print("Layout type is meant to be between 3 and 6")
            number = int(input("Input the layout type '3 for 3x3','4 for 4x4'. Your options are 3 through 6: "))
            
            self.layout(number, self.character)
        
        
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
                if j == character:
                    pass
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
        if self.character == character:
            for i in combination_set:
                for j in i:
                    if j in self.user:
                        count += 1
                if count == 3:
                    return "user won"
                else:
                    count = 0
                    
        else:
            count = 0
            for i in combination_set:
                for j in i:
                    if j in self.computer:
                        count += 1
                if count == 3:
                    return "computer won"
                else:
                    count = 0
    
    
    def comp_move(self, difficulty):
        if difficulty == "easy":
            pass
        
        else:
            pass
    
    
    
def main():
    number = int(input("Input the layout type '3 for 3x3','4 for 4x4'. Your options are 3 through 6: "))
    character = input("Which would you prefer.... 'X' or 'O' ....:").upper()
    
    game = frame()
    game.layout(number, character)
    
    game_end = False

    while not game_end:
        
        game.display()
        user_input = int(input("Reply with a tile number: "))
        while user_input < 0 or user_input > (number*number):
            print("Number is put of bounds")
            user_input = int(input("Reply with a tile number: "))
            
        
        game.modify(user_input, character)
        if game.compare(character) == "user won":
            os.system('cls||clear')    
            game.display()
            print("You win!!!")
            game_end = True
            return
        os.system('cls||clear')    
        game.display()
        
        
        print("I am thinking")
        time.sleep(2)
        
        game.modify(int(input("Comp turn: ")), "O")
        if game.compare("O") == "computer won":
            os.system('cls||clear')    
            game.display()
            print("You Loose!!!")
            game_end = True
            return
        
        
        
        
        
        
    
if __name__ == '__main__':
    main()
    
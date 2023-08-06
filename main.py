class TicTocToe:
    def __init__(self):
        self.current_state = ['.','.','.','.','.','.','.','.','.']
        self.player_turn = 'O'
        self.status = False
        self.result = None        

    def is_valid(self, place):
        if place<0 or place >8:
            return False
        elif self.current_state[place] != '.':
            return False
        else:
            return True

    def check(self):
        # Vertical 
        for i in range(0, 3):
            if (self.current_state[i] != '.' and
                self.current_state[i] == self.current_state[i+3] and
                self.current_state[i+3] == self.current_state[i+6]):
                return (True,self.current_state[i])

        # Horizontal
        if (self.current_state[0] != '.' and
            self.current_state[0] == self.current_state[1] and
            self.current_state[1] == self.current_state[2]):
            return (True,self.current_state[0])
        if (self.current_state[3] != '.' and
            self.current_state[3] == self.current_state[4] and
            self.current_state[4] == self.current_state[5]):
            return (True,self.current_state[3])
        if (self.current_state[6] != '.' and
            self.current_state[6] == self.current_state[7] and
            self.current_state[7] == self.current_state[8]):
            return (True,self.current_state[6])

        # diagonal 
        if (self.current_state[0] != '.' and
            self.current_state[0] == self.current_state[4] and 
            self.current_state[4] == self.current_state[8]):
            return (True,self.current_state[0])
        if (self.current_state[2] != '.' and
            self.current_state[2] == self.current_state[4] and
            self.current_state[4] == self.current_state[6]):
            return (True,self.current_state[2])

        # Not a Terminal State
        for i in range(0, 9):
                if (self.current_state[i] == '.'):
                    return (False,'.')

        # Tie
        return (True,'.')

    def max_alpha_beta(self, alpha, beta):
        max_value = -10
        place = None
        (status,result) = self.check()
        
        if status == True:
            if result == 'O':
                return (-1, 0)
            elif result == 'X':
                return (1, 0)
            elif result == '.':
                return (0, 0)

        for i in range(0, 9):
                if self.current_state[i] == '.':
                    self.current_state[i] = 'X'
                    (m, min_place) = self.min_alpha_beta(alpha, beta)
                    if m > max_value:
                        max_value = m
                        place = i
                       
                    self.current_state[i] = '.'
                    if max_value >= beta:
                        return (max_value, place)

                    if max_value > alpha:
                        alpha = max_value

        return (max_value,place)

    def min_alpha_beta(self, alpha, beta):
        min_value = 10
        place = None

        (status,result) = self.check()

        if status == True:
            if result == 'O':
                return (-1, 0)
            elif result == 'X':
                return (1, 0)
            elif result == '.':
                return (0, 0)

        for i in range(0, 9):
                if self.current_state[i] == '.':
                    self.current_state[i] = 'O'
                    (m, max_place) = self.max_alpha_beta(alpha, beta)
                    if m < min_value:
                        min_value = m
                        place = i
                    self.current_state[i] = '.'

                    if min_value <= alpha:
                        return (min_value, place)

                    if min_value < beta:
                        beta = min_value

        return (min_value, place)

    def play(self):
        while True:
            self.display()            
            (self.status,self.result) = self.check() 

            if self.status == True:
                if self.result == 'X':
                    print('COMPUTER is the Winner!')
                elif self.result == 'O':
                    print('YOU are the Winner!')
                elif self.result == '.':
                    print("No one is our winner! ")
                return

            else:
                # AI's turn
                if self.player_turn == 'X':
                    (m, place) = self.max_alpha_beta(-10, 10)
                    self.current_state[place] = 'X'
                    self.player_turn = 'O'

                # player's turn
                else:
                    while True:
                        place = int(input('Insert the place of O [1...9]: '))
                        place = place - 1

                        if self.is_valid(place):
                            self.current_state[place] = 'O'
                            self.player_turn = 'X'
                            break
                        else:
                            print('The move is not valid! Try again.')

    def display(self): 
        for i in range(0, 9):
            if(i % 3 == 0 and i !=0):
                print()
            print(self.current_state[i], end=" ")
        print()
        print()

def start_game():
    while(True):
        g = TicTocToe()
        g.play()
        n = int(input("Do You want play?(If yes type 1, otherwise print 0.) "))
        if(n==0):
            break
        
if __name__ == "__main__":
    start_game()
# Problem: A farmer wants to take a fox, a chicken, and a bag of grain across a river. He has only one boat with which he can carry one item across the river at once. The only issue is that if the fox and chicken are left unsupervised, the fox will eat the chicken. The same goes for the chicken and the grain. 

# Goal: Write code to simulate the problem. 

# One way the farmer might solve this is to:
 
# Take chicken over
# Return alone
# Take fox over
# Return with chicken 
# Take grain over
# Return alone
# Take chicken over

# isGoal() -> return true when all items on right, false otherwise

# isValid() -> return true when none of the items eats another item, 
#remember fox eats chicken and chicken eats grain

# nextStates() -> return a List of State objects representing all possible next States
# [f, c, g]* [] 
# [c, g] [f]* 
# [f, g] [c]*
# [f, c] [g]* 
# [] [f, c, g]*


class Solution(object):
    def __init__(self, leftbank, rightbank, farmer_on_left):
        self.rightbank = rightbank
        self.leftbank = leftbank
        self.farmer_on_left = farmer_on_left
        
        self.nextStates = {}
        self.isEnd = False

    def isGoal(self):
        if len(self.rightbank) == 3:
            return True
        return False
        
    def isValid(self):
        if self.farmer_on_left:
            temp = self.rightbank
        else:
            temp = self.leftbank
            
        if "Chicken" in temp and "Fox" in temp:
            return False
        elif "Grain" in temp and "Chicken" in temp:
            return False
        else:
            return True
            
    def gameStates(self):
        counter = 1
        if self.farmer_on_left:
            #move with an item
            for item in self.leftbank:
                # copy of current left and right
                temp_left = [elem for elem in self.leftbank]
                temp_right = [elem for elem in self.rightbank]

                # remove from left (item)
                temp_left.remove(item)
                # add to right (item)
                temp_right.append(item)

                # add to list of next states => Solution(new_left, new_right, new_farmer)
                self.nextStates[counter] = (Solution(temp_left,temp_right,not self.farmer_on_left)) 
                counter += 1

        else:
            # move with an item
            for item in self.rightbank:
                # copy of current left and right
                temp_left = [elem for elem in self.leftbank]
                temp_right = [elem for elem in self.rightbank]

                # remove from left (item)
                temp_right.remove(item)
                # add to right (item)
                temp_left.append(item)

                # add to list of next states => Solution(new_left, new_right, new_farmer)
                self.nextStates[counter] = (Solution(temp_left,temp_right,not self.farmer_on_left)) 
                counter += 1
            
        #move without an item     
        self.nextStates[counter] = (Solution(self.leftbank,self.rightbank, not self.farmer_on_left))
        counter += 1
            
        
        return self.nextStates
    
    def chooseState(self, userOption):
        if userOption not in self.nextStates:
            print("Invalid Option, choose again!")
            return
        chosenState = self.nextStates[userOption]
        
        if not chosenState.isValid():
            print("Invalid State!")
            return
        
        if chosenState.isGoal():
            print("Game End!")
            self.isEnd = True
            return
        
        self.leftbank = chosenState.leftbank
        self.rightbank = chosenState.rightbank
        self.farmer_on_left = chosenState.farmer_on_left
        self.nextStates = {}
        
        
         
        
leftbank = ["Fox", "Chicken","Grain"]
rightbank = []
farmer_on_left = True        
riddle = Solution(leftbank,rightbank,farmer_on_left)
gamecounter = 0
while(not riddle.isEnd):
    gamecounter += 1
    print("Current State: leftbank: " + str(riddle.leftbank) + " rightbank: " + str(riddle.rightbank) + " farmer on left side? : " + str(riddle.farmer_on_left))
    nextStates = riddle.gameStates()
    for option,state in nextStates.items():
        print(str(option) + ":  " + "leftbank: " + str(state.leftbank) + " rightbank: " + str(state.rightbank) + " farmer on left side? : " + str(state.farmer_on_left))
    

    chosenOption = input('Enter your choice: ')
    riddle.chooseState(int(chosenOption))
print("Steps to finish the game : " + str(gamecounter))

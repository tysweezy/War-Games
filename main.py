#Just some fun with python
#war-games
#main.py
#Author: Tyler Souza

def main():
    name = raw_input("Enter you name: ")
    print "Welcome", name
    play_game = raw_input("Do you want to play a game? ")
    
    #checks if user say yes your no
    if play_game.lower() == 'yes' and 'YES':
        print "How about a nice game of chess?"
    else:
        print "Ok, would you like to play a game?"
        
    

   

main()
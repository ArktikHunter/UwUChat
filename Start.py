from uwuBotFunc import EngToUwu
from uwuchat import converse


def printOptions():
    """
    Function to print the main options
    We can discuss if this is what you were thinking or whether its more spontaneous
    """
    print()
    print("Choose an option from the list below:")
    print("1. Translate text from english to uwu")
    print("2. Start the chatbot")
    print("3. Quit the application")
    return input(">")

def translator(string): 
    print()
    print(EngToUwu(string))
    print()

def chatbot():
    uwu = True
    print()
    while True:
        message = input("You: ")
        if message == "quit":
            break
        if message == "uwuOff":
            uwu = False
            continue
        if message == "uwuOn":      # toggle for uwu responses, can incorporate into chatbot later
            uwu = True
            continue
        
        if uwu:
            print(EngToUwu(converse(message)))
        else:
            print(converse(message))
    print()


def start():
    """
    A function that opens and closes the chatbot
    we can discuss later whether we need this or not
    """
    print("*****************************************************")
    print("Welcome to Uwu Chat") # we can discuss better names later - this is just a placeholder
    print("*****************************************************")
    print()
    print("type q: to quit specific mode of chatbot") # again 'q:' is just a placeholder, we can discuss later how exactly users will interact with system
    print()


    run = True
    choice = 0
    feature_running = False
    while(run):
        # only print the main options if the user is not interacting with the chatbot or translating text
        if not feature_running:
            choice = printOptions()
            # assume user chooses a valid feature
            feature_running = True

        if choice == "1":
            string = input("Enter text to translate>")
            # translate text; otherwise go back to home screen if user wishes to quit
            if not string == 'q':
                translator(string)
            else:
                feature_running = False


        elif choice == "2":
            chatbot()
            feature_running = False

        elif choice == "3":
            run= False
            print("Thanks for using Uwu Chat")
            print("Goodbye")      

        else:
            # invalid entry
            feature_running = False
            print()
            print("That is not a valid option")
            print()

if __name__ == "__main__":
    start()


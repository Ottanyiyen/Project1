import turtle
import random

# Dictionary mapping for synchronization of each character.
module_map = {
    "a": "moduleA",
    "b": "moduleB",
    "c": "moduleC",
    "d": "moduleD",
    "e": "moduleE",
    "f": "moduleF",
    "g": "moduleG",
    "h": "moduleH",
    "i": "moduleI",
    "j": "moduleJ",
    "k": "moduleK",
    "l": "moduleL",
    "m": "moduleM",
    "n": "moduleN",
    "o": "moduleO",
    "p": "moduleP",
    "q": "moduleQ",
    "r": "moduleR",
    "s": "moduleS",
    "t": "moduleT",
    "u": "moduleU",
    "v": "moduleV",
    "w": "moduleW",
    "x": "moduleX",
    "y": "moduleY",
    "z": "moduleZ"

}


# LogoChooser Class starts
class LogoChooser:

    # Constructor
    def __init__(self, module_name):
        self.module_name = module_name



    # To get  randomly 1 function of 10 different functions in related module.
    def draw_random_logo(self):
        # Clear turtle screen before drawing
        turtle.clearscreen()

        # Error-handling try-except mechanism
        try:
            # Import the module dynamically
            module = __import__(self.module_name)

            # Get a list of available logo functions in the module
            # And logo attributes are called only starts with "draw_logo_" by using dir function.
            logo = [func for func in dir(module) if func.startswith("draw_logo_")]

            if not logo:
                print(f"No logo functions found in {self.module_name}.")
                return

            # Select a random logo function
            get_random_logo = random.choice(logo)

            # Call the chosen logo function with module name
            # getattr (in this case, a function)
            getattr(module, get_random_logo)()


        # This part catches the error of module can't be imported.
        except ImportError:
            print(f"Module {self.module_name} not found.")

        # This part catches the error of function doesn't exist in the module.
        except AttributeError:
            print(f"Failed to call the logo function in {self.module_name}.")


# end


# Class LogoGenerator starts
class LogoGenerator:

    """
    In the main of the code, set to value equals none Constructor
    holds an instance of LogoChooser class,
    the other means to encapsulate within the LogoChooser.
    """
    def __init__(self):
        self.logo_module = None

    # User must enter a character is says that as a function.
    def get_character(self):   
        while True:    
            character = input("Enter a character for the logo (A-Z): ").lower()
            if character in module_map:
                print(f"You entered {character.upper()}")
                return character
            else:
                print("Invalid input. Please enter a single character from A to Z.")


# end



# Main method connect all functions in a function.
def main():
    print("This code design was designed using the Turtle library of Turtle Graphics.")
    print("It is displayed what user enters as a character in terminal to convert as graphic interface.")
    print("INFO: Every specific module of character has 10 different functions.")

    screen = turtle.Screen()
    screen.setup(width=500, height=500)  # Screen size
    screen.title("Letter Generator")  # Window Title

    # Bring the window to the foreground
    try:
        screen.getcanvas().winfo_toplevel().attributes("-topmost", True)

    # If it is not supported, pass to error
    except AttributeError:
        pass

    while True:  # For looping create logos

        # To call LogoGenerator Class
        logo_generate = LogoGenerator()

        # To calling get_character() of LogoGenerator Class to  get character and to use as a char.
        char =  logo_generate.get_character()

        """ 
        To reach the module_map dictinoary make synchronization related char,
        inside LogoChooser class constructor. 
        And equals to LogoChooser class constructor as a LogoGenerator itself class fake constructor object to use it.    
        """
        logo_generate.logo_module =  LogoChooser(module_map[char])


        # End of the period, to call draw_random_logo function before we've declared thing one step behind.
        logo_generate.logo_module.draw_random_logo()



        while True:  # For looping choices

            choice = input("Do you want to continue to generate new logos ? (Y for Yes / N for No) : ").lower()
            if choice == "y":
                break

            elif choice == "n":
                print("The program has been successfully terminated.")
                turtle.bye()  # Close the turtle window
                exit()  # Exit the entire program

            else:
                print("Invalid input. Please enter Y or N.")


"""
  Checks the module name, if true related function is being run directly.
  When the script is executed directly, main() is called to run the primary logic.
  Evaluates whether the script is being run directly. 
"""
if __name__ == "__main__":
    main()


class Animal:
    def speak(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks.")

class Cat(Animal):
    def speak(self):
        print("The cat meows.")

def get_animal_sound(animal_type):
    try:
        # Attempt to create an instance of the specified animal type
        animal = globals()[animal_type]()
        animal.speak()
    except KeyError:
        print(f"ClassNotFoundException: The class '{animal_type}' does not exist.")
    except AttributeError:
        print(f"ClassNotFoundException: The class '{animal_type}' does not have a 'speak' method.")

def main():
    print("Enter the animal type (Dog, Cat, or Pig) or 'exit' to quit:")
    while True:
        try:
            animal_type = input("Animal type: ")
            if animal_type.lower() == "exit":
                break
            get_animal_sound(animal_type)
        except EOFError:
            print("\nEOFError: End of File reached. Exiting the program.")
            break

if __name__ == "__main__":
    main()


# Entering "Dog" or "Cat" creates an instance of the corresponding class and calls the speak() method.
# Entering "Pig" raises a ClassNotFoundException because the "Pig" class does not exist.
# Entering "exit" breaks the loop and exits the program.
# If you press Ctrl+D (or Ctrl+Z on Windows) without entering any input, it will raise an EOFError and exit the program.


# Sure, let’s break down the code step by step:

# Class Definitions
# python
# Copy code
# class Animal:
#     def speak(self):
#         print("The animal makes a sound.")
# class Animal: defines a base class Animal.
# def speak(self): defines a method speak within the Animal class.
# print("The animal makes a sound.") is the implementation of the speak method, which outputs a generic message for any animal.
# python
# Copy code
# class Dog(Animal):
#     def speak(self):
#         print("The dog barks.")
# class Dog(Animal): defines a subclass Dog that inherits from Animal.
# def speak(self): overrides the speak method from the Animal class.
# print("The dog barks.") outputs a message specific to Dog when speak is called.
# python
# Copy code
# class Cat(Animal):
#     def speak(self):
#         print("The cat meows.")
# class Cat(Animal): defines another subclass Cat that inherits from Animal.
# def speak(self): overrides the speak method from the Animal class.
# print("The cat meows.") outputs a message specific to Cat when speak is called.
# Function to Get Animal Sound
# python
# Copy code
# def get_animal_sound(animal_type):
#     try:
#         # Attempt to create an instance of the specified animal type
#         animal = globals()[animal_type]()
#         animal.speak()
#     except KeyError:
#         print(f"ClassNotFoundException: The class '{animal_type}' does not exist.")
#     except AttributeError:
#         print(f"ClassNotFoundException: The class '{animal_type}' does not have a 'speak' method.")
# def get_animal_sound(animal_type): defines a function that takes a string animal_type as an argument.
# animal = globals()[animal_type]() tries to create an instance of a class named animal_type using the globals() dictionary, which contains all global variables, including class definitions.
# animal.speak() calls the speak method of the created animal instance.
# except KeyError: handles the case where animal_type is not a valid class name in the globals() dictionary. It prints an error message indicating that the class does not exist.
# except AttributeError: handles the case where the class does not have a speak method. It prints an error message indicating that the class does not have the expected method.
# Main Function
# python
# Copy code
# def main():
#     print("Enter the animal type (Dog, Cat, or Pig) or 'exit' to quit:")
#     while True:
#         try:
#             animal_type = input("Animal type: ")
#             if animal_type.lower() == "exit":
#                 break
#             get_animal_sound(animal_type)
#         except EOFError:
#             print("\nEOFError: End of File reached. Exiting the program.")
#             break
# def main(): defines the main function of the program.
# print("Enter the animal type (Dog, Cat, or Pig) or 'exit' to quit:") prompts the user to enter an animal type or 'exit' to quit.
# while True: starts an infinite loop to continuously prompt the user for input.
# animal_type = input("Animal type: ") takes input from the user.
# if animal_type.lower() == "exit": checks if the user input is 'exit' (case-insensitive). If so, the loop is broken, and the program will terminate.
# get_animal_sound(animal_type) calls the function to process the user’s input.
# except EOFError: catches the EOFError which occurs if the end of the input stream is reached (e.g., if the user presses Ctrl+D or Ctrl+Z). It prints a message and breaks the loop to exit the program.
# Execution
# python
# Copy code
# if __name__ == "__main__":
#     main()
# This condition checks if the script is being run directly (not imported as a module). If it is, it calls the main() function to start the program.
# Summary
# The script defines a base class Animal and two subclasses Dog and Cat, each with a specific speak method.
# It provides a function get_animal_sound to instantiate the specified class and call its speak method.
# The main function repeatedly prompts the user to enter an animal type or 'exit', handles potential errors, and calls get_animal_sound accordingly.
# The script is designed to handle different user inputs and gracefully exit on errors or when requested.







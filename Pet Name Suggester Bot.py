import random
def get_pet_type():
    while True:
        pet_type = input("What type of pet do you have? (Dog/Cat/Rabbit/Bird): ").strip().lower()
        if pet_type in ["dog", "cat", "rabbit", "bird"]:
            return pet_type
        else:
            print("Oops! Please enter a valid pet type: Dog, Cat, Rabbit, or Bird.")

def suggest_name(pet_type):
    pet_names = {
        "dog": ["Bruno", "Max", "Daisy"],
        "cat": ["Luna", "Kitty", "Simba"],
        "rabbit": ["Fluffy", "Thumper", "Snowy"],
        "bird": ["Sky", "Tweety", "Coco"]
    }
    return random.choice(pet_names[pet_type])

def main():
    print("Welcome to the Pet Name Suggester Bot! 🐾")
    
    while True:
        pet_type = get_pet_type()
        name = suggest_name(pet_type)
        print(f"How about the name: {name}?")

        another = input("Do you want another name suggestion? (Yes/No): ").strip().lower()
        if another != "yes":
            print("Thanks for using the Pet Name Suggester Bot! Have a great day! 🐶🐱🐰🐦")
            break

if __name__ == "__main__":
    main()

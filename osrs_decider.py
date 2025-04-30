import random
import time
import sys

# List of options for different variables for penalties and tasks
raids = ["ToB", "ToA", "CoX"]
bosses = ["Duke", "Zulrah", "Bandos", "Vorkath", "Artio", "Muspah", "Mole", "Vardorvis", "Huey", "Titans"]
choices = ["Skilling", "Boss", "Raid", "Slayer", "GET THAT WARHAMMER", "Extra bloodshard?", "Corrupted Gauntlet"]
penalties = ["Tell Joe he's handsome"]

# User input to kick off function
user_input = input("What's the matter stupid, don't know what to do?: ")

# If the user input is anything besides "Yes"
if user_input.lower() != "yes":
    print("Then what the hell are you using this for??")
    sys.exit()

time.sleep(0.6)
print("What would you like to do?:")
time.sleep(0.5)
print("!new: to roll a new task")
time.sleep(0.5)
decision_input = input("Choice: ")

if decision_input.lower() == "!new":
    
    time.sleep(0.5)
    
    # function to add a little flair to make it look like it's loading
    def loading_flair(text, delay=0.4):
        # Split into main text and the dots
        main_text = text.rstrip('.')
        dots = text[len(main_text):]
        
        # Print the main text immediately
        sys.stdout.write(main_text)
        sys.stdout.flush()
        
        # Print the dots with delay
        for char in dots:
            time.sleep(delay)
            sys.stdout.write(char)
            sys.stdout.flush()

    # creates the illusion of loading if user_input == "yes"
    loading_flair("Calculating Choice....")

    print()

    time.sleep(1)

    # main function to determine choice
    def osrs_pick():
        result = random.choice(choices)
        match result:
            # If the function rolls Boss, added loading flair for effect
            case "Boss":
                chosen_boss = random.choice(bosses)
                print("Bosses rolled:", end=" ")
                loading_flair("Picking Boss....")
                print()
                time.sleep(1.2)
                print(f"Boss to kill is: {chosen_boss}")
                time.sleep(0.8)
                print(f"You must kill {random.randrange(10,50,1)} of {chosen_boss}")
            # If the function rolls Raid, added loading flair for effect  
            case "Raid":
                random_raid = random.choice(raids)
                print("Raids rolled:", end=" ")
                loading_flair("Picking Raid....")
                print()
                time.sleep(1.2)
                print(f"Raid to run is: {random_raid}")
            # Any other choice besides Raid and Boss
            case _:
                    print(f"Your OSRS task is: {result}")
                    time.sleep(0.8)
                    
    osrs_pick()
    time.sleep(0.5)
    print()

    # Function to roll a new task if user chooses to re-roll
    def penalty_picker():
        p_result = random.choice(penalties)
        print("You have the option to re-roll this choice for a penalty")
        time.sleep(1)
        new_input = input("Would you like to re-roll your choice?(Y/N) ")
        # If user chooses Y it will loop penalties and tasks until satisfied
        while new_input.lower() == "y":
            print()
            print("Penalty accepted:", end=" ")
            loading_flair("Rolling penalty....")
            print()
            time.sleep(1)
            print(f"Your penalty is {p_result}")
            time.sleep(1)
            print("Rolling new task", end="")
            loading_flair("....")
            print()
            time.sleep(1)
            osrs_pick()
            new_input = input("Would you like to re-roll your choice?(Y/N) ")
            time.sleep(0.5)
        else:
            print("Good luck, Have fun")
            time.sleep(3)

    penalty_picker()

    # Function to generate a new task and count completed tasks
    def new_task():
        completed_counter = 0
        
        # While any if statements return true, loops creating new tasks until user chooses not to
        while True:
            completed_input = input("Have you completed your task? (Y/N): ")
            time.sleep(0.5)
            # If yes adds to counter for completed tasks and asks to roll a new task
            if completed_input.lower() == "y":
                completed_counter += 1
                time.sleep(0.3)
                print(f"Number of tasks completed: {completed_counter}")
                time.sleep(1)

                new_task_input = input("Would you like a new task? (Y/N): ")
                print()
                # If yes to a new task generates a new task and asks for penalty re-roll
                if new_task_input.lower() == "y":
                    print("Generating new task:", end="")
                    loading_flair("....")
                    print()
                    osrs_pick()
                    time.sleep(0.8)
                    print()
                    penalty_picker()
                    print()
                    time.sleep(2)
                # If no for generating a new task script ends
                else:
                    print("Ending script")
                    sys.exit()
            # If has not been completed yet loops back to ask again until task is completed
            elif completed_input.lower() == "n":
                print("No problem, I will ask again later. Get to it.")
                time.sleep(3)
                print()
            # Safeguard in case any other option besides Y or N is picked
            else:
                print("Please enter Y or N.")
    new_task()


       

     
    
import random
import time
import sys

# List of options for different variables for penalties and tasks
raids = ["ToB", "ToA", "CoX"]
bosses = ["Duke", "Zulrah", "Bandos", "Vorkath", "Artio", "Muspah", "Mole", "Vardorvis", "Huey", "Titans"]
choices = ["Skilling", "Boss", "Raid", "Slayer", "GET THAT WARHAMMER", "Extra bloodshard?", "Corrupted Gauntlet"]

file_name = "osrs_decider_log.txt"
counter_file_name = "osrs_decider_counter.txt"

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
        
def task_saver(input, filename):
    with open(filename, 'w') as f:
         f.write(str(input))
         
def task_loader(filename):
    try:
        with open(filename, 'r') as f:
            read = f.read()
        return read
    except FileNotFoundError:
        return "No saved task found. Use !new to generate one."
    
completed_tasks = int(task_loader(counter_file_name))
        
loading_flair("Booting up OSRS Decider....")
print()
print()
time.sleep(1)
print("Welcome to FishpasteRS's OSRS Task Decider!")
time.sleep(0.8)
print(f"Current number of completed tasks: {completed_tasks}")
print()
time.sleep(0.8)
print("What would you like to do?:")
time.sleep(0.8)
print("!new : to roll a new task")
time.sleep(0.8)
print("!task : to view current task")
time.sleep(0.8)
print()
time.sleep(0.8)
decision_input = input("Choice: ")
print()

# main function to determine choice
def osrs_pick():
    result = random.choice(choices)
    match result:
        # If the function rolls Boss
        case "Boss":
            chosen_boss = random.choice(bosses)
            return f"""Bosses rolled:
Boss to kill is: {chosen_boss}
You must kill {random.randrange(10,50,1)} of {chosen_boss}"""
        # If the function rolls Raid  
        case "Raid":
            random_raid = random.choice(raids)
            return f"""Raids rolled:
Raid to run is: {random_raid}"""
        # Any other choice besides Raid and Boss
        case _:
            return f"""Your OSRS task is: {result}"""
        
def roll_new_task():
    global completed_tasks   
    # While any if statements return true, loops creating new tasks until user chooses not to
    while True:
        completed_input = input("Have you completed your task?(Y/N): ")
        print()
        time.sleep(0.5)
        # If yes adds to counter for completed tasks and asks to roll a new task
        if completed_input.lower() == "y":
            completed_tasks += 1
            time.sleep(0.3)
            print(f"Number of tasks completed: {completed_tasks}")
            task_saver(str(completed_tasks), counter_file_name)
            time.sleep(1)
            new_task_input = input("Would you like a new task?(Y/N): ")
            print()
            # If yes to a new task generates a new task and overwrites old task
            if new_task_input.lower() == "y":
                print("Generating new task:", end="")
                loading_flair("....")
                print()
                time.sleep(1)
                task = osrs_pick()
                task_saver(task, file_name)
                print(task)
                print()
                time.sleep(3)
            # If no for generating a new task script ends
            else:
                print("Ending script")
                sys.exit()
        # If has not been completed yet loops back to ask again until task is completed
        elif completed_input.lower() == "n":
            end_input = input("Would you like to close the decider and report completion later?(Y/N): ")
            if end_input.lower() == "y":
                print("Okay! Please use !task when loading the program again")
                time.sleep(0.8)
                print()
                print("Ending script")
                sys.exit()
            elif end_input.lower() == "n":
                print("No problem, I will check again in a bit.")   
                time.sleep(3)
                print()
        # Safeguard in case any other option besides Y or N is picked
        else:
            print("Please enter Y or N.")
    

if decision_input.lower() == "!new":
    
    time.sleep(0.8)
    
    # creates the illusion of loading if decision_input == "!new"
    loading_flair("Choosing new task....")
    print()
    print()
    time.sleep(1)
    
    task = osrs_pick()
    
    task_saver(task, file_name)
    print("Here is your new task:")
    time.sleep(1)
    print(task)
    print()
    time.sleep(4)
    
    roll_new_task()
    
elif decision_input.lower() == "!task":

    time.sleep(1)

    current_task = task_loader(file_name)
    loading_flair("Loading current task....")
    print()
    time.sleep(1)
    print("This is your current task:")
    time.sleep(1)
    print(current_task)
    time.sleep(4)
    print()

    roll_new_task()


       

     
    
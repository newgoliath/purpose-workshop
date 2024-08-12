# Author: Caleb Miller
# Friendly Reviewer: Judd Maltin
# Innocent Onlooker: Masuda Rahimi

import json


def main_signup():
    print("Welcome to the Purpose Cooperative!")
    while True:
        workshop_choice = get_workshop_choice()
        print("You chose workshop ID number ", workshop_choice)
        signup_info = get_signup_info(workshop_choice)
        print("Sign-up Info:", signup_info)
        confirm = input("Do you want to confirm your sign up? Press Y to confirm or N to cancel: ")
        if confirm == "Y" or confirm == "y":
            save_signup(signup_info)
            print("Thank you for signing up for our", workshop_choice, "workshop!")
            confirm2 = input("would you like to sign up for onother workshop? Press Y to confirm or N to cancel: ")
            if confirm2 == "Y" or confirm2 == "y":
                continue
            else:
                print("good bye")
                break
        else:
            print("good bye")
            break

def save_options_json(options):
    pass
    # write you code to write to the file "workshop_signups.json"
    # here


def read_options_json(file_name):
    file_object = open(file_name, "r")
    return json.load(file_object)

def save_signup(signup_info):
    print("In Save Signup!")
    print("Data I want to save:", signup_info)
    # call the other function to save this data
    # include, as json, the person's name, email, and the workshop ID
    with open('data.json', 'a') as f:
      json.dump(signup_info, f, ensure_ascii=False)


    #file_object = open("data.json",'w', encoding='utf-8')
    #json.dump(signup_info, file_object, ensure_ascii=False, indent=4)

    return



def get_workshop_choice():
    print("Which workshop do you want to sign up for?")

    options = read_options_json("../data/workshop_list.json")

    for workshop in options["workshops"]:
        print(workshop['id'], workshop['name'])

    answer = input()
    return answer

def get_signup_info(workshop_choice):
    answer = {}
    print("What is your name?")

    answer["name"] = input()
    answer["workshop"] = workshop_choice

    print("You told me:")
    print(answer["name"])
    return answer


main_signup()

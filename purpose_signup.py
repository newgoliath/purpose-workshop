def main_signup():
    print("welcome to the purpose makerspace!")
    while True:
        workshop_choice = get_workshop_choice()
        signup_info = get_info(workshop_choice)
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

def read_options(file_name):
    f = open(file_name)
    unstripped = f.readlines()
    result = []
    for item in unstripped:
        new_item = item.strip()
        result.append(new_item)
    return result

def get_workshop_choice():
    print("Wich workshop do you want to sign up for?")

    answer = "workshop"
    return answer

def get_info(workshop_choice):
    info = {}
    return info

def save_signup(signup_info):
    return

main_signup()

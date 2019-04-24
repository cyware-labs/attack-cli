from .attack_navigation import AttackNavigator
import sys
import os



def execute():
    a = AttackNavigator()
    a.initialize()
    while True:
        print('Hello World !!! Select from options provided below :')
        print("Enter 1 to list all Tactics")
        # print("Enter 2 to Search for a Tactic")
        print("Enter 2 to List all Techniques")
        # print("Enter 4 to Search a Technique")
        print("Enter 3 to list all APT groups")
        # print("Enter 6 to search for an APT group")
        print("Enter 4 to exit")
        inputt = int(input("Enter your choice:: "))
        os.system('clear')
        if int(inputt) not in range(1, 5):
            print("Invalid Input. Please try again")
            continue
        if inputt == 1:
            while True:
                print("{:<20} || {:<10} || {:<30} ||".format('Name', 'ID', 'Url'))
                for tactic in a.get_tactics():
                    print("{:<20} || {:<10} || {:<30} ||".format(tactic['name'], tactic['id'], tactic['url']))
                print("Enter 1 to see the details of a Tactic.")
                print("Enter 2 to return to the Main Screen.")
                print("Enter 3 to exit the CLI.")
                try:
                    inputtt = int(input("Enter your choice:: "))
                    os.system('clear')
                except:
                    print("Invalid Input. Please try again")
                    os.system('clear')
                    continue
                if inputtt not in range(1, 4):
                    print("Invalid Input. Please try again")
                    os.system('clear')
                    continue
                if inputtt == 1:
                    input_id = int(input("Please enter the ID of the tactic you wish to see the details of :: "))
                    data = a.get_tactic(input_id)
                    print("Tactic Name")
                    print("-------------------------------------------------")
                    print(data['name'])
                    print("-------------------------------------------------")
                    print("-------------------------------------------------")
                    print("Description")
                    print("-------------------------------------------------")
                    print(data['description'])
                    print("-------------------------------------------------")
                    print("-------------------------------------------------")
                    print("Techniques associated with this Tactic")
                    print("-------------------------------------------------")
                    for technique in data['techniques']:
                        print(technique['name'])
                    print("-------------------------------------------------")
                    print("-------------------------------------------------")
                    print("-------------------------------------------------")
                    while True:
                        print("Enter 1 to return to the Previous Screen.")
                        print("Enter 2 to exit the CLI.")
                        inputt = int(input("Enter your choice:: "))
                        os.system('clear')
                        if inputt not in range(1, 3):
                            print("Invalid Input. Please try again")
                            continue
                        if inputt == 1:
                            os.system('clear')
                            break
                        if inputt == 2:
                            os.system('clear')
                            print("Good Bye!")
                if inputtt == 2:
                    os.system('clear')
                    break
                if inputtt == 3:
                    os.system('clear')
                    print("Good Bye!")
        # if inputt == 2:
        #     while True:
        #         search_input = input("Enter the name of tactic you wish to search for ::")
        #         print("{:<20} || {:<10} || {:<30} ||".format('Name', 'ID', 'Url'))
        #         for tactic in a.get_tactics(query=search_input):
        #             print("{:<20} || {:<10} || {:<30} ||".format(tactic['name'], tactic['id'], tactic['url']))
        #         print("Enter 1 to see the details of a Tactic.")
        #         print("Enter 2 to return to the Main Screen.")
        #         print("Enter 3 to exit the CLI.")
        #         try:
        #             inputtt = int(input("Enter your choice:: "))
        #             os.system('clear')
        #         except:
        #             print("Invalid Input. Please try again")
        #             os.system('clear')
        #             continue
        #         if inputtt not in range(1, 4):
        #             print("Invalid Input. Please try again")
        #             os.system('clear')
        #             continue
        #         if inputtt == 1:
        #             input_id = int(input("Please enter the ID of the tactic you wish to see the details of :: "))
        #             data = a.get_tactic(input_id)
        #             print("Tactic Name")
        #             print("-------------------------------------------------")
        #             print(data['name'])
        #             print("-------------------------------------------------")
        #             print("-------------------------------------------------")
        #             print("Description")
        #             print("-------------------------------------------------")
        #             print(data['description'])
        #             print("-------------------------------------------------")
        #             print("-------------------------------------------------")
        #             print("Techniques associated with this Tactic")
        #             print("-------------------------------------------------")
        #             for technique in data['techniques']:
        #                 print(technique['name'])
        #             print("-------------------------------------------------")
        #             print("-------------------------------------------------")
        #             print("-------------------------------------------------")
        #             while True:
        #                 print("Enter 1 to return to the Previous Screen.")
        #                 print("Enter 2 to exit the CLI.")
        #                 inputt = int(input("Enter your choice:: "))
        #                 os.system('clear')
        #                 if inputt not in range(1, 3):
        #                     print("Invalid Input. Please try again")
        #                     continue
        #                 if inputt == 1:
        #                     os.system('clear')
        #                     break
        #                 if inputt == 2:
        #                     os.system('clear')
        #                     print("Good Bye!")
        #                     quit()
        #         if inputtt == 2:
        #             os.system('clear')
        #             break
        #         if inputtt == 3:
        #             os.system('clear')
        #             print("Good Bye!")
        #             quit()
        if inputt == 2:
            while True:
                print("{:<60} || {:<10} ||".format('Name', 'ID'))
                for technique in a.get_techniques():
                    print("{:<60} || {:<10} ||".format(technique['name'], technique['id']))
                print("Enter 1 to see the details of a Technique.")
                print("Enter 2 to return to the Main Screen.")
                print("Enter 3 to exit the CLI.")
                try:
                    inputtt = int(input("Enter your choice:: "))
                    os.system('clear')
                except:
                    print("Invalid Input. Please try again")
                    os.system('clear')
                    continue
                if inputtt not in range(1, 4):
                    print("Invalid Input. Please try again")
                    os.system('clear')
                    continue
                if inputtt == 1:
                    input_id = int(input("Please enter the ID of the technique you wish to see the details of :: "))
                    data = a.get_technique(input_id)
                    print("Technique Name")
                    print("-------------------------------------------------")
                    print(data['name'])
                    print("-------------------------------------------------")
                    print("-------------------------------------------------")
                    print("Description")
                    print("-------------------------------------------------")
                    print(data['description'])
                    print("-------------------------------------------------")
                    print("-------------------------------------------------")
                    if data['tactic']:
                        print("Tactic associated with this Technique")
                        print("-------------------------------------------------")
                        for tactic in data['tactics']:
                            print(tactic['name'])
                        print("-------------------------------------------------")
                        print("-------------------------------------------------")
                        print("-------------------------------------------------")
                    while True:
                        print("Enter 1 to return to the Previous Screen.")
                        print("Enter 2 to exit the CLI.")
                        inputt = int(input("Enter your choice:: "))
                        os.system('clear')
                        if inputt not in range(1, 3):
                            print("Invalid Input. Please try again")
                            continue
                        if inputt == 1:
                            os.system('clear')
                            break
                        if inputt == 2:
                            os.system('clear')
                            print("Good Bye!")
                            quit()
                if inputtt == 2:
                    os.system('clear')
                    break
                if inputtt == 3:
                    os.system('clear')
                    print("Good Bye!")
                    quit()
        if inputt == 3:
            while True:
                print("{:<60} || {:<10} ||".format('Name', 'ID'))
                for apt in a.get_apts():
                    print("{:<60} || {:<10} ||".format(apt['name'], apt['id']))
                print("Enter 1 to see the details of an APT group.")
                print("Enter 2 to return to the Main Screen.")
                print("Enter 3 to exit the CLI.")
                try:
                    inputt = int(input("Enter your choice:: "))
                    os.system('clear')
                except:
                    print("Invalid Input. Please try again")
                    os.system('clear')
                    continue
                if inputt not in range(1, 4):
                    print("Invalid Input. Please try again")
                    os.system('clear')
                    continue
                if inputt == 1:
                    input_id = int(input("Please enter the ID of the APT group you wish to see the details of :: "))
                    data = a.get_apt(input_id)
                    print("Technique Name")
                    print("-------------------------------------------------")
                    print(data['name'])
                    print("-------------------------------------------------")
                    print("-------------------------------------------------")
                    print("Description")
                    print("-------------------------------------------------")
                    print(data['description'])
                    print("-------------------------------------------------")
                    print("-------------------------------------------------")
                    if data['techniques']:
                        print("Tactic associated with this Technique")
                        print("-------------------------------------------------")
                        for technique in data['techniques']:
                            print(technique['name'])
                        print("-------------------------------------------------")
                        print("-------------------------------------------------")
                        print("-------------------------------------------------")
                    while True:
                        print("Enter 1 to return to the Previous Screen.")
                        print("Enter 2 to exit the CLI.")
                        inputt = int(input("Enter your choice:: "))
                        os.system('clear')
                        if inputt not in range(1, 3):
                            print("Invalid Input. Please try again")
                            continue
                        if inputt == 1:
                            os.system('clear')
                            break
                        if inputt == 2:
                            os.system('clear')
                            print("Good Bye!")
                            quit()
                if inputt == 2:
                    os.system('clear')
                    break
                if inputt == 3:
                    os.system('clear')
                    print("Good Bye!")
                    quit()
        if inputt == 4:
            os.system('clear')
            print("Good Bye!")
            quit()
        # print(a.get_apts())
        # print(a.get_apt(0))

from attack_navigation import AttackNavigator

import sys
import os


class Main(object):
    def execute(self):
        a = AttackNavigator()
        a.initialize()
        while True:
            print('Welcome to the World!!!!!')
            print("Enter 1 to list all Tactics")
            print("Enter 2 to Search for a Tactic")
            print("Enter 3 to List all Techniques")
            print("Enter 4 to Search a Technique")
            print("Enter 5 to list all APT groups")
            print("Enter 6 to search for an APT group")
            inputt = int(input("Enter your choice:: "))
            os.system('clear')
            if int(inputt) not in range(1, 7):
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
                                quit()
                    if inputt == 2:
                        os.system('clear')
                        break
                    if inputt == 3:
                        os.system('clear')
                        print("Good Bye!")
                        quit()
            print(a.get_techniques())
            print(a.get_technique(0))
            print(a.get_apts())
            print(a.get_apt(0))


if __name__ == '__main__':
    Main().execute()
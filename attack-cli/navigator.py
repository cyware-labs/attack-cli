from models import AttackNavigator

class Main(object):
    def execute(self):
        print('Welcome to the World!!!!!')
        a = AttackNavigator()
        a.initialize()
        print(a.get_tactics())
        print(a.get_tactic(0))
        print(a.get_techniques())
        print(a.get_technique(0))
        print(a.get_apts())
        print(a.get_apt(0))



if __name__ == '__main__':
    Main().execute()
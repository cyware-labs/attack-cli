from models import AttackNavigator

class Main(object):
    def execute(self):
        print('Welcome to the World!!!!!')
        a = AttackNavigator()
        a.initialize()
        print('Sending you list of tactics')
        print(a.get_tactics())



if __name__ == '__main__':
    Main().execute()
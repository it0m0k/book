class User:

    def __init__(self,name):

        self.name = name
        print("コンストラクタが呼ばれました")

    def hello(self):
        print("Hello "+ self.name)

user = User("Taro")
py = User("python")

user.hello()
py.hello()
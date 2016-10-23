import os


class hello():
    def __init__(self):
        print("init sucessful!")

    def run(self):
        print("hello world!")
        print os.getcwd()


if __name__=="__main__":
    abc=hello()
    abc.run()

"""
magic method
"""
import time


class FooBar:
    """最简单的例子"""

    def __init__(self, sentence):
        self.somevar = sentence


f = FooBar("Testing parameters")
print(f.somevar)


class Bird:
    """鸟例子"""

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaahhhh..")
            self.hungry = False
        else:
            print("I'm full")


b = Bird()
b.eat()
print("--------")
b.eat()


class Songbird(Bird):
    def __init__(self):
        super().__init__()  # 调用超类
        self.sound = "Squawk!"
        self.color = "black"

    def sing(self):
        print(self.sound)


sb = Songbird()
sb.sing()
sb.eat()
sb.eat()

"""
https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
对象转Json字符串
"""
import jsonpickle


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    user = User('Jon Snow', 23)
    print(jsonpickle.dumps(user))
    list_ = [user]
    print(jsonpickle.dumps(list_))


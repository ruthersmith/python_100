'''
    file to play with creating a decorator
'''
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(1)
        print('waited a second')
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print('hello')


if __name__ == '__main__':
    say_hello()

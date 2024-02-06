import time

def delay_decorator(function):
    def wrapper():
        time.sleep(5)
        #some operations
        function()
        #some operations
    return wrapper

def log():
    print("hello")

mylog = delay_decorator(log)
mylog()
import time
current_time = time.time()
#print(current_time) # seconds since Jan 1st, 1970

# Write your code below 👇

def speed_calc_decorator(function):
  def wrapper():
    time_init = time.time()
    function()
    time_final = time.time()
    print(f"{function.__name__} run speed: {time_final-time_init}")
  return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(100000000):
    i * i
fast_function()
slow_function()

import threading
import time
def bomb_timer1():
    print('10sec passed!')
    global timer
    timer = threading.Timer(10, bomb_timer1)
    timer.start()
timer = threading.Timer(1, bomb_timer1)
timer.start()
time.sleep(40)
timer.cancel()
print("You have 50sec left")

def bomb_timer2():
    print('10sec passed!')
    global timer
    timer = threading.Timer(10, bomb_timer2)
    timer.start()
timer = threading.Timer(1, bomb_timer2)
timer.start()
time.sleep(40)
timer.cancel()
print("Game over")
print("YOU FAILED")
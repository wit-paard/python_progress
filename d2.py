# Not necessary library
import time

# Error value text
err = print("n/a")

# Here's an elementary I/O for Python.
print("Hello!")
print("Can you tell me who I'm talking to?")

# And there's "scanf" analog for this PL.
# Also, "sep" is for separator between functions, and "end" shows what symbol should be at the end of every action of function.
name = input("")
print('Oh, so you are ', name, ". Nice to meet you!", sep="")
print('Now I want you to type a number you prefer.')
integer = int(input(""))
print(integer, '... okay, I see.')
time.sleep(3) # kind of delay (needs 'time' library as it seems to)
print("Since you can use your keyboard, I want you to type two integers for my")
print("ULTIMATE"); print ("AND"); print("ASTONISHING"); print("mathematical abilities.")

first_num = int(input(""))
second_num = int(input(""))
print("So you chose ", first_num, "and ", second_num, ".", sep="")
time.sleep(2)
print("And my ONLY right answer is...")
time.sleep(3)
print("...")
time.sleep(1)
print("...")
time.sleep(2.2)
print('"u gay"')
time.sleep(0.5)
print("... WAIT WAIT WAIT NO NO NO!!!!!!!!!")
print("It is:")

try:
    division = first_num / second_num
except ZeroDivisionError:
    print(first_num + second_num, first_num - second_num, first_num * second_num, "YOU DUMB OR SMTH")
print(first_num + second_num, first_num - second_num, first_num * second_num, first_num / second_num)
# It's 2:30 AM GMT+7, I wanna sleep... gn xoxo

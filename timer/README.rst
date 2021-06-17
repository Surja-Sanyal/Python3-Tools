This 'timer' module can be used for timekeeping theoughout the code.

This module is intended to be used as a performance metric for code pieces.

Please include in code with statement "import timer".

Please use timer functions with "timer.timer.<function_name(<function_arguments>)>".

Sample usage is included below in Python3:

#-------------------

#Import timer module
import timer

#Reset timer with current timestamp. Exit timers not displayed.
timer.timer.reset(details_flag = 1)

#Reset timer with current timestamp. Exit timers not displayed.
timer.timer.reset()

for _ in range(5):
	#Split time. Split not displayed.
	timer.timer.split(display = 'OFF')

#Returns total number of splits.
count = timer.timer.count()
print("Total splits:", count)

#Split time. Split displayed.
timer.timer.split(display = 1)

#Split time. Split not displayed.
timer.timer.split()

#Print total number of splits.
#Returns total number of splits.
timer.timer.count(show = 'ON')

#Displays time elapsed after a specific split.
timer.timer.display(split = 2)

#Displays time elapsed after a specific split with custom statement.
timer.timer.display(split = 3, statement = 'Time from third split: ')

#Displays all recorded split timings.
timer.timer.display()

#Displays last recorded split.
timer.timer.last()

#Displays total time elapsed from the first recorded timestamp.
timer.timer.finish()

#-------------------

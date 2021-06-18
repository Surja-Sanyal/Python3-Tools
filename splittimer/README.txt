
This 'splittimer' module can be used for timekeeping theoughout the code.

This module is intended to be used as a performance metric for code pieces.

Please include in code with statement "import splittimer".

Please use splittimer functions with "splittimer.splittimer.<function_name(<function_arguments>)>".

Sample usage is included below in Python3:

#-------------------

#Import splittimer module
import splittimer

#Reset splittimer with current timestamp. Exit timers not displayed.
splittimer.splittimer.reset(details_flag = 1)

#Reset splittimer with current timestamp. Exit timers displayed.
splittimer.splittimer.reset()

for _ in range(5):
	#Split time. Split not displayed.
	splittimer.splittimer.split(display = 'OFF')

#Returns total number of splits.
count = splittimer.splittimer.count()
print("Total splits:", count)

#Split time. Split displayed.
splittimer.splittimer.split(display = 1)

#Split time. Split not displayed.
splittimer.splittimer.split()

#Print total number of splits.
#Returns total number of splits.
splittimer.splittimer.count(show = 'ON')

#Displays time elapsed after a specific split.
splittimer.splittimer.display(split = 2)

#Displays time elapsed after a specific split with custom statement.
splittimer.splittimer.display(split = 3, statement = 'Time from third split: ')

#Displays all recorded split timings.
splittimer.splittimer.display()

#Displays last recorded split.
splittimer.splittimer.last()

#Displays total time elapsed from the first recorded timestamp.
splittimer.splittimer.finish()

#-------------------


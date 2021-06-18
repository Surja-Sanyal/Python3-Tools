
#--------------------------------------------------------------------
#This module can be used for timekeeping theoughout the code.
#Can be used as a performance metric for code pieces.
#Please include in code with statement "import splittimer".
#Please use splittimer functions with 
#"splittimer.splittimer.<function_name(<function_arguments>)>".

#Language   : Python3
#Input      : NA
#Output     : Split timings in code execution
#Author     : Surja Sanyal
#Mail       : hi.surja06@gmail.com
#Created    : 16 JUN 2021
#Modified   : 16 JUN 2021
#--------------------------------------------------------------------


#Import related modules.
import atexit
import datetime

#Class Timer.
class SplitTimer:
    #Initiate self.
    #If details_flag == 0 then details will be displayed (default).
    def __init__(self, details_flag = 0):
        self.set_variables(details_flag)
        self.set_exit()
    
    #Initiate class variables and flags.
    def set_variables(self, details_flag = 0):
        self.details_flag = details_flag
        self.start_times = []
        self.start_times.append(datetime.datetime.now())
    
    #Add exit time display code if details_flag == 0 .
    def set_exit(self):
        if self.details_flag == 0:
            atexit.register(self.total_time)
    
    #Counts the number of splits recorded.
    #Returns the number of splits recorded.
    #Returns the number of splits recorded if str(show).upper() in ['1', 'ON'] .
    def count(self, show = ''):
        total = len(self.start_times)-1
        if str(show).upper() in ['1', 'ON']:
            print("Total {} splits have been recorded.".format(total))
        return total
    
    #Resets the first timestamp recorded.
    #Updates the details_flag, if provided.
    def reset(self, details_flag = 0):
        self.set_variables(details_flag)
        print("Timer reset successfully. Display exit timers: ", "No." if self.details_flag == 1 else "Yes.")
    
    #Shows split timing from last timestamp if str(display).upper() == 'ON' or 1 (default).
    #Saves current timestamp for next split timing.
    def split(self, display = 'ON'):
        current_time = datetime.datetime.now()
        if str(display).upper() in ['1', 'ON']:
            print("Split time {}:".format(len(self.start_times)), current_time - self.start_times[-1])
        self.start_times.append(current_time)
    
    #Displays the split timing or total timing depending on the split value.
    #Displays all split timings if split value not provided or not in range.
    #Displays custom text provided in statement variable.
    #Displays time for code exit if self.details_flag == 0 (default).
    def display(self, split=-1, statement=""):
        if self.details_flag == 1:
            pass
        elif split in range(1, len(self.start_times) + 1):
            if statement == "":
                print("Time elapsed from split ", str(split) + " is ", datetime.datetime.now() - self.start_times[split-1], sep="")
            else:
                print(statement, datetime.datetime.now() - self.start_times[split - 1], sep="")
        else:
            print("Printing all splits: Total = {}".format(len(self.start_times) - 1))
            [print(str(_i + 1) + ".", self.start_times[_i + 1] - self.start_times[_i]) for _i in range(len(self.start_times) - 1)]
    
    #Displays last split timing recorded.
    #Does not record current time for next split recording.
    def last(self):
        print("Last split time: ", datetime.datetime.now() - self.start_times[-1], sep="")
    
    #Displays total time elapsed from the first recorded timestamp.
    #Does not record current time for next split recording.
    def finish(self):
        print("Program Execution Time: ", datetime.datetime.now() - self.start_times[0], sep="")
    
    #Displays total time elaspsed from the first recorded timestamp until object memory deallocation.
    #Displays only when self.details_flag == 0 .
    def __del__(self):
        if self.details_flag == 0:
            print("Memory deallocation time: ", datetime.datetime.now() - self.start_times[0], sep="")
    
    #Displays code exit time.
    def total_time(self):
        self.display(1, "Code exit time: ")

#Instantiate Timer object.
splittimer = SplitTimer()

#Sample code snippets demonstrating package usage.
#Please copy to calling code.

'''
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

'''


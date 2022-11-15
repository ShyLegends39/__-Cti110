# Brief Description: This program work on some employee info and salary,
#  that processes the salary and info then displays it! Will stop if put in None at where the name would go
#  

# CTI-110

# P4HW2 - Salary Calculator

# Kelly Bullard

# November 13, 2022

#

# In Python do this:
# NOTE: Under NEW are new features and updates also some woven in with old features:
# (You can have it either way, however you would just add Hrs to totalRegPay but we will be using regPay for this assignment, okay?!)
# NOTE 2: For inputs does needs to be woven into the the process sections and will pointed out by using this: INPUT/HEREv.
# NEW:
# Input: Ask for the user employee name(emplName) w/ this in the middle of the prompt after or and have \"None\",
# then have them enter user  and hours worked and pay rate(payRate) and (float input for these last two) & them w/ this in the middle of the prompt after did, have:
# + emplName +, but after that in payRate's, make sure to have this: "\'.
# Next it is after that goes through then it will ask you the same things as before and have input opt of "None" in the prompt when doing the user employee name input,
# And having this in there will when you type in will stop it.

# Process: Before all of this you must set the global variables to hold all of the totals for: employees entered, and overtime pay and regular pay and gross pay for all employees.
# Next, put in a while loop(Set while to True and have INPUT/HEREv: emplName, after the line 'while' for that),
# and with a if-else loop that has if emplName == "None": and having the break function, and else: having this that increases employee count 1(w/ +=) and end it & then go to next thing.
# That is having INPUT/HEREv: hoursWork and payRate in that order. Next, set variables to calculate values from input data for that current user employee. Now, add a new if-else loop,
# that if hoursWork is > than 40 (this works w/ that sign this time and sorry for last time)
# then calculute and process with overTime and overTimePay and with regPay and grossPay. Then for else: process and calculate and have just regPay and grossPay.
# Now, end that one and then have the process and calculate for once the loop stops, process them with the number of employees entered(numOfEmp),
# total overtime pay, total regular pay, and total gross pay by adding(+=) from what the global variables has gather from the loop,
# in other words like this: totalOverTimePay += overTimePay.

# Output: And after that have an output for emplName with 'Employee's name: ',
# and then use print('') after & before emplName's output for a space to seperate the next part.
# Next in the output, you have these labels (Hours Worked, Pay Rate, OverTime, OverTime Pay, RegHour Pay, Gross Pay)/w spacing
# for hoursWork, payRate, overTime, overTimePay, regPay, grossPay, and then a line of - (really long), and then the output (w/ float)
# for hoursWork, payRate, overTime, overTimePay, regPay, grossPay w/ the first three having .1f and the last three having .2f
# w/ the last two having $ before this { and lastly with each one .1f or .2f and before that have: <15(w/ first one and the last two), <13(w/ second one and the third one),
# <18(w/ the fourth one), but after the :. So, the they are aline with their labels(also have this print('') for spacing after the prompt).
# After that then have output for whenever "None" is type in and have an ouput
# for print number of employees entered, total overtime pay, total regular pay, and total gross pay(these needs this: f', and { around the variables and just the last three having: $ before
# the { and then after variable within {} have : and .2f, like this: ${totalRegPay:.2f}), and lastly have before this have: print('') for spacing.
# BONUS NOTE: Remember to use the right format and to tab and space when needed?! 
# Sorry for this being so long, I wanted make sure that everything is there, if not, again sorry! I hope this is okay?!?!

#

# Input and more...
# set global variables for:
numOfEmp = 0
totalOverTimePay = 0
totalRegPay = 0  
totalGrossPay = 0 

# Run a loop until user wants to exit
while True:
    emplName = input("Enter employee's name or \"None\" to terminate: ")

    # If name is "None", then it breaks the loop without any more user input
    if emplName == "None":
        break
    else:
        
        # If correct then increase employee count by 1
        numOfEmp += 1
    
    hoursWork = float(input("How many hours did " + emplName + " worked? "))
    payRate = float(input("What did " + emplName + "\'s pay rate? "))
    # For this employee,
    overTime = 0
    overTimePay = 0
    regPay = 0
    grossPay = 0
    
    # Calculate and process
    if hoursWork > 40:
    
        overTime = hoursWork - 40

        overTimePay = overTime * payRate * 1.5

        regPay = 40 * payRate
        
        grossPay = regPay + overTimePay
    else:

        # Processing just regular and gross pay
        regPay = hoursWork * payRate
        grossPay = regPay
 
    # Add over time pay to total over time pay
    totalOverTimePay += overTimePay
    
    # Add regular pay to total regular pay
    totalRegPay += regPay
    
    # Add gross pay to total gross pay
    totalGrossPay += grossPay


    # Output
    print('') # Space
    print('Employee name:  ', emplName)
    print('') # Space
    print('Hours Worked   Pay Rate     OverTime     OverTime Pay      RegHour Pay     Gross Pay       ')
    print('-----------------------------------------------------------------------------------------------')
    print(f'{hoursWork:<15.1f}{payRate:<13.1f}{overTime:<13.1f}{overTimePay:<18.2f}${regPay:<15.2f}${grossPay:<15.2f}')
    print('') # Space 

# Output for when "None" is type in the input for emplName
print('') # Space
print(f'Total number of employees entered:{numOfEmp}')
print(f'Total amount payed for overtime: ${totalOverTimePay:.2f}')
print(f'Total amount payed for regular hours: ${totalRegPay:.2f}')
print(f'Total amount payed in gross: ${totalGrossPay:.2f}')

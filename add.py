'''
Script: add.py
By: L00170964
Purpose: To test all the operators in Arithmetic Operators
Prerequisites: Read lecturer note "Walkthroughs - 1. Assignments and Variables"
Tested: on Python v3.10.7 under Windows 11
Revision History:
Alpha version: 08SEPT22
Notes:
Program to test arithemetic operators in python 
'''
print("Arithmetic Operators")
# Stores user inputs to variable
input_num_1 = int(input("Enter 1st number : "))
input_num_2 = int(input("Enter 2nd number : "))
input_choice = int(input("1. Add \n2. Subtract \n3. Multiply \n4. Divide\n"))
# Control statement to work with the Option selected by user
if input_choice == 1:
    print("Result = ", input_num_1 + input_num_2 )
elif input_choice == 2:
    print("Result = ", input_num_1 - input_num_2 )
elif input_choice == 3:
    print("Result = ", input_num_1 * input_num_2 )
elif input_choice == 4:
    print("Result = ", input_num_1 / input_num_2 )
else:
    print("Wrong choice, Enter 1-4 !!")
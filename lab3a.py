#!/usr/bin/env python3

#Author ID: 154742225

#return_text_value() function
#Definition: create fuction that does not take argument but returns a string

def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting


#return_number_value() function
#Definition: function that does not take argument but returns an number

def return_number_value():
    num1 = 10
    num2 = 5
    num3 = num1 + num2
    return num3


#Main Program

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))





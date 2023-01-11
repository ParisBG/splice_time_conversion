#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:41:39 2022
@author: parisbg

Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

s = '07:05:45PM'
#s = '12:05:45PM'
#Splicing with a starting negative index starts at end of string and grabs only 2 chars
meridiem = s[-2:]
hour = s[:2]
remove_meridiem = len(s)-2

if meridiem == 'PM':
    if int(hour) == 12:
        print( s[:remove_meridiem])
    else:
        new_hour = int(hour) + 12
        print( str(new_hour) + s[2:remove_meridiem]  )      
    
if meridiem == 'AM':
    if int(hour) == 12:
        print( '00' + s[2:remove_meridiem])
    else:
        print( s[:remove_meridiem])


        #00:00:00 - 12am 
    #01:00:00 - 1am
    #02:00:00 - 2am
    #03:00:00 - 3am
    #04:00:00 - 4am
    #05:00:00 - 5am
    #06:00:00 - 6am
    #07:00:00 - 7am
    #08:00:00 - 8am
    #09:00:00 - 9am
    #10:00:00 - 10am
    #11:00:00 - 11am
    
        #12:00:00 - 12pm
    #13:00:00 - 1pm
    #14:00:00 - 2pm
    #15:00:00 - 3pm
    #16:00:00 - 4pm
    #17:00:00 - 5pm
    #18:00:00 - 6pm
    #19:00:00 - 7pm
    #20:00:00 - 8pm
    #21:00:00 - 9pm
    #22:00:00 - 10pm
    #23:00:00 - 11pm
    
    '''
    arr[start:stop]         # items start through stop-1
    arr[start:]             # items start through the rest of the array
    arr[:stop]              # items from the beginning through stop-1
    arr[:]                  # a copy of the whole array
    arr[start:stop:step]    # start through not past stop, by step
    '''
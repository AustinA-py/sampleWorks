stop = "" #assign variable for evaluation
while stop != 'q': #evaluate based on desired input to end program
    try:                                    #try loop to repeat input until valid value is given or program ended
        input1 = input('give number1...')
        val1 = int(input1)
    except ValueError:                      #if input is not a number
        if input1 == 'q':                   #end prorgram if "q"
            stop = 'q'
            print('Program Ended...')
            continue
        else:
            print('Please enter a whole number to continue...') #retry input if not a number and not "q"
            continue
    else:
        pass                                #continue to next input if input is number


    try:
        input2 = input('give number2...')
        if input2 == 'q':
            stop = 'q'
            print('program ended...')
            continue
        else:
            val2 = int(input2)
    except ValueError:
        print('Please enter a whole number to continue...')
        continue
    else:
        pass


    try:                                   #similar try statement to above but with a different flavor for variety
        input3 = input('Enter 1 to add...')
        if input3 == 'q':                  #end program if q
            stop = 'q'
            print('program ended...')
            continue
        elif input3 == '1':                #execute sum if 1
            sum = val1 + val2
            print(f"{input1} + {input2} = {sum}")
        else:                              #manually raising exception if not "q" or "1"
            raise Exception('Invalid input...')
    except Exception as e:                 #when not "q" or "1", try again
        print(e)
        continue
    else:
        pass                               #end of loop, restart

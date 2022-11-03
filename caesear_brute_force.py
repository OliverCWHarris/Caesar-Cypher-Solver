def out_of_bounds_check():                                      #check to see if new ascii number is in the range of capital letter numbers (65-90)
    global shifted
    if shifted>90:                                              #if the new ascii number is equivalent to z or higher (90 is z) then ...
        shifted=shifted-26                                      #subtract 26 from the new ascii number, this has the efect of the dictionary 'wrapping'
        shifted=chr(shifted)                                    #convert the new ascii number to new letter
    
    else:                                                       #if the new ascii number is not larger than z...
        shifted=chr(shifted)                                    #just change the number to a letter (this line is here entirely for line 17's benefit)

def shift(to_shift_letter,shift_by):                            #where the magic happens, this process shifts the letters by the specified amount
    
    global count
    global shifted

    to_shift_ascii=ord(to_shift_letter)                         #sets new variable to ascii value of letter

    if to_shift_ascii==32:                                      #check to see if the letter is a space  (ascii of ' ' is 32)
        shifted=to_shift_ascii                                  #if letter is space then set shifted to ascii value (basicly skips shifting it)
        out_of_bounds_check()                                   #go to line 1
    
    else:                                                       #if the letter is not a space then shift the letter by whatever the shifting value is
        shifted=to_shift_ascii+shift_by                         #does the shifting as said above
        out_of_bounds_check()                                   #go to line 1

    with open('caesar.txt','a') as f:                           #opens text file and appends the shifted letter
        f.write(shifted)
    
    count=count+1                                               #adds 1 to count (count is letter we are going to shift)

global count
count=0

def main():                                                     #the 'brain' of the program, tells the rest of it what to do
    global count
    global input_str
    global input_str_list
    global to_shift_places
    
    input_str=str(input('Enter encoded string\n>'))             #user enters teh encoded string (with spaces)
    input_str=input_str.upper()                                 #makes the string entirly upper case (see above as to why)
    input_str_list=list(input_str)                              #turns that string into a list, youll see why further down

    to_shift_places=1                                           #starting value of amount of places to shift

    for x in range(26):                                         #'master' loop, runs 26 times so shifts letters by all possible combinations
        for i in range(len(input_str_list)):                    #'slave' loop, runs however many times the input list is long
            shift(input_str_list[count], to_shift_places)       #runs the shift program with 2 inputs: the letter (found with count), and the amount of places to shift it (see above)
        else:                                                   #after running as many times as the input is long (ie shifted every letter)...
            with open('caesar.txt','a') as f:                   #we write a new line to the text file, this is done because the next itteration (because of line 45) with append to the file, so we need to start on a new line
                f.write('\n')
                to_shift_places=to_shift_places+1               #adds 1 onto the amount of places to shift, so next runthrough will eg shift 2 instead of 1
        count=0                                                 #once the program has run through the entire input once the count (letter place we are on) is reset to 0, starting us from the begining again
    with open('caesar.txt','a') as f:                           #after running through 26 times (everything is done) we write a new line to the text file, so next time the program is run we can see the split in the output data
        f.write('\n')


main()                                                          #starts the brain, if this is gone then nothing will happen

#EPGDPN XVZNVM RVN VNNVNNDIVOZY JI OCZ ADAOZZIOC JA HVMXC DI MJHZ   this is input data, if everything works correctly somewhere in the output should be a number (in word form)
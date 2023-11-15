def OoB_check(to_check):                                                    #out of bounds check, if ascii value of letter is above 90 (capital z)
    try:                                                                    #it will subtract 26 in order to 'wrap' the list of all capital letters
        if to_check>90:
            to_check-=26
            return(to_check)
        else:
            return(to_check)
    except:
        print('error in OoB_check')
def S_check(to_check):                                                      #space check, if ascii value of letter is 32 (' ')
    try:                                                                    #it will return it imediatly and perform no other
        if to_check==32:                                                    #opperations on it
            return True
        else:
            return False
    except:
        print('error in S_check')
def shift(to_shift,shift_by):                                               #the main part of the programm, acts as the hub for all function calls
    try:
        ascii_shifted=ord(to_shift)
        if S_check(ascii_shifted)==True:
            return(chr(ascii_shifted))
        else:
            ascii_shifted+=shift_by
            return(chr(OoB_check(ascii_shifted)))
    except:
        print('error in shift')
def main(position,shift_by):                                                #main function, takes user input, has the loops to run entire program
    in_str=list(input('Enter encoded string with spaces\n>').upper())       #26 times (26 letters in alphabet = 26 possible shifts) and to run
    for i in range(26):                                                     #as many times as the input is long withing those 26 times
        for j in range(len(in_str)):
            with open('output.txt','a') as f:                               #opens output file and writes shifted letter
                f.write(shift(in_str[position],shift_by))
            position+=1
        with open('output.txt','a') as f:
            f.write('\n')
        position=0
        shift_by+=1
main(0,1)
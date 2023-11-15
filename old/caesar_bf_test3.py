def out_of_bounds_check():
    global shifted
    if shifted>90:
        shifted=shifted-26
        shifted=chr(shifted)
    
    else:
        shifted=chr(shifted)

def shift(to_shift_letter,shift_by):
    
    global count
    global shifted

    to_shift_ascii=ord(to_shift_letter)

    if to_shift_ascii==32:
        shifted=to_shift_ascii
        out_of_bounds_check()
    
    else:
        shifted=to_shift_ascii+shift_by
        out_of_bounds_check()

    with open('caesar.txt','a') as f:
        f.write(shifted)
    
    count=count+1

global count
count=0

def main():
    global count
    global input_str
    global input_str_list
    global to_shift_places

    input_str=str(input('Enter encoded string\n>'))
    input_str=input_str.upper()
    input_str_list=list(input_str)

    to_shift_places=1

    for x in range(26):
        for i in range(len(input_str_list)):
            shift(input_str_list[count], to_shift_places)
        else:
            with open('caesar.txt','a') as f:
                f.write('\n')
                to_shift_places=to_shift_places+1
        count=0
    with open('caesar.txt','a') as f:
        f.write('\n')


main()

#EPGDPN XVZNVM RVN VNNVNNDIVOZY JI OCZ ADAOZZIOC JA HVMXC DI MJHZ
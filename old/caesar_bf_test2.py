def shift(to_shift):
    global count

    input_letter=input_str_list[count]
    old_letter=ord(input_letter)
    new_letter=old_letter+to_shift
    if new_letter>90:
        new_letter=new_letter-26
    new_letter=chr(new_letter)
    count=count+1
    
    with open('caesar.txt','a') as f:
        f.write(new_letter)

input_str=str(input("Enter encoded string\n>"))
input_str=input_str.upper()
to_shift=int(input("Enter number of places to shift\n>"))
input_str_list=list(input_str)
count=0


for i in range(len(input_str_list)):
    shift(to_shift)

#EPGDPN XVZNVM RVN VNNVNNDIVOZY JI OCZ ADAOZZIOC JA HVMXC DI MJHZ
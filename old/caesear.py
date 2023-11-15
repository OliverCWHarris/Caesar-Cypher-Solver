dict=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def shift():                                                    #function to shift 1 letter at a time
    global count1                                               #global variables because otherwise it breaks
    global count2
    letter=input_str_list[count1]                               #grabs the next letter from the list of characters
    to_shift=dict.index(letter)                                 #find letters place in dictory and saves it as a number
    shifted=dict[to_shift+count2]                               #value set as number from original letters number+number of places to shift
    count1=count1+1                                             #adds to the count so next time function is run it will grab the next letter

    f=open('caesar.txt','a')                                    #opens file in append mode
    f.write(shifted)                                            #writes shifted letter to file
    f.close()                                                   #closes file

full_input_str=str(input('Enter entire encoded string\n>'))     #user enteres entire encoded string
shifter=int(input('Enter number of times to shift\n>'))         #user enters how many places forward the shifter will go
input_str_list=list(full_input_str.lower())                     #converets inputed string into a list
x=len(input_str_list)                                           #variable x created with value length of list(from string)
y=x                                                             #second variable used to see when program is finshed running

count1=0
count2=1

for i in range(shifter):                                        #'master' loop, runs entire things as many times as word needs to be shifted
    for i in range(x):                                          #'slave' loop, iterates through list of charaters and shifts them all sequentialy
        shift()                                                 #runns shift function to shift 1 letter at a time and record it in a file
        y=y-1                                                   #second count to check when program is done
        if y==0:                                                #when program is done print out the contents of shifted file
            f=open('caesar.txt','a')                            #writes a line change to file so next time program is run output will be on next line
            f.write('\n')
            f.close()
            y=x

    f=open('caesar.txt','r')
    print(f.read())
    f.close()

    count1=0
    count2=count2+1                                             #adds one to count to shift letters 1 place further eg first time will shift a to b, second time will shift a to c
#current problem: brute force shifts everything by 1 place 26 times, so runs through every sigle possible combination, however it is looking for
#an item in the dict list that doesnt exist eg shift z by 26 places, it looks for item 52, which doesnt exist

from itertools import cycle


dictionary=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dict=cycle(dictionary)

def shift():
    global count1
    global count2
    letter=input_str_list[count1]
    to_shift=dict.index(letter)
    shifted=dict[to_shift+count2]
    count1=count1+1

    f=open('caesar.txt','a')
    f.write(shifted)
    f.close()

full_input_str=str(input('Enter entire encoded string\n>'))
input_str_list=list(full_input_str.lower())
x=len(input_str_list)
y=x

count1=0
count2=1

for i in range(26):
    for i in range(x):
        shift()
        y=y-1
        if y==0:
            f=open('caesar.txt','a')
            f.write('\n')
            f.close()
            y=x

    count1=0
    count2=count2+1
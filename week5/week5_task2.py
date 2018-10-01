#File Transfer
import numpy as np
def check(i,j):
    return True

def check_connected():
    if True:
        print('The network is connected.')
    else:
        print('There are ' + 2 + ' components.')

num = int(input())
network = np.zeros(num)
command = input().split()
while(command[0]!='S'):
    if(command[0]=='I'):
        network[int(command[1])-1,int(command[2])-1]=1
        network[int(command[2])-1,int(command[1])-1]=1
    if(command[0]=='C'):
        if check(int(command[1])-1,int(command[2])-1):
            print('yes')
        else:
            print('no')
    command=input().split()

check_connected()

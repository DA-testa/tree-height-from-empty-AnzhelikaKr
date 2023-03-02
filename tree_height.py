# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Write this function
    max_height = 0
    height=np.zeros(n).astype(int)
    # Your code here
    
    for i in range(n):
        h=0
        j=i
        while(j!=-1):
            if height[j]==0:
                h+=1
            else: 
                h+=height[j]
                break
            j=parents[j]
        height[i]=h
        if h>max_height:
            max_height=h

    return max_height



def main():
    
    # implement input form keyboard and from files
    a = input()
    #n=0
    #parents=[]
    if "i" in a.lower():
        n=int(input())
        string=input().split()
        parents=np.array(string).astype(int)
    elif 'f' in a.lower(): 
        name=input()
        if 'a' not in name:
            with open("./test/"+name, mode='r',encoding="utf8") as fail:
                n=int(fail.readline())
                s=fail.readline()
                parents=np.array(s.split()).astype(int)
    else: 
        print("Wrong format")
        return
    res=compute_height(n,parents)
    print(res)
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))

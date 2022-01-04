#Finds the smallest number which is not in the list and greater than zero 
A=[-1,1,2,5]

def solution(A):
    # write your code in Python 3.6
    new_min=min(A)
    if new_min>0:
      while new_min in A:
        new_min +=1
      print(new_min)
    else:
      new_min=1
      while new_min in A:
        new_min +=1
      print(new_min)
    
        
    
   
solution(A)

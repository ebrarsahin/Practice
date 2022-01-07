#This code convert the given seconds to hours minutes and seconds format

T=7500
def solution(T):
    s=T%60
    m=(T//60)%60
    h=(T//60)//60
    last=str(h)+str("h")+str(m)+str("m")+str(s)+str("s")
    return last

print(solution(T))

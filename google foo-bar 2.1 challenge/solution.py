def solution(l):
    bit=[]
    fibo=[1,1]
    x=0
    while x<=l:
        a=2**x
        bit.append(a)
        if sum(bit)>l:
            break
        x+=1
    y=0
    while y<=l:
        b=fibo[y]+fibo[y+1]
        fibo.append(b)
        if sum(fibo)>l:
            break
        y+=1
    g=len(bit)-len(fibo)
    return abs(g)

print(solution(143))

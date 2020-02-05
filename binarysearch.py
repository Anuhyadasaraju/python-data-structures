pos=-1
def b_s(list,n):
    l=0
    u=len(list)-1
    while l<u:
        m=(l+u)//2
        if list[m]==n:
            globals()['pos']=m
            return True
        else:
            if n<list[m]:
                u=m-1
            else:
                l=m+1
                
    return False
list=[4,7,20,56,97,106]
n=65

if b_s(list,n):
    print("found at",pos+1)
else:
        print("not found")

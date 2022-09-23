def f(l,w):
    for e in w:
        if e.lower()==l.lower():
            return 1
    return -1

l=["RAEHTF","KABRE","CYROTNU","RENEG","OAERELANP"]
w=[["father","hafter","trefah"],["baker","brake","break","kebar"],["country"],["genre","green"],["aeroplane"]]
total=0
for i in range(0,5):
    print("Arrange the letters to form valid word:")
    print(l[i])
    x=input()
    if(f(x,w[i])==1):
        print("Correct")
        total+=1
    else:
        print("Wrong")
        total-=1
print("Net score is",total)







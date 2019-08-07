

if __name__ == '__main__':
    a=input();
    Out={}
    for i in a:
        if i in Out:
            Out[i]+=1
        else:
            Out[i]=1
    print(Out)
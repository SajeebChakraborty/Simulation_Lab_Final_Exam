def LCM(x0,a,c,M,n):

    x=[0]*n
    r=[0]*n

    x[0]=x0

    for i in range(0,n-1):

        x[i+1]=(a*x[i] + c) % M
        r[i]=x[i+1]/M
    
    return x


def main():

    a,b,c,M=2,1,0,10

    print(LCM(c,a,b,M,13))


if __name__ == "__main__":

    main()
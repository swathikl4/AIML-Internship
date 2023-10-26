def plusMinus(arr):
    # Write your code here
    count=0
    x=0
    y=0
    z=0
    for i in range(len(arr)):
        if i>0:
            count=count+1
        x=count/n
        if i<0:
            count=count+1
        y=count/n
        if i==0:
            count=count+1
        z=count/n
    print(x+"\n"+y+"\n"+z+"\n")
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

def fun(mat):
    n=len(mat)
    path=[]
    dis=[]
    for i in range(0,1<<n):
        dis.append([10000000]*n)
    prevBitmask=[]
    for i in range(0,1<<n):
        prevBitmask.append([0]*n)
    prevNode=[]
    for i in range(0,1<<n):
        prevNode.append([0]*n)

    dis[1][0]=0
    for i in range(2,1<<n):
        v=[]
        for j in range(0,n):
            if((1<<j)&i):
                v.append(j)
        for j in v:
            temp=(1<<j)^i
            for k in v:
                if j==k or j==0:
                    continue;
                if dis[i][j]>dis[temp][k]+mat[k][j]:
                    dis[i][j]=dis[temp][k]+mat[k][j]
                    prevBitmask[i][j]=temp
                    prevNode[i][j]=k

    temp=(1<<n)-1
    min_dis=dis[temp][0]
    index=0
    bitmask=(1<<n)-2
    min_dis=dis[temp][0]
    for i in range(1,n):
        if dis[temp][i]<min_dis:
            min_dis=dis[temp][i]
            index=i
            bitmask=temp

    while index!=0:
        path.append(index)
        index1=prevNode[bitmask][index]
        bitmask=prevBitmask[bitmask][index]
        index=index1
    path.append(0)
    path1=[]
    for i in reversed(path):
        path1.append(i)
    return path1,min_dis

#matrix = [[0,10,8,9,7],[10,0,10,5,6],[8,10,0,8,9],[9,5,8,0,6],[7,6,9,6,0]]
#matrix = [[0,10,8,9,11],[10,0,10,5,6],[8,10,0,8,9],[9,5,8,0,6],[11,6,9,6,0]]
matrix = [[0,7693,6780,6885],[7693,0,2800,3881],[6780,2800,0,429],[6885,3881,429,0]]
path,dis=fun(matrix)
print path,dis

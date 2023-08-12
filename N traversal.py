#taking Input from user
n = int(input("Enter the row value of Square mat:" ))
mat = []  #matrix 
Ans = []  #answer
for t in range(n):
    arr = list(map(int,(input().split())))
    mat.append(arr)
print("YOur Entered Matrix is:",mat)
#lets start coding
#using a for loop to travel from column 0, row n-1 to column 0, row 0
for i in range(n-1,-1,-1):
    Ans.append(mat[i][0])
for i in range(1,n,1):   #for diogonal ie: i = j
    Ans.append(mat[i][i])
for i in range(1,-1,-1):  # for column n-1,row n-2 to row 0
    Ans.append(mat[i][n-1])
print(*Ans)
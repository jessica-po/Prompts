n = int(input())

board =[]

for i in range(n):
    board.append(list(input()))
    
f = 1
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            if i < n - 2 and j < n - 1 and j > 0 and board[i+1][j] == '.' and board[i+2][j] == '.' and board[i+1][j-1] == '.' and board[i+1][j+1] == '.':
                board[i+1][j] = '#'
                board[i+2][j] = '#'
                board[i+1][j-1] = '#'
                board[i+1][j+1] = '#'
            else:
                f = 0
                break

if f == 1:
    print("YES")
else:
    print("NO")
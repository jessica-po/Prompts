A = input()
B = input()
C = input()
turn = 'a'
while True:
  if turn == 'a':
    if len(A) == 0:
      print('A')
      break
    turn = A[0]
    A = A[1:]
  elif turn == 'b':
    if len(B) == 0:
      print('B')
      break
    turn = B[0]
    B = B[1:]
  else:
    if len(C) == 0:
      print('C')
      break
    turn = C[0]
    C = C[1:]
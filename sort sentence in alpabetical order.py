def Func(S):
  W = S.split(" ")
  for i in range(len(W)):
      W[i]=W[i].lower() 
  S = sorted(W)
  print(' '.join(S))
S = "the lost of us"
Func(S)

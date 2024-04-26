stack = []
x = 0
y = 350 + 1
i = open('5input.txt', 'r').read() + '.'*(y+1)

while x < y*(y-1)-2:
  flag = 0
  if i[x+1] == '#':
    flag += 1
  if i[x+y] == '#':
    flag += 2
  #print(str(x)+"  "+str(flag))
  stack.append(flag)
  if flag % 2:
    x += 1
  elif flag == 2:
    x += y
  else:
    t = stack.pop()
    while t != 3:
      if t == 2:
        x -= y
      else:
        x -= 1
      t = stack.pop()
    stack.append(2)
    x += y

for e in stack:
  if e % 2:
    print('R')
  else:
    print('D')

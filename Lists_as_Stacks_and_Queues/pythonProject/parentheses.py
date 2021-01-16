from collections import deque

data = deque(input())
mirror = {'(' : ')', '[':']', '{': '}'}
balanced = True
open = []

while data:
   a = data.popleft()
   if a in "({[":
       open.append(a)
   else:
       if not open:
           balanced = False
           break
       else:
           b = open.pop()
           if mirror[b] == a:
               continue
           else:
               balanced = False
               break

if balanced:
    print("YES")
else:
    print("NO")
#100/100 - wih dictionary and mirror
#87/100 - not included option (])
#75/100 - not included internal
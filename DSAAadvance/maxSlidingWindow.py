from collections import deque

q = deque()
n = [5,5,5,5,5,6]
l, r = 0, 0
while r < len(n):
    if not q or n[r] < n[q[-1]]:
        q.append(r)
    else:
        while q and n[r] > n[q[-1]]:
            q.pop()
        q.append(r)
    r += 1
    if r >= 3: 
        if r!= 3:
            if q[0] == l:
                q.popleft()
            l += 1
        print(n[q[0]])
# for i in range(len(n)):
#     if not stack:
#         stack.append(n[i])
#     else:
#         while stack:
#             temp = stack.pop()
#             if n[i] > temp:
#                 if not stack:
#                     stack.append(n[i])
#                     break
#             else:
#                 stack.append(temp)
#                 stack.append(n[i])
#                 if len(stack) > 3:
#                     stack = stack[1:]
#                 break
#         if i >= 2:
#             print(stack[0])

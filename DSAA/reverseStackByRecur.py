def returnBottom(stack):  #返回栈最底部的值，并将栈除了最底元素以外压回
    temp = stack.pop()
    if not stack:
        return temp
    else:
        last = returnBottom(stack)
        stack.append(temp)
        return last

def reverseStackByRecur(stack):  #不用额外空间，仅使用递归来使栈逆序
    if not stack:
        return
    temp = returnBottom(stack)
    reverseStackByRecur(stack)
    stack.append(temp)

stack = [4,3,2,1]
print(stack)
#print(returnBottom(stack))
reverseStackByRecur(stack)
print(stack)

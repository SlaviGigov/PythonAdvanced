# from collections import deque
#
# def palindrome(word, i):
#     data = deque(word)
#     if len(data) <= 1:
#         return print(f"{word} is a palindrome")
#     if data.popleft() == data.pop():
#         palindrome(data, 0)
#     else:
#         return f"{word} is not a palindrome"
# work well but can not print

def palindrome(data, i):
    if i == len(data)//2:
        return f"{data} is a palindrome"

    if data[i] == data[-(i+1)]:
        return palindrome(data, i+1)
    else:
        return f"{data} is not a palindrome"


print(palindrome("abcba", 0))
# Algorithm is OK - I do not know why it return None - I have MISSED RETURN when call back recurssion
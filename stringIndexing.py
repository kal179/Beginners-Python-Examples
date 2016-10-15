# string indexing

'''
Indexing
0  1  2  3  4
H  E  L  L  O
'''

message = 'Hello'
print(message[0]) # this will print H that is first letter in the string
print(message[1:4]) # this will print from index one to index four
print(message[:3]) # this will print from starting to index 3
print(message[2:]) # this will print from index 2 till end
print(message[:]) # this prints whole string
print(message[0:4:2]) # this escapes 2 characters from string

# negative Indexing
'''
negative Indexing
  P  y  t  h  o  n
 -6 -5 -4 -3 -2 -1
'''

awesome = 'Python is awesome'
print(awesome[:-1]) # -1 prints last character
print(awesome[-2]) # this prints m from starting
print(awesome[-7:]) # try this one out in interpreter

print('You are ' + awesome[10:] + ' you are learning ' + awesome[:6])

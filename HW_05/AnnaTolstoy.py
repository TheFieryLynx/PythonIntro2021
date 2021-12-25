import sys
import random
N = int(input())
Txt = sys.stdin.read().replace("\n    ", " @ ").split()

text_lenght = len(Txt)

dictionary = {}  #словарь словарей

if Txt[0] == '@':
   Txt[0] = "\n    "

if Txt[1] == '@':
   Txt[1] = "\n    "
   
for i in range(text_lenght - 2):
   if Txt[i + 2] == '@':
      Txt[i + 2] = "\n    "
   if Txt[i] not in dictionary:
      dictionary[Txt[i]] = {}
      
   if Txt[i + 1] in dictionary[Txt[i]]:
      dictionary[Txt[i]][Txt[i + 1]].add(Txt[i + 2])
   else:
      dictionary[Txt[i]][Txt[i + 1]] = {Txt[i + 2]}

result = random.sample(Txt, 1)
result += random.sample(list(dictionary[result[0]].keys()), 1)
   
for i in range(N - 2):
   result += random.sample(list(dictionary[result[i]][result[i + 1]]), 1)

print(*result, sep = ' ')
   
   
   
   
   
def match_words(words):
 ctr=0
 lst=[]
 for x in words:
  if len(x)> 1 and x[0]==x[-1]:
   ctr+=1
   lst.append(x)
 print("list of words with the first and last characters the same\n", lst)
 return ctr
count= match_words(['abc', 'cfc', 'xyz', 'aba', '1221', 'pip'])
print("numbers of words having first and last characters same: ", count)
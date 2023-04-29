s = "Python"
rev = ""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
if(s == rev):
   print("pallindrome")
else:
    print("not pallidrome")
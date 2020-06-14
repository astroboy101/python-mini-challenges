# --------------
def palindrome(num):
    i=num+1
    while(str(i)!=str(i)[::-1]):
        i=i+1
    print(i)
    return i




# --------------
#Code starts here
def a_scramble(str_1,str_2):
    str_1=str_1.lower()
    str_2=str_2.lower()
    for i in str_2:
        if i in str_1:
            flag=0
            str_1=str_1.replace(i,"0",1)
        else:
            flag=1
            break
    if flag==0:
        return True
    else:
        return False



# --------------
def fib(num):
    if num==0 or num==1:
        return num
    else:
        k=fib(num-1)+fib(num-2)
        return k
def check_fib(num):
    i=0
    while(num>fib(i)):
        i=i+1
    print(num==fib(i))
    return num==fib(i)

    


# --------------
#Code starts here
def compress(word):
    c=1
    x="a"
    word=word.lower()
    for i in range(0,len(word)-1):
        if word[i]==word[i+1]:
            c=c+1
        else:
            x=x+word[i]+str(c)
            c=1
        if c==len(word):
            x=x+word[i]+str(c)
    x=x[1:]
    if word[i]!=word[i+1]:
        x=x+word[i+1]+"1"
    return x
print(compress("Ss"))


# --------------
#Code starts here
def k_distinct(string,k):
    string=string.lower()
    a=set()
    for i in string:
        a.add(i)
    return len(a)==k



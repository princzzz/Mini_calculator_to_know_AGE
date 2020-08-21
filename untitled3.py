f=open("b.txt","r")
if f.mode == 'r':
    print (f.read())
f.close()
def text_len(random):
    return len(words)
file=open("b.txt","rt")
data=file.read()
words=data.split()
t=text_len(words)
print('\nTotal Word:', t)
print("\nFirst 10 word")
for i in range(0,10):
    print(words[i])
print("\n")
print("avoid word like an,the,how")    
a=["an","the","how"]
for i in range(0,10):
    k=0
    for j in a:
        if j!=words[i]:
            k=k+1
        if k==3:
            print(words[i])



           





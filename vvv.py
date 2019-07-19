a1,a2=map(int,input().split())
char=input().split()
b=[]
for c in char:
	if(int(c)%2!=0):
		b.append(c)
print(b[a2-1])

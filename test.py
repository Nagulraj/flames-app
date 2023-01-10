r="sridhar"
s="nagul"

for i in r:
    for j in s:
            if i==j:
                print(i)
                print(j)
                r=r.replace(j, '', 1)
                s=s.replace(j,'',1)
#             
total_length=len(r)+len(s)
print(r)
print(s)
print(total_length)  


flames=["Frnds","love","Affection","Marriage","Enemy","sister"]

# index=0
# for i in range(6,0):
#     print(i)
#     if i==1:
#         break
#     if i>=1:
#         print(i)


while len(flames) > 1 : 
	split_index = (total_length % len(flames) - 1) 
	if (split_index>=0) :
		right = flames[split_index + 1 : ]
		left = flames[ : split_index] 
		flames = right + left
	else : 
		flames = flames[ : len(flames) - 1]            
result=flames[0]
print(result)

r="sridhar"
s="nagul"
def remove(element,string):

    input_str = string
   

   
    result_str = "" 
   
    for i in range(0, len(input_str)): 
        count=0
        if count==0:
            if input_str[i] != element: 
                result_str = result_str + input_str[i] 
            if input_str[i] == element:
                count=1
    return result_str




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
n=6
for i in range(6,0):
    if i==1:
        break
    if i!=1:
        
        index=total_length%i
        flames.pop(index-1)
           
print(flames)    
result=flames[0]
print(result)

r="nagul"
s="keerthanaa"
def remove(element,string):

    input_str = string
   
# Printing original string  
    # print ("Original string: " + input_str) 
   
    result_str = "" 
   
    for i in range(0, len(input_str)): 
        if input_str[i] != element: 
            result_str = result_str + input_str[i] 

    return result_str

# k=s.replace('a', '', 1)
# print(k)



for i in r:
    for j in s:
       
        if i==j:
            print(i)
            print(j)
            r=r.replace(i, '', 1)
            s=s.replace(i,'',1)
            print(r)
            print(s)
total_length=len(r)+len(s)
  

count=0
for k in range(0,total_length,6):
    count+=1
flames=["Frnds","love","Affection","Marriage","Enemy","sister"]
result=flames[count]
print(result)

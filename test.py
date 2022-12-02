r="nagul"
s="keerthana"
def remove(element,string):

    input_str = string
   
# Printing original string  
    # print ("Original string: " + input_str) 
   
    result_str = "" 
   
    for i in range(0, len(input_str)): 
        if input_str[i] != element: 
            result_str = result_str + input_str[i] 

    return result_str

# k=remove('a',r)
# print(k)



# for i in r:
#     for j in s:
       
#         if i==j:
#             print(i)
#             print(j)
#             r.replace(i,'',1)
#             s.replace(i,'',1)
# print(r)
# print(s)

a=[1,4,6,'elon musk',1971,54,'Tesla',[3,'XAI'] ]  # sample input
result={'str':0 , 'int':0 ,'list':0 } # Initialize result dictionary
while a: # Iterate until the list empty
    b=a.pop(0)
    if isinstance(b,str):
        result['str']+=1
    elif isinstance(b,int):
        result['int']+=1
    elif isinstance(b,list):
        result['list']+=1
    else:
        break
print('result=',result)  # print final result
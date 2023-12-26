input_number=6
a=[3,2,4]
index_value=set()
counter=0
inner_counter=1
while counter<len(a):
    while inner_counter<len(a):
        if input_number==a[counter]+a[inner_counter]:
            index_value.add(counter)#adding in set
            index_value.add(inner_counter)
    counter+=1
print(index_value)


        
        

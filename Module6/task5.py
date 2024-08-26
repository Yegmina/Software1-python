list_of_integers=[1,2,3,4,5,6,7,8,9]

def list_without_uneven(list):
    output_list=[]
    for i in range(0,len(list)):
        if list[i]%2==0:
            output_list.append(list[i])
    return output_list

print(list_of_integers)
print(list_without_uneven(list_of_integers))
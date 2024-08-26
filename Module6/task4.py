list_of_integers=[1,2,3,4,5,6,7,8,9]

def list_sum(list):
    sum=0
    for i in range(0,len(list_of_integers)):
        sum=sum+list[i]
    return sum

print(list_sum(list_of_integers))
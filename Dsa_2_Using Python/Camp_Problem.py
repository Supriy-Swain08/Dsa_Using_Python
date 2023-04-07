def calculate_total_chocolates():
    return sum(chocolates_received)

def reward_child(child_id_rewarded,extra_chocolates):
    Id=child_id.index(child_id_rewarded)
    chocolates_received[Id]=chocolates_received[Id]+extra_chocolates

child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
print(*child_id,"\n",*chocolates_received)
print(calculate_total_chocolates())
childid=int(input('which child you want to reward'))
extra=int(input('No of extra Chocolate:'))
if extra<1:
    print("Extra chocolates is less than 1")
elif childid not in child_id:
    print('Invalid Id')
else:
    reward_child(childid,extra)
print(*child_id,"\n",*chocolates_received)

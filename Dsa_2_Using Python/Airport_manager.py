ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067",
             "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148",
             "AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]
def find_passengers_flight(data):
    count=0
    for i in ticket_list:
        if i[0:2]==data:
            count+=1
    return count
            
def find_passengers_destination(data):
    for i in ticket_list:
        if i[-7:-4]==data:
            print(i)
def sort_passenger_list():
    print(sorted(ticket_list))
def find_passengers_per_flight():
    a,b,s=0,0,0
    for i in ticket_list:
        if i[0:2]=='AI':
            a+=1
        elif i[0:2]=='BA':
            b+=1
        elif i[0:2]=='SI':
            s+=1
    print('AI:',a,'BA:',b,'SI:',s)
print(find_passengers_flight("AI"))
(find_passengers_destination('LON'))
sort_passenger_list()
find_passengers_per_flight()

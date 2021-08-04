import math
budget = 1500

def cost_of_trip(flight_cost, hotel_cost, car_rental, duration):
    total_cost = flight_cost + ( hotel_cost * duration ) + ( car_rental / 7 ) * duration
    total_cost = math.ceil(total_cost)
    return total_cost

paris = cost_of_trip(200, 20, 200, 4)  
print(paris)

london = cost_of_trip(250, 30, 120, 4)
print(london)

dubai = cost_of_trip(370, 15, 80, 4)
print(dubai)

newyork = cost_of_trip(450, 10, 70, 4)
print(newyork)

if ( paris < london and paris < dubai and paris < newyork ) and paris <= budget:
    print('paris ${}'.format(paris))
    
elif ( london < paris and london < dubai and london < newyork ) and london <= budget:
    print('london ${}'.format(london))
    
elif ( dubai < paris and dubai < london and dubai < newyork ) and london <= budget:
    print('dubai ${}'.format(dubai))

elif ( newyork < paris and newyork < london and newyork < dubai ) and newyork <= budget:
    print('newyork ${}'.format(newyork))
    
else:
    print('you are out of budget')
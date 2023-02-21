
print('\n Question 8-12')
def sandwich_items(*items):
    print('\n making sandwich')
    for item in items:
        print(f" - {item}")
 
sandwich_items('Big', 'Suger', 'flour', 'baking powder')
sandwich_items('snmall','pepe', 'magi', 'chees')
sandwich_items('meat', 'spices','magerine')

print('\n Question 8-13')
def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Halima', 'Abdul',
                                location='Yobe',
                                field='Computer Science', Others= ['Teaching', 'learning', 'Philantropist' ])
print(user_profile)

print('\n Question 8-14')
def car_info(manufacturer_name, model_num, **car):
    car['name'] = manufacturer_name
    car['type'] = model_num
    return car

car_details = car_info('Toyota', 'wagon', color='Red')
print(car_details)
 

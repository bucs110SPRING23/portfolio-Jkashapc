import random 
weeks = 16
classes = 4
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))
print("Cost per week:", cost_per_week)
classes_per_week = 10
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class,type(cost_per_class))
print("So that means each class costs:", cost_per_class)
my_list= (1,2,3,4,5)
rando = random.choice(my_list)
print(rando)

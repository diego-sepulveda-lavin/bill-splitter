# the list "walks" is already defined
# your code here
total_distance = 0
day_counter = 0

for walk in walks:
    distance = walk['distance']
    total_distance += distance
    day_counter += 1

mean_distance = total_distance // day_counter
print(mean_distance)

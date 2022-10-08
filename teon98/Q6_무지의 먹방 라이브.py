food_times = [3,1,2]
k=6

for i in range(1,k+1):
    index = i%len(food_times)
    i_list = []
    if index == 0:
        index = len(food_times)
    if food_times[index-1] == 0:
        food_times[index%len(food_times)] -= 1
        i_list.append(index%len(food_times)+1)
    else:
        food_times[index-1] -= 1
        i_list.append(index)
    # print(food_times)
    # print(i_list)

print(i_list[0])
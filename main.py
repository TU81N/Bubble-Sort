list1 = [4, 8, 2, 10, 3]

def bubble_sort(a_list):
  # Your code here
  # Ascending order
  for i in range(len(a_list)): 
    for j in range(len(a_list) - 1): 
      if a_list[i] > a_list[j+1]:
        temp = a_list[i]
        a_list[i] = a_list[j+1]
        a_list[j+1] = a_list[i]
        
  return a_list


print(bubble_sort(list1))

def bubblesort(list):
  length = len(list)
  for i in range(length - 1):
    for j in range (length - 1):
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
  return list

def main():
  input_list = [2,8,7,6,5]
  bubble_sort(input_list)

main()

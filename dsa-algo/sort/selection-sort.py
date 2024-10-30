def selection_sort(list):
  legnth = len(list)
  for i in range(length-1):
    minimum = i
    for j in range(i+1, length):
      if list[j] < list[min]:
        minimum = j
    if minimum != i:
      list[i], list[minimum] = list[minimum], list[i]
  return list

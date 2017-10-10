def build_ints_list():
  ints_list = []
  x = 0
  while True:
    x = input("Enter an int (enter 'STOP' to end): ")
    if x == "STOP":
      break
    ints_list.append(int(x))
  return ints_list

def flip(lst, i, j):
  return lst[0:i] + lst[i:j+1][::-1] + lst[j+1:]

def sort_in_ascending_order(lst):
  for i in range(len(lst)-1):
    # Keep flipping until the integer at index i+1 isn't smaller than the one before it
    while not (lst[i+1] >= lst[i] or i < 0):
      lst = flip(lst, i, i+1)
      i -= 1
  return lst
    
if __name__ == "__main__":
  your_list = build_ints_list()
  print("Your list: ", your_list)
  your_list = sort_in_ascending_order(your_list)
  print ("Your sorted list: ", your_list)

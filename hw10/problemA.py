def find_the_mins(dictionary):
  new_dict = {}
  for item in dictionary:
    if len(dictionary[item]) > 0:
      new_dict[item] = min(dictionary[item])
  
  return new_dict

if __name__ == "__main__":
   print(find_the_mins({
    "One": [1, 2, 3],
    "Two": [4, 5, 6],
    "Three": [44, 41, 41]
  }))

   print(find_the_mins({
    "X": [-1, 3, -33, 100],
    "Y": [], "Z": [1, 1, 0],
    "W": [3]
   }))

   print(find_the_mins({
    "In": [12, 100, 72, 74, 11, 89],
    "Out": [14, 100],
    "Failed": [-1, 0, 0, 1],
    "Queued": [3],
    }))
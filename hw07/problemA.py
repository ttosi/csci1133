import hw07
from pprint import pprint
import copy
# matrix = [
#     [[127, 127, 127], [0, 0, 0]],
#     [[255, 255, 0], [50, 128, 255]],
#     [[0, 0, 255], [0, 255, 0]],
#     [[255, 0, 0], [255, 255, 255]],
# ]

matrix = [
    [[255, 1, 0], [255, 0, 0], [255, 153, 0], [255, 255, 0], [255, 204, 51], [255, 204, 51]],
    [[255, 2, 0], [0, 255, 0], [0, 255, 255], [50, 128, 255], [255, 204, 51], [255, 204, 51]],
    [[255, 3, 0], [0, 0, 255], [153, 0, 255], [255, 0, 255], [255, 204, 51], [122, 0, 25]],
    [[255, 4, 0], [0, 0, 0], [255, 204, 51], [122, 0, 25], [122, 0, 25], [122, 0, 25]],
    [[255, 5, 0], [255, 204, 51], [122, 0, 25], [122, 0, 25], [122, 0, 25], [122, 0, 25]],
    [[255, 6, 0], [122, 0, 25], [122, 0, 25], [122, 0, 25], [122, 0, 25], [122, 0, 25]],
]

# def get_col(img_matrix, width, height):
#     for col in range(width):
#         for row in range(height):
#             print(img_matrix[row][col])


def mirror(img_matrix):
    height = len(img_matrix)  # Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0])  # Width = # of columns, i.e. length of one row
    new_matrix = copy.deepcopy(img_matrix)

    for col in range(width):
       index = 1
       for row in range(height):
         print("r", row, "c", col, "w-i", width - index, "w-c", width - col - 1)
        #  print("before", new_matrix[row][col], new_matrix[row][width - index])
         new_matrix[row][width - col - 1] = new_matrix[row][col]
        #  print("after", new_matrix[row][col], new_matrix[row][width - index])
        #  pprint(new_matrix, width=140)
         index += 1
    # pprint(img_matrix, width=140)
    pprint(new_matrix, width=140)
# for y in range(height):

# for x in range(width):
#     pass



if __name__ == "__main__":
    mirror(matrix)

import hw07

# matrix = [
#     [[127, 127, 127], [0, 0, 0]],
#     [[255, 255, 0], [50, 128, 255]],
#     [[0, 0, 255], [0, 255, 0]],
#     [[255, 0, 0], [255, 255, 255]],
# ]

matrix = [
    [[255, 0, 0], [255, 153, 0], [255, 255, 0], [255, 204, 51], [255, 204, 51]],
    [[0, 255, 0], [0, 255, 255], [50, 128, 255], [255, 204, 51], [255, 204, 51]],
    [[0, 0, 255], [153, 0, 255], [255, 0, 255], [255, 204, 51], [122, 0, 25]],
    [[0, 0, 0], [255, 204, 51], [122, 0, 25], [122, 0, 25], [122, 0, 25]],
    [[255, 204, 51], [122, 0, 25], [122, 0, 25], [122, 0, 25], [122, 0, 25]],
    [[122, 0, 25], [122, 0, 25], [122, 0, 25], [122, 0, 25], [122, 0, 25]],
]


# def get_col(img_matrix, width, height):
#     for col in range(width):
#         for row in range(height):
#             print(img_matrix[row][col])


def mirror(img_matrix):
    height = len(img_matrix)  # Height = # of rows, i.e. length of matrix
    width = len(img_matrix[0])  # Width = # of columns, i.e. length of one row
    mirror_matrix = []
    cols = []
    for col in range(width):
        rows = []
        for row in range(height):
            rows.append(img_matrix[row][col])
        cols.append(rows)
        print(rows)
#     half = int(width / 2)
#     print(half)
#     print(mirror_matrix[0:half])
#     print(mirror_matrix[half:-1])
#     print(cols)

#     cols[:-1] = cols[0]
#     print(cols)
    
#     for i in range(int(len(cols) / 2) + 1):
#         print(cols[i][0])
        # print(cols[:-i + 1])
        # cols[:-1] = cols[i]



# for y in range(height):

# for x in range(width):
#     pass


if __name__ == "__main__":
    mirror(matrix)

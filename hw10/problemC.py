def create_lists(file_name):
    file = open(file_name, "r")
    shopping_list = {}
    for line in file:
        data = line.split(",")
        store = data[0]
        item = data[1]
        quantity = data[2]

        if store not in shopping_list.keys():
            # when the store isn't in the shopping list, create the key
            shopping_list[store] = {item: int(quantity.strip())}
        else:
            # when the item isn't in the store, create it
            if item not in shopping_list[store].keys():
                shopping_list[store][item] = int(quantity.strip())
            else:
                # the item exists, so add it to the running total
                shopping_list[store][item] += int(quantity.strip())

    return shopping_list


if __name__ == "__main__":
    # print(create_lists("small.csv"))
    # print(create_lists("medium.csv"))
    print(create_lists("large.csv"))

result = {
    "Corner Store": {
        "Chewing Gum": 8,
        "Canned Soups": 3,
        "Pen": 5,
        "Legumes": 6,
        "Chips": 15,
    },
    "7-11": {
        "Tuna": 1,
        "Insta Pot": 8,
        "Frozen Peas": 6,
        "Tomato Sauce": 11,
        "Cheese": 17,
        "Batteries": 2,
        "Water": 6,
        "Toothpaste": 1,
        "Hand Sanitizer": 6,
        "Hair Brush": 3,
    },
    "Target": {"Milk": 12, "Dish Soap": 11, "Cereal": 5, "Nuts": 2, "Sweater Box": 16},
    "Nate's": {
        "Folding Table": 7,
        "Honey": 2,
        "Candy": 12,
        "Vinegar": 7,
        "Soda": 13,
        "Cheese": 0,
        "Dog Food": 12,
    },
    "Dan's": {
        "Apple": 9,
        "Donuts": 5,
        "Bananas": 10,
        "Rice": 2,
        "Maple Syrup": 8,
        "Bread": 12,
        "Candy": 5,
    },
    "Islands": {"Tea": 12, "Sandwich": 6, "Meatballs": 13, "Eggs": 0},
}

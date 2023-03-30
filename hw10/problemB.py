def find_the_contact(directory, name, field):
    for user in directory:
        if name == user:
            return directory[user][field]

        try:
            return directory[name]
        except KeyError:
            return name[:3]


if __name__ == "__main__":
    a_dict = {
        "Lee": {"Phone": "643-756-5612", "Email": "example@umn.edu", "Username": "Lee"},
        "Katie": {"Email": "test_email@gmail.com", "Username": "Kat"},
        "Amanda": {
            "Phone": "234-462-4513",
            "Email": "no_email@yahoo.com",
            "Username": "Ama",
        },
    }
    print(find_the_contact(a_dict, "Lee", "Phone"))
    print(find_the_contact(a_dict, "Nat", "Email"))
    print(find_the_contact(a_dict, "Abi", "Email"))

    # a_dict = {
    #   'Lee': {'Phone': '643-756-5612', 'Email': 'example@umn.edu', 'Username': 'Lee'},
    #   'Katie': {'Email': 'test_email@gmail.com', 'Username': 'Kat'},
    #   'Amanda': {'Phone': '234-462-4513', 'Email': 'no_email@yahoo.com', 'Username': 'Ama'},
    #   'Nat': {'Phone': '612-379-5234', 'Username': 'Nat'},
    #   'Abi': {'Username': 'Abi'}
    # }
    # print(find_the_contact(a_dict, "Abby", "Username"))

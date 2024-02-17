shopping_list = []

while True:
    item = input("> ")
    if item.lower() == 'done':
        break

    elif item.lower() == 'show':
        print("Your Shopping List!")
        for item in shopping_list:
            print(item)

    elif item.lower() == 'save':
        print("Saving...")
        with open("list.txt", 'w') as file:
            for index, item in enumerate(shopping_list):
                file.write(str(index+1) + ') ' + item + '\n')

    else:
        if item not in shopping_list:
            shopping_list.append(item)

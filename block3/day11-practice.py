

def find_longest_name(list_names):
    return max(list_names, key=len)


def sum_of_letters(list_names):
    return sum(len(word) for word in list_names if word != '\n')


def find_shortest_name(list_names):
    shortest_len = len(min(list_names, key=len))
    return [word for word in list_names if len(word) == shortest_len]


def length_of_each_into_file(list_names):
    with open("name_length.txt", "w") as file:
        for x in list_names:
            file.write(str(len(x)) + "\n")


def find_desired_length(list_names, desired_length):
    return [word for word in list_names if len(word) == desired_length]


def main():
    try:
        with open('names.txt', 'r') as file:
            list_names = [line.strip() for line in file]
            print(list_names)
            print(find_longest_name(list_names))
            print(sum_of_letters(list_names))
            print(*find_shortest_name(list_names), sep="\n")
            length_of_each_into_file(list_names)
            desired_length = int(input("enter desired length of name por favor: "))
            print(*find_desired_length(list_names, desired_length), sep="\n")

    except FileNotFoundError:
        print("File is not found")
        return


if __name__ == "__main__":
    main()


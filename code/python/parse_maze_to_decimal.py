def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def parser(read_filename, write_filename):
    maze = []
    with open(read_filename) as a:
        for i in a:
            line = i.strip()
            split_strings = []
            for index in range(0, len(line), 4):
                split_strings.append(binaryToDecimal(int(line[index: index + 4])))
            maze.append(split_strings)
    with open(write_filename, 'w') as f:
        for line in maze:
            f.write(','.join([str(x) for x in line]))
            f.write('\n')

    print(maze)


read_file = input("Read filename: ")
write_file = input("Write filename: ")

parser(read_file, write_file)
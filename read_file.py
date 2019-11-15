def read_file(file):
    with open(file, "r") as file:
        width = int(file.readline())
        line = file.readline().split()
        heights = []
        for x in line:
            heights.append(int(x))
    return width, heights

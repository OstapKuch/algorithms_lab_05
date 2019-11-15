from read_file import read_file
import math


def optimiser(heights):
    heights = sorted(heights, reverse=True)
    new_heights = []
    for x in range(0, math.ceil(len(heights) / 2)):
        new_heights.append(heights[x])
        new_heights.append(1)
    if len(heights) % 2:
        new_heights.pop()
    return new_heights


def get_max_cable_width(width, heights):
    result = 0
    previous_length = math.sqrt(abs(heights[0] - 1) ** 2 + width ** 2)
    if heights[-1] == 1:
        print(len(heights))
        result = previous_length + 2 * math.sqrt(abs(heights[len(heights) - 2] - 1) ** 2 + width ** 2)
    else:
        result = previous_length + math.sqrt(abs(heights[len(heights) - 1] - 1) ** 2 + width ** 2)
    for x in range(2, len(heights) - 2, 2):
        result = result + 2 * math.sqrt(abs(heights[x] - 1) ** 2 + width ** 2)
    return result


def main():
    width, heights = read_file("file.in")
    new_heights = optimiser(heights)
    result = get_max_cable_width(width, new_heights)
    print(result)


main()

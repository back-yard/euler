def triangle(limit):
    triangle_nums = [1]
    index = 1
    while triangle_nums[-1] < limit:
        triangle_nums.append(triangle_nums[index-1] + index + 1)
        index += 1

    if triangle_nums[-1] > limit:
        triangle_nums.pop()

    return triangle_nums

if __name__ == '__main__':
    print triangle(100)

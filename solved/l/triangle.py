def triangle(length):
    triangle_nums = [1]
    index = 1
    while len(triangle_nums) < length:
        triangle_nums.append(triangle_nums[index-1] + index + 1)
        index += 1
    return triangle_nums

if __name__ == '__main__':
    print triangle(10)

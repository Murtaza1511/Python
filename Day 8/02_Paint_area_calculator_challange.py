import math
def paint_calc(height,width,coverage):
    area = height*width
    num_of_cans = math.ceil(area / coverage)
    print(f'You will need {num_of_cans} cans of paint')

test_h = int(input('Height of wall: '))
test_w = int(input('Width of wall: '))
coverage = 5 # i.e. One paint box can cover 5 square meters
paint_calc(test_h,test_w,coverage)

def draw_triangle(height):
    
    for i in range(height):
        if i == height - 1:
            print('_' * (2 * height - 1))
        else:
            print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')

draw_triangle(5)

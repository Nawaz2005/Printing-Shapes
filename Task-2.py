class task2:
    def pyramid(n):
        rows = int(input("Enter the number of rows for the pyramid: "))
        for i in range(rows):
            print(' ' * (rows - i - 1) + '*' * (2 * i + 1))
    def square(n):
        size = int(input("Enter the size of the square: "))
        for i in range(size):
            for j in range(size):
                print('*', end=' ')
            print()     
    def reversepyramid(n):
        rows = int(input("Enter the number of rows for the reverse pyramid: "))
        for i in range(rows, 0, -1):
            print(' ' * (rows - i) + '*' * (2 * i - 1))
            
    def rightanglepyramid(n):
        rows = int(input("Enter the number of rows for the right angle triangle: "))
        for i in range(1, rows + 1):
            print('*' * i)

    def print_circle(n):
        radius = int(input("Enter the radius of the circle: "))
        center_x = radius
        center_y = radius

        for y in range(2 * radius + 1):
            for x in range(2 * radius + 1):
                distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                if distance <= radius + 0.5:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print()
while(True):
    print(" 1 for pyramid \n 2 for square \n 3 for reverse pyramid \n 4 for right angle pyramid \n 5 for circle \n 6 for exit")
    n = int(input("Enter a nummber \n"))  
    if n == 1:
        task2.pyramid(n)
    elif n == 2:
        task2.square(n)
    elif n == 3:
        task2.reversepyramid(n)
    elif n == 4:
        task2.rightanglepyramid(n)
    elif n == 5:
        task2.print_circle(n)
    elif n == 6:
        break
    else:
        print("invalid input")

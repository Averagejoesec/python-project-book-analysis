width = int(input("Enter width: "))
height = int(input("Enter height: "))

def rectangle_area(width, height):
    area = width * height
    return area

def rectangle_perimeter(width, height):
    perimeter = 2 * (width + height)
    return perimeter

print(rectangle_area(width, height))
print(rectangle_perimeter(width, height))
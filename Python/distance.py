#7 Distance between 2 numbers
def newton_method(number,number_iters=1000):
    a = float(number)
    for i in range(number_iters):
        iter_number=number
        number = 0.5 * (number + a/number)
        if number == iter_number:
            break
    return number

def distance(pointA, pointB):
    x1, y1 = pointA
    x2, y2 = pointB
    
    distX = x1 - x2
    distY = y1 - y2

    return round(newton_method(distX**2 + distY**2),2)

pointA = int(input("Enter the x cordinate (x1) for PointA : ")), \
int(input("Enter the y cordinate (y1) for PointA : "))

pointB = int(input("Enter the x cordinate (x2) for PointB : ")), \
int(input("Enter the y cordinate (y2) for PointB : "))

print(f"distance between points {pointA},{pointB} >>> {distance(pointA,pointB)}")
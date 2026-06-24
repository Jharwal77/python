import math

redius = int(input("Please Enter your Redius of circle: "))

def area_and_circle(redius):
    return (math.pi)*(redius**2), 2*(math.pi)*redius

# result = area_and_circle(redius)
# print("Area of circle is",result[0],"And Circumference of circle",result[1])

a, c = area_and_circle(redius)
print("Area of circle is",round(a,2),"And Circumference of circle",round(c,2))
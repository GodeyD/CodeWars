# Write a function that returns the total surface area and volume of a box as an array: [area, volume]

# My answer:
def get_size(w,h,d):
    area = 2*d*w+2*d*h+2*h*w
    volume = w*h*d
    return [area, volume]
    #your code here
print(get_size(1, 2, 2))
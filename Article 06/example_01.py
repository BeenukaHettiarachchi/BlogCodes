# Get length & width as inputs
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Define function to calculate area
def calculate_area(length, width):
    return length * width

# Call the function
area = calculate_area(length, width)

# Display the result
print("Area of the rectangle is:", area)

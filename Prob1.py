########################################
# Name: Andrew Cerqui   
# Collaborators: None
# Estimated time spent (hr): .5
########################################

def draw_console_pyramid(height):


    width = 2 * height - 1

    for i in range(1, height + 1):
        spaces = " " * ((width - (2 * i - 1)) // 2)
        stars = "*" * (2 * i - 1)
        row = spaces + stars
        print(row)
##line 13 and 14 do math depending on what row it is to put the right amount of * with the right spacing
## stores that information in line 15 and prints those rows








if __name__ == '__main__':
    # You can alter the below value to test your function with a variety
    # of numeric inputs!
    rows = 5
    draw_console_pyramid(rows)

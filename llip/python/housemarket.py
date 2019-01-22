import ipy_lib

''' Assignment: HouseMarket
    Created on 19 jan 2019
    @author: Millen Mortier'''

def read_house_data_file(filename) :
    house_data = []
    file_contents_lines = open(filename).readlines()
    for line in file_contents_lines :
        split_line = line.split(';')
        size = float (split_line[0])
        price = int(split_line[1])
        house = [size, price]
        house_data.append(house)
    return house_data

def mean(x) :
    sum = 0
    for xi in x :
        sum += xi
    # cast sum to a float to avoid integer division
    return float(sum) / len(x)

# Takes vectors x and y
# Quick reminder:
#   covariance = sum_of((xi - xmean) * (yi - ymean)) / (N -1) 
def covariance(x, y) :
    mean_x = mean(x)
    mean_y = mean(y)
    n = len(x)
    sum = 0
    for i in range(0, n) :
        sum += ((x[i] - mean_x) * (y[i] - mean_y))
    # cast the sum to a float to avoid integer division
    return float(sum) / (n - 1)

# Returns the variance of a vector x as a float.
# Quick reminder:
#   variance = sum_of((xi - xmean)^2) / n
def variance(x) :
    mean_x = mean(x)
    sum = 0
    for xi in x :
        sum += ((xi - mean_x) ** 2)
    # cast sum to a float to avoid integer division
    return float(sum) / len(x)

# Get simple linear regression line
# Takes a list of [x,y] data pairs, so the data params will look like:
#   [[x1, y1], [x2, y2], ..., [xn, yn]]
# Return the alpha and beta (as floats) of the line in a list, as:
#   [alpha, beta] 
def get_slr_line(data) :
    x = [x_y[0] for x_y in data]
    y = [x_y[1] for x_y in data]
    beta = covariance(x, y) / variance(x)
    mean_x = mean(x)
    mean_y = mean(y)
    alpha = mean_y - beta * mean_x
    return [alpha, beta]

# Plots a list of the form [[x1, y2], [x2, y2], ..., [xn, yn]] as dots using
# the ipy_lib's UI functions (ipy_lib's UI object is passed as the first param).
# The color param is passed directly to the plot_dot function.
def plot_house_data(ui, data, color) :
    for x_y in data :
        ui.plot_dot(x_y[0], x_y[1], color)

# This function does the calculation on whether the houses in the houses_for_sale
# param are either expensive or affordable. It uses the alpha and beta params
# as the norm 
def print_houses_affordability(houses_data, alpha, beta) :
    expensive_houses_counter = 0
    for house in houses_data :
        # test y > alpha + beta*x
        if house[1] > (alpha + house[0] * beta) :
            expensive_houses_counter += 1
        else :
            expensive_houses_counter -= 1
    if expensive_houses_counter > 0 :
        print "The houses are expensive"
    else :
        print "The houses are affordable"


''' Start Program '''
ui = ipy_lib.HouseMarketUserInterface()

# Read in and plot the houses_sold data
houses_sold_data = read_house_data_file('houses_sold.txt')
plot_house_data(ui, houses_sold_data, 'b')

# Calculate and plot the simple linear regression line
slr_data = get_slr_line(houses_sold_data)
alpha = slr_data[0]
beta = slr_data[1]
ui.plot_line(alpha, beta)

# Read in and plot the houses_for_sale data
houses_for_sale_data = read_house_data_file('houses_for_sale.txt')
plot_house_data(ui, houses_for_sale_data, 'r')

print_houses_affordability(houses_for_sale_data, alpha, beta)

ui.show()
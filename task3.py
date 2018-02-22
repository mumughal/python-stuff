import matplotlib.pyplot as plt
from task1 import calculate

def generate_y_values(y, x_values):
    y_values = []
    for x in x_values:
        new_y = y.replace('x', str(x))
        y_values.append(calculate(new_y))
    return y_values

def main():
    x_values = [1,2,3,4]
    y = "2 * x + 1"
    y_values = generate_y_values(y, x_values)
    plt.plot(x_values, y_values)
    plt.axis([0, 6, 0, 20])
    plt.show()

main()

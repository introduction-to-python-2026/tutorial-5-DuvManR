from matplotlib import pyploy as plt

def build_histogram(data):
    my_dict = {}
    for i in data:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

def plot_histogram(histogram):
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()



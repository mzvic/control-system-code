import matplotlib.pyplot as plt

def plot_graph(x, y, x_label, y_label):
    plt.plot(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


list_x = []
list_y = []
with open("timestamp.csv") as f:
    for row in f:
        print(row.split(",")[0])
        list_x.append(row.split(",")[0])
        list_y.append(row.split(",")[1])

plot_graph(list_x, list_y, "Time", "Counting")
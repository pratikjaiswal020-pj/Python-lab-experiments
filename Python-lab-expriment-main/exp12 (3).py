
import matplotlib.pyplot as plt
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]
plt.hist(data, bins=5, color='purple', label="Histogram Data")
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
data = [7, 8, 5, 6, 9, 10, 15, 20, 21]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()
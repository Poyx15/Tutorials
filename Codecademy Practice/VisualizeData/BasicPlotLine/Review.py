# import codecademylib
from matplotlib import pyplot as plt

x = range(11)
y1 = [num * num for num in x]
y2 = [num * num for num in y1]

print(x)
print(y1)
print(y2)

plt.plot(x, y1, color='pink', marker='o')
plt.plot(x, y2, color='gray', marker='o')
plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
legends = ['y1', 'y2']
plt.legend(legends)
plt.axis([0, 10, 0, 100])
plt.show()

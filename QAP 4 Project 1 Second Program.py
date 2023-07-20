# Program description: This is a program designed to enter the total amount of sales for each month from January to December
# Written by: Ethan Miller
# Date written: July-18-2023 - July-20-2023

# Import

import matplotlib.pyplot as plt

# Graph

x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = [100.00, 200.00, 240.00, 300.00, 320.00, 350.00, 370.00, 380.00, 400.00, 500.00, 530.00, 550.00]

plt.plot(x_axis, y_axis)
plt.scatter(x_axis, y_axis, marker="x", color="blue")

plt.xlabel('Domain Values (x)')
plt.ylabel('Range Values (y)')

plt.title('Graph of total sales against the months')
plt.grid(True)

plt.show()
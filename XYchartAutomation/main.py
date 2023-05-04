import pandas as pd
import matplotlib.pyplot as plt


excel = pd.read_excel("Book1.xlsx")
print(excel)
month = excel["Month"][0:12]
cost = excel["cost"][0:12]
income = excel["income"][0:12]
gross_profit = excel["Gross profit"][0:12]
print(gross_profit)

fig, (pic1, pic2) = plt.subplots(2, 1, figsize=(10, 5))
pic1.plot(month, cost, label="cost", linewidth=3, color='g', marker='o',
         markerfacecolor='black', markersize=10)
pic1.plot(month, income, label="income", linewidth=3, color='r', marker='o',
         markerfacecolor='black', markersize=10)
pic1.plot(month, gross_profit, label="gross_profit", linewidth=3, color='y',
         marker='o', markerfacecolor='black', markersize=10)

pic1.set_xlabel("month")
pic1.set_ylabel("dollars")
pic1.set_title("the monthly stream")
pic1.legend()
pic1.grid()


cost_sum = excel["cost"][13]
income_sum = excel["income"][13]
gross_profit = excel["Gross profit"][13]
print(cost_sum, income_sum, gross_profit)

sum_x_label = excel.columns.tolist()[1:]
sum_y_values = [cost_sum, income_sum, gross_profit]
pic2.bar(sum_x_label, sum_y_values)

pic2.set_title("Yearly total cost, income and gross profit")
pic2.set_xlabel("items")
pic2.set_ylabel("dollars")
plt.subplots_adjust(hspace=0.9)

plt.gcf().set_size_inches(10, 5)
plt.savefig('two_pics.png', bbox_inches='tight', dpi=200)
plt.show()
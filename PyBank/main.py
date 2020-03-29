import csv
import os

input_file = os.path.join("PyBank/Resources/budget_data.csv")
output_file = os.path.join("PyBank/Resources/budget_analysis.txt")

total_months = 0
monthly_change = []
revenue_change = []
max_increase = ["", 0]
max_decrease = ["", 1000000000]
net_change = 0
net_change_list = []
total_net = 0

with open(input_file) as financial_data:
    fin_info = csv.reader(financial_data)
    header = next(fin_info)
    first_row = next(fin_info)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])

    for item in fin_info:
        total_months = total_months + 1
        total_net = total_net + int(item[1])
        net_change = int(item[1]) - prev_net
        prev_net = int(item[1])
        net_change_list = net_change_list + [net_change]
        monthly_change = monthly_change + [item[0]]

        if net_change > max_increase[1]:
            max_increase[0] = item[0]
            max_increase[1] = net_change

        if net_change < max_decrease[1]:
            max_decrease[0] = item[0]
            max_decrease[1] = net_change

net_monthly_avg = sum(net_change_list) / len(net_change_list)

output = (
    f"end analysis \n"
    f"---------------------------- \n"
    f"total months: {total_months} \n"
    f"net total: ${total_net} \n"
    f"average change: ${net_monthly_avg:.2f} \n"
    f"max increase: {max_increase[0]} (${max_increase[1]}) \n"
    f"max decrease: {max_decrease[0]} (${max_decrease[1]}) \n")

print(output)

with open(output_file, "w") as txt_file:
    txt_file.write(output)
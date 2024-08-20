import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
from statistics import mean

# vars for S&P market return
market_average = 7.9
market_stdev = 19

# vars for program behavior
num_reps = 500
num_bins = 15
view_annual_return_plot = False  # set to True only with a low num_reps since every single rep will display a plot
view_annual_balance_plot = False  # set to True only with a low num_reps since every single rep will display a plot
output_files = False

# vars of user for simulation
age = 16
start_balance = 1000
retire_age = 65
annual_contribution = 5000
end_balance_goal = 1000000

# initialize program vars
current_balance = 0
contribution_balance = 0
all_stats = []
years_to_retire = retire_age - age

for i in range(num_reps):
    current_balance_list = []

    annual_market_return_list = np.random.normal(market_average, market_stdev, years_to_retire).round(2)

    current_balance = start_balance
    contribution_balance = annual_contribution

    for item in annual_market_return_list:
        annual_return_float = float(item) * 0.01
        new_balance = current_balance * annual_return_float + current_balance + annual_contribution
        current_balance = new_balance
        contribution_balance = contribution_balance + annual_contribution
        current_balance_list.append(current_balance)

    df_return = pd.DataFrame(index=range(years_to_retire), data={"annual_return": annual_market_return_list,
                                                                 "balance": current_balance_list})
    if view_annual_return_plot:
        print("=== Annual Return Summary Table ===")
        print(df_return.describe())
        print("=" * 35)
        df_return['annual_return'].plot(kind='hist', title="Annual Return Distribution")
        plt.show()
        plt.close()

    if view_annual_balance_plot:
        df_return['balance'].plot(kind='line', title="Balance Over Time")
        plt.show()
        plt.close()

    all_stats.append({'start_balance': start_balance, 'contribution': contribution_balance,
                      'end_balance': round(current_balance, 0), 'average_return': mean(annual_market_return_list)})

df_all_stats = pd.DataFrame.from_dict(all_stats)
df_all_stats.round(4)

# output End Balance summary table
print("=" * 6 + " End Balance Table %s Runs " %(num_reps) + "=" * 6)
print(df_all_stats)
print("=" * 6 + " End Balance Summary Table %s Runs " %(num_reps) + "=" * 6)
print(df_all_stats.describe().round(0))
print("=" * 60)

success_rate = float(df_all_stats[df_all_stats['end_balance'] > end_balance_goal].count()['end_balance']) / float(num_reps)

print("Success rate of end balance greater than %s: %s" %(end_balance_goal, success_rate))

# prepare the save file names
random_digits = (str(int(random.random() * 1000)))  # for file name
csv_filename = "results/allstats_%s.csv" % (random_digits)
png_filename = "results/end_balance_dist_%s.png" % (random_digits)
png_clean_filename = "results/end_balance_dist_clean_%s.png" % (random_digits)

if output_files:
    # Save summary table
    df_all_stats.describe().to_csv(csv_filename)

    # Save success rate
    with open('results/success_rate.csv', 'a') as f:
        f.write(repr(random_digits) + ',' + repr(end_balance_goal) + ',' + repr(success_rate) + '\n')

    # Save cleaned end balance distribution histogram
    df_all_stats['end_balance'].plot(kind='hist', bins=num_bins, xticks=[], xlabel='', yticks=[], ylabel='')
    plt.savefig(png_clean_filename)
    plt.close()

df_all_stats['end_balance'].plot(kind='hist', title="End Balance Distribution", bins=num_bins, grid=True)
plt.axvline(x = end_balance_goal, c = 'r')
if output_files:
    # Save end balance distribution histogram
    plt.savefig(png_filename)
else:
    plt.show()
plt.close()

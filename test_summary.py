import sys
import glob
import pandas as pd

csv_files = glob.glob('results/allstats*.csv')

if len(csv_files) == 0:
    print('The results/allstats*.csv files were not found.  Run main.py with the "output_files = True" setting')
    sys.exit(1)

for item in csv_files:
    df = pd.read_csv(item)

    end_balance_mean = (df.at[1,'end_balance'])
    end_balance_std = (df.at[2,'end_balance'])

    average_return_mean = (df.at[1, 'average_return'])
    average_return_std = (df.at[2, 'average_return'])

    assert end_balance_mean > 2100000, f"end balance mean is too small, got {end_balance_mean}"
    assert end_balance_mean < 3000000, f"end balance mean is too large, got {end_balance_mean}"

    assert end_balance_std > 2300000, f"end balance std is too small, got {end_balance_std}"
    assert end_balance_std < 8100000, f"end balance std is too large, got {end_balance_std}"

    assert average_return_mean > 7.5, f"average return mean is too small, got {average_return_mean}"
    assert average_return_mean < 8.5, f"average return mean is too large, got {average_return_mean}"

    assert average_return_std > 2.5, f"average return std is too small, got {average_return_std}"
    assert average_return_std < 2.93, f"average return std is too large, got {average_return_std}"

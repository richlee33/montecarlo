import sys
import pandas as pd

try:
    df = pd.read_csv('results/success_rate.csv', header=None, usecols=[2])
except FileNotFoundError:
    print('The results/success_rate.csv file was not found.  Run main.py with the "output_files = True" setting')
    sys.exit(1)

df_summary = df.describe()
#print(df_summary)

success_rate_mean = df_summary.at['mean', 2]
success_rate_std = df_summary.at['std', 2]

assert success_rate_mean > .66, f"success rate mean is too small, got {success_rate_mean}"
assert success_rate_mean < .70, f"success rate mean is too large, got {success_rate_mean}"

assert success_rate_std > .020, f"success rate std is too small, got {success_rate_std}"
assert success_rate_std < .024, f"success rate std is too large, got {success_rate_std}"

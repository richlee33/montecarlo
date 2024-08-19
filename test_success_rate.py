import pandas as pd

df = pd.read_csv('results/success_rate.csv', header=None, usecols=[2])

df_summary = df.describe()
#print(df_summary)

success_rate_min = df_summary.at['min', 2]
success_rate_max = df_summary.at['max', 2]

#print(success_rate_min)
#print(success_rate_max)

assert success_rate_min > .62, f"success rate min is too small, got {success_rate_min}"
assert success_rate_min < .65, f"success rate min is too large, got {success_rate_min}"

assert success_rate_max > .72, f"success rate max is too small, got {success_rate_max}"
assert success_rate_max < .73, f"success rate max is too large, got {success_rate_max}"

# %% import pandas and read the csv file 
# modify the path if needed
import pandas as pd

df = pd.read_csv("..\lab1\rectangles.csv")
# df["area"] = ?

# %%
summary = [
    ("Total Count", df["area"].shape[0]),
    ("Total Area", df["area"].sum()),
    # ("Average Area", ?),
    # ("Maximum Area", ?),
    # ("Minimum Area", ?),
]

for key, value in summary:
    print(f"{key}: {str(value)}")

# %%
# pd.DataFrame(dict(summary), index=[0]).?

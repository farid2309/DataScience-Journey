import pandas as pd
import matplotlib.pyplot as plt

csv_path = "seagal.csv"

df = pd.read_csv(csv_path, sep=";")

dataFrame = pd.DataFrame(df)

dataFrame["Profit"] = dataFrame["box_office"] - dataFrame["budget"]

sorted_df = dataFrame.sort_values(by="Profit", ascending=False)

print(sorted_df)
print(sorted_df.info())

sorted_df.plot(x="film", y="Profit", kind="bar", color="blue", alpha=0.5)
plt.xlabel("Film")
plt.ylabel("Profit")
plt.title("Steven Seagal Movie Profitability")
plt.legend()
plt.show()

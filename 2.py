import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "3.xlsx"
df = pd.read_excel(file_path)

print("DataFrame:")
print(df)

size_col = df.columns[0]

alg_cols = df.columns[1:]

plt.figure(figsize=(10, 6))
x = range(len(df))
width = 0.25

for i, col in enumerate(alg_cols):
    plt.bar([p + i*width for p in x], df[col], width=width, label=col)

plt.xticks([p + width for p in x], df[size_col], rotation=45)
plt.xlabel("Data Size")
plt.ylabel("Run Time")
plt.title("Bar Chart of Algorithms Runtime")
plt.legend()
plt.tight_layout()
plt.savefig("bar_chart.png", dpi=300)
plt.close()

plt.figure(figsize=(10, 6))
for col in alg_cols:
    plt.plot(df[size_col], df[col], marker='o', label=col)

plt.xlabel("Data Size")
plt.ylabel("Run Time")
plt.title("Line Chart of Algorithms Runtime")
plt.legend()
plt.tight_layout()
plt.savefig("line_chart.png", dpi=300)
plt.close()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[alg_cols])
plt.xticks(range(len(alg_cols)), alg_cols)
plt.xlabel("Algorithms")
plt.ylabel("Run Time")
plt.title("Box Plot of Algorithms Runtime")
plt.tight_layout()
plt.savefig("box_plot.png", dpi=300)
plt.close()

mean_alg2 = df["Alg.2"].mean()
print("\nMean runtime of Alg.2:", mean_alg2)

new_row = pd.DataFrame([["700KB", 80, 320, 700]], columns=df.columns)
df_updated = pd.concat([df, new_row], ignore_index=True)

print("\nUpdated DataFrame:")
print(df_updated)

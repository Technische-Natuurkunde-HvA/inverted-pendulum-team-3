import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data\data_22-11-2025_19-59.csv")

df.plot(x='Time', subplots=True, layout=(3, 1), figsize=(8, 10), title=['Angle', 'Output', 'RPM'])
plt.tight_layout()  # adjusts spacing
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data\DataUpsideDownFinal.csv")

df.plot(x='Time', subplots=True, layout=(3, 1), figsize=(8, 10), title=['Angle', 'Output', 'RPM'])
plt.tight_layout()  # adjusts spacing
plt.show()


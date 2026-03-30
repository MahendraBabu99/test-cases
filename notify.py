import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'git projects' : [1, 2, 3, 4, 5],
    'stars' : [10, 2, 6, 8, 4]
}

df  = pd.DataFrame(data)

sns.lineplot(x='git projects', y='stars', data=df, markers='o')
plt.show()

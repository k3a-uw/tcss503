from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_data(centers, points_per, std_dev, seed=None):
    np.random.seed(seed)
    x = None
    y = None
    for m in centers:
        if x is None:
            x = np.random.normal(m, std_dev, size=points_per)
            y = np.random.normal(m, std_dev, size=points_per)
        else:
            x = np.hstack((x, np.random.normal(m, std_dev, size=points_per)))
            y = np.hstack((y, np.random.normal(m, std_dev, size=points_per)))

    return pd.DataFrame({'x': x, 'y': y})

def draw_plot(df, colors='grey'):
    plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=colors, cmap='brg')
    plt.show()


df = generate_data(centers=[10, 15, 20], points_per=10, std_dev=2, seed=10)
draw_plot(df)
model = KMeans(n_clusters=2)
model.fit(df)
plt.scatter(df.x, df.y, c=model.labels_, cmap='brg')
plt.show()
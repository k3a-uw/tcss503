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

def draw_plot_with_predicts(train, colors, test, predictions):
    ax = plt.gca()
    ax.scatter(train.iloc[:, 0], train.iloc[:, 1], c=colors, cmap='brg')
    ax.scatter(test.iloc[:, 0], test.iloc[:,1], c=predictions, cmap='brg', marker='x')
    plt.show()

df = generate_data(centers=[10, 15, 20], points_per=10, std_dev=2, seed=10)
draw_plot(df)
model = KMeans(n_clusters=3)
model.fit(df)
plt.scatter(df.x, df.y, c=model.labels_, cmap='brg')
plt.show()

new_point = pd.DataFrame({'x': [12, 16, 22], 'y': [12, 16, 22]})
new_labels = model.predict(new_point)

draw_plot_with_predicts(df, model.labels_, new_point, new_labels)

def cosine_distance(x1, x2):
    x1_magnitude = np.sqrt(np.sum(np.square(x1)))
    x2_magnitude = np.sqrt(np.sum(np.square(x2)))
    return 1 - np.dot(x1, x2) / (x1_magnitude * x2_magnitude)

import seaborn as sns

sns.clustermap(df, col_cluster=False)
plt.show()

import scipy.cluster.hierarchy as shc
model = shc.linkage(df)
dend = shc.dendrogram(model)
plt.show()
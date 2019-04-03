from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()
# 数据集

# print(iris)

knn.fit(iris.data, iris.target)

predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
#进行预测

print(predictedLabel)
from sklearn import svm

X = [[2, 0], [1, 1], [2,3]]
y = [0, 0, 1]
clf = svm.SVC(kernel = 'linear')
#SVC支持向量机
clf.fit(X, y)

print (clf)

# get support vectors
print (clf.support_vectors_)

# get indices of support vectors下标
print (clf.support_)

# get number of support vectors for each class多少个点
print (clf.n_support_ )




print(clf.predict([[2,.0]]))
# print(clf.predict([2 ,.0]))

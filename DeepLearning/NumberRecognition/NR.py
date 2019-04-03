from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras import models
from keras import layers
from keras.utils import to_categorical

(train_images,train_labels), (test_images,test_labels) = mnist.load_data()
print(train_images)
print(train_labels)
print(test_images.shape)
print(test_labels)
digit = test_images[1]
plt.imshow(digit,cmap=plt.cm.binary)
plt.show()
network = models.Sequential()
#串联起来
network.add(layers.Dense(512, activation='relu', input_shape=(28*28, )))
#二维数组
network.add(layers.Dense(10, activation="softmax"))
network.compile(optimizer='rmsprop', loss='categorical_crossentropy',
               metrics=['accuracy'])

train_images = train_images.reshape((60000,28*28))
train_images = train_images.astype('float32')/255

test_images = test_images.reshape((10000,28*28))
test_images = test_images.astype('float32')/255

print("转换前：", test_labels[0])
train_labels = to_categorical(train_labels)
test_labels  = to_categorical(test_labels)
print("转换后：", test_labels[0])

network.fit(train_images, train_labels, epochs=5, batch_size=128)

test_loss ,test_acc = network.evaluate(test_images, test_labels, verbose=1)
print("准确度：",test_acc)

res = network.predict(test_images)

for i in range(res[1].shape[0]):
    if (res[1][i] == 1):
        print("the number for the picture is : ", i)
        break
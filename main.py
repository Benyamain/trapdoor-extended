from keras.models import load_model

mnist_model = load_model('trapdoor/models/mnist_model.h5')
cifar_model = load_model('trapdoor/models/cifar_model.h5')

mnist_model.summary()
cifar_model.summary()
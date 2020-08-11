# https://github.com/qubvel/classification_models
# install from git source.


# for keras
#from classification_models.keras import Classifiers

# for tensorflow.keras
from classification_models.tfkeras import Classifiers

ResNet18, preprocess_input = Classifiers.get('resnet18')
model = ResNet18((224, 224, 3), weights='imagenet')

model.save("resnet18_model.h5")

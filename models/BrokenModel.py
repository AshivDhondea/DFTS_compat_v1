#import keras hans commented out 17 june 2020.
#import tensorflow as tf
#from tf.keras.layers import Input
#from tf.keras.models import Model

# 22 June 2020
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

from .utils.cloud import remoteModel, modelOut
import numpy as np

class BrokenModel(object):
    """Can split the model at the given layer into two parts.
    """
    def __init__(self, model, splitLayer, custom_objects):
        """
        # Arguments
            model: keras model to be split
            splitLayer: layer to split the model at
        """
        super(BrokenModel, self).__init__()
        self.model      = model
        self.layers     = [i.name for i in self.model.layers]
        self.splitLayer = splitLayer
        self.layerLoc   = self.layers.index(self.splitLayer)
        self.custom_objects = custom_objects

    def splitModel(self):
        """Splits the given keras model at the specified layer.
        """
        deviceOuts, remoteIns, skipNames = modelOut(self.model, self.layers, self.layerLoc)

        self.deviceModel = tf.keras.models.Model(inputs=self.model.input, outputs=deviceOuts)
        self.remoteModel = remoteModel(self.model, self.splitLayer, self.custom_objects)

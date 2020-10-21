from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense


def add_projection_head(base_model, projectionHeadMode, resnet50=False):
    if projectionHeadMode == "linear":
        return get_linear_head(base_model, resnet50=resnet50)
    elif projectionHeadMode == "nonlinear":
        return get_non_linear_head(base_model, resnet50=resnet50)
    elif projectionHeadMode == "none":
        return base_model  # We are just passing the input hiddens as output
    else:
        raise Exception("This mode for the projection head is not supported: " + str(projectionHeadMode))


def get_linear_head(base_model, resnet50=False):
    if resnet50:
        return Dense(2048, name="projection_head_linear")(base_model)
    else:
        return Dense(512, name="projection_head_linear")(base_model)


def get_non_linear_head(base_model, resnet50=False):
    """
    :param base_model: The output of the hidden from the base model (ResNet)
    :return: Output of the last hidden layer in the MLP (projection head)
    """
    if resnet50:
        projection_1 = Dense(2048, name="projection_head_1")(base_model)
        projection_1 = Activation("relu")(projection_1)
        projection_2 = Dense(128, name="projection_head_2")(projection_1)
    else:
        projection_1 = Dense(512, name="projection_head_1")(base_model)  # Original paper is 2048
        projection_1 = Activation("relu")(projection_1)
        projection_2 = Dense(32, name="projection_head_2")(projection_1)  # Original paper is 128
    return projection_2

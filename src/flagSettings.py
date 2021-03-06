# This file contain all the settings and flags that is changeable for the model
import lossFunctions

# Data settings
data_set = "cifar-10"
num_classes = 10  # CIFAR-10

# Encoder settings
input_shape = (32, 32, 3)

# Warm up
nr_epochs_warmup = 10
weight_decay_layers = 10e-6

# Pretraining settings
learning_rate = 0.5
temperature = 0.1  # Temperature in the loss function
batch_size = 128
weight_decay = 10e-6
loss_function = lossFunctions.NT_Xent_loss
nr_epochs = 100
use_checkpointing = True

# Image augmentation settings
color_jitter_strength = 0.5
use_gaussian_blur = False
augmentation_type = 'simclr'  # 'rand' or 'simclr'
rand_augs = 3  # The number of augments to do (N)
rand_strength = 5  # How strong the augments will be (M)

# Fine-tune settings
percentage_fine_tune_data = 0.01
fine_tune_batch_size = 128
fine_tune_momentum = 0.9
fine_tune_lr = 0.025  # Following this formula (0.05 * batch_size/ 256)
fine_tune_nr_epochs = 60  # For 1% data => 60 epochs, 10% data => 30 epochs

# Linear Evaluation settings
linear_evaluation_nr_epochs = 90
linear_evaluation_lr = 0.1  # Following this formula (0.1 * batch_size/ 256)
linear_evaluation_momentum = 0.9
linear_evaluation_batch_size = 128

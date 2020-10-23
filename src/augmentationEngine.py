# abstact class representing a sequence of augmentation transformations


from dataAugmentations import *
from randAugment import *

AUTOTUNE = tf.data.experimental.AUTOTUNE
from flagSettings import *


class AugmentationEngine:
    def transform(self, data):  # function to be implemented with a sequence of trasformations
        pass


class SimClrAugmentation(AugmentationEngine):
    def transform(self, data, augment=augmentation_type):
        if augment == 'simclr':
            print('using simclr augmentations')
            data = data.map(lambda x, y: (augmentBatch(x, y)),
                            num_parallel_calls=AUTOTUNE)
        if augment == 'rand':
            print('using randaug augmentations')
            aug = RandAugment(rand_augs, rand_strength)
            data = data.map(lambda x, y: (aug.__call__(x, y)),
                            num_parallel_calls=AUTOTUNE)
        return data


class TestAugmentation(AugmentationEngine):
    def transform(self, data):
        data = data.map(lambda x, y: (x, x, x, y),
                        num_parallel_calls=AUTOTUNE)
        print('using test augmentations')
        return data


class AugmentationStudy(AugmentationEngine):
    def __init__(self, augmentation1, augmentation2):
        self.augmentation1 = augmentation1
        self.augmentation2 = augmentation2

    # @tf.function
    def augment(self, input_data, augmentation_type1, augmentation_type2):
        augmentations = [augmentation_type1, augmentation_type2]
        x = input_data
        for augmentation in augmentations:
            if augmentation == "crop":
                x = crop_resize(x)
            elif augmentation == "cutout":


                print(input_data)
                for x,y in input_data:
                    plt.imshow(x.numpy())



                x = cut_out(x)
            elif augmentation == "color":
                x = color_jitter(x, s=1)
            elif augmentation == "sobel":
                x = sobel(x)
            elif augmentation == "gaussian_noise":
                raise NotImplemented("Gaussian noise not implemented")
            elif augmentation == "gaussian_blur":
                std = random.uniform(.1, 2)
                x = gaussian_blur(x, std)
            elif augmentation == "rotate":
                x = rotate_randomly(x)
            elif augmentation == "nothing":
                pass
            else:
                raise Exception("Invalid argument for augment test")
        return x

    def transform(self, data):
        """
        We augment 1 image and keep the second one the same
        :param data:
        :return: (image, augmented image, image, labels)
        """
        data = data.map(lambda x, y: (x, self.augment(x, self.augmentation1, self.augmentation2), x, y),
                        num_parallel_calls=AUTOTUNE)
        return data

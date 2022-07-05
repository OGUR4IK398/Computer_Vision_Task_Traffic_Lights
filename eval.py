import numpy as np
import cv2


def one_hot_encode(label):

    """ Функция осуществляет перекодировку текстового входного сигнала
     в массив элементов, соответствующий выходному сигналу

     Входные параметры: текстовая метка

     Выходные параметры: метка ввиде массива

     Пример:

        one_hot_encode("red") должно возвращать: [1, 0, 0]
        one_hot_encode("yellow") должно возвращать: [0, 1, 0]
        one_hot_encode("green") должно возвращать: [0, 0, 1]

     """

    one_hot_encoded = []

    if label == "red":
        one_hot_encoded = [1, 0, 0]
    elif label == "yellow":
        one_hot_encoded = [0, 1, 0]
    elif label == "green":
        one_hot_encoded = [0, 0, 1]

    return one_hot_encoded

# приведение входного изображения к стандартному виду
def standardize_input(image):
    standard_im = image
    """Приведение изображений к стандартному виду. 
    Входные данные: изображение
    Выходные данные: стандартизированное изображений.
    """

    ## TODO: Если вы хотите преобразовать изображение в формат, одинаковый для всех изображений, сделайте это здесь.

    return standard_im

# Определение сигнала светофора по изображению

def predict_label(rgb_image):
    """
     функция определения сигнала светофора по входному изображению

     Входные данные: rgb изображение
     Выходные данные:

    """
    ## TODO: ваша функция распознавания сигнала светофора должна быть здесь.
    predicted_label = "yellow"
    encoded_label = one_hot_encode(predicted_label)

    return encoded_label

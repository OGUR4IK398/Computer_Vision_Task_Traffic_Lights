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
    # Преобразуем к общему размеру и переводим кодировку в HSV
    # Получаем значения высоты и ширины картинки
    height, width = standard_im.shape[:2]
    print(width, height)

    standard_im = cv2.resize(standard_im, (int(height * 0.75), int(width * 0.8)))
    standard_im = cv2.cvtColor(standard_im, cv2.COLOR_BGR2HSV)
    # Фильтруем по яркости
    # standard_im = standard_im_hsv[:, :, 2]


    return standard_im

# Определение сигнала светофора по изображению

def predict_label(rgb_image):
    """
     функция определения сигнала светофора по входному изображению

     Входные данные: rgb изображение
     Выходные данные:

    """
    ## TODO: ваша функция распознавания сигнала светофора должна быть здесь.
    # Получаем черно-белое изображение
    image = standardize_input(rgb_image)
    image = image[:, :, 2]

    # Общее изменение цвета даёт небольшой прирост (~1.5 %)
    image = image.astype(np.float64)
    image += 40
    image = np.clip(image, 0, 255)
    image = image.astype(np.uint8)

    height_step = int(image.shape[0] / 3)


    # Считаем кол-во белого в каждом секторе
    red_weight = np.sum(image[0:height_step, :])
    yellow_weight = np.sum(image[height_step:2 * height_step, :])
    green_weight = np.sum(image[2 * height_step:3 * height_step, :])

    # Там где максимальное кол-во белого - там находится включенный цвет светофора
    if max([red_weight, yellow_weight, green_weight]) == red_weight:
        predicted_label = "red"
    elif max([red_weight, yellow_weight, green_weight]) == yellow_weight:
        predicted_label = "yellow"
    else:
        predicted_label = "green"

    encoded_label = one_hot_encode(predicted_label)

    return encoded_label

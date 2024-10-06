import os
import shutil
import cv2
import datetime


def dir_check(filepath, print_flag=True, empty_flag=False):
    if os.path.exists(filepath) and empty_flag:
        del_file(filepath)
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    if print_flag:
        print('Output folder %s has been cleaned and created' % filepath)


def del_file(filepath):
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


if __name__ == '__main__':

    start = datetime.datetime.now()
    input_dir = [r'ct_scans/covid_test',r'ct_scans/covid_train']
    output_dir = ['train', 'test', 'show']
    dir_check(output_dir[0], empty_flag=True)
    dir_check(output_dir[1], empty_flag=True)
    dir_check(output_dir[2], empty_flag=True)
    num1 = 1  
    for f in os.listdir(input_dir[0]):
        if num1 <= 500:
            img_path = os.path.join(input_dir[0], f)
            img = cv2.imread(img_path)  
            cv2.imwrite(os.path.join(output_dir[0], '%d.png' % num1), img)  
            end = datetime.datetime.now()  
            num1 = num1 + 1
    num2 = 1
    for f in os.listdir(input_dir[1]):
        if num2 <= 200:
            img_path = os.path.join(input_dir[1], f)
            img = cv2.imread(img_path) 
            b, g, r = cv2.split(img)
            cv2.imwrite(os.path.join(output_dir[1], '%d.png' % num2), img) 
            end = datetime.datetime.now() 
            num2 = num2 + 1

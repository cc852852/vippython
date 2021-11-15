# 咕噜咕噜的丁丁
# 不浪费一分一秒
# 你可以的
# 时间：2021/9/25 21:31
import heapq

import cv2 as cv
import numpy as np

def show(name,img):
    cv.namedWindow(name,cv.WINDOW_NORMAL)
    cv.inshow(name,img)
    cv.waitKey()
    cv.destroyAllWindows()

def get_A(img,row,col,k=100):
    RGB_min = np.min(img,axis=2).ravel()

    max_c = heapq.nlargest(k,range(len(RGB_min)),RGB_min.take)
    max_c = np.unravel_index(max_c,(row,col),order='C')
    c_x , c_y = zip((max_c[0],max_c[1]))

    hun_max = np.sum(img[c_x,c_y],axis=2)
    sum_max = np.argmax(hun_max)

    A = img[c_x[0][sum_max],c_y[0][sum_max]]
    A = np.tile(A,(row,col,1))

def main():
    path = r'E:\Snipaste_2021-09-25_22-02-15.png'
    img = cv.imread(path)

    row,col,c = img.shape
    show('img',img)

    inv = 255 -img
    show('inv',inv)

    inv=inv.astype(np.float)

    A = get_A(inv,row,col)
    tx = get_tx(inv, row, col,A)

    p = np.zeros_like(tx)

import cv2 as cv
import os
import random
import math
import numpy as np
import skimage

class predeal:

    def color2black(self,path):
        fname, fjpg = path.split('.', 1)
        img = cv.imread(path)
        rows, cols = img.shape[:2]

        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        retval, img_at_fixed = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY)
        newpath = fname + '-bw.' + fjpg
        cv.imwrite(newpath, img_gray)

    def addNoise(self,path,type):
        fname, fjpg = path.split('.', 1)

        im = skimage.io.imread(path)
        dst = skimage.util.random_noise(im, mode=type, seed=None, clip=True) #‘gaussian’,‘localvar’,‘poisson’,‘salt’,‘pepper’,‘s&p’ ,‘speckle’
        # cv.imshow('1',dst)
        # cv.waitKey(0)
        newpath = fname + '-n.' + fjpg
        skimage.io.imsave(newpath, dst)

    def SaltAndPepper(self,path, percetage):
        fname, fjpg = path.split('.', 1)
        src = cv.imread(path)
        NoiseImg = src
        NoiseNum = int(percetage * src.shape[0] * src.shape[1])
        for i in range(NoiseNum):
            randX = random.randint(0, src.shape[0] - 1)
            randY = random.randint(0, src.shape[1] - 1)
            if random.randint(0, 1) == 0:
                NoiseImg[randX, randY] = 0
            else:
                NoiseImg[randX, randY] = 255
        newpath = fname + '-n.' + fjpg
        cv.imwrite(newpath,NoiseImg)


    def rotate(self,path,degree,flag):
        #print(degree)
        fname, fjpg = path.split('.', 1)
        img = cv.imread(path)
        rows, cols = img.shape[:2]

        if degree == 90:
            dst = np.rot90(img)
            newpath = fname + flag + fjpg
            cv.imwrite(newpath, dst)

        elif degree == 270:
            #print(1)
            dst = np.rot90(img,3)
            newpath = fname + flag + fjpg
            cv.imwrite(newpath, dst)

        else:
            # print(degree)
            #print(2)
            degree_new = math.degrees(math.atan(rows / cols))
            # print(degree_new)
            length = math.pow(rows * rows + cols * cols, 1 / 2)
            # 角度为degree时
            rows_new1 = abs(length * math.sin(math.radians(degree + degree_new)))

            cols_new1 = abs(length * math.cos(math.radians(degree_new + degree)))
            # 角度为-degree_new时
            rows_new2 = abs(length * math.sin(math.radians(degree - degree_new)))
            cols_new2 = abs(length * math.cos(math.radians(degree - degree_new)))

            rows_new = max([rows_new2, rows_new1])
            cols_new = max([cols_new2, cols_new1])

            # print(str(rows_new1)+','+str(rows_new2)+','+str(rows))
            # print(str(cols_new1)+',' +str(cols_new2)+ ',' + str(cols))

            propotion1 = rows / rows_new
            propotion2 = cols / cols_new

            propotion = min([propotion1, propotion2])
            if propotion > 1:
                propotion = 1

            # print(propotion)

            M = cv.getRotationMatrix2D((cols / 2, rows / 2), degree, propotion)
            dst = cv.warpAffine(img, M, (cols, rows))
            newpath = fname + flag + fjpg
            cv.imwrite(newpath, dst)

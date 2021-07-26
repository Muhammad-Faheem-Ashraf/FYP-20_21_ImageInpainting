# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:44:03 2020

@author: i1701
"""

from skimage import io, img_as_float
import bm3d
import cv2
import numpy as np
from PIL import ImageEnhance
from skimage.restoration import denoise_nl_means, estimate_sigma
from PIL import Image

class Noise:
  def __init__(self, Img):
    self.noisyImg = Img
  def deNoiseColor_Img(self):
      
      image = img_as_float(io.imread("potw1948a.jpg", as_gray=False))
      
      
      
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**1
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      #BM3D_denoised_image = bm3d.bm3d(image, sigma_psd=0.5, stage_arg=bm3d.BM3DStages.ALL_STAGES)
      
      sigma_est = np.mean(estimate_sigma(image, multichannel=True))
      print(sigma_est)
      BM3D_denoised_image1 = bm3d.bm3d(image, .2, stage_arg=bm3d.BM3DStages.ALL_STAGES)
      
      io.imsave("testing.png",BM3D_denoised_image1)
      
      cv2.imshow("Denoised1", BM3D_denoised_image1)
      cv2.imshow("Orignal",image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      
  def deNoiseBaW_Img(self):
      
      image = img_as_float(io.imread("image.png", as_gray=True))
      
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**1
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      BM3D_denoised_image = bm3d.bm3d(image, sigma_psd=0.5, stage_arg=bm3d.BM3DStages.ALL_STAGES)
      sigma_est = np.mean(estimate_sigma(BM3D_denoised_image, multichannel=True))
      BM3D_denoised_image1 = bm3d.bm3d(BM3D_denoised_image, sigma_est, stage_arg=bm3d.BM3DStages.ALL_STAGES)
      io.imsave("testing.png",BM3D_denoised_image)
      
      
  def Sharpening_Img(self):      
      imageObject1 = Image.open("potw1948a.jpg")
      imageObject = Image.open("testing.png")
      enhancer=ImageEnhance.Sharpness(imageObject)
      f=.5
      fn=enhancer.enhance(f)
      imageObject1.show("Orignal")
      fn.save("sharp.png")
      fn.show()
    
    


a=Noise("helo")
a.deNoiseColor_Img()
a.Sharpening_Img()

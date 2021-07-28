# FYP-20_21_ImageInpainting


In today’s time, the use of digital photography has become such an important part of our life that from ID cards to Security footages, everything revolves around it. But sometimes the image you capture may not be what you were looking for. This is where image inpainting plays a vital role. Image inpainting can be described as a process to restore damaged or deteriorated image, or to super resolution an image. The purpose of our project is to use deep learning models on image inpainting in order to remove restore images for modern times without user intervention. The user will be to inpaint the images using a web-based interface.



For Denoising Purpose we are using BM3D library
In "Noise.py" file to denoise the image


For Super Resolution Purpose we are using simple CV2 library functions
In "superresolution.ipynb" we are enhancing the image quality


For Colorization Purpose we are using a Research Paper CHROMA-GAN
In "training-chroma.ipynb" file we are using it to train our model (New/transfer Learning)
In "Testing_chroma.ipynb" file we are using it to get colorized images from our trained model (by predicting the colors)


For Restroration Purpose we are using a Research Paper "Old Photo Restoration via Deep Latent Space Translation"
In "imageResoration.ipynb" file we implement the functionalities of image restoration, denoising and super-resolution


In "Cloud_Linkage_Iteration_4.ipynb" we are deploying our Denoiseing Module on Azure cloud

For front end Purpose we used Flutter
In "quicover.zip" all the files required for flutter app are present

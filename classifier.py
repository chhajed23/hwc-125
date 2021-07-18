import numpy as np
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LogisticRegression
from sklearn.datasets import fetch_openml
import PIL.ImageOps

X=np.load('image.npz')['arr_0']
y=pd.read_csv("labels.csv")["labels"]
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=9,train_size=3500,test_size=500)
X_train_scaled=X_train/255.0
X_test_scaled=X_test/255.0
clf=LogisticRegression(solver="saga",multi_class='multinomial').fit(X_train_scaled,y_train)
def getPrediction(image):
    im_pil=Image.open(image)
    image_bw=im_pil.convert('L')
    image_bw_resize=image_bw.resize((28,28),Image.ANTIALIAS)
    pixel_filter=20
    min_pixel=np.percentile(image_bw_resize,pixel_filter)
    image_bw_resize_invert=np.clip(image_bw_resize-min_pixel,0,255)
    max_pixel=np.max(image_bw_resize)
    image_bw_resize_invert=np.asarray(image_bw_resize_invert)/max_pixel
    test_sample=np.array(image_bw_resize_invert).reshape(1,784)
    test_pred=clf.predict(test_sample)
    return test_pred[0]

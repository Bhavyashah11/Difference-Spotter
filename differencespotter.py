from PIL import Image,ImageChops
img1=Image.open("image1.jpg")
img2=Image.open("image2.jpg")
diff=Image.Chops.difference(img1,img2)
if diff.getbbox():
    diff.show()

from PIL import Image

 

# Create an Image object from an Image

colorImage  = Image.open("./test (16).jpg")

 

# Rotate it by 45 degrees

rotated     = colorImage.rotate(45)

colorImage.show()

rotated.show()

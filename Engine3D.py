#Andree Toledo 18439    
#Lab 5

from gl import Render
from gl import color


render = Render()

render.load('cuerpo.obj', translate=(550, 100, 0), scale = (75, 75, 400))

render.glFinish(filename='output.bmp')
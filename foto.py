from picamera import PiCamera

def tirarFoto():
   camera = PiCamera()
   
   camera.resolution = (1200, 800)
   camera.capture("imagens/entrada.jpg")

   camera.close()
##   with picamera.PiCamera() as picx:
#      picx.start_preview()
#      time.sleep(5)
#      picx.capture('imagens/entrada.jpg')
#      picx.stop_preview()
#      picx.close()

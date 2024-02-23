import cv2

def count():
	# Carregue o classificador pré-treinado para detecção de pessoas
	hog = cv2.HOGDescriptor()
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

	# Carregue a imagem
	image = cv2.imread('imagens/entrada.jpg')

	# Execute a detecção de pessoas na imagem
	boxes, weights = hog.detectMultiScale(image, winStride=(8, 8))

	# Exiba o total de pessoas na imagem
	total_pessoas = len(boxes)
	return total_pessoas
#	print(f"Total de pessoas na imagem: {total_pessoas}")

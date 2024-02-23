import cv2
import numpy as np
import os

# Diretório do modelo YOLO
yolo_dir = 'yolo'

# Caminhos para o modelo YOLO
yolo_weights = os.path.join(yolo_dir, 'yolov3-tiny.weights')
yolo_cfg = os.path.join(yolo_dir, 'yolov3-tiny.cfg')
yolo_names = os.path.join(yolo_dir, 'coco.names')

# Carregue o modelo YOLO pré-treinado
net = cv2.dnn.readNet(yolo_weights, yolo_cfg)

# Carregue as classes que o modelo YOLO pode detectar
with open(yolo_names, 'r') as f:
    classes = f.read().strip().split('\n')

# Carregue a imagem local
image_path = 'imagens/1.jpg'
image = cv2.imread(image_path)

# Redimensione a imagem para um tamanho adequado ao modelo YOLO
blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)

# Defina a entrada para a rede neural
net.setInput(blob)

# Execute a detecção de objetos
detections = net.forward()

# Inicialize a variável de contagem de pessoas
person_count = 0

for detection in detections:
    scores = detection[5:]
    class_id = np.argmax(scores)
    confidence = scores[class_id]

    if confidence > 0.5 and classes[class_id] == 'person':
        person_count += 1

# Mostre o total de pessoas na imagem
print(f'Total de Pessoas: {person_count}')

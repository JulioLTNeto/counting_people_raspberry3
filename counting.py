import cv2
import numpy as np

def count():
    # Carregar arquivos do YOLO
    net = cv2.dnn.readNet('yolo/yolov3-tiny.weights', 'yolo/yolov3-tiny.cfg')
    classes = []

    with open('yolo/coco.names', 'r') as f:
        classes = f.read().strip().split('\n')

    # Carregar imagem
    image = cv2.imread('imagens/5.jpg')

    # Obter dimensões da imagem
    height, width, _ = image.shape

    # Preparar imagem para detecção
    blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(net.getUnconnectedOutLayersNames())  # Obter nomes das camadas de saída

    # Informações de detecção
    class_ids = []
    confidences = []
    boxes = []

    # Definir limite de confiança
    confidence_threshold = 0.5

    # Processar as detecções
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > confidence_threshold:
                # Coordenadas da caixa delimitadora
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Coordenadas da caixa delimitadora (canto superior esquerdo)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Aplicar supressão não máxima para eliminar caixas delimitadoras sobrepostas
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, 0.4)

    # Contagem de pessoas detectadas
    person_count = 0

    # Desenhar as caixas delimitadoras e contar pessoas
    for i in range(len(boxes)):
        if i in indexes:
            label = str(classes[class_ids[i]])
            if label == 'person':
                person_count += 1
                x, y, w, h = boxes[i]
                color = (0, 255, 0)  # Cor da caixa delimitadora (verde)
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    # Salvar a imagem com as caixas delimitadoras
    cv2.imwrite('imagens/saida.jpg', image)

    # print(imagem_64)

    # Exibir o número de pessoas detectadas
    # print(f'Número de pessoas detectadas: {person_count}')
    return(person_count)

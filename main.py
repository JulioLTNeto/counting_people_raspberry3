import counting
import counting_without_yolo
import api
import baseConverter
import datetime
import foto
import configs

import time

def foraH():
    # Obtenha a data e hora atual
    agora = datetime.datetime.now()
    
    config = configs.getConfigs()

    # Extraia as horas, minutos e segundos
    horas = agora.hour
    #print(horas)
    if (horas >= config["hora_comeca"] & horas <= config["hora_termina"]):
        return(True)
    
    return(False)
    
def gravaConfiguracoes():
    config = configs.getConfigs()
    id_config_camera = '1'
    try:
        id_config_camera = str(config["id_config_camera"])
    except NameError as e:
        id_config_camera = '1'
    except KeyError as e:
        id_config_camera = '1'
        
    resposta = api.pegarConfiguracoes(id_config_camera)
    nome = resposta["nome"]
    configs.setConfig("nome", nome)
    hora_comeca = resposta["hora_comeca"]
    configs.setConfig("hora_comeca", hora_comeca)
    hora_termina = resposta["hora_termina"]
    configs.setConfig("hora_termina",hora_termina)
    intervalo = resposta["intervalo"]
    configs.setConfig("intervalo", intervalo)
    return True

def main():
    
    gravaConfiguracoes()
    
    valores = configs.getConfigs()
    id_camera = 0
    #Realizando o cadastro da câmera se não tiver
    if valores["id_camera"] == 0:
        id_camera = api.cadastrarCamera()
        print(id_camera)
        configs.setConfig("id_camera", id_camera)
    
    valores = configs.getConfigs()
    id_camera = valores["id_camera"] 

    sair = 1
    estado = 'IDLE'
    imagem_64 = ''

    while(1):

        total = 0

        if estado == 'IDLE':
            if foraH() == True:
                estado = 'CONFIG'

            print("Estado IDLE - INATIVO")
        
        elif estado == 'CONFIG':
            gravaConfiguracoes()
            estado = 'INFO'
            
            print("Estado CONFIG - INFO")

        elif estado == 'INFO':
            if foraH() == False:
                estado = 'IDLE'
            
            print("Capturando foto...")
            foto.tirarFoto()

            print("Estado INFO -> PROCESS")
            estado = 'PROCESS'

        elif estado == 'PROCESS':
            print("Contando as pessoas na imagem...")
            total = counting_without_yolo.count()
            print('PESSOAS ENCONTRADAS: ', total)
            
            print("Convertendo imagem para base64..")
            imagem_64 = baseConverter.converter()
            
            print("Estado PROCESS -> ENV")

            estado = 'ENV'

        elif estado == 'ENV':
            if foraH() == False:
                estado = 'IDLE'
            print("Enviando informações para o servidor...")
            retorno = api.cadastrarFoto(id_camera, total, imagem_64)
            print("Estado ENV -> INFO")
            print("Delay de 5 minutos para o próximo ciclo")
            time.sleep(valores["intervalo"])
            estado = 'INFO'

        #sair = input("Sair? 0 Para Sim: ")

main()

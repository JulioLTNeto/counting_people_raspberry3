
import os
from supabase_py import create_client

# Configurações do Supabase
SUPABASE_URL = 'SUA_URL_SUPABASE'
SUPABASE_KEY = 'SUA_CHAVE_SUPABASE'

# É nescessário ter uma extrutura de banco de dados no supabase semelhante a usada nesse. No caso você pode criar uma do zero e fazer as alterações nescessárias.

# Criar cliente Supabase
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def cadastrarCamera():
    # Dados para inserção
    dados_para_inserir = {'nome': 'Camera01', 'id_setor': 1, 'id_config_camera': 1}

    try:
        # Inserir dados na tabela e obter o ID gerado
        response = supabase.table('camera').insert(dados_para_inserir).execute()
        print("Resposta da rota")
        print(response)
        # Verificar e lidar com a resposta
        if 'data' in response and len(response['data']) > 0 and 'id' in response['data'][0]:
            novo_id = response['data'][0]['id']
            print(f"Novo ID inserido: {novo_id}")
            return novo_id
        else:
            print("Nenhum ID retornado")
            return -1

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
        return -2

def cadastrarFoto(id_camera, quant_pessoas, foto):
    # Dados para inserção
    dados_para_inserir = {'id_camera': id_camera, 'quant_pessoas': quant_pessoas, 'foto': foto}

    try:
        # Inserir dados na tabela e obter o ID gerado
        response = supabase.table('fotos').insert(dados_para_inserir).execute()

        # Verificar e lidar com a resposta
        if 'data' in response and len(response['data']) > 0 and 'id' in response['data'][0]:
            novo_id = response['data'][0]['id']
            print(f"Novo ID inserido: {novo_id}")
            return novo_id
        else:
            print("Nenhum ID retornado")
            return -1

    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
        return -2

def pegarConfiguracoes(id_config_camera):
    # Consulta para buscar o valor específico
    response = supabase.table('config_camera').select('*').eq('id', id_config_camera).execute()
    #(response)
    # Verificar e lidar com a resposta
    if 'data' in response and len(response['data']) > 0:
        resposta = response['data'][0]
        #print(f"Valor desejado: {resposta}")
        return resposta
    else:
        print("Nenhum resultado encontrado")
        return -2

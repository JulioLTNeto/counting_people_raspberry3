import json

caminho = "configs/inv.json"
def getConfigs():
	with open(caminho, 'r') as arquivo:
		dados_json = json.load(arquivo)
		return dados_json
	
def setConfig(chave, dado):
	with open(caminho, 'r') as arquivo:
		dados_json = json.load(arquivo)
		
	dados_json[chave] = dado
	
	with open(caminho, 'w') as arquivo:
		json.dump(dados_json, arquivo, indent=4)

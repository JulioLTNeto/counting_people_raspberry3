import api
import configs

def main():
	resposta = api.pegarConfiguracoes('1')
	nome = resposta["nome"]
	configs.setConfig("nome", nome)
	hora_comeca = resposta["hora_comeca"]
	configs.setConfig("hora_comeca", hora_comeca)
	hora_termina = resposta["hora_termina"]
	configs.setConfig("hora_termina",hora_termina)
	intervalo = resposta["intervalo"]
	configs.setConfig("intervalo", intervalo)
	
	print(resposta)
	
main()

import random  # Importa o módulo random para geração de números aleatórios
import time  # Importa o módulo time para manipulação de tempo

class PalavrasCruzadas:  # Define a classe PalavrasCruzadas
    def __init__(self):  # Define o método de inicialização da classe
        self.banco_de_dados = {  # Define um dicionário com os dados das palavras cruzadas
            "Iniciante": [  # Define um nível de palavras cruzadas para iniciantes
                {  # Define um conjunto de palavras cruzadas
                    "palavras_cruzadas": [  # Define as pistas das palavras cruzadas
                        "1. Fruta amarela: _ _ _ _ _ _ _ _",  # Pista para a primeira palavra
                        "2. Animal doméstico: _ _ _ _ _",  # Pista para a segunda palavra
                        "3. Cor Primária: _ _ _ _ _"  # Pista para a terceira palavra
                    ],
                    "respostas": ["Banana", "Gato", "Azul"],  # Define as respostas para as palavras cruzadas
                    "dicas": ["É uma fruta alongada.", "É um animal de estimação comum.", "É uma das cores do arco-íris."],  # Define as dicas para as palavras cruzadas
                    "tempo_limite": 60  # Define o tempo limite para responder as palavras cruzadas
                },
                {
                    "palavras_cruzadas": [
                        "1. País da América do Sul: _ _ _ _ _ _",  # Pista para a primeira palavra
                        "2. Peixe de água doce: _ _ _ _ _ _",  # Pista para a segunda palavra
                        "3. Parte do corpo humano: _ _ _ _ _"  # Pista para a terceira palavra
                    ],
                    "respostas": ["Brasil", "Tilápia", "Braço"],  # Define as respostas para as palavras cruzadas
                    "dicas": ["Possui a maior floresta tropical do mundo.", "É muito apreciado na culinária.", "É utilizado para realizar movimentos."],  # Define as dicas para as palavras cruzadas
                    "tempo_limite": 60  # Define o tempo limite para responder as palavras cruzadas
                }
            ],
            "Intermediário": [  # Define um nível de palavras cruzadas intermediário
                {
                    "palavras_cruzadas": [
                        "1. Capital da França: _ _ _ _ _",  # Pista para a primeira palavra
                        "2. Elemento químico símbolo 'Fe': _ _ _ _",  # Pista para a segunda palavra
                        "3. País com maior população: _ _ _ _ _ _"  # Pista para a terceira palavra
                    ],
                    "respostas": ["Paris", "Ferro", "China"],  # Define as respostas para as palavras cruzadas
                    "dicas": ["É conhecida como a Cidade Luz.", "É usado para fabricar objetos de ferro.", "Tem a maior população do mundo."],  # Define as dicas para as palavras cruzadas
                    "tempo_limite": 45  # Define o tempo limite para responder as palavras cruzadas
                },
                {
                    "palavras_cruzadas": [
                        "1. Cidade sede do Vaticano: _ _ _ _ _",  # Pista para a primeira palavra
                        "2. Língua mais falada do mundo: _ _ _ _ _ _",  # Pista para a segunda palavra
                        "3. Planeta conhecido como Planeta Vermelho: _ _ _ _ _ _"  # Pista para a terceira palavra
                    ],
                    "respostas": ["Roma", "Mandarim", "Marte"],  # Define as respostas para as palavras cruzadas
                    "dicas": ["É conhecida como a Cidade Eterna.", "É falada por mais de um bilhão de pessoas.", "Tem a superfície coberta por óxido de ferro, dando a coloração característica."],  # Define as dicas para as palavras cruzadas
                    "tempo_limite": 45  # Define o tempo limite para responder as palavras cruzadas
                }
            ],
            "Avançado": [  # Define um nível de palavras cruzadas avançado
                {
                    "palavras_cruzadas": [
                        "1. Famoso físico teórico: _ _ _ _ _ _",  # Pista para a primeira palavra
                        "2. Elemento químico símbolo 'Hg': _ _ _ _ _",  # Pista para a segunda palavra
                        "3. Primeiro presidente dos EUA: _ _ _ _ _ _ _"  # Pista para a terceira palavra
                    ],
                    "respostas": ["Einstein", "Mercúrio", "Washington"],  # Define as respostas para as palavras cruzadas
                    "dicas": ["Desenvolveu a teoria da relatividade.", "É conhecido como o metal líquido.", "Foi o primeiro presidente dos Estados Unidos."],  # Define as dicas para as palavras cruzadas
                    "tempo_limite": 30  # Define o tempo limite para responder as palavras cruzadas
                },
                {
                    "palavras_cruzadas": [
                        "1. Unidade de energia: _ _ _ _ _ _",  # Pista para a primeira palavra
                        "2. Quarto planeta do Sistema Solar: _ _ _ _ _ _",  # Pista para a segunda palavra
                        "3. Autor de 'Dom Quixote': _ _ _ _ _ _ _ _ _"  # Pista para a terceira palavra
                    ],
                    "respostas": ["Joule", "Marte", "Cervantes"],  # Define as respostas para as palavras cruzadas
                    "dicas": ["É a quantidade de trabalho necessário para mover uma carga de 1 coulomb através de um potencial de 1 volt.", "Tem uma atmosfera fina e gelada.", "É considerado um dos maiores romancistas de todos os tempos."],  # Define as dicas para as palavras cruzadas
                    "tempo_limite": 30  # Define o tempo limite para responder as palavras cruzadas
                }
            ]
        }
        self.palavras_personalizadas = {}  # Inicializa um dicionário vazio para armazenar palavras cruzadas personalizadas

    def criar_palavras_personalizadas(self):  # Define o método para criar palavras cruzadas personalizadas
        nome_palavras = "Personalizada"  # Solicita ao usuário um nome para as palavras cruzadas personalizadas
        palavras_cruzadas = []  # Inicializa uma lista vazia para armazenar as pistas e respostas das palavras cruzadas
        dicas = []  # Inicializa uma lista vazia para armazenar as dicas das palavras cruzadas
        tempo_limite = int(input("Digite o tempo limite em segundos: "))  # Solicita ao usuário o tempo limite para resolver as palavras cruzadas
        while True:  # Inicia um loop infinito para receber as pistas e respostas das palavras cruzadas
            pista = input("Digite uma pista (ou 'fim' para terminar): ")  # Solicita ao usuário uma pista para a palavra cruzada
            if pista.lower() == "fim":  # Verifica se o usuário digitou 'fim' para encerrar a entrada de pistas
                break  # Sai do loop caso o usuário tenha digitado 'fim'
            resposta = input("Digite a resposta para a pista: ")  # Solicita ao usuário a resposta para a pista
            dica = input("Digite uma dica para a pista: ")  # Solicita ao usuário uma dica para a pista
            palavras_cruzadas.append({"pista": pista, "resposta": resposta, "dicas" : dica})  # Adiciona a pista e a resposta à lista de palavras cruzadas

        # Adiciona as palavras cruzadas personalizadas ao dicionário de palavras personalizadas, associando-as ao nome fornecido pelo usuário
        self.palavras_personalizadas[nome_palavras] = {
            "palavras_cruzadas": palavras_cruzadas,  # Armazena as pistas e respostas das palavras cruzadas

            "tempo_limite": tempo_limite  # Armazena o tempo limite para resolver as palavras cruzadas
        }
        print("Palavras cruzadas personalizadas criadas com sucesso!")  # Informa ao usuário que as palavras cruzadas personalizadas foram criadas com sucesso
        return nome_palavras  # Retorna o nome das palavras cruzadas personalizadas

    def exibir_palavras_cruzadas(self, nivel, num_jogadores, modo_estudo=False, jogo_personalizado = None):  # Define o método para exibir as palavras cruzadas
        print(f"Bem-vindo ao jogo de palavras cruzadas ({nivel})!")  # Imprime uma mensagem de boas-vindas ao jogo
        if modo_estudo:  # Verifica se o modo de jogo é de estudo
            print("Modo de Estudo: Resolva as palavras cruzadas sem se preocupar com pontuações ou limites de tempo.")  # Imprime uma mensagem indicando que está no modo de estudo
        else:  # Se não estiver no modo de estudo
            print("Preencha as palavras cruzadas com as respostas corretas ou peça uma dica se precisar.\n")  # Imprime uma mensagem instruindo o jogador a preencher as palavras cruzadas

        if jogo_personalizado: # Verifica se há um jogo personalizado fornecido
            jogos = [jogo_personalizado] * num_jogadores # Cria uma lista com o jogo personalizado repetido para o número de jogadores
        else:
            jogos = random.choices(self.banco_de_dados[nivel], k=num_jogadores)  # Seleciona aleatoriamente os jogos para o nível e quantidade de jogadores especificados

        pontuacoes = {}  # Inicializa um dicionário para armazenar as pontuações dos jogadores

        for jogador, jogo in zip(range(1, num_jogadores + 1), jogos):  # Loop sobre cada jogador e jogo
            nome_jogador = input(f"Jogador {jogador}, digite seu nome: ")  # Solicita o nome do jogador
            pontuacoes[nome_jogador] = 0  # Inicializa a pontuação do jogador como zero

            palavras_cruzadas = jogo["palavras_cruzadas"]  # Obtém as palavras cruzadas do jogo
            respostas = jogo["respostas"]  # Obtém as respostas do jogo
            dicas = jogo["dicas"]  # Obtém as dicas do jogo
            tempo_limite = jogo["tempo_limite"]  # Obtém o tempo limite do jogo

            print(f"Jogo {jogador}:")  # Imprime uma mensagem indicando o número do jogo
            for indice, pista in enumerate(palavras_cruzadas, 1):  # Loop sobre cada pista das palavras cruzadas
                resposta_correta = respostas[indice - 1]  # Obtém a resposta correta para a pista atual
                dica = dicas[indice - 1]  # Obtém a dica para a pista atual

                print(f"{pista}: ")  # Imprime a pista atual
                inicio_pista = time.time()  # Registra o tempo inicial para a pista atual

                resposta_usuario = input(f"{nome_jogador}, sua resposta ou 'dica' para pedir uma dica: ").strip().lower()  # Solicita a resposta do jogador ou uma dica

                while resposta_usuario == "dica":  # Enquanto o jogador pedir uma dica
                    print(f"Dica: {dica}\n")  # Imprime a dica correspondente
                    resposta_usuario = input(f"{nome_jogador}, sua resposta ou 'dica' para pedir uma dica: ").strip().lower()  # Solicita novamente a resposta do jogador ou uma dica

                if not modo_estudo:  # Se não estiver no modo de estudo
                    if resposta_usuario == resposta_correta.lower():  # Se a resposta do jogador estiver correta
                        fim_pista = time.time()  # Registra o tempo final para a pista atual
                        duracao = fim_pista - inicio_pista  # Calcula a duração para responder a pista atual
                        pontuacoes[nome_jogador] += 1 + int(tempo_limite - duracao)  # Atualiza a pontuação do jogador
                        print("Correto!\n")  # Imprime uma mensagem indicando que a resposta está correta
                    else:  # Se a resposta do jogador estiver incorreta
                        print(f"Incorreto! A resposta correta era: {resposta_correta}\n")  # Imprime a resposta correta

        if not modo_estudo:  # Se não estiver no modo de estudo
            print("\nPontuações dos jogadores:")  # Imprime uma mensagem indicando as pontuações dos jogadores
            for jogador, pontuacao in pontuacoes.items():  # Loop sobre cada jogador e pontuação
                print(f"{jogador}: {pontuacao} ponto(s)")  # Imprime o nome do jogador e sua pontuação

    def jogar(self):  # Define o método para jogar o jogo de palavras cruzadas
        while True:  # Loop principal do jogo
            print("Escolha o nível de dificuldade:")  # Imprime uma mensagem instruindo o jogador a escolher o nível de dificuldade
            print("1. Iniciante")  # Imprime a opção para o nível iniciante
            print("2. Intermediário")  # Imprime a opção para o nível intermediário
            print("3. Avançado")  # Imprime a opção para o nível avançado
            print("4. Criar palavras cruzadas personalizadas")
            nivel = input("Digite o número do nível: ")  # Solicita ao jogador que digite o número correspondente ao nível escolhido

            if nivel in ["1", "2", "3"]:  # Verifica se o nível escolhido é válido
                modo_estudo = False  # Inicializa a variável de controle do modo de estudo como False
                modo_jogo = input("Escolha o modo de jogo (normal/estudo): ").lower()  # Solicita ao jogador que escolha o modo de jogo
                if modo_jogo == "estudo":  # Se o jogador escolher o modo de estudo
                    modo_estudo = True  # Atualiza a variável de controle do modo de estudo como True

                num_jogadores = int(input("Quantos jogadores participarão? "))  # Solicita ao jogador que digite o número de jogadores participantes
                niveis = ["Iniciante", "Intermediário", "Avançado"]  # Define uma lista com os níveis disponíveis
                self.exibir_palavras_cruzadas(niveis[int(nivel) - 1], num_jogadores, modo_estudo)  # Exibe as palavras cruzadas do nível escolhido
            elif nivel == "4":
                nome_palavras_personalizadas = self.criar_palavras_personalizadas()  # Chama o método para criar palavras cruzadas personalizadas e armazena o nome
                if nome_palavras_personalizadas:  # Se as palavras cruzadas personalizadas forem criadas com sucesso
                    num_jogadores = int(input("Quantos jogadores participarão? "))  # Solicita ao jogador o número de jogadores
                    if nome_palavras_personalizadas in self.palavras_personalizadas:  # Se o nome das palavras cruzadas personalizadas estiver no banco de dados
                        palavras_cruzadas_personalizadas = self.palavras_personalizadas[nome_palavras_personalizadas]  # Obtém as palavras cruzadas personalizadas
                        jogo_personalizado = {"palavras_cruzadas": [], "respostas": [], "dicas": [], "tempo_limite": 0}  # Inicializa um jogo personalizado
                        for palavra in palavras_cruzadas_personalizadas["palavras_cruzadas"]:  # Loop pelas palavras cruzadas personalizadas
                            jogo_personalizado["palavras_cruzadas"].append(palavra["pista"])  # Adiciona as pistas ao jogo personalizado
                            jogo_personalizado["respostas"].append(palavra["resposta"])  # Adiciona as respostas ao jogo personalizado
                            jogo_personalizado["dicas"].append(palavra["dicas"])  # Adiciona as dicas ao jogo personalizado (não há dicas para palavras personalizadas)
                        jogo_personalizado["tempo_limite"] = palavras_cruzadas_personalizadas["tempo_limite"]  # Define o tempo limite para o jogo personalizado
                        self.exibir_palavras_cruzadas("Personalizado", num_jogadores, modo_estudo=False, jogo_personalizado=jogo_personalizado)  # Exibe as palavras cruzadas personalizadas

            else:  # Se o nível escolhido não for válido
                print("Nível inválido. Escolha entre 1, 2, 3 ou 4.")  # Imprime uma mensagem indicando que o nível é inválido

            jogar_novamente = input("\nDeseja jogar novamente? (sim/não): ").lower()  # Solicita ao jogador se deseja jogar novamente
            if jogar_novamente != "sim":  # Se o jogador não quiser jogar novamente
                break  # Encerra o loop principal do jogo

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    jogo = PalavrasCruzadas()  # Cria uma instância do jogo de palavras cruzadas
    jogo.jogar()  # Inicia o jogo

# Variáveis Globais

TIPO_CODIFICACAO = 'BIN'        # BIN, INT, INT-PERM, REAL
POP=10                          # Tamanho da população
DIM=30                         # Dimensão, tamanho do cromossomo, L
L=DIM
RUN=5                           # Número de execuções
GEN=500                           # Número de iterações (gerações)
MAXIMIZAR=True                  # False para minimizar

#Bounds
Li = -2
Ui = 2

## Seleção

# Roleta

# Torneio Estocástico
K=2
KP=1

D=5                     # Distância 


# Vizinhança linear (anel)
CRITERIO_VIZINHANCA=0   # 0 -> Melhor Fitness       1 -> Fitness proporcional       2 -> Aleatório
OPCAO_ELITISMO=0        # 0 -> Booleano             1 -> Preservar melhor indivíduo para próxima geração


# Operadores Genéticos

PC=0.9                  # probabilidade de crossover
TIPO_CROSSOVER=3        # 0 -> Uniforme      1 -> Um ponto   2 -> 2 pontos    3 -> PMX     4 -> BLX-a      5 -> Aritmético
TIPO_SELECAO=1          # 0 -> roleta        1 -> Torneio
PM=0.02                 # probabilidade de mutação




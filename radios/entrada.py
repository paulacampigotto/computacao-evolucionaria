
# Variáveis Globais


TIPO_CODIFICACAO = 'BIN'        # BIN, INT, INT-PERM, REAL
POP=100                         # Tamanho da população
DIM=10                          # Dimensão, tamanho do cromossomo, L
L=DIM
RUN=10                           # Número de execuções
GEN=100                         # Número de iterações (gerações)
MAXIMIZAR=True                  # False para minimizar

#Bounds
Li_standard = 0
Ui_standard = 24
Li_luxo = 0
Ui_luxo = 16

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
TIPO_CROSSOVER=0        # 0 -> Uniforme      1 -> Um ponto   2 -> 2 pontos    3 -> PMX     4 -> BLX-a      5 -> Aritmético

PM=0.08                 # probabilidade de mutação




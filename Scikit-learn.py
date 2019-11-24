########################################
#Weverson Mateus dos Reis Ribeiro
#Ciência da Computação 8º período
#RA: 16322858
########################################

# Lendo um conjunto de dados íris como exemplo
from sklearn.datasets import load_iris
iris = load_iris()

# Armazenando a matriz de recursos X e o vetor de resposta Y
X = iris.data
y = iris.target

# Armazenando os nomes dos recursos e destinos
feature_names = iris.feature_names
target_names = iris.target_names

# Printando os recursos e os nomes de destino do conjunto de dados
print("Feature names:", feature_names)
print("Target names:", target_names)

# X e Y são matrizes NumPy
print("\nType of X is:", type(X))

# Printando as 5 primeiras linhas de entrada
print("\nFirst 5 rows of X:\n", X[:5])

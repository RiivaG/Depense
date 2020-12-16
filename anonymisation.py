import pandas as pd

def script():
	
	file = pd.read_csv('depenses.csv')
	file.to_csv('depenses_anonymes.csv')
	
	file2 = pd.read_csv('depenses_anonymes.csv')
	
	nom = list(set(file2['nom'].tolist()))
	
	idnom = []
	for i in range(len(nom)):
		idnom.append('id'+str(i))
	
	ville = list(set(file2['ville'].tolist()))
	
	idville = []
	for i in range(len(ville)):
		idville.append('id'+str(i))
	
	file2['nom'] = file2['nom'].replace(nom, idnom)
	file2['ville'] = file2['ville'].replace(ville, idville)
	
		
script()

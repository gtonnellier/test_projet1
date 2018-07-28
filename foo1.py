#! usr/bin/env python3
# -*- coding: utf-8 -*-

##En-tête conforme à PEP 263

#guide spécial python sos-micro

##types de données : integer, float, boolean, string, list, tuple

var_str = "hello"
var_int = 7
var_float = 3.1
var_bool = True
var_tuple = ()
var_list=["hello", "ceci", "est", "une", "liste"]
print(var_list)

#Méthodes pour les strings


#Méthodes pour les int et float


#Méthodes pour les booleans

########################################
########################################
################méthodes pour les listes
#Créer une liste vide lis()
foo_list=list()

#Méthode Append pour ajouter un élément à la liste, à la suite
foo_list.append("hello")
foo_list.append("ceci")
foo_list.append("est")
foo_list.append("une")
foo_list.append("liste")
print(foo_list)

#list.insert(i,x) : insère élément x à la position i
foo_list.insert(5, "insert")
print(foo_list)

#list.remove(x) : supprimer l'élément x (le 1er élément trouvé)
foo_list.remove("insert")
print(foo_list)

#list.pop(i) : supprimer l'élément situé à la position i 
foo_list.pop(0)
print(foo_list)

#list.clear() : supprimer le contenu de la liste
#foo_list.clear()

#list.count(x) : renvoi le nbre d'éléments x dans la liste
foo_list.count("ceci")
print(foo_list.count("ceci"))

#list.index(x) : retourne l'index de x
print(foo_list.index("ceci"))

#utilisation d'une liste comme FIFO pile
stack=[5,6,7]
print(stack)
stack.append(8)
print(stack)
stack.append(9)
print(stack)
stack.pop()
print(stack)

########################################
########################################
################méthodes pour les tuples
#Les tuples sont immuables et contiennent souvent des séquences 
#hétérogènes d’éléments qui sont accédés par « déballage » (voir plus loin) ou indexation 
#(ou même par attributs dans le cas des namedtuples). Les listes sont souvent muable et 
#contiennent des éléments homogènes qui sont accédés par itération sur la liste.
t = 12345, 54321, 'hello!'   #exemple d'emballage d'un tuple. Les 3 valeurs sont dans un même tuple
print(t)
#t.append("stop")   - on ne peut pas ajouter de valeur append au tuple
#t.insert("stop") - on ne peut pas ajouter de valeur insert au tuple
print(t)
print(t[2])


########################################
########################################
################méthodes pour les dictionnaires
#les dict sont indexées par des clés, contenant une paire de clé : valeur
tel = {'jack': 4098, 'sape': 4139}
print(tel)
tel['jack'] = 4562  #ajout d'un élément
print(tel['sape']) #recherche d'un élément 
del tel['jack'] #suppression d'une valeur
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  #le constructeur dict crée un dictionnaire à partir de tuple
print(tel.items())

#structures de contrôle ####################
############################################
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i in reversed(range(1, 10, 2)):
    print(i)
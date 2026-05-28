# Congruence

Ce notebook est un cours sur les congruences, sujet introduit en arithmétique modulaire. Nous définirons ce qu'est une congruence ainsi que ses propriétés. Nous verrons un cas d'application avec le théorème des restes chinois suivis d'un exercice corrigé comme exemple.

---

## Définition

Historiquement, la notion de congruence sur les entiers relatifs a été introduite par Gauss vers 1801. Les congruences sont très utiles car elles permettent de ramener des calculs avec de très grands nombres à des calculs avec des nombres raisonnables.

En arithmétique modulaire, on dit que deux entiers relatifs `a` et `b` sont congrus modulo `n`, avec:

$$
n \in \mathbb{N}
$$

si et seulement `a` et `b` ont le même reste de la division euclidienne par `n`.

On note alors :

$$
a \equiv b \ [n]
$$

Nous pouvons ajouter qu'ils sont congrus modulo `n` si leur différence est un multiple de `n` :

$$
(a - b) [n] = 0
$$

### Remarque

Je note ici le modulo, qui est le reste d'une division euclidienne, par `n`.

$$
a \equiv b \ [n]
$$

ou autrement noté:
$$
a \equiv b \ mod (n)
$$

---

## Exemple

```text
a = 18, b = 23 et n = 5

18 mod 5 = 3
23 mod 5 = 3

Les restes de 18 et 23 divisé par 5 sont identiques.
a et b sont donc congrus.

18 ≡ 23 [5]
```

# Propriétés

## 1. Relation d'équivalence

Dans un ensemble, des éléments similaires dus à certaines propriétés sont regroupés en classes d'équivalence.

- Réflexivité $$\forall a \in \mathbb{N}, \ a \equiv a \ [n]$$

- Symétrie

$$
\forall a,b \in \mathbb{N},
\ a \equiv b \ [n]
\iff
b \equiv a \ [n]
$$

- Transitivité
$$\forall a,b,c \in \mathbb{N}$$
si 
$$a \equiv b \ [n], b \equiv c \ [n]$$

alors
$$a \equiv c \ [n]$$

---

## 2. Propriétés algébriques

si
$$a \equiv b \ [n], c \equiv d \ [n]$$
alors:

- addition: $a + c \equiv b + d \ [n]$

- multiplication: $\forall k \in \mathbb{Z}, \ k \cdot a \equiv k \cdot b \ [n]$

- produit: $a \cdot c \equiv b \cdot d \ [n]$

- puissance: $\forall k \in \mathbb{N}, \ a^k \equiv b^k \ [n]$

---

# Théorème des restes chinois

La forme originale du théorème apparaît dans le *Sunzi Suanjing* datant du IIIe siècle.

Selon Ulrich Libbrecht, la motivation de ce type de calcul chez les Chinois serait l'astronomie.

Exemple de problème :

> Dans combien de jours la pleine lune tombera-t-elle au solstice d'hiver ?

Si :
- il reste 6 jours avant le solstice d'hiver
- il reste 3 jours avant la pleine lune

Alors, existe-t-il un entier `x` tel que :

$$
x \equiv 6 \ [365]
$$

et :

$$
x \equiv 3 \ [28]
$$

---

## Formulation générale

Soit :

$$
m_1, m_2, ..., m_n
$$

des entiers premiers entre eux deux à deux, ainsi que :

$$
a_1, a_2, ..., a_n
$$

des entiers naturels non nuls.

Nous cherchons un entier `N` tel que :

$$
N \equiv a_1 \ [m_1]
$$

$$
N \equiv a_2 \ [m_2]
$$

$$
...
$$

$$
N \equiv a_n \ [m_n]
$$

Nous avons :

$$
m = m_1 \times m_2 \times ... \times m_n
$$

Avec :

$$
j \in [1,n]
$$

on a :

$$
pgcd\left(\frac{m}{m_j}, m_j\right)=1
$$

D'après le théorème de Bézout :

$$
\frac{m}{m_j} \times b_j \equiv 1 \ [m_j]
$$

Donc :

$$
\frac{m}{m_j} \times b_j \times a_j
\equiv
a_j \ [m_j]
$$

Finalement :

$$
x_0 =
\left(
\sum_{j=1}^{N}
\frac{m}{m_j}
\times b_j
\times a_j
\right)
[m_i]
$$

---

# Exemple

$$
x \equiv 3 \ [17]
$$

$$
x \equiv 4 \ [11]
$$

$$
x \equiv 5 \ [6]
$$

Calculons :

$$
m = 3 \times 4 \times 5 = 60
$$

Il faut résoudre :

$$
\frac{60}{3} \times b_1 \equiv 1 \ [3]
$$

$$
\frac{60}{4} \times b_2 \equiv 1 \ [4]
$$

$$
\frac{60}{5} \times b_3 \equiv 1 \ [5]
$$

On obtient :

$$
b_1 = 2
$$

$$
b_2 = 3
$$

$$
b_3 = 3
$$

Alors :

$$
x_0 =
(20 \times 2 \times 2)
+
(15 \times 3 \times 1)
+
(12 \times 3 \times 3)
= 233
$$

Donc :

$$
x = 233 \ [60] = 53
$$

Ce qui donne :

$$
53 \equiv 2 \ [3]
$$

$$
53 \equiv 1 \ [4]
$$

etc.

Toutes les autres solutions sont données par :

$$
x = 53 + 60k
$$

avec :

$$
k \in \mathbb{Z}
$$

---

# Ressource complémentaire

- Théorème des restes chinois :  
  https://bibmath.net/crypto/index.php?action=affiche&quoi=complements/resteschinois
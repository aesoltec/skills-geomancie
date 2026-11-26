---
name: geomancie-maitre
description: >-
  Compétence maîtresse de géomancie sacrée ('Ilm al-Raml, Turabu, Kinyèda, Laturu)
  fondée sur les traités d'al-Ṭūkhī (Bulūgh al-Amal, Manbaʿ Uṣūl al-Raml), les études
  ouest-africaines (Kassibo, Bertaux, Jansen, Maupoil) et le corpus manuscrit/PDF du projet.
  Utiliser ce skill pour calculer ou vérifier un thème géomantique à 16 maisons (Takht),
  appliquer les niveaux de preuve [A/B/C/D], ou router vers les skills spécialisés
  (figures/maisons, ḍamīr/interprétation, Afrique de l'Ouest/saraka, manuscrits/OCR).
---

# Géomancie Sacrée — Compétence Maîtresse (`geomancie-maitre`)

## 1. Architecture de la suite de compétences

Ce dossier regroupe cinq compétences complémentaires issues du corpus PDF, texte et manuscrit :

| Skill | Rôle | Quand l'activer |
|---|---|---|
| **`geomancie-maitre`** | Fondements binaires, génération du *Takht* (16 maisons), épistémologie `[A/B/C/D]`, script de calcul | Tout calcul de thème, vérification mathématique ou cadrage épistémologique |
| **`geomancie-figures-maisons`** | Dictionnaire des 16 figures, 16 maisons, *taskīn*, correspondances arabe/latin/mandingue | Identifier une figure, comparer des traditions, lire les maisons |
| **`geomancie-damir-interpretation`** | *Ḍamīr* (5 voies + miroir), Témoins/Juge/Sentence, durées (166), rencontre/litige, restitution | Interpréter un thème, calculer une durée, trancher un litige ou rédiger un verdict |
| **`geomancie-afrique-ouest-rituels`** | *Kinyèda*/*Laturu*/*Fâ*, *Saraka* (offrandes), éthique des initiés (*dalilu*/*kirisiw*) | Contexte ouest-africain (Kassibo, Bertaux, Jansen, Maupoil) ou protocoles d'offrandes |
| **`geomancie-manuscrits-ocr`** | Lecture visuelle de manuscrits arabes/cahiers, translittération, audit des sources | Transcrire ou vérifier une image/PDF scanné (`bulugh`, `mnba`, cahiers manuscrits) |

---

## 2. Règle épistémologique absolue (Niveaux de preuve)

Toute règle, table ou affirmation doit être qualifiée par son niveau de preuve. **Ne jamais présenter une convention `[D]` ou un calcul `[C]` comme un texte attesté `[A]`.**

- **`[A]` Attesté** : lu directement dans un traité imprimé du corpus (*Bulūgh al-Amal*, *Manbaʿ Uṣūl al-Raml*, *al-Falak al-Mashḥūn*) ou une publication académique (Kassibo 1992, Jansen 2011, Bertaux 1984, Maupoil 1943, Hébert 1961).
- **`[B]` Source unique / non collationnée** : forum de praticiens, OCR non recoupé à l'image (ex. leçons 20–42 du *Manbaʿ*), grille de repos *taskīn* des praticiens, portail confessionnel unique.
- **`[C]` Calculé / dérivé** : résultat mathématique reproductible (addition modulo 2, parité, complémentarité, *al-Sahm*).
- **`[D]` Convention / cahier des charges** : choix d'interface ou de modèle non attesté dans les traités (ex. roue circulaire, score en buts, métrologie Abjad × 54 cm, mapping thématique direct du *ḍamīr*).

---

## 3. Fondements mathématiques et génération du *Takht*

### 3.1 Représentation binaire et sens de lecture

- Chaque figure comporte **4 rangs** lus **de haut en bas** :
  1. **Feu** (Tête / *Raʾs*)
  2. **Air** (Cœur / *Ṣadr*)
  3. **Eau** (Ventre / *Baṭn*)
  4. **Terre** (Pied / *Qadam*)
- Valeurs : `1` = point impair (*khalwa*, point unique `•`) ; `2` = deux points pairs (*zawjiyya*, trait `—` ou `••`).
- ⚠️ **Piège critique** : inverser le sens de lecture (haut→bas vs bas→haut) transforme une figure en une autre (ex. `1121` *Puer* ↔ `1211` *Puella*). Toujours figer l'ordre **haut → bas**.

### 3.2 Loi de copulation (Addition modulo 2) `[A]/[C]`

```text
1 ⊕ 1 = 2   (impair + impair → pair)
2 ⊕ 2 = 2   (pair + pair     → pair)
1 ⊕ 2 = 1   (impair + pair   → impair)
2 ⊕ 1 = 1   (pair + impair   → impair)
```

Propriétés algébriques `[C]` :
- L'ensemble des 16 figures forme un groupe abélien d'exposant 2.
- L'élément **neutre** est **`2222` (*al-Ǧamāʿa* / Populus)**, jamais `1111` (*al-Ṭarīq* / Via).
- L'addition avec `1111` (*al-Ṭarīq*) produit le **complément miroir** (`1 ↔ 2` sur chaque rang).

### 3.3 Algorithme des 16 maisons `[A]/[C]`

1. **Mères (`M1–M4`)** : 4 figures tirées au hasard (ou saisies), posées **de droite à gauche** (`M1` à l'extrême droite).
2. **Filles (`M5–M8`)** : lecture **horizontale** des rangs des 4 Mères :
   - `M5` = rangs Feu (têtes) de `[M1, M2, M3, M4]`
   - `M6` = rangs Air (cœurs) de `[M1, M2, M3, M4]`
   - `M7` = rangs Eau (ventres) de `[M1, M2, M3, M4]`
   - `M8` = rangs Terre (pieds) de `[M1, M2, M3, M4]`
3. **Nièces (`M9–M12`)** : `M9 = M1 ⊕ M2`, `M10 = M3 ⊕ M4`, `M11 = M5 ⊕ M6`, `M12 = M7 ⊕ M8`.
4. **Témoins (`M13–M14`)** : `M13` (Droit / Demandeur) = `M9 ⊕ M10` ; `M14` (Gauche / Sujet) = `M11 ⊕ M12`.
5. **Juge (`M15`)** : `M15 = M13 ⊕ M14`.
   - **Validation obligatoire `[A]`** : la somme des points de `M15` doit être **paire** (donc 0, 2 ou 4 rangs impairs). Un Juge impair invalide le thème.
6. **Sentence (`M16` / *ʿĀqibat al-ʿāqiba*)** : `M16 = M15 ⊕ M1`.

### 3.4 Disposition du Bouclier (*Takht* `8 · 4 · 2 · 1 · 1`) `[A]`

```text
M8   M7   M6   M5   M4   M3   M2   M1
     M12  M11  M10  M9
          M14       M13
               M15
               M16
```

- La disposition en **roue circulaire** (`M1` en haut, sens horaire) est une convention de visualisation `[D]`, jamais une disposition attestée dans les traités arabes.

---

## 4. Outil de calcul et vérification déterministe

Pour générer ou auditer un thème sans erreur arithmétique, exécuter le script :
[takht.py](./scripts/takht.py)

Exemple d'utilisation :
```bash
python scripts/takht.py 1111 2121 2112 1222
```

Ce script calcule les 16 maisons, vérifie la parité du Juge (`M15`), affiche le bouclier `8·4·2·1·1`, calcule la Part de Fortune (*al-Sahm*), détecte les passations (répétitions de `M1` et d'autres figures) et produit une sortie JSON ou texte.

---

## 5. Cartographie du corpus

Pour connaître les ouvrages exacts disponibles, leurs éditions, les erreurs d'attribution à éviter (notamment *Manbaʿ Uṣūl al-Raml* d'al-Ṭūkhī vs *Manbaʿ Uṣūl al-Ḥikma* d'al-Būnī) et l'état de dépouillement des PDF/images, lire :
[corpus-sources.md](./references/corpus-sources.md)

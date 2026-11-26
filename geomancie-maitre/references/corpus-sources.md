# Cartographie des Sources du Corpus Géomancie

Ce document recense les sources disponibles dans le dossier `geomancie/` avec leur nature, leur auteur réel et leur statut épistémologique.

---

## 1. Traités arabes imprimés (Cheikh al-Ṭūkhī et corpus classique)

| Sigle | Titre | Auteur | Édition / Format | Contenu vérifié |
|---|---|---|---|---|
| **B** | *Bulūgh al-Amal fī ʿIlm al-Raml* (بلوغ الأمل في علم الرمل) | ʿAbd al-Fattāḥ al-Sayyid al-Ṭūkhī | Dār al-Kutub al-ʿIlmiyya, Beyrouth, 1991, 96 p. impr. (98 PDF) | Manuel pratique en 40 chapitres (*bāb*) : tracé, générations, natures, durées (ch. 7), *taskīn*, *ḍamīr* (ch. 9–10), lettres/abjad (ch. 11–12), chose cachée, malade (ch. 24), rencontre, chapitres détaillés des 16 figures. Traduction française intégrale dans `traduction-bulugh/Bulugh-al-Amal_fr.md`. |
| **M** | *Manbaʿ Uṣūl al-Raml* (منبع أصول الرمل — الشرح على مائتي بيت وأصل) | ʿAbd al-Fattāḥ al-Sayyid al-Ṭūkhī | 66 p. numérisées + `ocr-indra/test/mnba asol alrml.md` + `doc images/mnba_*.png` | Commentaire versifié en 5 leçons : tracé, ascendant, *taskīn*, aspects (*naẓar*, *taʿāqub*, *ittiṣāl*, *infiṣāl*), maisons, table planétaire (*taskīn al-kawākib*), litige (p. 75), rencontre des deux armées (p. 77). |
| **F** | *al-Falak al-Mashḥūn fī ʿIlm al-Raml al-Maṣūn* (الفلك المشحون في علم الرمل المصون) | Anonyme | PDF + texte Al-Saydia | Takht à 16 cases et domaines des maisons. |

### ⚠️ Erreurs d'attribution à ne jamais reproduire
1. **`منبع أصول الحكمة` (*Manbaʿ Uṣūl al-Ḥikma*)** : recueil de quatre traités attribué à **Abū al-ʿAbbās Aḥmad ibn ʿAlī al-Būnī** (m. 622 H.), édité au Caire (1946). **Ce n'est pas un livre de Cheikh al-Ṭūkhī**, malgré la proximité du titre.
2. **Muḥammad al-Zanātī** (*Faṣl fī Uṣūl ʿIlm al-Raml*, éd. 1955, 72 p.) : auteur distinct d'al-Ṭūkhī ; ne pas attribuer le *Manbaʿ* à al-Zanātī.
3. **Sources fantômes** : Savage-Smith et Regourd ne figurent pas dans les PDF numérisés du dossier ; ne pas les citer comme sources vérifiées localement.

---

## 2. Études académiques sur l'Afrique de l'Ouest et le comparatisme

| Sigle | Référence | Extraction locale | Apport principal |
|---|---|---|---|
| **K** | Bréhima Kassibo, « La géomancie ouest-africaine. Formes endogènes et emprunts extérieurs », *Cahiers d'études africaines* 128, 1992, p. 541–596 | `doc txt/formes_endogenes_brehima.txt`, `doc txt/ouest_africaine.txt` | Noms mandé/bambara des 16 figures et maisons (p. 549, 552–558), transfert des noms de maisons sur les figures, éléments/directions/couleurs/saraka. |
| **J** | Jan Jansen, « Éducation arithmétique sous forme d'apprentissage. La géomancie dans les Monts Mandingues », *Cahiers d'études africaines* 201, 2011, p. 9–49 | `doc txt/etudes_africaines_16581.txt` | Système *kinyèda*/*kala jan* (22 *sow*, 4 figures initiales → 256 schémas) vs *laturu* (16 cases, 65 536 schémas), 6 leçons arithmétiques, *dalilu* et *kirisiw*, éthique du secret. |
| **Be** | Colette Bertaux, « La technique des prescriptions sacrificielles dans la géomancie bambara (région de Ségou, Mali) », *Systèmes de pensée en Afrique noire* 6, 1984, p. 117–130 | Notes de lecture intégrées | Seule base empirique des offrandes de Ségou (matières, jours, orientations, évitement) ; aucune posologie médicale. |
| **Ma** | Bernard Maupoil, *La Géomancie à l'ancienne Côte des Esclaves*, Paris, Institut d'ethnologie, 1943 | Catalogué | Système *Fâ* fon/gun (16 mères, 256 signes, noix de palme), thèse historique sur l'origine musulmane. |
| **H** | J.-C. Hébert, « Analyse structurale des géomancies comoriennes, malgaches et africaines », *J. Soc. Africanistes* 31/2, 1961, p. 115–208 | `doc txt/analyse_structurale_comores.txt` | Comparatisme structural (Comores, Madagascar *sikidy*, Soudan, Touareg) ; règle Humain (pair) / Djinn (impair) p. 149. |

---

## 3. Corpus européen, indo-persan et manuscrits complémentaires

- **Aide française** : `doc pdf/Geomancie-Aide.pdf` → `doc txt/geomancie_aide.txt` (correspondances latines, éléments, planètes, zodiaque, jours, durées).
- **Corpus latin / Renaissance** : Robert Fludd (`utriusquecosmima01flud.pdf`, `utriusquecosmima02flud.pdf`), `astrolabiumplanu00ange.pdf`.
- **Traités ourdous / persans** (`doc txt/*_djvu.txt`) : *Aaftaab-ur-Ramal*, *Aina-e-Ramal*, *Complete Asbaq Al Ramal*, *Complete Raheem ul Ramaal* (1–3), *Israr E Ramal*, *Jame Al Ramal*, *Kanz al Hussain*, *Khulasa al Ramal*, *Madaan ul Ramal*, *Mahbub Al Ramal*, *Misbah Al Ramal*, *Misdaq Al Ramal*, *Qawaneen-e-Ramaal*, *Shamsul Ramal*, *Siraj ur ramal*, *Surkhaab e Ramal*.
- **Manuscrits et cahiers en images** (`doc images/`) :
  - Planches scannées `bulugh_*.png` et `mnba_*.png`.
  - Cahier arabe manuscrit (`WhatsApp Image 2026-11-10 at 12.33.*` et `12.39.*`) : répartition des figures par éléments autour de *al-Arḍ*, matrices des rapports (*ṭālib*, *maṭlūb*, *naẓar*, *ittiṣāl*, *infiṣāl*, *shāhid*, *dalīl*, *sirr*, *mustawlī*).
- **Veille contemporaine (hors barème `[B]`/`[D]`)** : transcription de Traoré Yssouf (`transcriptions/16-figures-7-etoiles.md`) et captures d'écran de l'application (`imgs/WhatsApp Image 2026-11-13*`).

# GB Santé · recettes

Recettes pour **une personne**, françaises et européennes, plutôt hypocaloriques et riches en protéines,
pour le plan de repas de GB Santé (3 repas et 2 collations par jour).

- `outils/ingredients.py` : les ingrédients, chacun relié à un code de la table **CIQUAL** (ANSES, licence ouverte).
- `outils/recettes_src.py` : les recettes (ingrédients en grammes, étapes, astuce).
- `outils/construire.py` : calcule les valeurs nutritionnelles d'après `donnees/ciqual.tsv`, contrôle les règles
  et écrit `recettes/*.json` (une par recette), `recettes.json` (la liste complète) et `manifeste.json` (sha256).
- Règles par portion : petit-déjeuner 200 à 450 kcal et au moins 15 g de protéines ; plat 300 à 600 kcal et au moins 28 g ;
  collation 80 à 250 kcal et au moins 6 g.
- À chaque envoi, GitHub Actions contrôle, vérifie que les fichiers sont à jour et publie la version « derniere-liste »
  (`recettes.json` + `manifeste.json`). GB Santé l'importe par fichier, comme la base d'aliments : rien n'est téléchargé par l'appli.

Lot 1 : 1 011 recettes (15 petits-déjeuners, 63 plats, 22 collations). Objectif : 1 000.

Ajouter des recettes : compléter `recettes_src.py`, lancer `python3 outils/construire.py`, envoyer.

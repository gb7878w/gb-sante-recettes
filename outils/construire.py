#!/usr/bin/env python3
"""Construit les recettes : calcule les valeurs nutritionnelles d'après CIQUAL, contrôle les règles,
écrit recettes/*.json, recettes.json (liste complète) et manifeste.json (empreinte sha256).

Usage : python3 outils/construire.py [--verifier] [--stats]
"""
import hashlib, json, re, sys, unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingredients import I, ALLERGENES, VIANDES
from recettes_src import RECETTES

COLONNES = ["code", "nom", "groupe", "kcal", "proteines", "glucides", "lipides", "sucres", "fibres", "satures", "sel",
            "fer", "calcium", "magnesium", "potassium", "zinc", "iode", "vitd", "vitc", "b12", "b9", "alcool"]
MACROS = ["kcal", "proteines", "glucides", "lipides", "sucres", "fibres", "satures", "sel"]
MICROS = COLONNES[11:]
MOMENTS = {"petit-dejeuner": ["PETIT_DEJEUNER"], "plat": ["DEJEUNER", "DINER"], "collation": ["COLLATION"]}
# Règles par portion : (kcal min, kcal max, protéines min en g)
REGLES = {"petit-dejeuner": (200, 450, 15), "plat": (300, 600, 28), "collation": (80, 250, 6)}


def charger_ciqual():
    table = {}
    for ligne in (RACINE / "donnees" / "ciqual.tsv").read_text(encoding="utf-8").splitlines()[2:]:
        c = ligne.split("\t")
        table[c[0]] = {k: (float(v) if v not in ("", "-") else 0.0) for k, v in zip(COLONNES[3:], c[3:])} | {"nom": c[1]}
    return table


def slug(texte):
    s = unicodedata.normalize("NFKD", texte.replace("œ", "oe").replace("Œ", "oe")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:48]


def construire():
    ciqual = charger_ciqual()
    erreurs, sortie, vus = [], [], set()
    for n, r in enumerate(RECETTES, 1):
        rid = f"r{n:03d}-{slug(r['nom'])}"
        if r["nom"] in vus: erreurs.append(f"{rid}: nom en double")
        vus.add(r["nom"])
        if r["categorie"] not in MOMENTS: erreurs.append(f"{rid}: catégorie inconnue"); continue
        total = {k: 0.0 for k in MACROS + MICROS}
        ingredients, poids = [], 0.0
        for alias, g in r["ingredients"]:
            if alias not in I: erreurs.append(f"{rid}: ingrédient inconnu « {alias} »"); continue
            code, libelle = I[alias]
            if code not in ciqual: erreurs.append(f"{rid}: code CIQUAL {code} absent"); continue
            if not 0 < g <= 800: erreurs.append(f"{rid}: quantité absurde {alias} {g}")
            for k in total: total[k] += ciqual[code][k] * g / 100
            ingredients.append({"ciqual": code, "nom": libelle, "g": g}); poids += g
        aliases = {a for a, _ in r["ingredients"]}
        allergenes = sorted(k for k, l in ALLERGENES.items() if aliases & set(l))
        vegetarien = not (aliases & set(VIANDES)) and "poisson" not in allergenes and "crustaces" not in allergenes
        mn, mx, pmin = REGLES[r["categorie"]]
        if not mn <= total["kcal"] <= mx: erreurs.append(f"{rid}: {total['kcal']:.0f} kcal hors de {mn}-{mx}")
        if total["proteines"] < pmin: erreurs.append(f"{rid}: {total['proteines']:.0f} g de protéines (< {pmin})")
        if len(r["etapes"]) < (1 if r["categorie"] == "collation" else 2): erreurs.append(f"{rid}: pas assez d'étapes")
        if not 2 <= r["temps"] <= 90: erreurs.append(f"{rid}: durée {r['temps']}")
        if "lowcarb" in r.get("tags", []):
            lmax = {"petit-dejeuner": 20, "plat": 22, "collation": 12}[r["categorie"]]
            if total["glucides"] > lmax: erreurs.append(f"{rid}: {total['glucides']:.0f} g de glucides (> {lmax}, pauvre en glucides)")
        sortie.append({
            "id": rid, "nom": r["nom"], "categorie": r["categorie"], "moments": MOMENTS[r["categorie"]],
            "tempsMin": r["temps"], "portions": 1, "poidsG": round(poids), "tags": r.get("tags", []),
            "allergenes": allergenes, "vegetarien": vegetarien,
            "ingredients": ingredients, "etapes": r["etapes"], "astuce": r.get("astuce", ""),
            "nutrition": {k: round(v, 2) for k, v in total.items()},
        })
    return sortie, erreurs


def main():
    sortie, erreurs = construire()
    if "--stats" in sys.argv:
        for s in sortie:
            x = s["nutrition"]
            print(f"{s['id'][:40]:40} {x['kcal']:5.0f} kcal  P{x['proteines']:4.0f} G{x['glucides']:4.0f} L{x['lipides']:4.0f}  {s['poidsG']} g")
    for e in erreurs: print("ERREUR", e)
    if erreurs: sys.exit(1)
    if "--verifier" in sys.argv: return
    dossier = RACINE / "recettes"
    dossier.mkdir(exist_ok=True)
    for f in dossier.glob("*.json"): f.unlink()
    for s in sortie:
        (dossier / f"{s['id']}.json").write_text(json.dumps(s, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    liste = json.dumps({"version": 1, "recettes": sortie}, ensure_ascii=False, separators=(",", ":")) + "\n"
    (RACINE / "recettes.json").write_text(liste, encoding="utf-8")
    manifeste = {"version": 1, "nombre": len(sortie), "fichier": "recettes.json",
                 "sha256": hashlib.sha256(liste.encode("utf-8")).hexdigest()}
    (RACINE / "manifeste.json").write_text(json.dumps(manifeste, indent=1) + "\n", encoding="utf-8")
    print(f"{len(sortie)} recettes écrites")


if __name__ == "__main__":
    main()

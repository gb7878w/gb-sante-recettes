"""Ingrédients des recettes : nom court -> (code CIQUAL, libellé affiché).
Les grammes d'une recette sont ceux de l'aliment dans l'état du code (cuit, cru, égoutté…)."""
I = {
    # viandes, poissons, œufs
    "poulet": ("36018", "Filet de poulet sauté"), "cuissepoulet": ("36006", "Cuisse de poulet rôtie, sans peau"),
    "dinde": ("36306", "Escalope de dinde sautée"), "hache5": ("6251", "Steak haché 5 % cuit"),
    "rumsteck": ("6207", "Rumsteck grillé"), "porc": ("28203", "Filet mignon de porc cuit"),
    "veau": ("6520", "Escalope de veau cuite"), "agneau": ("21503", "Gigot d'agneau rôti"),
    "jambon": ("28913", "Jambon blanc découenné dégraissé"), "jambondinde": ("28964", "Blanc de dinde en tranche"),
    "lardons": ("28504", "Lardons nature cuits"), "saumon": ("25996", "Saumon cuit"),
    "cabillaud": ("26023", "Cabillaud au four"), "thon": ("26039", "Thon au naturel égoutté"),
    "merlu": ("26120", "Merlu cuit à l'étouffée"), "sardine": ("26136", "Sardine grillée"),
    "sardinehuile": ("26231", "Sardines à l'huile d'olive égouttées"), "crevette": ("10007", "Crevettes cuites"),
    "moule": ("10013", "Moules cuites"), "lieu": ("26192", "Lieu jaune cuit"), "truite": ("27014", "Truite au four"),
    "maquereau": ("26123", "Maquereau au naturel égoutté"), "haddock": ("26090", "Haddock"),
    "eglefin": ("26008", "Églefin vapeur"), "lapin": ("34004", "Lapin cuit"),
    "stjacques": ("10004", "Noix de Saint-Jacques cuites"), "oeuf": ("22000", "Œuf"), "oeufdur": ("22010", "Œuf dur"),
    # féculents, légumineuses
    "lentille": ("20587", "Lentilles vertes cuites"), "poischiche": ("20507", "Pois chiches cuits"),
    "haricotrouge": ("20503", "Haricots rouges cuits"), "haricotblanc": ("20502", "Haricots blancs cuits"),
    "pates": ("9811", "Pâtes cuites"), "patescompl": ("9871", "Pâtes complètes cuites"), "riz": ("9125", "Riz basmati cuit"),
    "rizcompl": ("9103", "Riz complet cuit"), "quinoa": ("9341", "Quinoa cuit"), "boulgour": ("9691", "Boulgour cuit"),
    "semoule": ("9611", "Semoule cuite"), "pdt": ("4003", "Pommes de terre vapeur"), "pdtfour": ("4026", "Pommes de terre au four"),
    "patatedouce": ("4102", "Patate douce cuite"), "paincompl": ("7110", "Pain complet"), "painblanc": ("7012", "Pain"),
    "biscotte": ("7340", "Biscotte complète"), "flocons": ("9311", "Flocons d'avoine"), "farine": ("9440", "Farine de blé T45"),
    # légumes
    "courgette": ("20021", "Courgette cuite"), "courgettecrue": ("20020", "Courgette crue"), "aubergine": ("20002", "Aubergine cuite"),
    "poivron": ("20087", "Poivron rouge"), "tomate": ("20276", "Tomate"), "tomatecerise": ("20172", "Tomates cerises"),
    "oignon": ("20239", "Oignon"), "echalote": ("20097", "Échalote"), "ail": ("11000", "Ail"), "carotte": ("20009", "Carotte"),
    "carottecuite": ("20008", "Carotte cuite"), "champignon": ("20056", "Champignons de Paris"), "epinard": ("20336", "Épinards cuits"),
    "epinardcru": ("20059", "Épinards frais"), "brocoli": ("20304", "Brocoli vapeur"), "chouxfleur": ("20017", "Chou-fleur cuit"),
    "poireau": ("20040", "Poireau cuit"), "butternut": ("20138", "Courge butternut"), "petitspois": ("20326", "Petits pois cuits"),
    "harivert": ("20320", "Haricots verts cuits"), "laitue": ("20031", "Laitue"), "romaine": ("20171", "Salade romaine"),
    "concombre": ("20019", "Concombre"), "chou": ("20116", "Chou blanc"), "betterave": ("20003", "Betterave cuite"),
    "celeri": ("20023", "Céleri branche"), "fenouil": ("20028", "Fenouil"), "endive": ("20026", "Endive"), "avocat": ("13004", "Avocat"),
    "mais": ("20066", "Maïs doux égoutté"), "olive": ("13032", "Olives noires"), "capres": ("11040", "Câpres"),
    "cornichon": ("11004", "Cornichons"), "mache": ("20099", "Mâche"), "artichaut": ("20155", "Cœurs d'artichaut"),
    "persil": ("11014", "Persil"), "basilic": ("11033", "Basilic"),
    # produits laitiers et gras
    "fb0": ("19644", "Fromage blanc 0 %"), "fb3": ("19646", "Fromage blanc 3 %"), "yaourt": ("19600", "Yaourt nature"),
    "kefir": ("19865", "Kéfir"), "emmental": ("12118", "Emmental râpé"), "chevre": ("12813", "Fromage de chèvre allégé"),
    "mozzarella": ("19590", "Mozzarella"), "feta": ("12066", "Feta"), "parmesan": ("12120", "Parmesan"),
    "cremelegere": ("19436", "Crème légère"), "lait": ("19041", "Lait demi-écrémé"), "beurre": ("16414", "Beurre"),
    "huileolive": ("17270", "Huile d'olive"), "colza": ("17130", "Huile de colza"), "petitsuisse": ("19661", "Petit-suisse"),
    "soja": ("18901", "Boisson au soja nature"), "tofu": ("20904", "Tofu nature"), "laitcoco": ("18041", "Lait de coco"),
    # fruits, secs, divers
    "pomme": ("13039", "Pomme"), "banane": ("13005", "Banane"), "orange": ("13034", "Orange"), "fraise": ("13014", "Fraises"),
    "framboise": ("13015", "Framboises"), "poire": ("13188", "Poire"), "citron": ("13009", "Citron"), "pruneau": ("13042", "Pruneaux"),
    "amande": ("15000", "Amandes"), "noix": ("15005", "Noix"), "noisette": ("15004", "Noisettes"), "pignon": ("15025", "Pignons de pin"),
    "cacahuete": ("15053", "Cacahuètes non salées"), "cacao": ("18100", "Cacao non sucré"), "miel": ("31008", "Miel"),
    "chocolat": ("31030", "Chocolat noir sans sucres ajoutés"), "coulis": ("20260", "Coulis de tomates"),
    "concentre": ("20068", "Concentré de tomate"), "vinblanc": ("5215", "Vin blanc sec"), "moutarde": ("11013", "Moutarde"),
    "vinaigre": ("11018", "Vinaigre"), "bouillon": ("25948", "Bouillon de légumes"), "curry": ("11005", "Curry"),
    "cumin": ("11042", "Cumin"), "herbes": ("11060", "Herbes de Provence"), "cannelle": ("11025", "Cannelle"),
}

# Allergènes par alias d'ingrédient (les 14 allergènes réglementaires qui concernent ces recettes).
ALLERGENES = {
    "gluten": ["flocons", "farine", "pates", "patescompl", "boulgour", "semoule", "paincompl", "painblanc", "biscotte"],
    "lactose": ["lait", "fb0", "fb3", "yaourt", "kefir", "emmental", "chevre", "mozzarella", "feta", "parmesan", "cremelegere", "beurre", "petitsuisse"],
    "oeufs": ["oeuf", "oeufdur"],
    "fruits-a-coque": ["amande", "noix", "noisette", "pignon"],
    "arachide": ["cacahuete"],
    "poisson": ["saumon", "cabillaud", "thon", "merlu", "sardine", "sardinehuile", "lieu", "truite", "maquereau", "haddock", "eglefin"],
    "crustaces": ["crevette", "moule", "stjacques"],
    "soja": ["soja", "tofu"],
    "moutarde": ["moutarde"],
    "celeri": ["celeri"],
}
VIANDES = ["poulet", "cuissepoulet", "dinde", "hache5", "rumsteck", "porc", "veau", "agneau", "jambon", "jambondinde", "lardons", "lapin"]

"""Sixième lot : Suisse, Autriche, Belgique, Pays-Bas, Royaume-Uni, Irlande (pauvres en glucides, riches en protéines)."""
from recettes_src import R, PD, PL, CO

LC = "lowcarb"

# ---------------------------------------------------------------- petits-déjeuners (15)
R("Omelette au gruyère et au jambon (Suisse)", PD, 12, [("oeuf", 130), ("gruyere", 25), ("jambon", 40), ("beurre", 4)],
  ["Battez les œufs.", "Cuisez dans le beurre avec le jambon, ajoutez le gruyère et repliez."], [LC, "Suisse", "oeufs", "rapide"])
R("Fromage blanc, noix et pomme râpée (Suisse)", PD, 5, [("fb0", 220), ("pomme", 60), ("noix", 10), ("cannelle", 1), ("oeufdur", 55)],
  ["Mélangez le fromage blanc et la pomme râpée.", "Ajoutez noix et cannelle, servez avec l'œuf dur."], [LC, "Suisse", "vegetarien", "oeufs", "rapide"])
R("Œufs au plat et lard grillé (Suisse)", PD, 10, [("oeuf", 120), ("bacon", 50), ("tomate", 80)],
  ["Grillez le bacon.", "Faites cuire les œufs au plat, servez avec la tomate."], [LC, "Suisse", "oeufs", "rapide"])
R("Œufs brouillés au saumon fumé et à l'aneth (Autriche)", PD, 10, [("oeuf", 120), ("saumonfume", 50), ("aneth", 3), ("beurre", 5)],
  ["Brouillez les œufs dans le beurre.", "Ajoutez saumon fumé et aneth."], [LC, "Autriche", "poisson", "oeufs", "rapide"])
R("Omelette soufflée au fromage (Autriche)", PD, 15, [("oeuf", 130), ("fb0", 60), ("emmental", 20), ("ciboulette", 3)],
  ["Séparez blancs et jaunes, mêlez jaunes, fromage blanc et emmental.", "Incorporez les blancs montés, cuisez à couvert 6 minutes."], [LC, "Autriche", "vegetarien", "oeufs"])
R("Assiette de jambon, fromage et œuf dur (Autriche)", PD, 10, [("jambon", 50), ("gruyere", 25), ("oeufdur", 55), ("cornichon", 30), ("radis", 40)],
  ["Disposez jambon, fromage, œuf dur, cornichons et radis.", "Assaisonnez de poivre et servez frais."], [LC, "Autriche", "rapide"])
R("Œufs brouillés aux crevettes grises (Belgique)", PD, 12, [("oeuf", 120), ("crevette", 60), ("persil", 3), ("beurre", 5)],
  ["Brouillez les œufs dans le beurre.", "Ajoutez les crevettes et le persil."], [LC, "Belgique", "poisson", "oeufs", "rapide"])
R("Fromage blanc et jambon d'Ardenne (Belgique)", PD, 6, [("fb0", 200), ("jambonsec", 50), ("radis", 40), ("ciboulette", 3), ("noix", 8)],
  ["Mélangez le fromage blanc et la ciboulette.", "Servez avec le jambon sec et les radis."], [LC, "Belgique", "rapide"])
R("Omelette aux endives et au jambon (Belgique)", PD, 15, [("oeuf", 130), ("endive", 100), ("jambon", 40), ("beurre", 5)],
  ["Faites revenir les endives émincées dans le beurre.", "Ajoutez les œufs battus et le jambon."], [LC, "Belgique", "oeufs", "rapide"])
R("Œufs pochés au saumon fumé, sauce citron (Pays-Bas)", PD, 12, [("oeuf", 120), ("saumonfume", 40), ("citron", 5), ("fb0", 40)],
  ["Pochez les œufs 3 minutes.", "Servez sur le saumon avec une sauce fromage blanc-citron."], [LC, "Pays-Bas", "poisson", "oeufs", "rapide"])
R("Plateau de fromages et de noix (Pays-Bas)", PD, 5, [("cheddar", 25), ("emmental", 25), ("fb0", 150), ("noix", 10), ("concombre", 50)],
  ["Disposez fromages, noix et concombre.", "Servez avec le fromage blanc."], [LC, "Pays-Bas", "vegetarien", "rapide"])
R("Petit-déjeuner anglais allégé (Royaume-Uni)", PD, 15, [("oeuf", 120), ("bacon", 40), ("champignon", 80), ("tomate", 80), ("beurre", 4)],
  ["Poêlez bacon et champignons.", "Ajoutez la tomate et les œufs au plat."], [LC, "Royaume-Uni", "oeufs"])
R("Haddock poché et œuf (Royaume-Uni)", PD, 15, [("haddock", 100), ("oeuf", 60), ("lait", 50), ("persil", 3)],
  ["Pochez le haddock dans le lait.", "Servez avec l'œuf poché et le persil."], [LC, "Royaume-Uni", "poisson", "oeufs"])
R("Œufs brouillés au cheddar et à la ciboulette (Irlande)", PD, 10, [("oeuf", 120), ("cheddar", 25), ("ciboulette", 3), ("beurre", 4)],
  ["Brouillez les œufs dans le beurre.", "Ajoutez cheddar et ciboulette."], [LC, "Irlande", "vegetarien", "oeufs", "rapide"])

# ---------------------------------------------------------------- collations (22)
R("Gruyère et pomme (Suisse)", CO, 3, [("gruyere", 30), ("pomme", 60), ("fb0", 60)], ["Coupez gruyère et pomme en tranches.", "Servez avec le fromage blanc."], [LC, "Suisse", "vegetarien", "rapide"])
R("Jambon sec façon viande des Grisons (Suisse)", CO, 3, [("jambonsec", 35), ("cornichon", 30), ("fb0", 60)], ["Roulez le jambon sec avec les cornichons.", "Servez avec le fromage blanc."], [LC, "Suisse", "rapide"])
R("Œuf dur à la moutarde (Suisse)", CO, 12, [("oeufdur", 110), ("moutarde", 6), ("fb0", 30)], ["Coupez l'œuf en deux.", "Garnissez de moutarde mêlée au fromage blanc."], [LC, "Suisse", "vegetarien", "oeufs"])
R("Saucisse grillée et radis (Suisse)", CO, 8, [("francfort", 50), ("radis", 60), ("moutarde", 6)], ["Grillez la saucisse.", "Servez avec les radis et la moutarde."], [LC, "Suisse", "rapide"])
R("Fromage frais aux fines herbes (Autriche)", CO, 5, [("fb0", 150), ("ciboulette", 3), ("persil", 3), ("radis", 50)], ["Mélangez fromage blanc et herbes.", "Servez avec les radis."], [LC, "Autriche", "vegetarien", "rapide"])
R("Saumon fumé et concombre (Autriche)", CO, 4, [("saumonfume", 40), ("concombre", 80), ("fb0", 50), ("aneth", 2)], ["Roulez le saumon avec le concombre.", "Servez avec le fromage blanc à l'aneth."], [LC, "Autriche", "poisson", "rapide"])
R("Œuf dur et jambon (Autriche)", CO, 12, [("oeufdur", 110), ("jambon", 40), ("cornichon", 20)], ["Servez l'œuf dur avec le jambon et les cornichons."], [LC, "Autriche", "oeufs"])
R("Crevettes grises au citron (Belgique)", CO, 4, [("crevette", 70), ("citron", 8), ("fb0", 50), ("persil", 2)], ["Mêlez les crevettes cuites au citron et au persil.", "Servez avec le fromage blanc."], [LC, "Belgique", "poisson", "rapide"])
R("Fromage de caractère et radis (Belgique)", CO, 4, [("munster", 30), ("radis", 60), ("fb0", 60)], ["Servez le fromage avec les radis et le fromage blanc."], [LC, "Belgique", "vegetarien", "rapide"])
R("Endive garnie de fromage blanc et de jambon (Belgique)", CO, 8, [("endive", 100), ("fb0", 80), ("jambon", 40), ("ciboulette", 2)], ["Garnissez les feuilles d'endive de fromage blanc et de jambon roulé."], [LC, "Belgique", "rapide"])
R("Fromage à pâte ferme et concombre (Pays-Bas)", CO, 3, [("cheddar", 30), ("concombre", 80), ("fb0", 60)], ["Coupez le fromage en dés.", "Servez avec le concombre et le fromage blanc."], [LC, "Pays-Bas", "vegetarien", "rapide"])
R("Hareng fumé et oignon (Pays-Bas)", CO, 5, [("harengfume", 60), ("oignon", 20), ("cornichon", 20), ("fb0", 50)], ["Servez le hareng avec l'oignon et les cornichons.", "Ajoutez le fromage blanc."], [LC, "Pays-Bas", "poisson", "rapide"])
R("Œuf dur et saumon fumé (Pays-Bas)", CO, 12, [("oeufdur", 110), ("saumonfume", 30)], ["Servez l'œuf avec le saumon fumé."], [LC, "Pays-Bas", "poisson", "oeufs"])
R("Cheddar et céleri (Royaume-Uni)", CO, 3, [("cheddar", 30), ("celeri", 60), ("fb0", 60)], ["Coupez céleri et fromage.", "Servez avec le fromage blanc."], [LC, "Royaume-Uni", "vegetarien", "rapide"])
R("Œuf dur écossais allégé (Royaume-Uni)", CO, 20, [("oeufdur", 55), ("francfort", 40), ("moutarde", 4)], ["Enrobez l'œuf dur de saucisse écrasée.", "Enfournez 12 minutes à 200 °C."], [LC, "Royaume-Uni", "four"])
R("Saumon fumé et fromage frais (Royaume-Uni)", CO, 4, [("saumonfume", 40), ("fb0", 80), ("citron", 5)], ["Servez le saumon avec le fromage blanc citronné."], [LC, "Royaume-Uni", "poisson", "rapide"])
R("Jambon et moutarde en roulés (Royaume-Uni)", CO, 3, [("jambon", 60), ("moutarde", 6), ("concombre", 50)], ["Étalez la moutarde sur le jambon.", "Roulez avec le concombre."], [LC, "Royaume-Uni", "rapide"])
R("Saumon fumé irlandais et citron (Irlande)", CO, 4, [("saumonfume", 50), ("citron", 8), ("fb0", 50), ("aneth", 2)], ["Servez le saumon avec le citron et le fromage blanc."], [LC, "Irlande", "poisson", "rapide"])
R("Cheddar irlandais et radis (Irlande)", CO, 3, [("cheddar", 30), ("radis", 60), ("fb0", 60)], ["Servez le cheddar avec les radis et le fromage blanc."], [LC, "Irlande", "vegetarien", "rapide"])
R("Œuf dur et bacon croustillant (Irlande)", CO, 12, [("oeufdur", 110), ("bacon", 30)], ["Faites griller le bacon.", "Servez avec l'œuf dur."], [LC, "Irlande", "oeufs"])

# ---------------------------------------------------------------- plats (63)
R("Fondue au fromage allégée et crudités (Suisse)", PL, 25, [("gruyere", 50), ("emmental", 40), ("vinblanc", 40), ("chouxfleur", 150), ("champignon", 100), ("jambonsec", 40)],
  ["Faites fondre les fromages avec le vin à feu doux.", "Servez avec chou-fleur et champignons cuits et le jambon sec."], [LC, "Suisse", "viande"])
R("Émincé de veau à la zurichoise sans rösti (Suisse)", PL, 25, [("veau", 160), ("champignon", 150), ("cremelegere", 40), ("vinblanc", 30), ("persil", 4)],
  ["Saisissez le veau en lanières.", "Ajoutez champignons, vin et crème, mijotez 8 minutes."], [LC, "Suisse", "viande"])
R("Raclette suisse de légumes et de viande des Grisons (Suisse)", PL, 30, [("raclette", 90), ("jambonsec", 40), ("chouxfleur", 150), ("courgette", 100), ("cornichon", 30)],
  ["Cuisez chou-fleur et courgette.", "Faites fondre le fromage dessus, servez avec jambon et cornichons."], [LC, "Suisse", "viande"])
R("Filets de perche au beurre et aux amandes (Suisse)", PL, 20, [("lieu", 180), ("beurre", 12), ("amande", 12), ("citron", 10), ("harivert", 200)],
  ["Poêlez le poisson au beurre.", "Ajoutez amandes effilées et citron, servez avec les haricots verts."], [LC, "Suisse", "poisson"])
R("Poulet à la crème de gruyère (Suisse)", PL, 30, [("poulet", 150), ("gruyere", 30), ("cremelegere", 40), ("brocoli", 200)],
  ["Poêlez le poulet, nappez de crème et de gruyère.", "Servez avec le brocoli."], [LC, "Suisse", "viande"])
R("Saucisse aux oignons et chou (Suisse)", PL, 30, [("francfort", 130), ("jambon", 70), ("oignon", 40), ("chou", 200), ("moutarde", 8)],
  ["Faites revenir l'oignon, ajoutez le chou, braisez 15 minutes.", "Servez avec saucisses et jambon."], [LC, "Suisse", "viande"])
R("Tafelspitz, bœuf bouilli aux légumes (Autriche)", PL, 60, [("boeufmaigre", 180), ("carotte", 80), ("celerirave", 80), ("poireau", 100), ("moutarde", 8), ("beurre", 8), ("fb0", 80)],
  ["Mijotez le bœuf avec les légumes 45 minutes.", "Servez avec la moutarde."], [LC, "Autriche", "viande"])
R("Escalope viennoise de dinde sans chapelure (Autriche)", PL, 25, [("dinde", 160), ("oeuf", 40), ("parmesan", 15), ("citron", 10), ("laitue", 80)],
  ["Trempez l'escalope dans l'œuf et le parmesan.", "Poêlez 3 minutes par face.", "Servez avec citron et salade."], [LC, "Autriche", "viande"])
R("Goulache autrichienne et chou-fleur (Autriche)", PL, 60, [("boeufmaigre", 150), ("oignon", 60), ("paprika", 5), ("coulis", 80), ("chouxfleur", 150), ("huileolive", 10), ("fb0", 80)],
  ["Faites revenir bœuf, oignon et paprika.", "Ajoutez le coulis, mijotez 40 minutes.", "Servez avec le chou-fleur."], [LC, "Autriche", "viande"])
R("Truite des Alpes au beurre (Autriche)", PL, 25, [("truite", 170), ("beurre", 10), ("citron", 10), ("persil", 4), ("epinard", 150)],
  ["Poêlez la truite au beurre.", "Servez avec les épinards, citron et persil."], [LC, "Autriche", "poisson"])
R("Saucisses au chou rouge (Autriche)", PL, 30, [("francfort", 120), ("jambon", 70), ("chourouge", 200), ("moutarde", 8)],
  ["Braisez le chou rouge.", "Réchauffez les saucisses et servez avec le jambon."], [LC, "Autriche", "viande"])
R("Fricassée de poulet au paprika (Autriche)", PL, 40, [("poulet", 160), ("paprika", 4), ("oignon", 40), ("cremelegere", 40), ("courgette", 150)],
  ["Dorez le poulet avec l'oignon et le paprika.", "Ajoutez courgettes et crème, mijotez 15 minutes."], [LC, "Autriche", "viande"])
R("Gratin d'endives au jambon à la belge (Belgique)", PL, 40, [("endive", 300), ("jambon", 140), ("emmental", 30), ("cremelegere", 30)],
  ["Braisez les endives, enroulez-les dans le jambon.", "Nappez de crème et d'emmental, gratinez 15 minutes."], [LC, "Belgique", "viande", "four"])
R("Moules marinières à la belge sans frites (Belgique)", PL, 25, [("moule", 300), ("celeri", 40), ("echalote", 20), ("vinblanc", 30), ("persil", 4)],
  ["Faites ouvrir les moules avec céleri, échalote et vin.", "Parsemez de persil."], [LC, "Belgique", "poisson"])
R("Waterzooi de poulet (Belgique)", PL, 40, [("poulet", 160), ("poireau", 100), ("carotte", 60), ("celeri", 40), ("cremelegere", 40)],
  ["Mijotez poulet et légumes dans un peu de bouillon 25 minutes.", "Liez avec la crème."], [LC, "Belgique", "viande"])
R("Carbonade flamande allégée (Belgique)", PL, 70, [("boeufmaigre", 160), ("oignon", 80), ("moutarde", 10), ("vinaigre", 8), ("champignon", 100), ("huileolive", 10), ("fb0", 100), ("beurre", 8)],
  ["Faites revenir bœuf et oignons.", "Ajoutez moutarde, vinaigre et champignons, mijotez 50 minutes."], [LC, "Belgique", "viande"])
R("Filet américain, tartare de bœuf et salade (Belgique)", PL, 20, [("boeufmaigre", 150), ("oeuf", 60), ("cornichon", 30), ("capres", 8), ("laitue", 80), ("moutarde", 6), ("huileolive", 10), ("fb0", 100)],
  ["Mêlez le bœuf haché cuit refroidi, l'œuf, cornichons, câpres et moutarde.", "Servez sur la salade."], [LC, "Belgique", "viande", "rapide"])
R("Lapin à la bière sans pain d'épices (Belgique)", PL, 45, [("lapin", 160), ("oignon", 40), ("moutarde", 10), ("champignon", 100), ("harivert", 150)],
  ["Dorez le lapin avec l'oignon.", "Ajoutez moutarde et champignons, mijotez 30 minutes avec un peu d'eau.", "Servez avec les haricots verts."], [LC, "Belgique", "viande"])
R("Poireaux gratinés au jambon (Belgique)", PL, 40, [("poireau", 300), ("jambon", 130), ("emmental", 30), ("cremelegere", 30)],
  ["Cuisez les poireaux, enroulez-les dans le jambon.", "Nappez de crème et d'emmental, gratinez 15 minutes."], [LC, "Belgique", "viande", "four"])
R("Hareng frais et salade tiède (Pays-Bas)", PL, 20, [("harengfume", 150), ("oignon", 30), ("cornichon", 30), ("laitue", 80), ("oeufdur", 55)],
  ["Émincez l'oignon et les cornichons.", "Servez le hareng avec l'œuf dur sur la salade."], [LC, "Pays-Bas", "poisson", "oeufs", "rapide"])
R("Boulettes de bœuf néerlandaises (gehaktballen) et chou-fleur (Pays-Bas)", PL, 30, [("hache5", 150), ("oeuf", 30), ("oignon", 30), ("chouxfleur", 200), ("moutarde", 8)],
  ["Mélangez viande, œuf et oignon, formez des boulettes.", "Poêlez 10 minutes, servez avec le chou-fleur."], [LC, "Pays-Bas", "viande"])
R("Stamppot allégé, saucisse et chou braisé (Pays-Bas)", PL, 30, [("francfort", 120), ("jambon", 70), ("chou", 250), ("moutarde", 8)],
  ["Braisez le chou 15 minutes.", "Servez avec saucisse, jambon et moutarde."], [LC, "Pays-Bas", "viande"])
R("Saumon rôti au fromage blanc et à l'aneth (Pays-Bas)", PL, 25, [("saumon", 150), ("fb0", 100), ("aneth", 4), ("citron", 10), ("asperge", 150)],
  ["Rôtissez le saumon 12 minutes.", "Servez avec les asperges et une sauce fromage blanc-aneth."], [LC, "Pays-Bas", "poisson", "four"])
R("Asperges, jambon et œufs (Pays-Bas)", PL, 20, [("asperge", 250), ("jambon", 100), ("oeufdur", 110), ("beurre", 8)],
  ["Cuisez les asperges.", "Servez avec jambon, œufs durs et beurre fondu."], [LC, "Pays-Bas", "oeufs"])
R("Poulet rôti, brocoli au fromage (Pays-Bas)", PL, 40, [("poulet", 160), ("brocoli", 200), ("cheddar", 30), ("beurre", 5)],
  ["Rôtissez le poulet 25 minutes.", "Gratinez le brocoli avec le fromage."], [LC, "Pays-Bas", "viande", "four"])
R("Cabillaud et crevettes au beurre citronné (Pays-Bas)", PL, 20, [("cabillaud", 150), ("crevette", 70), ("beurre", 10), ("citron", 10), ("epinard", 150)],
  ["Poêlez cabillaud et crevettes au beurre.", "Servez avec les épinards et le citron."], [LC, "Pays-Bas", "poisson"])
R("Rôti de bœuf et légumes d'hiver (Royaume-Uni)", PL, 60, [("boeufmaigre", 160), ("chouxbruxelles", 150), ("navet", 100), ("moutarde", 8), ("beurre", 10), ("fb0", 100)],
  ["Rôtissez le bœuf 30 minutes à 190 °C.", "Servez avec choux de Bruxelles et navet."], [LC, "Royaume-Uni", "viande", "four"])
R("Fish pie sans pommes de terre au chou-fleur (Royaume-Uni)", PL, 45, [("eglefin", 150), ("saumon", 60), ("chouxfleur", 250), ("lait", 80), ("persil", 4)],
  ["Pochez les poissons dans le lait.", "Couvrez de purée de chou-fleur, enfournez 20 minutes."], [LC, "Royaume-Uni", "poisson", "four"])
R("Poulet rôti aux herbes et chou de Bruxelles (Royaume-Uni)", PL, 40, [("poulet", 160), ("chouxbruxelles", 200), ("thym", 2), ("beurre", 8)],
  ["Rôtissez le poulet au thym.", "Poêlez les choux de Bruxelles au beurre."], [LC, "Royaume-Uni", "viande", "four"])
R("Shepherd's pie au chou-fleur (Royaume-Uni)", PL, 50, [("agneau", 130), ("chouxfleur", 250), ("carotte", 60), ("coulis", 60), ("cheddar", 20)],
  ["Faites revenir l'agneau avec carotte et coulis.", "Couvrez de purée de chou-fleur et de cheddar, gratinez 20 minutes."], [LC, "Royaume-Uni", "viande", "four"])
R("Saumon poché, sauce à l'aneth (Royaume-Uni)", PL, 25, [("saumon", 150), ("fb0", 80), ("aneth", 4), ("concombre", 100), ("citron", 8)],
  ["Pochez le saumon 10 minutes.", "Servez avec sauce fromage blanc-aneth et concombre."], [LC, "Royaume-Uni", "poisson"])
R("Bœuf mijoté aux champignons et à l'oignon (Royaume-Uni)", PL, 65, [("boeufmaigre", 160), ("champignon", 150), ("oignon", 60), ("moutarde", 8), ("huileolive", 10), ("fb0", 100)],
  ["Faites revenir bœuf, oignon et champignons.", "Ajoutez moutarde et un peu d'eau, mijotez 45 minutes."], [LC, "Royaume-Uni", "viande"])
R("Haddock au four, sauce moutardée (Royaume-Uni)", PL, 25, [("haddock", 200), ("moutarde", 10), ("cremelegere", 50), ("epinard", 150), ("beurre", 8)],
  ["Enfournez le haddock 12 minutes.", "Nappez de crème moutardée, servez avec les épinards."], [LC, "Royaume-Uni", "poisson", "four"])
R("Saucisses grillées et chou (Royaume-Uni)", PL, 25, [("francfort", 120), ("jambon", 70), ("chou", 200), ("beurre", 5), ("moutarde", 8)],
  ["Poêlez le chou au beurre.", "Grillez les saucisses, servez avec jambon et moutarde."], [LC, "Royaume-Uni", "viande"])
R("Œufs écossais au four et salade (Royaume-Uni)", PL, 35, [("oeufdur", 165), ("hache5", 80), ("laitue", 80), ("tomate", 100)],
  ["Enrobez les œufs durs de viande hachée assaisonnée.", "Enfournez 20 minutes à 200 °C, servez avec la salade."], [LC, "Royaume-Uni", "viande", "four"])
R("Saumon fumé d'Irlande, œufs brouillés et épinards (Irlande)", PL, 15, [("saumonfume", 80), ("oeuf", 150), ("epinard", 100), ("beurre", 6)],
  ["Brouillez les œufs au beurre avec les épinards.", "Servez avec le saumon fumé."], [LC, "Irlande", "poisson", "oeufs", "rapide"])
R("Irish stew sans pommes de terre (Irlande)", PL, 60, [("agneau", 150), ("carotte", 80), ("oignon", 40), ("navet", 100), ("persil", 4)],
  ["Mijotez agneau, carotte, navet et oignon 45 minutes.", "Parsemez de persil."], [LC, "Irlande", "viande"])
R("Chou et bacon à l'irlandaise (Irlande)", PL, 30, [("bacon", 150), ("chou", 250), ("moutarde", 8), ("beurre", 5)],
  ["Faites cuire le chou 12 minutes.", "Poêlez le bacon, servez avec la moutarde et un peu de beurre."], [LC, "Irlande", "viande"])
R("Cabillaud irlandais au beurre et aux herbes (Irlande)", PL, 25, [("cabillaud", 180), ("beurre", 10), ("persil", 4), ("citron", 10), ("brocoli", 200)],
  ["Poêlez le cabillaud au beurre aux herbes.", "Servez avec le brocoli."], [LC, "Irlande", "poisson"])
R("Moules à la crème et au vin blanc (Irlande)", PL, 25, [("moule", 300), ("cremelegere", 40), ("echalote", 20), ("vinblanc", 30), ("persil", 4)],
  ["Faites ouvrir les moules avec échalote et vin.", "Ajoutez la crème et le persil."], [LC, "Irlande", "poisson"])
R("Boudin noir et chou braisé (Irlande)", PL, 25, [("boudinnoir", 130), ("chou", 200), ("bacon", 40), ("moutarde", 8)],
  ["Poêlez le boudin noir et le bacon.", "Servez avec le chou braisé et la moutarde."], [LC, "Irlande", "viande"])
R("Saumon grillé et asperges (Irlande)", PL, 25, [("saumon", 160), ("asperge", 200), ("beurre", 8), ("citron", 10)],
  ["Grillez le saumon.", "Servez avec les asperges au beurre citronné."], [LC, "Irlande", "poisson"])
R("Agneau aux herbes et haricots verts (Irlande)", PL, 35, [("agneau", 150), ("thym", 2), ("harivert", 200), ("beurre", 6)],
  ["Rôtissez l'agneau au thym 20 minutes à 200 °C.", "Servez avec les haricots verts au beurre."], [LC, "Irlande", "viande", "four"])
R("Poulet farci au cheddar et au bacon (Irlande)", PL, 35, [("poulet", 150), ("cheddar", 30), ("bacon", 40), ("brocoli", 200)],
  ["Ouvrez le poulet, garnissez de cheddar, enveloppez de bacon.", "Enfournez 25 minutes à 200 °C, servez avec le brocoli."], [LC, "Irlande", "viande", "four"])
R("Jambon cuit au four et choux de Bruxelles (Royaume-Uni)", PL, 30, [("jambon", 150), ("chouxbruxelles", 200), ("moutarde", 8), ("oeufdur", 55)],
  ["Réchauffez le jambon au four.", "Servez avec les choux de Bruxelles et l'œuf dur."], [LC, "Royaume-Uni", "viande", "four"])
R("Cuisses de poulet à la moutarde (Royaume-Uni)", PL, 40, [("cuissepoulet", 170), ("moutarde", 12), ("brocoli", 200), ("beurre", 5)],
  ["Badigeonnez le poulet de moutarde.", "Rôtissez 30 minutes à 200 °C, servez avec le brocoli."], [LC, "Royaume-Uni", "viande", "four"])
R("Terrine de saumon et de fromage frais (Royaume-Uni)", PL, 20, [("saumon", 130), ("saumonfume", 40), ("fb0", 100), ("citron", 8), ("concombre", 100)],
  ["Mixez saumon cuit, fromage blanc et citron.", "Entourez de saumon fumé, servez avec le concombre."], [LC, "Royaume-Uni", "poisson", "rapide"])
R("Escalope de veau au gruyère et aux épinards (Suisse)", PL, 25, [("veau", 150), ("gruyere", 30), ("epinard", 200), ("beurre", 6)],
  ["Poêlez l'escalope, couvrez de gruyère.", "Servez avec les épinards au beurre."], [LC, "Suisse", "viande"])
R("Perche et crevettes sauce citron (Suisse)", PL, 25, [("lieu", 150), ("crevette", 70), ("cremelegere", 50), ("citron", 10), ("asperge", 150), ("beurre", 8)],
  ["Pochez le poisson.", "Ajoutez crevettes, crème et citron, servez avec les asperges."], [LC, "Suisse", "poisson"])
R("Gratin de chou-fleur et de brocoli au gruyère (Suisse)", PL, 35, [("chouxfleur", 150), ("brocoli", 150), ("gruyere", 40), ("oeuf", 120), ("jambon", 60)],
  ["Disposez les légumes cuits avec le jambon.", "Nappez d'œufs battus et de gruyère, enfournez 20 minutes."], [LC, "Suisse", "viande", "four"])
R("Poulet paprika et chou-fleur (Autriche)", PL, 35, [("poulet", 150), ("paprika", 3), ("chouxfleur", 200), ("fb0", 100), ("oignon", 30)],
  ["Dorez le poulet avec oignon et paprika.", "Ajoutez le chou-fleur et le fromage blanc, mijotez 15 minutes."], [LC, "Autriche", "viande"])
R("Omelette aux asperges et au jambon (Autriche)", PL, 20, [("oeuf", 190), ("asperge", 150), ("jambon", 60), ("beurre", 6)],
  ["Poêlez les asperges au beurre.", "Ajoutez le jambon et les œufs battus."], [LC, "Autriche", "oeufs"])
R("Chou farci à l'autrichienne (Autriche)", PL, 55, [("hache5", 140), ("chou", 250), ("coulis", 80), ("oeuf", 30), ("paprika", 2)],
  ["Blanchissez les feuilles de chou.", "Garnissez de viande et d'œuf, mijotez dans le coulis 30 minutes."], [LC, "Autriche", "viande"])
R("Waterzooi de poisson (Belgique)", PL, 35, [("eglefin", 150), ("saumon", 60), ("poireau", 100), ("carotte", 50), ("cremelegere", 40)],
  ["Mijotez légumes et poissons 15 minutes.", "Liez avec la crème."], [LC, "Belgique", "poisson"])
R("Boulettes de dinde à la sauce tomate (Belgique)", PL, 30, [("dinde", 150), ("coulis", 100), ("oeuf", 30), ("oignon", 30), ("courgette", 150)],
  ["Formez des boulettes de dinde hachée avec l'œuf et l'oignon.", "Mijotez dans le coulis avec les courgettes."], [LC, "Belgique", "viande"])
R("Omelette à l'aneth et au saumon (Pays-Bas)", PL, 15, [("oeuf", 180), ("saumonfume", 60), ("aneth", 3), ("fb0", 60)],
  ["Battez les œufs avec l'aneth.", "Cuisez en omelette, garnissez de saumon et de fromage blanc."], [LC, "Pays-Bas", "poisson", "oeufs", "rapide"])
R("Steak, haricots verts et sauce moutarde (Pays-Bas)", PL, 20, [("entrecote", 150), ("harivert", 200), ("moutarde", 8), ("cremelegere", 25)],
  ["Grillez l'entrecôte.", "Servez avec haricots verts et sauce crème-moutarde."], [LC, "Pays-Bas", "viande", "rapide"])
R("Épaule d'agneau et légumes rôtis (Royaume-Uni)", PL, 50, [("agneau", 150), ("courgette", 150), ("aubergine", 100), ("romarin", 2), ("huileolive", 6)],
  ["Rôtissez l'agneau au romarin 30 minutes à 190 °C.", "Ajoutez les légumes en dés pour les 20 dernières minutes."], [LC, "Royaume-Uni", "viande", "four"])
R("Cabillaud, brocoli et sauce persil (Royaume-Uni)", PL, 25, [("cabillaud", 200), ("brocoli", 200), ("persil", 5), ("cremelegere", 50), ("huileolive", 8)],
  ["Pochez le cabillaud.", "Servez avec le brocoli et la sauce crème-persil."], [LC, "Royaume-Uni", "poisson"])
R("Bœuf haché, chou et oignons à l'irlandaise (Irlande)", PL, 25, [("hache5", 150), ("chou", 250), ("oignon", 40), ("beurre", 5)],
  ["Faites revenir bœuf et oignon.", "Ajoutez le chou, couvrez 12 minutes."], [LC, "Irlande", "viande"])
R("Lard et œufs au chou (Irlande)", PL, 20, [("bacon", 100), ("oeuf", 120), ("chou", 200), ("beurre", 5)],
  ["Poêlez bacon et chou.", "Ajoutez les œufs et couvrez 3 minutes."], [LC, "Irlande", "viande", "oeufs"])

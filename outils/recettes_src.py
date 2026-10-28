"""Les recettes, pour UNE personne. (alias d'ingrédient, grammes) ; voir ingredients.py."""
RECETTES = []


def R(nom, categorie, temps, ingredients, etapes, tags=(), astuce=""):
    RECETTES.append({"nom": nom, "categorie": categorie, "temps": temps, "ingredients": ingredients,
                     "etapes": etapes, "tags": list(tags), "astuce": astuce})

PD, PL, CO = "petit-dejeuner", "plat", "collation"

# ---------------------------------------------------------------- petits-déjeuners (15)
R("Porridge pomme-cannelle", PD, 10, [("flocons", 40), ("lait", 150), ("fb0", 100), ("pomme", 80), ("cannelle", 1), ("noix", 8)],
  ["Faites chauffer les flocons avec le lait pendant 4 minutes en remuant.", "Hors du feu, ajoutez le fromage blanc et la pomme coupée en dés.", "Saupoudrez de cannelle et de noix concassées."],
  ["vegetarien", "rapide"], "Préparé la veille et mangé froid, c'est aussi très bon.")
R("Omelette aux fines herbes et au jambon", PD, 10, [("oeuf", 120), ("jambon", 40), ("beurre", 5), ("persil", 3)],
  ["Battez les œufs avec le persil ciselé.", "Faites fondre le beurre dans une poêle et versez les œufs.", "Garnissez de jambon coupé en lanières et repliez."],
  ["oeufs", "rapide"])
R("Fromage blanc, framboises et amandes", PD, 5, [("fb0", 200), ("framboise", 80), ("amande", 15), ("miel", 5)],
  ["Versez le fromage blanc dans un bol.", "Ajoutez les framboises, les amandes concassées et un filet de miel."], ["vegetarien", "rapide"])
R("Tartines œuf-avocat", PD, 10, [("paincompl", 50), ("avocat", 50), ("oeufdur", 120)],
  ["Écrasez l'avocat à la fourchette avec un peu de citron.", "Tartinez le pain, ajoutez les œufs durs en rondelles, poivrez."], ["oeufs", "rapide"])
R("Œufs brouillés au saumon", PD, 12, [("oeuf", 110), ("saumon", 50), ("beurre", 5), ("paincompl", 30)],
  ["Faites fondre le beurre à feu doux.", "Ajoutez les œufs battus et remuez jusqu'à une texture crémeuse.", "Servez avec le saumon émietté et le pain toasté."], ["poisson", "oeufs", "rapide"])
R("Pancakes avoine et banane", PD, 15, [("flocons", 40), ("oeuf", 60), ("fb0", 100), ("banane", 60), ("colza", 3)],
  ["Mixez les flocons, l'œuf, le fromage blanc et la moitié de la banane.", "Faites cuire de petites galettes 2 minutes par face dans la poêle huilée.", "Servez avec le reste de la banane en rondelles."], ["vegetarien"])
R("Bol de fromage blanc, poire et noix", PD, 5, [("fb0", 200), ("yaourt", 125), ("poire", 100), ("noix", 12)],
  ["Mélangez le fromage blanc et le yaourt.", "Ajoutez la poire en dés et les noix."], ["vegetarien", "rapide"])
R("Tartines de fromage blanc, jambon de dinde et concombre", PD, 8, [("paincompl", 60), ("fb0", 80), ("jambondinde", 50), ("concombre", 40)],
  ["Tartinez le pain de fromage blanc.", "Posez le jambon et le concombre en rondelles, poivrez."], ["rapide"])
R("Œufs cocotte aux épinards", PD, 20, [("oeuf", 120), ("epinard", 100), ("cremelegere", 20), ("paincompl", 30)],
  ["Préchauffez le four à 180 °C. Répartissez les épinards dans deux ramequins.", "Cassez un œuf dans chacun, ajoutez la crème.", "Enfournez 10 à 12 minutes. Servez avec la mouillette de pain."], ["oeufs", "four"])
R("Smoothie banane-cacao protéiné", PD, 5, [("lait", 150), ("banane", 100), ("fb0", 150), ("cacao", 5)],
  ["Épluchez la banane et versez le lait dans le mixeur.", "Ajoutez le fromage blanc et le cacao, mixez jusqu'à obtenir une texture lisse."], ["vegetarien", "rapide"])
R("Galettes d'avoine à la pomme", PD, 15, [("flocons", 30), ("oeuf", 60), ("pomme", 100), ("fb0", 100)],
  ["Mélangez les flocons, l'œuf et la moitié de la pomme râpée.", "Faites dorer en galettes à la poêle antiadhésive.", "Servez avec le fromage blanc et le reste de pomme."], ["vegetarien"])
R("Tartine de chèvre, tomate et basilic", PD, 8, [("paincompl", 60), ("chevre", 50), ("tomate", 80), ("basilic", 3), ("huileolive", 3)],
  ["Grillez le pain.", "Garnissez de chèvre, de tomate en rondelles et de basilic, arrosez d'un filet d'huile."], ["vegetarien", "rapide"])
R("Muesli maison, fromage blanc et fruits rouges", PD, 5, [("flocons", 35), ("fb0", 150), ("framboise", 80), ("amande", 10)],
  ["Mélangez les flocons et le fromage blanc.", "Ajoutez les framboises et les amandes concassées."], ["vegetarien", "rapide"])
R("Omelette aux champignons et à l'emmental", PD, 15, [("oeuf", 120), ("champignon", 80), ("beurre", 4), ("emmental", 20), ("paincompl", 30)],
  ["Faites dorer les champignons émincés dans le beurre.", "Versez les œufs battus, parsemez d'emmental et repliez.", "Servez avec le pain."], ["oeufs"])
R("Œufs durs, tomate et pain complet", PD, 12, [("oeufdur", 120), ("tomate", 100), ("paincompl", 50), ("huileolive", 3)],
  ["Coupez les œufs durs et la tomate.", "Arrosez d'huile, poivrez et servez avec le pain."], ["oeufs", "rapide"])

# ---------------------------------------------------------------- collations (22)
R("Fromage blanc et fraises", CO, 3, [("fb0", 150), ("fraise", 100)], ["Coupez les fraises sur le fromage blanc."], ["vegetarien", "rapide"])
R("Yaourt, fromage blanc, noix et miel", CO, 3, [("yaourt", 125), ("fb0", 80), ("noix", 8), ("miel", 4)],
  ["Mélangez le yaourt et le fromage blanc.", "Parsemez de noix et de miel."], ["vegetarien", "rapide"])
R("Pomme, amandes et fromage blanc", CO, 3, [("pomme", 150), ("amande", 15), ("fb0", 80)], ["Croquez la pomme avec les amandes et le fromage blanc."], ["vegetarien", "rapide"])
R("Œufs durs et crudités", CO, 12, [("oeufdur", 110), ("carotte", 80), ("concombre", 50)],
  ["Faites cuire les œufs 10 minutes à l'eau bouillante, écalez-les.", "Servez avec des bâtonnets de carotte et de concombre."], ["oeufs"])
R("Roulés de jambon de dinde au fromage blanc", CO, 5, [("jambondinde", 60), ("fb0", 50), ("concombre", 50), ("persil", 2)],
  ["Mélangez le fromage blanc et le persil.", "Étalez sur les tranches, ajoutez un bâtonnet de concombre et roulez."], ["rapide"])
R("Houmous maison et bâtonnets de carotte", CO, 10, [("poischiche", 80), ("citron", 10), ("huileolive", 6), ("ail", 2), ("yaourt", 30), ("carotte", 100)],
  ["Mixez les pois chiches avec le citron, l'huile, l'ail et le yaourt.", "Servez avec les bâtonnets de carotte."], ["vegetarien"])
R("Smoothie fraise-fromage blanc", CO, 5, [("fb0", 150), ("fraise", 100), ("lait", 80)], ["Mixez les trois ingrédients."], ["vegetarien", "rapide"])
R("Thon-concombre sur biscottes", CO, 5, [("thon", 50), ("concombre", 60), ("biscotte", 20), ("yaourt", 20)],
  ["Mélangez le thon émietté et le yaourt.", "Étalez sur les biscottes, ajoutez le concombre."], ["poisson", "rapide"])
R("Bouchées cacao-avoine", CO, 10, [("flocons", 20), ("cacao", 5), ("miel", 8), ("cacahuete", 12), ("fb0", 30)],
  ["Mélangez tous les ingrédients.", "Formez des boules et laissez-les durcir 30 minutes au frais."], ["vegetarien"])
R("Fromage blanc, cacao et framboises", CO, 3, [("fb0", 150), ("cacao", 5), ("framboise", 80), ("miel", 4)],
  ["Mélangez le fromage blanc et le cacao.", "Ajoutez les framboises et le miel."], ["vegetarien", "rapide"])
R("Crème de fromage blanc au citron", CO, 5, [("fb0", 150), ("citron", 10), ("miel", 6)],
  ["Fouettez le fromage blanc avec le jus de citron et le miel."], ["vegetarien", "rapide"])
R("Mini-sandwich jambon de dinde et cornichon", CO, 4, [("paincompl", 40), ("jambondinde", 40), ("cornichon", 15)],
  ["Garnissez le pain de jambon et de cornichons émincés."], ["rapide"])
R("Œufs mimosa légers", CO, 15, [("oeufdur", 110), ("yaourt", 30), ("moutarde", 5)],
  ["Coupez les œufs durs en deux et retirez les jaunes.", "Écrasez les jaunes avec le yaourt et la moutarde.", "Remplissez les blancs."], ["oeufs"])
R("Chèvre, pomme et noix", CO, 4, [("chevre", 40), ("pomme", 100), ("noix", 6)], ["Servez le chèvre avec la pomme en tranches et les noix."], ["vegetarien", "rapide"])
R("Mozzarella, tomates cerises et basilic", CO, 5, [("mozzarella", 60), ("tomatecerise", 100), ("basilic", 3), ("huileolive", 3)],
  ["Coupez la mozzarella et les tomates.", "Ajoutez le basilic et un filet d'huile."], ["vegetarien", "rapide"])
R("Petit-suisse aux framboises", CO, 2, [("petitsuisse", 120), ("framboise", 60)], ["Garnissez le petit-suisse de framboises."], ["vegetarien", "rapide"])
R("Kéfir à la banane", CO, 3, [("kefir", 200), ("banane", 60)], ["Mixez le kéfir et la banane."], ["vegetarien", "rapide"])
R("Sardines sur biscottes", CO, 4, [("sardinehuile", 40), ("biscotte", 20), ("citron", 8)], ["Posez les sardines sur les biscottes, ajoutez un filet de citron."], ["poisson", "rapide"])
R("Soupe de tomate au fromage blanc", CO, 8, [("coulis", 150), ("fb0", 100), ("basilic", 3)],
  ["Chauffez le coulis de tomates.", "Hors du feu, incorporez le fromage blanc et le basilic."], ["vegetarien", "rapide"])
R("Poire au fromage blanc et cannelle", CO, 4, [("poire", 120), ("fb0", 150), ("cannelle", 1)],
  ["Coupez la poire en dés sur le fromage blanc, saupoudrez de cannelle."], ["vegetarien", "rapide"])
R("Crevettes à l'ail et au citron", CO, 8, [("crevette", 80), ("ail", 3), ("huileolive", 4), ("citron", 8)],
  ["Faites revenir l'ail dans l'huile.", "Ajoutez les crevettes 2 minutes, arrosez de citron."], ["poisson", "rapide"])
R("Tofu nature, concombre et boisson au soja", CO, 5, [("tofu", 60), ("concombre", 60), ("soja", 100)],
  ["Coupez le tofu et le concombre en dés.", "Servez avec le verre de boisson au soja."], ["vegetarien", "rapide"])

# ---------------------------------------------------------------- plats : viandes (20)
R("Poulet rôti, haricots verts et pommes de terre", PL, 40, [("cuissepoulet", 150), ("harivert", 150), ("pdt", 150), ("huileolive", 5), ("ail", 3)],
  ["Préchauffez le four à 200 °C. Frottez le poulet d'ail et d'herbes, enfournez 30 minutes.", "Faites cuire les pommes de terre et les haricots verts à la vapeur.", "Servez avec un filet d'huile d'olive."], ["viande", "four"])
R("Blanquette de dinde légère", PL, 35, [("dinde", 150), ("carotte", 80), ("champignon", 80), ("poireau", 60), ("cremelegere", 40), ("riz", 100), ("bouillon", 150)],
  ["Faites mijoter la dinde en morceaux avec les légumes dans le bouillon 20 minutes.", "Ajoutez la crème légère hors du feu.", "Servez sur le riz."], ["viande"])
R("Poulet à la moutarde et riz", PL, 25, [("poulet", 150), ("moutarde", 10), ("cremelegere", 40), ("riz", 120), ("harivert", 100)],
  ["Faites dorer le poulet en morceaux.", "Ajoutez la moutarde et la crème, laissez napper 3 minutes.", "Servez avec le riz et les haricots verts."], ["viande", "rapide"])
R("Escalope de veau à la crème, petits pois", PL, 25, [("veau", 150), ("cremelegere", 40), ("champignon", 80), ("petitspois", 120), ("pdt", 100)],
  ["Poêlez l'escalope puis réservez.", "Faites revenir les champignons, ajoutez la crème et remettez la viande.", "Servez avec les petits pois et les pommes de terre vapeur."], ["viande"])
R("Steak haché maison et ratatouille", PL, 35, [("hache5", 130), ("courgette", 100), ("aubergine", 80), ("poivron", 60), ("tomate", 100), ("oignon", 40), ("huileolive", 8), ("pdt", 100)],
  ["Faites revenir l'oignon puis les légumes en dés dans l'huile, couvrez 20 minutes.", "Poêlez le steak à sec.", "Servez avec les pommes de terre vapeur."], ["viande"])
R("Sauté de porc aux légumes de printemps", PL, 30, [("porc", 140), ("carotte", 80), ("petitspois", 80), ("oignon", 40), ("huileolive", 6), ("riz", 100)],
  ["Faites dorer le porc en lamelles dans l'huile.", "Ajoutez l'oignon, la carotte et 100 ml d'eau, cuisez 12 minutes puis les petits pois.", "Servez avec le riz."], ["viande"])
R("Dinde au curry et au lait de coco", PL, 25, [("dinde", 150), ("laitcoco", 40), ("curry", 3), ("oignon", 50), ("poivron", 80), ("riz", 100), ("huileolive", 3)],
  ["Faites revenir l'oignon et le poivron avec le curry.", "Ajoutez la dinde en dés et le lait de coco, mijotez 10 minutes.", "Servez avec le riz."], ["viande", "rapide"])
R("Boulettes de bœuf à la tomate et pâtes", PL, 30, [("hache5", 120), ("coulis", 150), ("oignon", 40), ("ail", 3), ("pates", 150), ("parmesan", 10)],
  ["Mélangez la viande avec l'oignon haché, formez des boulettes.", "Poêlez-les puis laissez mijoter 10 minutes dans le coulis et l'ail.", "Servez sur les pâtes avec le parmesan."], ["viande"])
R("Rôti de porc et lentilles", PL, 45, [("porc", 130), ("lentille", 150), ("carotte", 60), ("oignon", 30), ("moutarde", 5), ("huileolive", 4)],
  ["Badigeonnez le porc de moutarde et rôtissez-le 30 minutes à 180 °C.", "Faites revenir l'oignon et la carotte dans l'huile et ajoutez les lentilles cuites.", "Tranchez le rôti et servez."], ["viande", "four"])
R("Gigot d'agneau aux haricots blancs", PL, 45, [("agneau", 120), ("haricotblanc", 150), ("tomate", 100), ("ail", 3), ("herbes", 1), ("huileolive", 5)],
  ["Rôtissez l'agneau avec l'ail et les herbes 25 minutes à 200 °C.", "Réchauffez les haricots avec la tomate et l'huile.", "Servez ensemble."], ["viande", "four"])
R("Lapin à la moutarde", PL, 40, [("lapin", 150), ("moutarde", 10), ("cremelegere", 40), ("champignon", 80), ("pdt", 150)],
  ["Faites dorer le lapin avec les champignons.", "Ajoutez la moutarde, la crème et un peu d'eau, mijotez 15 minutes.", "Servez avec les pommes de terre vapeur."], ["viande"])
R("Poulet basquaise", PL, 40, [("poulet", 150), ("poivron", 150), ("tomate", 150), ("oignon", 60), ("huileolive", 8), ("riz", 100)],
  ["Faites revenir l'oignon et les poivrons dans l'huile.", "Ajoutez les tomates et le poulet en morceaux, mijotez 25 minutes.", "Servez avec le riz."], ["viande"])
R("Dinde gratinée aux courgettes", PL, 35, [("dinde", 150), ("courgette", 200), ("mozzarella", 40), ("coulis", 80), ("pates", 100)],
  ["Disposez la dinde et les courgettes en rondelles dans un plat, couvrez de coulis.", "Ajoutez la mozzarella et enfournez 20 minutes à 200 °C.", "Servez avec les pâtes."], ["viande", "four"])
R("Pot-au-feu allégé", PL, 50, [("rumsteck", 120), ("carotte", 100), ("poireau", 100), ("chou", 100), ("pdt", 150), ("bouillon", 200)],
  ["Portez le bouillon à frémissement avec le bœuf coupé en gros morceaux.", "Après 20 minutes, ajoutez les légumes et les pommes de terre.", "Cuisez 25 minutes de plus."], ["viande"])
R("Bœuf aux oignons et purée de patate douce", PL, 30, [("rumsteck", 130), ("oignon", 100), ("patatedouce", 200), ("huileolive", 6)],
  ["Faites fondre les oignons dans l'huile 10 minutes.", "Poêlez le bœuf en lamelles, mélangez.", "Servez avec la patate douce écrasée."], ["viande"])
R("Jambon braisé aux endives", PL, 35, [("jambon", 120), ("endive", 200), ("cremelegere", 40), ("pdt", 150), ("emmental", 15)],
  ["Faites braiser les endives 15 minutes à la poêle couverte.", "Enroulez-les dans le jambon, nappez de crème et d'emmental.", "Passez 10 minutes au four, servez avec les pommes de terre vapeur."], ["viande", "four"])
R("Poulet à l'ail et légumes d'hiver", PL, 40, [("poulet", 150), ("butternut", 150), ("carotte", 80), ("pdtfour", 120), ("ail", 3), ("huileolive", 6)],
  ["Coupez les légumes en cubes et enfournez-les avec l'huile 25 minutes à 200 °C.", "Ajoutez le poulet en morceaux et l'ail, poursuivez 12 minutes."], ["viande", "four"])
R("Brochettes de dinde et légumes grillés, semoule", PL, 30, [("dinde", 140), ("poivron", 80), ("courgettecrue", 100), ("oignon", 40), ("semoule", 120), ("huileolive", 6)],
  ["Enfilez la dinde et les légumes en brochettes, huilez-les.", "Faites cuire 12 minutes à la plancha ou au four.", "Servez avec la semoule."], ["viande"])
R("Salade de poulet, œuf et avocat", PL, 20, [("poulet", 120), ("laitue", 80), ("avocat", 50), ("oeufdur", 55), ("tomatecerise", 80), ("huileolive", 8), ("vinaigre", 5)],
  ["Disposez la salade, les tomates et l'avocat en tranches.", "Ajoutez le poulet en lamelles et l'œuf dur coupé.", "Assaisonnez d'huile et de vinaigre."], ["viande", "rapide"])
R("Bœuf aux carottes", PL, 45, [("rumsteck", 130), ("carotte", 150), ("oignon", 50), ("pdt", 150), ("huileolive", 5)],
  ["Faites dorer le bœuf en cubes avec l'oignon dans l'huile.", "Ajoutez les carottes et un verre d'eau, mijotez 30 minutes.", "Servez avec les pommes de terre vapeur."], ["viande"])

# ---------------------------------------------------------------- plats : poissons (16)
R("Cabillaud, brocoli et pommes de terre", PL, 25, [("cabillaud", 180), ("brocoli", 150), ("pdt", 150), ("huileolive", 8), ("citron", 10)],
  ["Enfournez le cabillaud 12 minutes à 180 °C avec un filet de citron.", "Cuisez le brocoli et les pommes de terre à la vapeur.", "Arrosez d'huile d'olive."], ["poisson", "four"])
R("Saumon, riz et épinards", PL, 25, [("saumon", 130), ("riz", 100), ("epinard", 150), ("citron", 10)],
  ["Cuisez le saumon à la poêle ou au four 10 minutes.", "Faites tomber les épinards 3 minutes.", "Servez avec le riz et le citron."], ["poisson"])
R("Merlu à la tomate et semoule", PL, 25, [("merlu", 170), ("coulis", 100), ("semoule", 120), ("olive", 20), ("huileolive", 5)],
  ["Réchauffez le coulis avec les olives.", "Déposez le merlu et laissez cuire 8 minutes à couvert.", "Servez avec la semoule."], ["poisson", "rapide"])
R("Papillote de lieu aux légumes", PL, 35, [("lieu", 170), ("courgettecrue", 100), ("carotte", 80), ("poireau", 80), ("pdt", 150), ("huileolive", 6)],
  ["Coupez les légumes en fines lamelles et disposez-les sur une feuille de papier cuisson avec le poisson.", "Arrosez d'huile, fermez la papillote et enfournez 20 minutes à 180 °C.", "Servez avec les pommes de terre vapeur."], ["poisson", "four"])
R("Truite aux amandes", PL, 25, [("truite", 140), ("amande", 10), ("harivert", 150), ("pdt", 150), ("beurre", 5)],
  ["Faites cuire la truite au four 12 minutes.", "Faites dorer les amandes dans le beurre et nappez-en le poisson.", "Servez avec les haricots verts et les pommes de terre."], ["poisson", "four"])
R("Moules marinières et pommes de terre au four", PL, 30, [("moule", 200), ("pdtfour", 150), ("vinblanc", 50), ("echalote", 30), ("persil", 3), ("beurre", 5), ("cremelegere", 20)],
  ["Faites suer l'échalote dans le beurre, ajoutez le vin blanc.", "Versez les moules, couvrez 5 minutes jusqu'à ouverture.", "Ajoutez la crème et le persil. Servez avec les pommes de terre."], ["poisson"])
R("Parmentier de haddock", PL, 40, [("haddock", 150), ("pdt", 200), ("lait", 80), ("epinard", 80), ("beurre", 5)],
  ["Écrasez les pommes de terre cuites avec le lait et le beurre.", "Disposez le haddock émietté et les épinards dans un plat, couvrez de purée.", "Gratinez 15 minutes à 200 °C."], ["poisson", "four"])
R("Thon à la provençale", PL, 30, [("thon", 150), ("tomate", 150), ("poivron", 80), ("olive", 20), ("pates", 120), ("huileolive", 5)],
  ["Faites revenir le poivron dans l'huile, ajoutez les tomates en dés.", "Incorporez le thon et les olives, chauffez 5 minutes.", "Servez avec les pâtes."], ["poisson"])
R("Crevettes sautées, riz et petits légumes", PL, 20, [("crevette", 150), ("riz", 100), ("poivron", 80), ("petitspois", 80), ("huileolive", 6), ("ail", 3)],
  ["Faites sauter l'ail et le poivron en lanières dans l'huile.", "Ajoutez les petits pois et les crevettes, 3 minutes.", "Servez avec le riz."], ["poisson", "rapide"])
R("Cabillaud en croûte de moutarde, chou-fleur", PL, 30, [("cabillaud", 170), ("moutarde", 10), ("paincompl", 15), ("chouxfleur", 200), ("pdt", 100), ("huileolive", 6)],
  ["Badigeonnez le cabillaud de moutarde et recouvrez de chapelure de pain.", "Enfournez 15 minutes à 200 °C.", "Servez avec le chou-fleur et les pommes de terre vapeur."], ["poisson", "four"])
R("Sardines grillées, pommes de terre et salade", PL, 25, [("sardine", 130), ("pdt", 150), ("laitue", 60), ("huileolive", 6), ("vinaigre", 5)],
  ["Faites griller les sardines 3 minutes par face.", "Cuisez les pommes de terre à la vapeur.", "Assaisonnez la salade d'huile et de vinaigre."], ["poisson", "rapide"])
R("Maquereau, lentilles à la moutarde", PL, 20, [("maquereau", 100), ("lentille", 150), ("oignon", 30), ("moutarde", 5), ("vinaigre", 5)],
  ["Réchauffez les lentilles avec l'oignon haché.", "Assaisonnez avec la moutarde et le vinaigre.", "Posez le maquereau émietté dessus."], ["poisson", "rapide"])
R("Noix de Saint-Jacques et fondue de poireaux", PL, 25, [("stjacques", 150), ("poireau", 200), ("cremelegere", 40), ("riz", 80)],
  ["Faites fondre les poireaux émincés à feu doux 12 minutes.", "Ajoutez la crème.", "Saisissez les Saint-Jacques 2 minutes par face. Servez avec le riz."], ["poisson"])
R("Truite et fenouil rôtis", PL, 35, [("truite", 150), ("fenouil", 200), ("pdt", 150), ("huileolive", 6)],
  ["Coupez le fenouil en quartiers, huilez et enfournez 20 minutes à 200 °C.", "Ajoutez la truite pour les 12 dernières minutes.", "Servez avec les pommes de terre vapeur."], ["poisson", "four"])
R("Soupe de poissons et croûtons", PL, 35, [("lieu", 150), ("pdt", 150), ("carotte", 80), ("poireau", 80), ("tomate", 80), ("ail", 3), ("paincompl", 30), ("huileolive", 5)],
  ["Faites revenir les légumes coupés avec l'ail dans l'huile, couvrez d'eau et cuisez 20 minutes.", "Ajoutez le poisson 5 minutes, mixez grossièrement.", "Servez avec des croûtons de pain."], ["poisson"])
R("Saumon et lentilles aux épinards", PL, 25, [("saumon", 120), ("lentille", 150), ("epinard", 80)],
  ["Poêlez le saumon 8 minutes.", "Réchauffez les lentilles avec les épinards.", "Servez ensemble."], ["poisson", "rapide"])

# ---------------------------------------------------------------- plats : œufs et végétariens (11)
R("Quiche sans pâte jambon-poireau", PL, 40, [("oeuf", 150), ("jambon", 60), ("poireau", 100), ("lait", 100), ("emmental", 25)],
  ["Faites revenir le poireau émincé quelques minutes.", "Battez les œufs avec le lait, ajoutez le jambon, le poireau et l'emmental.", "Versez dans un plat et enfournez 25 minutes à 180 °C."], ["oeufs", "four"])
R("Frittata aux légumes et au chèvre", PL, 30, [("oeuf", 180), ("courgettecrue", 100), ("poivron", 60), ("chevre", 30), ("oignon", 40), ("huileolive", 5), ("pdt", 100)],
  ["Faites revenir l'oignon, la courgette et le poivron en dés dans l'huile.", "Versez les œufs battus et ajoutez le chèvre en morceaux.", "Cuisez 10 minutes à couvert. Servez avec les pommes de terre vapeur."], ["oeufs"])
R("Tofu sauté, brocoli et riz complet", PL, 25, [("tofu", 200), ("brocoli", 120), ("rizcompl", 100), ("huileolive", 4)],
  ["Poêlez le tofu en cubes jusqu'à ce qu'il soit doré.", "Ajoutez le brocoli cuit à la vapeur.", "Servez avec le riz complet."], ["vegetarien", "rapide"])
R("Curry de lentilles et pois chiches, raïta", PL, 30, [("lentille", 150), ("poischiche", 80), ("laitcoco", 40), ("tomate", 80), ("oignon", 50), ("curry", 3), ("fb0", 100)],
  ["Faites revenir l'oignon avec le curry, ajoutez la tomate, les lentilles et les pois chiches.", "Versez le lait de coco, mijotez 10 minutes.", "Servez avec le fromage blanc en raïta."], ["vegetarien"])
R("Gratin de chou-fleur au jambon", PL, 40, [("chouxfleur", 250), ("jambon", 100), ("lait", 100), ("emmental", 30), ("oeuf", 60)],
  ["Faites cuire le chou-fleur 10 minutes à la vapeur.", "Disposez-le avec le jambon dans un plat, nappez du mélange œuf-lait et d'emmental.", "Enfournez 25 minutes à 180 °C."], ["oeufs", "four"])
R("Salade de pois chiches, feta et thon", PL, 15, [("poischiche", 150), ("feta", 50), ("concombre", 80), ("tomate", 100), ("thon", 60), ("huileolive", 8)],
  ["Mélangez les pois chiches, le concombre et la tomate en dés.", "Ajoutez la feta, le thon et l'huile."], ["poisson", "rapide"])
R("Omelette espagnole légère", PL, 30, [("oeuf", 180), ("pdt", 150), ("oignon", 60), ("jambondinde", 40), ("huileolive", 8)],
  ["Faites fondre l'oignon et les pommes de terre en dés dans l'huile 10 minutes.", "Versez les œufs battus avec le jambon.", "Cuisez 5 minutes de chaque côté."], ["oeufs"])
R("Lasagnes d'aubergines", PL, 50, [("aubergine", 250), ("hache5", 100), ("coulis", 150), ("mozzarella", 50), ("parmesan", 10)],
  ["Faites griller les tranches d'aubergine.", "Superposez aubergines, viande poêlée mêlée au coulis, mozzarella.", "Enfournez 25 minutes à 190 °C avec le parmesan."], ["viande", "four"])
R("Chili con carne léger", PL, 35, [("hache5", 100), ("haricotrouge", 120), ("coulis", 150), ("poivron", 60), ("oignon", 50), ("riz", 80)],
  ["Poêlez la viande avec l'oignon et le poivron.", "Ajoutez le coulis et les haricots rouges, mijotez 20 minutes.", "Servez avec le riz."], ["viande"])
R("Velouté de butternut, œufs durs et fromage blanc", PL, 30, [("butternut", 250), ("oeufdur", 110), ("fb0", 120), ("paincompl", 50), ("bouillon", 200)],
  ["Cuisez la courge en cubes dans le bouillon 15 minutes, mixez avec le fromage blanc.", "Servez avec les œufs durs en quartiers et le pain."], ["oeufs"])
R("Poêlée de pois chiches, épinards et œufs", PL, 20, [("poischiche", 150), ("epinard", 150), ("oeuf", 120), ("huileolive", 6), ("ail", 3)],
  ["Faites revenir l'ail et les pois chiches dans l'huile, ajoutez les épinards.", "Creusez deux puits, cassez-y les œufs et couvrez 5 minutes."], ["oeufs", "rapide"])

# ---------------------------------------------------------------- plats : classiques d'Europe (16)
R("Soupe de légumes et poulet effiloché", PL, 35, [("poulet", 120), ("carotte", 80), ("poireau", 80), ("pdt", 150), ("pates", 80), ("bouillon", 250)],
  ["Cuisez les légumes en morceaux dans le bouillon 20 minutes.", "Ajoutez les pâtes et le poulet effiloché 5 minutes."], ["viande"])
R("Salade niçoise", PL, 20, [("thon", 100), ("oeufdur", 55), ("harivert", 100), ("tomate", 100), ("olive", 20), ("pdt", 100), ("huileolive", 8)],
  ["Disposez les légumes cuits et crus dans un saladier.", "Ajoutez le thon, l'œuf dur et les olives.", "Assaisonnez d'huile d'olive."], ["poisson", "rapide"])
R("Salade de lentilles au saumon", PL, 20, [("saumon", 100), ("lentille", 150), ("echalote", 20), ("huileolive", 6), ("vinaigre", 5), ("persil", 3)],
  ["Mélangez les lentilles avec l'échalote hachée, l'huile et le vinaigre.", "Posez le saumon émietté et le persil."], ["poisson", "rapide"])
R("Taboulé de quinoa au poulet", PL, 20, [("poulet", 120), ("quinoa", 150), ("concombre", 80), ("tomate", 100), ("citron", 15), ("huileolive", 6)],
  ["Mélangez le quinoa froid avec les légumes en dés.", "Ajoutez le poulet en lamelles, le citron et l'huile."], ["viande", "rapide"])
R("Boulgour, pois chiches et poulet", PL, 25, [("boulgour", 150), ("poischiche", 80), ("poulet", 100), ("courgette", 100), ("huileolive", 5)],
  ["Poêlez le poulet et la courgette en dés dans l'huile.", "Mélangez avec le boulgour et les pois chiches."], ["viande"])
R("Gratin dauphinois léger au jambon", PL, 55, [("pdt", 250), ("jambon", 100), ("lait", 100), ("emmental", 25), ("ail", 3)],
  ["Disposez les pommes de terre en rondelles et le jambon dans un plat frotté d'ail.", "Versez le lait, parsemez d'emmental.", "Enfournez 40 minutes à 180 °C."], ["viande", "four"])
R("Hachis Parmentier léger", PL, 45, [("hache5", 130), ("pdt", 200), ("lait", 40), ("carotte", 60), ("oignon", 40), ("emmental", 15)],
  ["Faites revenir l'oignon et la carotte, ajoutez la viande.", "Couvrez de purée de pommes de terre au lait.", "Gratinez avec l'emmental 15 minutes à 200 °C."], ["viande", "four"])
R("Cassoulet léger", PL, 50, [("haricotblanc", 200), ("porc", 100), ("lardons", 20), ("coulis", 100), ("carotte", 60)],
  ["Faites revenir les lardons, ajoutez le porc en dés, le coulis et la carotte.", "Ajoutez les haricots, mijotez 30 minutes."], ["viande"])
R("Carbonara allégée", PL, 20, [("patescompl", 150), ("lardons", 40), ("oeuf", 60), ("parmesan", 10), ("fb0", 50)],
  ["Faites cuire les pâtes. Poêlez les lardons.", "Mélangez l'œuf, le fromage blanc et le parmesan.", "Hors du feu, enrobez les pâtes de la sauce avec les lardons."], ["viande", "rapide"])
R("Pâtes aux crevettes et aux courgettes", PL, 20, [("pates", 150), ("crevette", 120), ("courgette", 150), ("ail", 3), ("huileolive", 8), ("citron", 10)],
  ["Faites revenir l'ail et les courgettes en rondelles dans l'huile.", "Ajoutez les crevettes 2 minutes.", "Mêlez aux pâtes avec le citron."], ["poisson", "rapide"])
R("Spaghettis bolognaise allégée", PL, 30, [("pates", 150), ("hache5", 110), ("coulis", 150), ("carotte", 50), ("oignon", 40), ("parmesan", 8)],
  ["Faites revenir l'oignon et la carotte râpée, ajoutez la viande puis le coulis, mijotez 15 minutes.", "Servez sur les pâtes avec le parmesan."], ["viande"])
R("Risotto de riz aux champignons et au poulet", PL, 30, [("riz", 120), ("poulet", 100), ("champignon", 120), ("parmesan", 15), ("bouillon", 150), ("oignon", 30), ("huileolive", 5)],
  ["Faites revenir l'oignon et les champignons dans l'huile.", "Ajoutez le riz cuit, le poulet en dés et le bouillon, réduisez 5 minutes.", "Terminez avec le parmesan."], ["viande"])
R("Moussaka légère", PL, 50, [("aubergine", 250), ("agneau", 100), ("coulis", 100), ("fb0", 100), ("oeuf", 30)],
  ["Faites griller les aubergines, poêlez l'agneau avec le coulis.", "Superposez en couches, nappez du mélange fromage blanc et œuf.", "Enfournez 25 minutes à 190 °C."], ["viande", "four"])
R("Endives au jambon gratinées", PL, 45, [("endive", 300), ("jambon", 120), ("lait", 100), ("emmental", 25), ("farine", 8), ("pdt", 120)],
  ["Faites braiser les endives 15 minutes, enroulez-les dans le jambon.", "Préparez une béchamel allégée avec le lait et la farine, nappez.", "Gratinez avec l'emmental, servez avec les pommes de terre."], ["viande", "four"])
R("Gratin de poisson aux poireaux", PL, 40, [("eglefin", 170), ("poireau", 150), ("cremelegere", 50), ("pdt", 150), ("emmental", 15)],
  ["Disposez le poisson et les poireaux fondus dans un plat, nappez de crème.", "Parsemez d'emmental et gratinez 20 minutes à 190 °C.", "Servez avec les pommes de terre vapeur."], ["poisson", "four"])
R("Poulet citron-thym, courgettes et semoule", PL, 30, [("poulet", 140), ("courgette", 150), ("semoule", 100), ("huileolive", 5), ("citron", 15)],
  ["Marinez le poulet au citron et aux herbes.", "Poêlez-le avec les courgettes en rondelles.", "Servez avec la semoule."], ["viande"])


import recettes_lot2  # noqa: E402,F401  (deuxième lot)
import recettes_lot3  # noqa: E402,F401  (troisième lot)
import recettes_lot4  # noqa: E402,F401  (quatrième lot)
import recettes_lot5  # noqa: E402,F401  (cinquième lot)

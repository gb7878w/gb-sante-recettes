"""Deuxième lot de recettes (pour UNE personne), ajouté après le premier."""
from recettes_src import R, PD, PL, CO

# ---------------------------------------------------------------- petits-déjeuners (15)
R("Porridge poire-noisette", PD, 10, [("flocons", 40), ("lait", 150), ("fb0", 100), ("poire", 80), ("noisette", 8)],
  ["Faites chauffer les flocons avec le lait 4 minutes en remuant.", "Ajoutez le fromage blanc et la poire en dés, parsemez de noisettes."], ["vegetarien", "rapide"])
R("Omelette au fromage de chèvre et aux herbes", PD, 10, [("oeuf", 120), ("chevre", 30), ("beurre", 4), ("persil", 3), ("paincompl", 30)],
  ["Battez les œufs avec les herbes.", "Faites cuire dans le beurre, ajoutez le chèvre en morceaux et repliez.", "Servez avec le pain grillé."], ["vegetarien", "oeufs", "rapide"])
R("Skyr maison, fraises et amandes", PD, 5, [("fb0", 200), ("yaourt", 100), ("fraise", 100), ("amande", 12)],
  ["Mélangez le fromage blanc et le yaourt dans un bol.", "Ajoutez les fraises coupées et les amandes concassées."], ["vegetarien", "rapide"])
R("Tartine au thon et au concombre", PD, 8, [("paincompl", 60), ("thon", 60), ("fb0", 40), ("concombre", 40)],
  ["Écrasez le thon avec le fromage blanc et le poivre.", "Tartinez le pain, ajoutez le concombre en rondelles."], ["poisson", "rapide"])
R("Œufs au plat, tomates grillées et pain complet", PD, 12, [("oeuf", 120), ("tomate", 120), ("paincompl", 40), ("huileolive", 4)],
  ["Faites griller les tomates coupées en deux dans l'huile.", "Cassez les œufs dans la poêle et laissez cuire.", "Servez avec le pain."], ["vegetarien", "oeufs"])
R("Bol de flocons d'avoine, kéfir et banane", PD, 5, [("flocons", 40), ("kefir", 200), ("fb0", 80), ("banane", 80), ("noix", 8)],
  ["Versez le kéfir sur les flocons et laissez gonfler 5 minutes.", "Ajoutez la banane en rondelles et les noix."], ["vegetarien", "rapide"])
R("Pain perdu léger à la cannelle", PD, 15, [("paincompl", 60), ("oeuf", 60), ("lait", 100), ("cannelle", 1), ("fb0", 100), ("beurre", 4)],
  ["Battez l'œuf avec le lait et la cannelle.", "Trempez le pain puis faites-le dorer dans le beurre.", "Servez avec le fromage blanc."], ["vegetarien"])
R("Salade de fruits et fromage blanc", PD, 8, [("fb0", 200), ("orange", 100), ("pomme", 80), ("amande", 12), ("flocons", 20)],
  ["Coupez l'orange et la pomme en morceaux.", "Mélangez avec le fromage blanc et ajoutez les flocons et les amandes."], ["vegetarien", "rapide"])
R("Omelette au jambon de dinde et aux poivrons", PD, 12, [("oeuf", 120), ("jambondinde", 40), ("poivron", 60), ("huileolive", 4)],
  ["Faites revenir les poivrons en lanières dans l'huile.", "Versez les œufs battus, ajoutez le jambon et repliez."], ["oeufs", "rapide"])
R("Tartines de saumon fumé et fromage blanc", PD, 8, [("paincompl", 60), ("saumon", 50), ("fb0", 60), ("citron", 5)],
  ["Mélangez le fromage blanc et le citron.", "Tartinez le pain, posez le saumon émietté."], ["poisson", "rapide"])
R("Crêpes protéinées au fromage blanc", PD, 15, [("farine", 30), ("oeuf", 60), ("fb0", 120), ("lait", 80), ("fraise", 60)],
  ["Mixez la farine, l'œuf, le lait et la moitié du fromage blanc.", "Cuisez de fines crêpes dans une poêle antiadhésive.", "Garnissez avec le reste de fromage blanc et les fraises."], ["vegetarien"])
R("Œufs mimosa et pain complet", PD, 15, [("oeufdur", 110), ("fb0", 30), ("moutarde", 3), ("paincompl", 40)],
  ["Coupez les œufs durs en deux et écrasez les jaunes avec le fromage blanc et la moutarde.", "Garnissez les blancs et servez avec le pain."], ["vegetarien", "oeufs"])
R("Yaourt grec, miel et noix", PD, 3, [("fb0", 200), ("yaourt", 125), ("miel", 8), ("noix", 12)],
  ["Mélangez le fromage blanc et le yaourt.", "Ajoutez le miel et les noix concassées."], ["vegetarien", "rapide"])
R("Tartine d'avocat, œuf et tomate", PD, 10, [("paincompl", 50), ("avocat", 40), ("oeuf", 100), ("tomate", 60)],
  ["Écrasez l'avocat sur le pain grillé.", "Ajoutez la tomate et l'œuf poché ou au plat."], ["vegetarien", "oeufs", "rapide"])
R("Smoothie fraise-vanille protéiné", PD, 5, [("lait", 150), ("fraise", 120), ("fb0", 150), ("flocons", 15)],
  ["Mettez tous les ingrédients dans le mixeur.", "Mixez jusqu'à obtenir une boisson onctueuse."], ["vegetarien", "rapide"])

# ---------------------------------------------------------------- collations (22)
R("Pomme et amandes", CO, 2, [("pomme", 150), ("amande", 15), ("fb0", 60)], ["Coupez la pomme en quartiers.", "Servez avec les amandes et le fromage blanc."], ["vegetarien", "rapide"])
R("Fromage blanc à la cannelle", CO, 3, [("fb0", 150), ("cannelle", 1), ("miel", 5)], ["Mélangez le fromage blanc avec la cannelle et le miel."], ["vegetarien", "rapide"])
R("Œuf dur et crudités", CO, 12, [("oeufdur", 110), ("carotte", 80), ("concombre", 60)], ["Écalez l'œuf dur.", "Servez avec les bâtonnets de carotte et de concombre."], ["oeufs"])
R("Yaourt nature et framboises", CO, 3, [("yaourt", 125), ("framboise", 80), ("fb0", 60)], ["Versez le yaourt et le fromage blanc dans un bol.", "Ajoutez les framboises."], ["vegetarien", "rapide"])
R("Tranche de jambon de dinde roulée au fromage blanc", CO, 5, [("jambondinde", 60), ("fb0", 50), ("concombre", 50)], ["Étalez le fromage blanc sur le jambon.", "Roulez avec un bâtonnet de concombre."], ["rapide"])
R("Poire et noix", CO, 2, [("poire", 150), ("noix", 12), ("fb0", 80)], ["Coupez la poire.", "Servez avec les noix et le fromage blanc."], ["vegetarien", "rapide"])
R("Biscottes au fromage frais", CO, 3, [("biscotte", 20), ("fb0", 80), ("tomatecerise", 60)], ["Tartinez les biscottes de fromage blanc.", "Ajoutez les tomates cerises coupées."], ["vegetarien", "rapide"])
R("Boisson au soja et banane", CO, 3, [("soja", 200), ("banane", 80), ("fb0", 80)], ["Mixez tous les ingrédients."], ["vegetarien", "rapide"])
R("Houmous léger et bâtonnets de légumes", CO, 10, [("poischiche", 60), ("fb0", 50), ("citron", 8), ("carotte", 80), ("concombre", 60)], ["Mixez les pois chiches avec le fromage blanc et le citron.", "Servez avec les bâtonnets de légumes."], ["vegetarien"])
R("Kéfir et fraises", CO, 3, [("kefir", 200), ("fraise", 100), ("fb0", 50)], ["Versez le kéfir dans un verre.", "Ajoutez les fraises coupées et le fromage blanc."], ["vegetarien", "rapide"])
R("Petit-suisse aux fruits rouges", CO, 3, [("petitsuisse", 120), ("framboise", 80), ("fb0", 50)], ["Servez le petit-suisse avec les framboises."], ["vegetarien", "rapide"])
R("Mini-brochettes mozzarella et tomates", CO, 5, [("mozzarella", 50), ("tomatecerise", 80), ("basilic", 2), ("fb0", 50)], ["Alternez mozzarella, tomates et basilic sur des piques.", "Servez avec le fromage blanc."], ["vegetarien", "rapide"])
R("Orange et fromage blanc", CO, 3, [("orange", 150), ("fb0", 120)], ["Pelez l'orange et coupez-la en quartiers.", "Servez avec le fromage blanc."], ["vegetarien", "rapide"])
R("Œuf dur et petits pois", CO, 12, [("oeufdur", 110), ("petitspois", 60)], ["Écalez l'œuf dur.", "Servez-le avec les petits pois tièdes et du poivre."], ["oeufs"])
R("Lait chaud cacao et biscotte", CO, 5, [("lait", 200), ("cacao", 4), ("biscotte", 15), ("fb0", 60)], ["Faites chauffer le lait avec le cacao.", "Servez avec la biscotte et le fromage blanc."], ["vegetarien", "rapide"])
R("Thon et tomates cerises", CO, 3, [("thon", 60), ("tomatecerise", 100), ("fb0", 50)], ["Servez le thon égoutté avec les tomates.", "Ajoutez le fromage blanc."], ["poisson", "rapide"])
R("Compote maison et yaourt", CO, 15, [("pomme", 150), ("cannelle", 1), ("yaourt", 125), ("fb0", 60)], ["Faites cuire la pomme en morceaux avec la cannelle 10 minutes.", "Écrasez et servez avec le yaourt."], ["vegetarien"])
R("Concombre-feta", CO, 5, [("concombre", 100), ("feta", 30), ("fb0", 80)], ["Coupez le concombre en dés.", "Ajoutez la feta émiettée et le fromage blanc."], ["vegetarien", "rapide"])
R("Banane et fromage blanc", CO, 3, [("banane", 100), ("fb0", 150)], ["Écrasez la banane et mélangez avec le fromage blanc."], ["vegetarien", "rapide"])
R("Jambon blanc et cornichons", CO, 3, [("jambon", 60), ("cornichon", 30), ("fb0", 60)], ["Roulez le jambon avec les cornichons.", "Servez avec le fromage blanc."], ["rapide"])
R("Yaourt, flocons et pomme", CO, 5, [("yaourt", 125), ("flocons", 15), ("pomme", 80), ("fb0", 60)], ["Mélangez le yaourt et les flocons.", "Ajoutez la pomme en dés."], ["vegetarien", "rapide"])
R("Saumon et fromage frais sur biscotte", CO, 5, [("saumon", 40), ("fb0", 80), ("biscotte", 15)], ["Tartinez les biscottes de fromage blanc.", "Posez le saumon émietté."], ["poisson", "rapide"])

# ---------------------------------------------------------------- plats : viandes (22)
R("Poulet rôti aux herbes et haricots verts", PL, 40, [("poulet", 140), ("harivert", 200), ("pdt", 150), ("huileolive", 6), ("herbes", 2)],
  ["Assaisonnez le poulet aux herbes et rôtissez-le 25 minutes à 200 °C.", "Faites cuire les haricots verts.", "Servez avec les pommes de terre vapeur."], ["viande", "four"])
R("Blanquette de dinde aux champignons", PL, 40, [("dinde", 140), ("carotte", 80), ("champignon", 100), ("cremelegere", 40), ("riz", 120), ("farine", 6)],
  ["Faites mijoter la dinde en dés avec la carotte 20 minutes.", "Ajoutez les champignons, la crème et la farine délayée.", "Servez avec le riz."], ["viande"])
R("Steak haché, purée de patate douce et brocoli", PL, 30, [("hache5", 130), ("patatedouce", 200), ("brocoli", 150), ("huileolive", 4)],
  ["Écrasez la patate douce cuite en purée.", "Poêlez le steak, cuisez le brocoli à la vapeur."], ["viande"])
R("Escalope de veau à la crème et riz", PL, 25, [("veau", 140), ("cremelegere", 40), ("champignon", 100), ("riz", 120), ("huileolive", 4)],
  ["Poêlez l'escalope et les champignons dans l'huile.", "Ajoutez la crème et laissez réduire.", "Servez avec le riz."], ["viande"])
R("Sauté de porc aux légumes", PL, 25, [("porc", 130), ("poivron", 100), ("courgette", 100), ("riz", 120), ("huileolive", 5)],
  ["Poêlez le porc en lanières avec l'huile.", "Ajoutez les légumes en dés, cuisez 8 minutes.", "Servez avec le riz."], ["viande"])
R("Poulet mijoté aux poivrons et au riz", PL, 40, [("poulet", 140), ("poivron", 150), ("tomate", 100), ("oignon", 40), ("riz", 120), ("huileolive", 6)],
  ["Faites revenir l'oignon, les poivrons et le poulet.", "Ajoutez les tomates et mijotez 25 minutes.", "Servez avec le riz."], ["viande"])
R("Lapin mijoté à la moutarde ancienne", PL, 45, [("lapin", 150), ("moutarde", 12), ("cremelegere", 40), ("pdt", 200), ("harivert", 100)],
  ["Faites dorer le lapin, nappez de moutarde et de crème.", "Mijotez 30 minutes.", "Servez avec les pommes de terre et les haricots verts."], ["viande"])
R("Brochettes de poulet et riz complet", PL, 30, [("poulet", 140), ("poivron", 100), ("courgette", 100), ("rizcompl", 130), ("huileolive", 5)],
  ["Enfilez poulet et légumes sur des piques.", "Faites griller 10 minutes.", "Servez avec le riz complet."], ["viande"])
R("Pot-au-feu léger", PL, 60, [("rumsteck", 120), ("carotte", 100), ("poireau", 100), ("pdt", 200), ("celeri", 50)],
  ["Portez à frémissement la viande avec les légumes dans l'eau.", "Laissez mijoter 45 minutes.", "Servez avec un peu de moutarde."], ["viande"])
R("Dinde au curry et riz basmati", PL, 30, [("dinde", 140), ("curry", 3), ("laitcoco", 30), ("oignon", 40), ("riz", 130), ("courgette", 100)],
  ["Faites revenir l'oignon et la dinde en dés avec le curry.", "Ajoutez la courgette et le lait de coco, mijotez 10 minutes.", "Servez avec le riz."], ["viande"])
R("Rumsteck, haricots verts et pommes de terre", PL, 25, [("rumsteck", 130), ("harivert", 200), ("pdtfour", 180), ("huileolive", 5)],
  ["Poêlez le rumsteck à votre goût.", "Servez avec les haricots verts et les pommes de terre au four."], ["viande"])
R("Poulet à la crème et champignons", PL, 30, [("poulet", 140), ("champignon", 150), ("cremelegere", 40), ("pates", 130)],
  ["Poêlez le poulet puis les champignons.", "Ajoutez la crème, laissez réduire.", "Servez avec les pâtes."], ["viande"])
R("Tajine de poulet aux légumes", PL, 45, [("poulet", 140), ("carotte", 100), ("courgette", 100), ("poischiche", 60), ("semoule", 100), ("cumin", 2)],
  ["Faites revenir le poulet avec le cumin.", "Ajoutez les légumes et les pois chiches, mijotez 30 minutes.", "Servez avec la semoule."], ["viande"])
R("Boulettes de bœuf à la tomate", PL, 30, [("hache5", 130), ("coulis", 150), ("pates", 130), ("oignon", 30), ("herbes", 2)],
  ["Formez des boulettes avec la viande et l'oignon haché.", "Faites-les dorer puis mijotez-les dans le coulis.", "Servez avec les pâtes."], ["viande"])
R("Filet mignon de porc moutarde et haricots", PL, 30, [("porc", 130), ("moutarde", 10), ("harivert", 200), ("pdt", 180), ("cremelegere", 30)],
  ["Badigeonnez le porc de moutarde et de crème.", "Enfournez 20 minutes à 190 °C.", "Servez avec les haricots verts et les pommes de terre."], ["viande", "four"])
R("Poulet citron et quinoa", PL, 25, [("poulet", 140), ("quinoa", 150), ("citron", 15), ("epinardcru", 60), ("huileolive", 5)],
  ["Poêlez le poulet avec le citron.", "Mélangez le quinoa aux épinards frais, servez avec le poulet."], ["viande"])
R("Chili de bœuf et haricots rouges", PL, 35, [("hache5", 110), ("haricotrouge", 120), ("coulis", 120), ("poivron", 80), ("riz", 100), ("cumin", 2)],
  ["Faites revenir la viande et le poivron avec le cumin.", "Ajoutez haricots et coulis, mijotez 20 minutes.", "Servez avec le riz."], ["viande"])
R("Dinde et lentilles à la carotte", PL, 30, [("dinde", 130), ("lentille", 180), ("carotte", 80), ("oignon", 30), ("huileolive", 5)],
  ["Poêlez la dinde en dés avec l'oignon.", "Ajoutez les lentilles et la carotte râpée, chauffez 8 minutes."], ["viande"])
R("Jambon braisé et chou", PL, 35, [("jambon", 120), ("chou", 200), ("pdt", 200), ("moutarde", 8), ("huileolive", 5)],
  ["Faites braiser le chou 20 minutes avec un peu d'eau.", "Ajoutez le jambon, servez avec la moutarde et les pommes de terre."], ["viande"])
R("Wok de bœuf aux légumes", PL, 20, [("rumsteck", 120), ("brocoli", 150), ("carotte", 80), ("riz", 120), ("huileolive", 5)],
  ["Poêlez le bœuf en lanières 3 minutes.", "Ajoutez brocoli et carotte, cuisez 6 minutes.", "Servez avec le riz."], ["viande", "rapide"])
R("Escalope de dinde panée au four", PL, 30, [("dinde", 140), ("biscotte", 20), ("oeuf", 30), ("harivert", 200), ("pdt", 150)],
  ["Trempez l'escalope dans l'œuf puis dans les biscottes écrasées.", "Enfournez 15 minutes à 200 °C.", "Servez avec les légumes."], ["viande", "four"])
R("Cuisse de poulet rôtie et ratatouille", PL, 45, [("cuissepoulet", 150), ("aubergine", 100), ("courgette", 100), ("tomate", 100), ("poivron", 60), ("huileolive", 6)],
  ["Rôtissez la cuisse de poulet 30 minutes à 200 °C.", "Faites mijoter les légumes en dés dans l'huile.", "Servez ensemble."], ["viande", "four"])

# ---------------------------------------------------------------- plats : poissons (17)
R("Cabillaud au four, citron et courgettes", PL, 30, [("cabillaud", 170), ("courgette", 200), ("citron", 15), ("huileolive", 6), ("pdt", 180)],
  ["Posez le cabillaud et les courgettes dans un plat avec le citron et l'huile.", "Enfournez 18 minutes à 190 °C.", "Servez avec les pommes de terre."], ["poisson", "four"])
R("Saumon, riz et brocoli", PL, 25, [("saumon", 120), ("riz", 130), ("brocoli", 200), ("citron", 10)],
  ["Cuisez le saumon à la poêle ou au four.", "Servez avec le riz et le brocoli à la vapeur et le citron."], ["poisson"])
R("Merlu sauce citron et haricots verts", PL, 25, [("merlu", 170), ("harivert", 200), ("cremelegere", 30), ("citron", 10), ("pdt", 180)],
  ["Cuisez le merlu à l'étouffée.", "Chauffez la crème avec le citron et nappez.", "Servez avec les haricots verts et les pommes de terre."], ["poisson"])
R("Moules marinières et pommes de terre", PL, 25, [("moule", 250), ("echalote", 25), ("vinblanc", 40), ("persil", 4), ("pdt", 200), ("beurre", 5)],
  ["Faites revenir l'échalote dans le beurre, ajoutez le vin et les moules.", "Couvrez 5 minutes, parsemez de persil.", "Servez avec les pommes de terre vapeur."], ["poisson"])
R("Thon, tomates et riz complet", PL, 20, [("thon", 130), ("rizcompl", 130), ("tomate", 150), ("olive", 15), ("huileolive", 6)],
  ["Mélangez le riz froid, les tomates et les olives.", "Ajoutez le thon émietté et l'huile."], ["poisson", "rapide"])
R("Truite grillée aux amandes effilées", PL, 25, [("truite", 150), ("amande", 12), ("harivert", 200), ("pdt", 180), ("beurre", 5)],
  ["Cuisez la truite au four 15 minutes.", "Faites dorer les amandes dans le beurre et versez dessus.", "Servez avec les légumes."], ["poisson", "four"])
R("Sardines grillées et salade de tomates", PL, 15, [("sardine", 130), ("tomate", 200), ("oignon", 20), ("huileolive", 6), ("pdt", 180)],
  ["Faites griller les sardines.", "Préparez la salade de tomates à l'oignon et à l'huile.", "Servez avec les pommes de terre."], ["poisson", "rapide"])
R("Lieu en papillote, carottes et courgettes", PL, 30, [("lieu", 170), ("carotte", 100), ("courgette", 100), ("citron", 10), ("huileolive", 6), ("riz", 120)],
  ["Disposez poisson et légumes sur une feuille de papier cuisson.", "Fermez et enfournez 20 minutes à 190 °C.", "Servez avec le riz."], ["poisson", "four"])
R("Crevettes sautées à l'ail et riz", PL, 20, [("crevette", 150), ("ail", 4), ("riz", 130), ("poivron", 100), ("huileolive", 6)],
  ["Faites revenir l'ail et le poivron dans l'huile.", "Ajoutez les crevettes 3 minutes.", "Servez avec le riz."], ["poisson", "rapide"])
R("Saint-Jacques et poireaux", PL, 25, [("stjacques", 150), ("poireau", 200), ("cremelegere", 40), ("pdt", 180), ("beurre", 5)],
  ["Faites fondre les poireaux dans le beurre.", "Saisissez les Saint-Jacques 2 minutes par face.", "Servez avec la crème et les pommes de terre."], ["poisson"])
R("Haddock poché et pommes de terre", PL, 25, [("haddock", 160), ("pdt", 220), ("lait", 100), ("harivert", 150)],
  ["Pochez le haddock dans le lait 8 minutes.", "Servez avec les pommes de terre vapeur et les haricots verts."], ["poisson"])
R("Maquereau, lentilles et moutarde", PL, 20, [("maquereau", 110), ("lentille", 180), ("moutarde", 8), ("echalote", 20), ("huileolive", 5)],
  ["Mélangez les lentilles chaudes avec l'échalote, la moutarde et l'huile.", "Posez le maquereau émietté."], ["poisson", "rapide"])
R("Pâtes au saumon et aux épinards", PL, 20, [("patescompl", 140), ("saumon", 100), ("epinard", 100), ("cremelegere", 30)],
  ["Faites cuire les pâtes.", "Réchauffez les épinards avec la crème et le saumon émietté.", "Mélangez."], ["poisson", "rapide"])
R("Brandade de cabillaud légère", PL, 40, [("cabillaud", 150), ("pdt", 250), ("lait", 80), ("ail", 3), ("huileolive", 5)],
  ["Cuisez le poisson et les pommes de terre.", "Écrasez-les avec le lait chaud, l'ail et l'huile.", "Gratinez 10 minutes."], ["poisson", "four"])
R("Salade de crevettes et d'avocat", PL, 15, [("crevette", 130), ("avocat", 60), ("laitue", 80), ("tomate", 100), ("citron", 10), ("pdt", 150)],
  ["Composez la salade avec laitue, tomate et avocat.", "Ajoutez les crevettes, le citron et servez avec les pommes de terre tièdes."], ["poisson", "rapide"])
R("Soupe de poisson et croûtons", PL, 35, [("lieu", 150), ("poireau", 100), ("carotte", 80), ("coulis", 80), ("pdt", 120), ("paincompl", 30)],
  ["Faites cuire les légumes dans l'eau avec le coulis 15 minutes.", "Ajoutez le poisson 8 minutes, mixez à votre goût.", "Servez avec le pain grillé."], ["poisson"])
R("Tartare de saumon et salade", PL, 15, [("saumon", 130), ("avocat", 40), ("citron", 10), ("laitue", 80), ("pdt", 180), ("huileolive", 4)],
  ["Hachez le saumon cuit refroidi avec l'avocat et le citron.", "Servez sur la salade avec les pommes de terre."], ["poisson", "rapide"])

# ---------------------------------------------------------------- plats : œufs et végétariens (12)
R("Omelette aux champignons, salade et pommes de terre", PL, 20, [("oeuf", 180), ("champignon", 120), ("pdt", 150), ("laitue", 60), ("huileolive", 6)],
  ["Poêlez les champignons, ajoutez les œufs battus.", "Servez avec la salade et les pommes de terre."], ["vegetarien", "oeufs"])
R("Curry de pois chiches et épinards", PL, 25, [("poischiche", 180), ("epinard", 100), ("curry", 3), ("oignon", 40), ("riz", 100), ("fb0", 80)],
  ["Faites revenir l'oignon avec le curry, ajoutez pois chiches et épinards.", "Servez avec le riz et le fromage blanc."], ["vegetarien"])
R("Tofu sauté aux légumes et riz", PL, 20, [("tofu", 180), ("brocoli", 150), ("carotte", 80), ("riz", 120), ("huileolive", 5)],
  ["Poêlez le tofu en dés dans l'huile.", "Ajoutez les légumes 6 minutes.", "Servez avec le riz."], ["vegetarien", "rapide"])
R("Quiche sans pâte aux poireaux et au jambon", PL, 45, [("oeuf", 120), ("poireau", 150), ("jambon", 60), ("lait", 100), ("emmental", 20), ("paincompl", 40)],
  ["Mélangez œufs, lait et emmental, ajoutez poireaux et jambon.", "Versez dans un plat et enfournez 30 minutes à 180 °C.", "Servez avec le pain."], ["four"])
R("Salade de lentilles, chèvre et noix", PL, 15, [("lentille", 180), ("chevre", 50), ("noix", 10), ("echalote", 15), ("vinaigre", 5), ("fb0", 80)],
  ["Mélangez les lentilles avec l'échalote et le vinaigre.", "Ajoutez le chèvre, les noix et le fromage blanc."], ["vegetarien", "rapide"])
R("Frittata aux courgettes et à la feta", PL, 25, [("oeuf", 180), ("courgette", 150), ("feta", 40), ("huileolive", 5), ("pdt", 120)],
  ["Poêlez les courgettes dans l'huile.", "Versez les œufs battus avec la feta, cuisez à feu doux.", "Servez avec les pommes de terre."], ["vegetarien", "oeufs"])
R("Dal de lentilles et fromage blanc", PL, 25, [("lentille", 220), ("curry", 3), ("oignon", 40), ("coulis", 60), ("fb0", 150), ("riz", 80)],
  ["Faites revenir l'oignon avec le curry, ajoutez lentilles et coulis.", "Chauffez 10 minutes, servez avec le riz et le fromage blanc."], ["vegetarien"])
R("Gratin de courgettes à la mozzarella", PL, 35, [("courgette", 250), ("mozzarella", 80), ("oeuf", 60), ("coulis", 80), ("fb0", 100)],
  ["Disposez les courgettes en rondelles dans un plat avec le coulis.", "Ajoutez la mozzarella, l'œuf et le fromage blanc battus.", "Enfournez 25 minutes à 190 °C."], ["vegetarien", "four"])
R("Œufs durs, haricots verts et pommes de terre", PL, 20, [("oeufdur", 165), ("harivert", 200), ("pdt", 200), ("fb0", 80), ("moutarde", 6)],
  ["Mélangez haricots et pommes de terre tièdes.", "Ajoutez les œufs durs coupés et la sauce moutarde-fromage blanc."], ["vegetarien", "oeufs"])
R("Haricots rouges, riz et œuf", PL, 20, [("haricotrouge", 180), ("riz", 100), ("oeuf", 60), ("poivron", 80), ("cumin", 2)],
  ["Réchauffez les haricots avec le poivron et le cumin.", "Servez avec le riz et un œuf au plat."], ["vegetarien", "oeufs"])
R("Pâtes complètes, pesto de basilic et mozzarella", PL, 20, [("patescompl", 140), ("mozzarella", 90), ("basilic", 8), ("tomatecerise", 100), ("huileolive", 6), ("fb0", 100)],
  ["Mixez le basilic avec l'huile et le fromage blanc.", "Mêlez aux pâtes chaudes avec les tomates et la mozzarella."], ["vegetarien", "rapide"])
R("Soupe de pois chiches et légumes", PL, 30, [("poischiche", 200), ("carotte", 100), ("courgette", 100), ("coulis", 80), ("fb0", 120)],
  ["Faites cuire les légumes et le coulis dans l'eau 15 minutes.", "Ajoutez les pois chiches et mixez à moitié.", "Servez avec le fromage blanc."], ["vegetarien"])

# ---------------------------------------------------------------- plats : classiques d'Europe (12)
R("Pizza maison fine au jambon et à la mozzarella", PL, 40, [("painblanc", 80), ("coulis", 60), ("jambon", 60), ("mozzarella", 60), ("champignon", 60)],
  ["Étalez le coulis sur la pâte fine.", "Garnissez de jambon, champignons et mozzarella.", "Enfournez 15 minutes à 220 °C."], ["four"])
R("Lasagnes aux légumes et à la dinde", PL, 55, [("dinde", 110), ("patescompl", 100), ("courgette", 150), ("coulis", 100), ("fb0", 100), ("emmental", 20)],
  ["Superposez pâtes, viande à la tomate et courgettes.", "Nappez du fromage blanc et de l'emmental.", "Enfournez 30 minutes à 190 °C."], ["viande", "four"])
R("Paella légère au poulet et aux crevettes", PL, 35, [("poulet", 90), ("crevette", 70), ("riz", 130), ("poivron", 80), ("petitspois", 50), ("huileolive", 6)],
  ["Poêlez le poulet et les poivrons.", "Ajoutez le riz, le bouillon des petits pois et les crevettes, laissez gonfler 12 minutes."], ["viande", "poisson"])
R("Gratin de pâtes au jambon et brocoli", PL, 40, [("pates", 130), ("jambon", 80), ("brocoli", 150), ("fb0", 100), ("emmental", 25)],
  ["Mélangez pâtes, jambon et brocoli.", "Nappez de fromage blanc et d'emmental.", "Gratinez 20 minutes à 200 °C."], ["viande", "four"])
R("Potée légère aux légumes et à la saucisse de volaille", PL, 50, [("jambon", 100), ("chou", 150), ("carotte", 80), ("pdt", 200), ("haricotblanc", 60)],
  ["Faites mijoter chou, carotte et jambon 30 minutes.", "Ajoutez haricots et pommes de terre 15 minutes."], ["viande"])
R("Pâtes aux champignons et au poulet", PL, 25, [("pates", 130), ("poulet", 110), ("champignon", 150), ("cremelegere", 30), ("persil", 3)],
  ["Poêlez poulet et champignons.", "Ajoutez la crème, mêlez aux pâtes, parsemez de persil."], ["viande"])
R("Gnocchis de pomme de terre, tomate et thon", PL, 25, [("pdt", 220), ("thon", 100), ("coulis", 120), ("farine", 40), ("parmesan", 10)],
  ["Écrasez les pommes de terre cuites avec la farine, formez des gnocchis et pochez-les.", "Servez avec le coulis, le thon et le parmesan."], ["poisson"])
R("Soupe de poireaux-pommes de terre et œuf mollet", PL, 30, [("poireau", 200), ("pdt", 200), ("oeufdur", 110), ("fb0", 100), ("paincompl", 40)],
  ["Cuisez poireaux et pommes de terre 20 minutes, mixez.", "Ajoutez le fromage blanc, garnissez d'œufs et de pain grillé."], ["vegetarien", "oeufs"])
R("Spaghettis aux moules et à la tomate", PL, 25, [("pates", 140), ("moule", 150), ("coulis", 100), ("ail", 3), ("persil", 3)],
  ["Faites revenir l'ail dans le coulis.", "Ajoutez les moules cuites et mêlez aux pâtes.", "Parsemez de persil."], ["poisson"])
R("Rôti de dinde, purée et carottes", PL, 45, [("dinde", 140), ("pdt", 220), ("carottecuite", 150), ("lait", 50), ("beurre", 5)],
  ["Rôtissez la dinde 30 minutes à 190 °C.", "Préparez la purée au lait et au beurre.", "Servez avec les carottes."], ["viande", "four"])
R("Croque-monsieur léger et salade", PL, 20, [("paincompl", 70), ("jambon", 70), ("emmental", 30), ("fb0", 60), ("laitue", 60), ("tomate", 80)],
  ["Tartinez le pain de fromage blanc, garnissez de jambon et d'emmental.", "Faites gratiner 8 minutes.", "Servez avec la salade."], ["viande", "four"])
R("Tortilla espagnole légère", PL, 30, [("oeuf", 180), ("pdt", 200), ("oignon", 40), ("huileolive", 8), ("jambondinde", 40)],
  ["Faites revenir l'oignon et les pommes de terre cuites.", "Versez les œufs battus avec le jambon, cuisez à feu doux des deux côtés."], ["oeufs"])

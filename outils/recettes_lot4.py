"""Quatrième lot de recettes (pour UNE personne)."""
from recettes_src import R, PD, PL, CO

# ---------------------------------------------------------------- petits-déjeuners (15)
R("Porridge aux pruneaux et à la cannelle", PD, 10, [("flocons", 40), ("lait", 150), ("fb0", 100), ("pruneau", 25), ("cannelle", 1)],
  ["Chauffez les flocons avec le lait 4 minutes.", "Ajoutez le fromage blanc, les pruneaux coupés et la cannelle."], ["vegetarien", "rapide"])
R("Omelette aux oignons et au fromage", PD, 12, [("oeuf", 120), ("oignon", 40), ("emmental", 20), ("huileolive", 4), ("paincompl", 30)],
  ["Faites fondre l'oignon émincé dans l'huile.", "Versez les œufs battus, ajoutez l'emmental et repliez.", "Servez avec le pain."], ["vegetarien", "oeufs", "rapide"])
R("Bol de fromage blanc à l'orange", PD, 5, [("fb0", 220), ("orange", 120), ("flocons", 20), ("amande", 10)],
  ["Versez le fromage blanc dans un bol.", "Ajoutez l'orange en morceaux, les flocons et les amandes."], ["vegetarien", "rapide"])
R("Œufs durs, avocat et pain complet", PD, 12, [("oeufdur", 110), ("avocat", 40), ("paincompl", 50), ("citron", 3)],
  ["Écrasez l'avocat avec le citron sur le pain.", "Ajoutez les œufs durs en rondelles."], ["vegetarien", "oeufs"])
R("Pancakes à la banane et au yaourt", PD, 15, [("farine", 30), ("oeuf", 60), ("banane", 60), ("yaourt", 125), ("fb0", 60)],
  ["Écrasez la banane avec l'œuf, ajoutez farine et yaourt.", "Cuisez de petits pancakes.", "Servez avec le fromage blanc."], ["vegetarien"])
R("Tartine de fromage blanc, miel et noix", PD, 6, [("paincompl", 50), ("fb0", 150), ("miel", 6), ("noix", 10)],
  ["Tartinez le pain d'une partie du fromage blanc.", "Ajoutez miel et noix, servez le reste en bol."], ["vegetarien", "rapide"])
R("Œufs brouillés au jambon de dinde", PD, 10, [("oeuf", 120), ("jambondinde", 40), ("beurre", 4), ("paincompl", 40), ("tomatecerise", 50)],
  ["Faites brouiller les œufs dans le beurre.", "Ajoutez le jambon coupé.", "Servez avec le pain et les tomates cerises."], ["oeufs", "rapide"])
R("Smoothie pomme-cannelle protéiné", PD, 5, [("lait", 150), ("pomme", 120), ("fb0", 150), ("flocons", 15), ("cannelle", 1)],
  ["Coupez la pomme en morceaux.", "Mixez tous les ingrédients jusqu'à obtenir une texture lisse."], ["vegetarien", "rapide"])
R("Galette de flocons d'avoine aux fraises", PD, 15, [("flocons", 40), ("oeuf", 60), ("fraise", 100), ("fb0", 100)],
  ["Mixez les flocons avec l'œuf, cuisez une grosse galette.", "Garnissez de fromage blanc et de fraises."], ["vegetarien"])
R("Tartine de thon, tomate et basilic", PD, 8, [("paincompl", 50), ("thon", 60), ("tomate", 80), ("basilic", 2), ("fb0", 40)],
  ["Écrasez le thon avec le fromage blanc.", "Tartinez le pain, ajoutez la tomate et le basilic."], ["poisson", "rapide"])
R("Œuf cocotte aux champignons", PD, 20, [("oeuf", 120), ("champignon", 80), ("cremelegere", 20), ("paincompl", 40)],
  ["Poêlez les champignons et répartissez-les dans des ramequins.", "Cassez les œufs dessus, ajoutez la crème.", "Enfournez 12 minutes à 180 °C, servez avec le pain."], ["vegetarien", "oeufs", "four"])
R("Bol de yaourt, banane et flocons", PD, 5, [("yaourt", 125), ("fb0", 120), ("banane", 70), ("flocons", 30)],
  ["Mélangez yaourt et fromage blanc.", "Ajoutez la banane et les flocons."], ["vegetarien", "rapide"])
R("Crêpes fines au fromage blanc et au citron", PD, 15, [("farine", 30), ("oeuf", 60), ("lait", 100), ("fb0", 150), ("citron", 8)],
  ["Mixez farine, œuf et lait, cuisez de fines crêpes.", "Garnissez de fromage blanc au citron."], ["vegetarien"])
R("Saumon fumé, œuf mollet et pain grillé", PD, 10, [("saumon", 50), ("oeufdur", 60), ("paincompl", 50), ("fb0", 60)],
  ["Posez le saumon et l'œuf sur le pain grillé.", "Ajoutez une cuillère de fromage blanc."], ["poisson", "oeufs", "rapide"])
R("Fromage blanc, poire et flocons", PD, 5, [("fb0", 220), ("poire", 100), ("flocons", 25), ("noisette", 8)],
  ["Mélangez le fromage blanc et les flocons.", "Ajoutez la poire et les noisettes."], ["vegetarien", "rapide"])

# ---------------------------------------------------------------- collations (22)
R("Pomme au four à la cannelle", CO, 25, [("pomme", 180), ("cannelle", 1), ("fb0", 120)], ["Enfournez la pomme 20 minutes à 180 °C avec la cannelle.", "Servez avec le fromage blanc."], ["vegetarien", "four"])
R("Carottes et houmous léger", CO, 8, [("carotte", 100), ("poischiche", 50), ("fb0", 80), ("citron", 5)], ["Mixez pois chiches, fromage blanc et citron.", "Servez avec les carottes."], ["vegetarien", "rapide"])
R("Œuf dur et concombre croquant", CO, 12, [("oeufdur", 110), ("concombre", 100)], ["Écalez l'œuf.", "Servez avec le concombre en rondelles."], ["oeufs"])
R("Fraises et petit-suisse", CO, 3, [("fraise", 120), ("petitsuisse", 120)], ["Coupez les fraises.", "Servez avec le petit-suisse."], ["vegetarien", "rapide"])
R("Yaourt nature et poire", CO, 3, [("yaourt", 125), ("poire", 100), ("fb0", 80)], ["Coupez la poire.", "Servez avec le yaourt et le fromage blanc."], ["vegetarien", "rapide"])
R("Tranche de jambon et tomate cerise", CO, 3, [("jambon", 60), ("tomatecerise", 100), ("fb0", 50)], ["Roulez le jambon.", "Servez avec les tomates et le fromage blanc."], ["rapide"])
R("Banane et lait chaud", CO, 5, [("banane", 90), ("lait", 200), ("fb0", 60)], ["Chauffez le lait.", "Servez avec la banane et le fromage blanc."], ["vegetarien", "rapide"])
R("Fromage blanc au miel et framboises", CO, 3, [("fb0", 170), ("framboise", 80), ("miel", 4)], ["Mélangez le fromage blanc et le miel.", "Ajoutez les framboises."], ["vegetarien", "rapide"])
R("Salade de concombre au yaourt et au persil", CO, 8, [("concombre", 120), ("yaourt", 125), ("persil", 3), ("fb0", 50)], ["Mélangez yaourt, fromage blanc et persil.", "Ajoutez le concombre en dés."], ["vegetarien", "rapide"])
R("Pois chiches et tomates cerises", CO, 5, [("poischiche", 80), ("tomatecerise", 100), ("fb0", 60), ("cumin", 1)], ["Mélangez pois chiches et tomates.", "Assaisonnez de cumin et nappez de fromage blanc."], ["vegetarien", "rapide"])
R("Oeuf mollet et haricots verts", CO, 10, [("oeufdur", 110), ("harivert", 100)], ["Cuisez l'œuf 6 minutes.", "Servez avec les haricots verts tièdes."], ["oeufs"])
R("Compote de poire et fromage blanc", CO, 5, [("poire", 150), ("fb0", 150)], ["Écrasez la poire cuite.", "Mélangez avec le fromage blanc."], ["vegetarien", "rapide"])
R("Thon, citron et crudités", CO, 6, [("thon", 60), ("citron", 8), ("carotte", 80), ("fb0", 40)], ["Mêlez le thon au citron.", "Servez avec les bâtonnets de carotte."], ["poisson", "rapide"])
R("Orange et noix", CO, 3, [("orange", 150), ("noix", 12), ("fb0", 100)], ["Pelez l'orange.", "Servez avec les noix et le fromage blanc."], ["vegetarien", "rapide"])
R("Feta et tomates cerises", CO, 4, [("feta", 30), ("tomatecerise", 120), ("fb0", 60)], ["Mêlez la feta émiettée et les tomates.", "Ajoutez le fromage blanc."], ["vegetarien", "rapide"])
R("Biscotte au fromage blanc et aux fraises", CO, 4, [("biscotte", 20), ("fb0", 100), ("fraise", 80)], ["Tartinez les biscottes de fromage blanc.", "Posez les fraises."], ["vegetarien", "rapide"])
R("Soja chaud à la cannelle", CO, 4, [("soja", 200), ("cannelle", 1), ("fb0", 120)], ["Chauffez le soja avec la cannelle.", "Servez avec le fromage blanc."], ["vegetarien", "rapide"])
R("Œuf dur et tomate", CO, 12, [("oeufdur", 110), ("tomate", 100), ("basilic", 2)], ["Écalez l'œuf.", "Servez avec la tomate et le basilic."], ["vegetarien", "oeufs"])
R("Poulet froid et concombre", CO, 4, [("poulet", 60), ("concombre", 80), ("fb0", 40)], ["Coupez le poulet.", "Servez avec le concombre et le fromage blanc."], ["viande", "rapide"])
R("Lait chaud et biscotte au miel", CO, 5, [("lait", 200), ("biscotte", 15), ("miel", 4), ("fb0", 60)], ["Servez le lait avec la biscotte au miel.", "Ajoutez le fromage blanc."], ["vegetarien", "rapide"])
R("Kéfir et poire", CO, 3, [("kefir", 200), ("poire", 100), ("fb0", 40)], ["Coupez la poire.", "Servez avec le kéfir."], ["vegetarien", "rapide"])
R("Mozzarella, jambon de dinde et basilic", CO, 4, [("mozzarella", 40), ("jambondinde", 40), ("basilic", 2), ("tomatecerise", 50)], ["Roulez la mozzarella dans le jambon.", "Servez avec basilic et tomates."], ["rapide"])

# ---------------------------------------------------------------- plats : viandes (22)
R("Poulet rôti, carottes et boulgour", PL, 40, [("poulet", 140), ("carottecuite", 150), ("boulgour", 130), ("huileolive", 5)],
  ["Rôtissez le poulet 25 minutes à 200 °C.", "Servez avec les carottes et le boulgour."], ["viande", "four"])
R("Bœuf sauté, brocoli et pâtes", PL, 20, [("rumsteck", 120), ("brocoli", 150), ("pates", 130), ("huileolive", 5)],
  ["Saisissez le bœuf en lanières.", "Ajoutez le brocoli, mêlez aux pâtes."], ["viande", "rapide"])
R("Dinde aux champignons, purée de pommes de terre", PL, 30, [("dinde", 140), ("champignon", 150), ("pdt", 220), ("lait", 40), ("cremelegere", 20)],
  ["Poêlez dinde et champignons, ajoutez la crème.", "Servez avec la purée au lait."], ["viande"])
R("Porc à la moutarde et aux poireaux", PL, 30, [("porc", 130), ("moutarde", 8), ("poireau", 200), ("riz", 110)],
  ["Poêlez le porc, nappez de moutarde.", "Servez avec les poireaux fondus et le riz."], ["viande"])
R("Poulet rôti au curry et au yaourt", PL, 30, [("poulet", 140), ("yaourt", 100), ("curry", 3), ("riz", 120), ("concombre", 80)],
  ["Marinez le poulet avec yaourt et curry.", "Rôtissez-le 20 minutes à 200 °C.", "Servez avec le riz et le concombre."], ["viande", "four"])
R("Escalope de veau, haricots verts et pommes de terre", PL, 25, [("veau", 140), ("harivert", 200), ("pdt", 200), ("beurre", 5), ("citron", 8)],
  ["Poêlez l'escalope dans le beurre avec le citron.", "Servez avec les légumes."], ["viande"])
R("Steak haché et ratatouille", PL, 35, [("hache5", 130), ("courgette", 120), ("aubergine", 80), ("tomate", 100), ("pdt", 150), ("huileolive", 5)],
  ["Mijotez les légumes dans l'huile.", "Poêlez le steak.", "Servez avec les pommes de terre."], ["viande"])
R("Poulet aux olives et au citron", PL, 35, [("poulet", 140), ("olive", 20), ("citron", 15), ("semoule", 110), ("courgette", 100)],
  ["Faites dorer le poulet, ajoutez olives et citron.", "Mijotez 15 minutes avec la courgette.", "Servez avec la semoule."], ["viande"])
R("Rôti de dinde au thym, lentilles", PL, 45, [("dinde", 140), ("lentille", 160), ("carotte", 80), ("herbes", 2)],
  ["Rôtissez la dinde aux herbes 30 minutes.", "Servez avec les lentilles et la carotte."], ["viande", "four"])
R("Porc aux champignons et pâtes complètes", PL, 30, [("porc", 120), ("champignon", 150), ("patescompl", 130), ("cremelegere", 25)],
  ["Poêlez porc et champignons.", "Ajoutez la crème, servez sur les pâtes."], ["viande"])
R("Agneau, courgettes et semoule", PL, 35, [("agneau", 110), ("courgette", 150), ("semoule", 110), ("cumin", 2), ("huileolive", 4)],
  ["Poêlez l'agneau avec le cumin.", "Ajoutez les courgettes en rondelles.", "Servez avec la semoule."], ["viande"])
R("Poulet au four, patate douce et haricots", PL, 40, [("poulet", 140), ("patatedouce", 200), ("harivert", 150), ("huileolive", 4)],
  ["Rôtissez poulet et patate douce 30 minutes à 200 °C.", "Servez avec les haricots verts."], ["viande", "four"])
R("Rumsteck, salade et pommes de terre au four", PL, 25, [("rumsteck", 130), ("laitue", 80), ("pdtfour", 200), ("vinaigre", 5), ("huileolive", 5)],
  ["Poêlez le rumsteck.", "Servez avec la salade vinaigrée et les pommes de terre."], ["viande"])
R("Wok de poulet aux légumes croquants", PL, 20, [("poulet", 130), ("poivron", 100), ("brocoli", 120), ("carotte", 60), ("riz", 120), ("huileolive", 5)],
  ["Saisissez le poulet en lanières.", "Ajoutez les légumes 6 minutes.", "Servez avec le riz."], ["viande", "rapide"])
R("Dinde à la crème de moutarde", PL, 25, [("dinde", 140), ("moutarde", 10), ("cremelegere", 30), ("pates", 120), ("epinard", 80)],
  ["Poêlez la dinde, ajoutez moutarde et crème.", "Servez sur les pâtes avec les épinards."], ["viande"])
R("Chili de dinde aux haricots", PL, 35, [("dinde", 120), ("haricotrouge", 120), ("coulis", 120), ("poivron", 60), ("riz", 90), ("cumin", 2)],
  ["Faites revenir dinde hachée, poivron et cumin.", "Ajoutez coulis et haricots, mijotez 20 minutes.", "Servez avec le riz."], ["viande"])
R("Jambon rôti, gratin de courgettes", PL, 40, [("jambon", 120), ("courgette", 250), ("fb0", 100), ("emmental", 20), ("pdt", 120)],
  ["Disposez les courgettes en gratin avec fromage blanc et emmental.", "Enfournez 25 minutes à 190 °C.", "Servez avec le jambon et les pommes de terre."], ["viande", "four"])
R("Poulet sauté à l'ail et haricots blancs", PL, 25, [("poulet", 130), ("haricotblanc", 170), ("ail", 4), ("persil", 4), ("huileolive", 5)],
  ["Faites sauter le poulet avec l'ail.", "Ajoutez les haricots, parsemez de persil."], ["viande", "rapide"])
R("Lapin aux carottes et à la moutarde", PL, 45, [("lapin", 150), ("carotte", 150), ("moutarde", 10), ("pdt", 180)],
  ["Faites dorer le lapin, ajoutez moutarde et carottes.", "Mijotez 30 minutes avec un peu d'eau.", "Servez avec les pommes de terre."], ["viande"])
R("Veau mijoté aux petits pois", PL, 40, [("veau", 130), ("petitspois", 150), ("carotte", 80), ("oignon", 30), ("riz", 100)],
  ["Faites revenir veau et oignon.", "Ajoutez carotte et petits pois, mijotez 25 minutes.", "Servez avec le riz."], ["viande"])
R("Bœuf haché, aubergines gratinées", PL, 45, [("hache5", 130), ("aubergine", 250), ("coulis", 80), ("emmental", 20), ("riz", 70)],
  ["Garnissez les aubergines de viande à la tomate.", "Parsemez d'emmental, enfournez 30 minutes.", "Servez avec le riz."], ["viande", "four"])
R("Poulet pané au four, salade de tomates", PL, 30, [("poulet", 140), ("biscotte", 20), ("oeuf", 30), ("tomate", 150), ("pdt", 180)],
  ["Passez le poulet dans l'œuf puis la chapelure de biscotte.", "Enfournez 20 minutes à 200 °C.", "Servez avec tomates et pommes de terre."], ["viande", "four"])

# ---------------------------------------------------------------- plats : poissons (17)
R("Cabillaud rôti, purée de brocoli", PL, 30, [("cabillaud", 170), ("brocoli", 200), ("pdt", 200), ("lait", 40), ("huileolive", 4)],
  ["Rôtissez le cabillaud 15 minutes.", "Écrasez brocoli et pommes de terre avec le lait."], ["poisson", "four"])
R("Saumon au citron, riz et haricots verts", PL, 25, [("saumon", 120), ("riz", 130), ("harivert", 150), ("citron", 10)],
  ["Cuisez le saumon.", "Servez avec le riz, les haricots et le citron."], ["poisson"])
R("Thon mi-cuit, salade de courgettes", PL, 20, [("thon", 130), ("courgettecrue", 150), ("citron", 10), ("huileolive", 6), ("riz", 100)],
  ["Saisissez le thon cuit 1 minute par face.", "Servez avec les courgettes crues en lamelles et le riz."], ["poisson", "rapide"])
R("Merlu à la tomate et aux olives", PL, 25, [("merlu", 170), ("coulis", 100), ("olive", 15), ("pdt", 200)],
  ["Pochez le merlu dans le coulis avec les olives.", "Servez avec les pommes de terre."], ["poisson"])
R("Moules et riz parfumé", PL, 25, [("moule", 250), ("riz", 120), ("echalote", 20), ("vinblanc", 30), ("persil", 3)],
  ["Faites ouvrir les moules avec l'échalote et le vin.", "Servez avec le riz et le persil."], ["poisson"])
R("Truite aux herbes et pommes de terre", PL, 30, [("truite", 150), ("herbes", 2), ("pdt", 200), ("harivert", 150), ("citron", 8)],
  ["Rôtissez la truite aux herbes 15 minutes.", "Servez avec les pommes de terre et les haricots."], ["poisson", "four"])
R("Crevettes à la tomate et pâtes", PL, 20, [("crevette", 130), ("coulis", 120), ("pates", 130), ("ail", 3)],
  ["Faites revenir l'ail dans le coulis.", "Ajoutez les crevettes 3 minutes, mêlez aux pâtes."], ["poisson", "rapide"])
R("Lieu aux poireaux et à la crème", PL, 30, [("lieu", 170), ("poireau", 200), ("cremelegere", 30), ("pdt", 180)],
  ["Faites fondre les poireaux.", "Posez le poisson dessus, ajoutez la crème, couvrez 10 minutes.", "Servez avec les pommes de terre."], ["poisson"])
R("Salade de saumon, lentilles et épinards", PL, 20, [("saumon", 100), ("lentille", 140), ("epinardcru", 60), ("citron", 8), ("huileolive", 5)],
  ["Mélangez lentilles et épinards.", "Ajoutez le saumon émietté, le citron et l'huile."], ["poisson", "rapide"])
R("Sardines grillées, quinoa et tomates", PL, 20, [("sardine", 130), ("quinoa", 130), ("tomate", 120), ("citron", 8)],
  ["Grillez les sardines.", "Servez avec le quinoa, la tomate et le citron."], ["poisson", "rapide"])
R("Haddock gratiné aux pommes de terre", PL, 35, [("haddock", 160), ("pdt", 200), ("fb0", 80), ("emmental", 15), ("harivert", 100)],
  ["Disposez haddock et pommes de terre en tranches.", "Nappez de fromage blanc et d'emmental.", "Gratinez 20 minutes."], ["poisson", "four"])
R("Papillote de cabillaud, tomates et courgettes", PL, 30, [("cabillaud", 170), ("tomatecerise", 100), ("courgette", 120), ("huileolive", 5), ("riz", 110)],
  ["Disposez tout sur une feuille de papier cuisson et fermez.", "Enfournez 20 minutes à 190 °C.", "Servez avec le riz."], ["poisson", "four"])
R("Maquereau, pommes de terre et moutarde", PL, 25, [("maquereau", 110), ("pdt", 220), ("moutarde", 8), ("echalote", 20), ("fb0", 50)],
  ["Mélangez les pommes de terre tièdes à la moutarde et au fromage blanc.", "Servez avec le maquereau."], ["poisson", "rapide"])
R("Saint-Jacques, purée de patate douce", PL, 25, [("stjacques", 150), ("patatedouce", 200), ("beurre", 5), ("persil", 3)],
  ["Écrasez la patate douce cuite.", "Saisissez les Saint-Jacques dans le beurre 2 minutes par face."], ["poisson"])
R("Soupe de moules et de légumes", PL, 30, [("moule", 200), ("poireau", 100), ("carotte", 80), ("pdt", 150), ("cremelegere", 25)],
  ["Cuisez les légumes en soupe, mixez grossièrement.", "Ajoutez les moules décoquillées et la crème."], ["poisson"])
R("Thon, haricots blancs et tomates", PL, 15, [("thon", 110), ("haricotblanc", 170), ("tomate", 120), ("oignon", 20), ("huileolive", 5)],
  ["Mélangez haricots, tomate et oignon.", "Ajoutez le thon et l'huile."], ["poisson", "rapide"])
R("Églefin poché, légumes vapeur", PL, 25, [("eglefin", 170), ("carotte", 100), ("courgette", 100), ("pdt", 180), ("fb0", 50), ("citron", 8)],
  ["Pochez l'églefin.", "Cuisez les légumes à la vapeur.", "Servez avec une sauce fromage blanc-citron."], ["poisson"])

# ---------------------------------------------------------------- plats : œufs et végétariens (12)
R("Omelette aux pommes de terre et aux oignons", PL, 25, [("oeuf", 200), ("pdt", 150), ("oignon", 40), ("huileolive", 6)],
  ["Faites revenir pommes de terre cuites et oignon.", "Versez les œufs battus, cuisez des deux côtés."], ["vegetarien", "oeufs"])
R("Lentilles au curry et au lait de coco", PL, 25, [("lentille", 220), ("laitcoco", 20), ("curry", 3), ("oignon", 30), ("fb0", 150), ("riz", 70)],
  ["Faites revenir l'oignon et le curry.", "Ajoutez les lentilles et le lait de coco.", "Servez avec le riz et le fromage blanc."], ["vegetarien"])
R("Tofu grillé, légumes rôtis et quinoa", PL, 30, [("tofu", 200), ("courgette", 120), ("poivron", 80), ("quinoa", 110), ("huileolive", 5)],
  ["Rôtissez les légumes 20 minutes à 200 °C.", "Poêlez le tofu.", "Servez avec le quinoa."], ["vegetarien", "four"])
R("Flan de légumes et fromage blanc", PL, 45, [("oeuf", 120), ("courgette", 150), ("fb0", 150), ("emmental", 20), ("pdt", 150)],
  ["Mélangez œufs, fromage blanc et courgettes râpées.", "Enfournez 30 minutes à 180 °C.", "Servez avec les pommes de terre."], ["vegetarien", "four"])
R("Salade de pois chiches, feta et concombre", PL, 15, [("poischiche", 150), ("feta", 50), ("concombre", 100), ("tomate", 100), ("huileolive", 5), ("fb0", 100)],
  ["Mélangez tous les ingrédients.", "Assaisonnez d'huile et de poivre."], ["vegetarien", "rapide"])
R("Œufs pochés, épinards et pommes de terre", PL, 20, [("oeuf", 180), ("epinard", 120), ("pdt", 150), ("fb0", 60)],
  ["Pochez les œufs 3 minutes.", "Servez sur les épinards et les pommes de terre avec le fromage blanc."], ["vegetarien", "oeufs"])
R("Haricots rouges et riz à la tomate", PL, 20, [("haricotrouge", 180), ("riz", 100), ("coulis", 100), ("fb0", 150), ("cumin", 2)],
  ["Réchauffez les haricots dans le coulis avec le cumin.", "Servez avec le riz et le fromage blanc."], ["vegetarien"])
R("Pâtes complètes, courgettes et mozzarella", PL, 20, [("patescompl", 140), ("courgette", 150), ("mozzarella", 90), ("fb0", 100), ("huileolive", 4)],
  ["Poêlez les courgettes.", "Mêlez aux pâtes, mozzarella et fromage blanc."], ["vegetarien", "rapide"])
R("Soupe de lentilles vertes et de carottes", PL, 30, [("lentille", 200), ("carotte", 100), ("fb0", 150), ("cumin", 2), ("paincompl", 40)],
  ["Mixez lentilles cuites et carottes avec un peu d'eau.", "Servez avec le fromage blanc et le pain."], ["vegetarien"])
R("Frittata aux petits pois et au persil", PL, 25, [("oeuf", 180), ("petitspois", 100), ("persil", 4), ("feta", 30), ("pdt", 120)],
  ["Mêlez œufs, petits pois, persil et feta.", "Cuisez à feu doux, servez avec les pommes de terre."], ["vegetarien", "oeufs"])
R("Gratin de pois chiches et d'épinards", PL, 35, [("poischiche", 180), ("epinard", 120), ("fb0", 120), ("emmental", 25)],
  ["Mêlez pois chiches et épinards dans un plat.", "Nappez de fromage blanc et d'emmental.", "Gratinez 20 minutes."], ["vegetarien", "four"])
R("Houmous, œufs durs et légumes crus", PL, 20, [("poischiche", 130), ("oeufdur", 110), ("carotte", 100), ("concombre", 80), ("fb0", 60), ("paincompl", 40)],
  ["Mixez les pois chiches avec le fromage blanc.", "Servez avec les œufs, les crudités et le pain."], ["vegetarien", "oeufs"])

# ---------------------------------------------------------------- plats : classiques d'Europe (12)
R("Pizza légère au poulet et aux poivrons", PL, 40, [("painblanc", 80), ("coulis", 60), ("poulet", 60), ("poivron", 60), ("mozzarella", 50)],
  ["Étalez le coulis sur la pâte fine.", "Garnissez de poulet, poivron et mozzarella.", "Enfournez 15 minutes à 220 °C."], ["viande", "four"])
R("Spaghettis à la tomate et aux crevettes", PL, 20, [("pates", 140), ("crevette", 110), ("coulis", 120), ("basilic", 3)],
  ["Chauffez le coulis, ajoutez les crevettes.", "Mêlez aux pâtes avec le basilic."], ["poisson", "rapide"])
R("Gratin de pommes de terre et de poulet", PL, 45, [("pdt", 220), ("poulet", 110), ("fb0", 100), ("emmental", 25), ("ail", 3)],
  ["Disposez pommes de terre en rondelles et poulet en dés dans un plat frotté d'ail.", "Nappez de fromage blanc et d'emmental.", "Enfournez 35 minutes à 190 °C."], ["viande", "four"])
R("Risotto de riz au poulet et au parmesan", PL, 30, [("riz", 120), ("poulet", 110), ("bouillon", 150), ("parmesan", 15), ("petitspois", 60)],
  ["Réchauffez le riz cuit avec le bouillon.", "Ajoutez poulet en dés et petits pois, terminez au parmesan."], ["viande"])
R("Cannellonis aux épinards et au fromage blanc", PL, 45, [("pates", 110), ("epinard", 150), ("fb0", 150), ("coulis", 80), ("emmental", 20)],
  ["Mêlez épinards et fromage blanc, garnissez les pâtes.", "Nappez de coulis et d'emmental, enfournez 25 minutes."], ["vegetarien", "four"])
R("Poule au pot allégée", PL, 60, [("poulet", 140), ("carotte", 100), ("poireau", 100), ("pdt", 180), ("celeri", 40)],
  ["Mijotez le poulet avec les légumes 45 minutes dans l'eau.", "Servez avec un peu de bouillon."], ["viande"])
R("Sauté de porc façon paella", PL, 35, [("porc", 100), ("crevette", 60), ("riz", 120), ("poivron", 80), ("petitspois", 50)],
  ["Poêlez porc et poivron.", "Ajoutez le riz cuit, les petits pois et les crevettes."], ["viande", "poisson"])
R("Tarte salée sans pâte au thon et à la tomate", PL, 40, [("oeuf", 120), ("thon", 90), ("tomate", 120), ("fb0", 100), ("paincompl", 40)],
  ["Mélangez œufs, fromage blanc, thon et tomate.", "Enfournez 30 minutes à 180 °C.", "Servez avec le pain."], ["poisson", "oeufs", "four"])
R("Salade césar allégée au poulet", PL, 20, [("poulet", 120), ("romaine", 100), ("parmesan", 15), ("paincompl", 40), ("fb0", 80), ("citron", 8)],
  ["Mélangez le fromage blanc et le citron en sauce.", "Composez la salade avec poulet, parmesan et croûtons de pain grillé."], ["viande", "rapide"])
R("Minestrone au jambon", PL, 35, [("haricotblanc", 100), ("courgette", 100), ("carotte", 80), ("pates", 60), ("jambon", 90), ("coulis", 60)],
  ["Cuisez légumes, haricots et coulis dans l'eau 20 minutes.", "Ajoutez les pâtes puis le jambon en dés."], ["viande"])
R("Hachis de patate douce et de dinde", PL, 45, [("dinde", 130), ("patatedouce", 220), ("carotte", 60), ("oignon", 30), ("emmental", 15)],
  ["Faites revenir dinde, oignon et carotte.", "Couvrez de purée de patate douce et d'emmental.", "Gratinez 15 minutes."], ["viande", "four"])
R("Brochettes de porc, riz et poivrons", PL, 30, [("porc", 130), ("poivron", 120), ("oignon", 30), ("riz", 120), ("herbes", 2)],
  ["Enfilez porc, poivron et oignon sur des piques.", "Grillez 12 minutes.", "Servez avec le riz."], ["viande"])

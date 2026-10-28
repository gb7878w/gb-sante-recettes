"""Troisième lot de recettes (pour UNE personne)."""
from recettes_src import R, PD, PL, CO

# ---------------------------------------------------------------- petits-déjeuners (15)
R("Porridge banane-cacao", PD, 10, [("flocons", 40), ("lait", 150), ("fb0", 100), ("banane", 60), ("cacao", 4)],
  ["Faites chauffer les flocons avec le lait 4 minutes.", "Ajoutez le cacao, le fromage blanc et la banane écrasée."], ["vegetarien", "rapide"])
R("Omelette aux épinards et à la feta", PD, 12, [("oeuf", 120), ("epinard", 80), ("feta", 25), ("huileolive", 4)],
  ["Faites tomber les épinards dans l'huile.", "Versez les œufs battus, ajoutez la feta émiettée et repliez."], ["vegetarien", "oeufs", "rapide"])
R("Bol de fromage blanc, pomme et cannelle", PD, 5, [("fb0", 220), ("pomme", 100), ("cannelle", 1), ("flocons", 20), ("noix", 8)],
  ["Mélangez le fromage blanc et la cannelle.", "Ajoutez la pomme en dés, les flocons et les noix."], ["vegetarien", "rapide"])
R("Tartine de saumon fumé, avocat et citron", PD, 8, [("paincompl", 50), ("saumon", 50), ("avocat", 40), ("citron", 5), ("fb0", 40)],
  ["Écrasez l'avocat avec le fromage blanc et le citron.", "Tartinez le pain, posez le saumon."], ["poisson", "rapide"])
R("Œufs au jambon sur pain grillé", PD, 12, [("oeuf", 120), ("jambon", 40), ("paincompl", 40), ("beurre", 4)],
  ["Faites cuire les œufs dans le beurre.", "Posez-les sur le pain grillé avec le jambon."], ["oeufs", "rapide"])
R("Pancakes au fromage blanc et aux framboises", PD, 15, [("farine", 30), ("oeuf", 60), ("fb0", 150), ("lait", 50), ("framboise", 70)],
  ["Mélangez farine, œuf, lait et la moitié du fromage blanc.", "Faites cuire de petits pancakes.", "Servez avec le reste de fromage blanc et les framboises."], ["vegetarien"])
R("Yaourt, flocons d'avoine et poire", PD, 5, [("yaourt", 125), ("fb0", 100), ("flocons", 35), ("poire", 100)],
  ["Mélangez yaourt, fromage blanc et flocons.", "Ajoutez la poire en dés."], ["vegetarien", "rapide"])
R("Œufs brouillés à la tomate", PD, 12, [("oeuf", 120), ("tomate", 120), ("huileolive", 4), ("paincompl", 40), ("basilic", 2)],
  ["Faites revenir la tomate en dés dans l'huile 4 minutes.", "Ajoutez les œufs et remuez doucement.", "Servez avec le pain grillé et le basilic."], ["vegetarien", "oeufs", "rapide"])
R("Smoothie orange et fromage blanc", PD, 5, [("fb0", 200), ("lait", 100), ("orange", 120), ("flocons", 15)],
  ["Pressez ou coupez l'orange.", "Mixez avec le fromage blanc, le lait et les flocons."], ["vegetarien", "rapide"])
R("Tartine de fromage frais, concombre et saumon", PD, 8, [("paincompl", 50), ("fb0", 80), ("concombre", 50), ("saumon", 40)],
  ["Tartinez le pain de fromage blanc.", "Ajoutez le concombre et le saumon."], ["poisson", "rapide"])
R("Galette à l'œuf, au jambon et à l'emmental", PD, 15, [("farine", 35), ("oeuf", 60), ("jambon", 40), ("emmental", 15), ("lait", 60)],
  ["Préparez une pâte fine avec la farine, le lait et un peu d'eau.", "Cuisez la galette, garnissez d'œuf, de jambon et d'emmental."], ["oeufs"])
R("Bol protéiné au kéfir et aux fruits rouges", PD, 5, [("kefir", 200), ("fb0", 100), ("framboise", 70), ("flocons", 25)],
  ["Versez le kéfir et le fromage blanc dans un bol.", "Ajoutez les framboises et les flocons."], ["vegetarien", "rapide"])
R("Omelette roulée au thon", PD, 12, [("oeuf", 120), ("thon", 50), ("tomate", 60), ("persil", 2)],
  ["Battez les œufs avec le persil.", "Faites cuire en omelette fine, garnissez de thon et de tomate, roulez."], ["poisson", "oeufs", "rapide"])
R("Pain complet, fromage blanc et miel", PD, 5, [("paincompl", 60), ("fb0", 200), ("miel", 8), ("noix", 8)],
  ["Tartinez le pain de la moitié du fromage blanc et d'un filet de miel.", "Servez le reste avec les noix."], ["vegetarien", "rapide"])
R("Œuf cocotte au chèvre", PD, 20, [("oeuf", 120), ("chevre", 30), ("cremelegere", 20), ("paincompl", 40), ("persil", 2)],
  ["Préchauffez le four à 180 °C.", "Cassez les œufs dans des ramequins avec le chèvre et la crème.", "Enfournez 12 minutes, servez avec le pain grillé."], ["vegetarien", "oeufs", "four"])

# ---------------------------------------------------------------- collations (22)
R("Pomme et fromage blanc", CO, 3, [("pomme", 150), ("fb0", 150), ("cannelle", 1)], ["Coupez la pomme en dés.", "Mélangez avec le fromage blanc et la cannelle."], ["vegetarien", "rapide"])
R("Bâtonnets de carotte et fromage blanc aux herbes", CO, 8, [("carotte", 120), ("fb0", 150), ("persil", 3)], ["Mélangez le fromage blanc et le persil haché.", "Servez avec les bâtonnets de carotte."], ["vegetarien", "rapide"])
R("Œuf dur et tomates cerises", CO, 12, [("oeufdur", 110), ("tomatecerise", 100)], ["Écalez l'œuf dur.", "Servez avec les tomates cerises et du poivre."], ["oeufs"])
R("Banane et yaourt", CO, 3, [("banane", 90), ("yaourt", 125), ("fb0", 80)], ["Coupez la banane en rondelles.", "Servez sur le yaourt mêlé au fromage blanc."], ["vegetarien", "rapide"])
R("Roulés de jambon et de chèvre", CO, 5, [("jambon", 50), ("chevre", 25), ("concombre", 40)], ["Étalez le chèvre sur le jambon.", "Ajoutez un bâtonnet de concombre et roulez."], ["rapide"])
R("Salade d'orange et fromage blanc", CO, 5, [("orange", 130), ("fb0", 150)], ["Pelez l'orange et coupez-la en dés.", "Servez avec le fromage blanc."], ["vegetarien", "rapide"])
R("Thon et concombre en salade", CO, 5, [("thon", 60), ("concombre", 100), ("citron", 5), ("fb0", 40)], ["Coupez le concombre en dés.", "Mêlez le thon, le citron et le fromage blanc."], ["poisson", "rapide"])
R("Lait chaud et pomme", CO, 5, [("lait", 200), ("pomme", 100), ("fb0", 100)], ["Faites chauffer le lait.", "Servez avec la pomme et le fromage blanc."], ["vegetarien", "rapide"])
R("Fraises et fromage blanc frais", CO, 3, [("fb0", 180), ("fraise", 100)], ["Versez le fromage blanc dans un bol.", "Ajoutez les fraises coupées."], ["vegetarien", "rapide"])
R("Mini-omelette froide aux herbes", CO, 10, [("oeuf", 100), ("persil", 3), ("fb0", 30)], ["Battez les œufs avec le persil et le fromage blanc.", "Cuisez en omelette, laissez refroidir et coupez en dés."], ["oeufs"])
R("Pois chiches au cumin et yaourt", CO, 5, [("poischiche", 80), ("yaourt", 125), ("cumin", 1)], ["Réchauffez les pois chiches avec le cumin.", "Servez avec le yaourt."], ["vegetarien", "rapide"])
R("Saumon fumé et concombre", CO, 4, [("saumon", 50), ("concombre", 80), ("fb0", 60)], ["Roulez le saumon avec le concombre.", "Servez avec le fromage blanc."], ["poisson", "rapide"])
R("Poire et fromage blanc au miel", CO, 3, [("poire", 130), ("fb0", 130), ("miel", 5)], ["Coupez la poire.", "Servez avec le fromage blanc et le miel."], ["vegetarien", "rapide"])
R("Biscotte, jambon de dinde et cornichons", CO, 4, [("biscotte", 15), ("jambondinde", 50), ("cornichon", 20), ("fb0", 50)], ["Tartinez la biscotte de fromage blanc.", "Ajoutez le jambon et les cornichons."], ["rapide"])
R("Petit-suisse et banane", CO, 3, [("petitsuisse", 120), ("banane", 60), ("fb0", 50)], ["Écrasez la banane sur le petit-suisse.", "Ajoutez le fromage blanc."], ["vegetarien", "rapide"])
R("Crudités et sauce yaourt-citron", CO, 8, [("carotte", 80), ("concombre", 80), ("yaourt", 125), ("citron", 5), ("fb0", 60)], ["Mélangez le yaourt et le citron.", "Servez avec les crudités en bâtonnets."], ["vegetarien", "rapide"])
R("Œuf mollet et mouillette", CO, 8, [("oeufdur", 110), ("paincompl", 20)], ["Plongez l'œuf 6 minutes dans l'eau bouillante.", "Servez avec la mouillette de pain."], ["oeufs", "rapide"])
R("Compote sans sucre et fromage blanc", CO, 5, [("pomme", 150), ("fb0", 150), ("cannelle", 1)], ["Écrasez la pomme cuite.", "Mélangez avec le fromage blanc et la cannelle."], ["vegetarien", "rapide"])
R("Mozzarella et tomate", CO, 4, [("mozzarella", 60), ("tomate", 100), ("basilic", 2), ("fb0", 40)], ["Coupez tomate et mozzarella en tranches.", "Ajoutez le basilic et le fromage blanc."], ["vegetarien", "rapide"])
R("Soja vanille et framboises", CO, 3, [("soja", 200), ("framboise", 80), ("fb0", 100)], ["Servez le soja nature avec les framboises.", "Ajoutez le fromage blanc."], ["vegetarien", "rapide"])
R("Sardines sur biscotte", CO, 4, [("sardinehuile", 40), ("biscotte", 15), ("citron", 5), ("fb0", 40)], ["Écrasez les sardines avec le citron.", "Tartinez sur les biscottes avec le fromage blanc."], ["poisson", "rapide"])
R("Œuf dur, concombre et yaourt", CO, 12, [("oeufdur", 110), ("concombre", 60), ("yaourt", 100)], ["Écalez l'œuf.", "Servez avec le concombre et le yaourt."], ["oeufs"])

# ---------------------------------------------------------------- plats : viandes (22)
R("Poulet rôti, ratatouille et semoule", PL, 45, [("poulet", 140), ("aubergine", 80), ("courgette", 100), ("tomate", 100), ("semoule", 100), ("huileolive", 5)],
  ["Rôtissez le poulet 25 minutes à 200 °C.", "Faites mijoter les légumes dans l'huile.", "Servez avec la semoule."], ["viande", "four"])
R("Bœuf mijoté aux carottes et au vin blanc", PL, 60, [("rumsteck", 130), ("carotte", 200), ("oignon", 40), ("pdt", 150), ("vinblanc", 30)],
  ["Faites dorer la viande avec l'oignon.", "Ajoutez carottes, vin et un peu d'eau, mijotez 40 minutes.", "Servez avec les pommes de terre."], ["viande"])
R("Dinde à la moutarde et aux haricots verts", PL, 25, [("dinde", 140), ("moutarde", 10), ("cremelegere", 30), ("harivert", 200), ("riz", 100)],
  ["Poêlez la dinde, ajoutez la moutarde et la crème.", "Servez avec les haricots verts et le riz."], ["viande"])
R("Porc au lait et aux champignons", PL, 40, [("porc", 130), ("lait", 100), ("champignon", 120), ("pdt", 200)],
  ["Faites dorer le porc, ajoutez le lait et les champignons.", "Mijotez 20 minutes, servez avec les pommes de terre."], ["viande"])
R("Cuisse de poulet au citron et pommes de terre", PL, 50, [("cuissepoulet", 150), ("pdt", 200), ("citron", 20), ("herbes", 2), ("harivert", 100)],
  ["Disposez le poulet, les pommes de terre et le citron dans un plat.", "Enfournez 35 minutes à 200 °C.", "Servez avec les haricots verts."], ["viande", "four"])
R("Veau aux champignons et pâtes", PL, 30, [("veau", 130), ("champignon", 150), ("cremelegere", 30), ("pates", 130)],
  ["Poêlez le veau puis les champignons.", "Ajoutez la crème et servez avec les pâtes."], ["viande"])
R("Steak haché aux oignons et pommes de terre", PL, 30, [("hache5", 130), ("oignon", 80), ("pdtfour", 200), ("harivert", 100), ("huileolive", 4)],
  ["Faites fondre l'oignon dans l'huile.", "Poêlez le steak.", "Servez avec les pommes de terre au four et les haricots."], ["viande"])
R("Poulet au curry et lentilles", PL, 30, [("poulet", 130), ("lentille", 150), ("curry", 3), ("oignon", 30), ("fb0", 80)],
  ["Poêlez le poulet en dés avec l'oignon et le curry.", "Ajoutez les lentilles, servez avec le fromage blanc."], ["viande"])
R("Dinde aux poireaux", PL, 30, [("dinde", 140), ("poireau", 200), ("cremelegere", 30), ("riz", 120)],
  ["Faites fondre les poireaux.", "Ajoutez la dinde en dés et la crème, cuisez 10 minutes.", "Servez avec le riz."], ["viande"])
R("Agneau et haricots blancs", PL, 35, [("agneau", 110), ("haricotblanc", 180), ("coulis", 100), ("ail", 3), ("herbes", 2)],
  ["Faites revenir l'agneau avec l'ail.", "Ajoutez haricots, coulis et herbes, mijotez 15 minutes."], ["viande"])
R("Boulettes de dinde, sauce tomate et riz", PL, 30, [("dinde", 130), ("coulis", 150), ("riz", 120), ("oignon", 30), ("herbes", 2)],
  ["Formez des boulettes avec la dinde hachée et l'oignon.", "Faites-les dorer et mijoter dans le coulis.", "Servez avec le riz."], ["viande"])
R("Poulet grillé, salade de pommes de terre", PL, 30, [("poulet", 140), ("pdt", 200), ("echalote", 20), ("vinaigre", 5), ("moutarde", 6), ("huileolive", 6)],
  ["Grillez le poulet.", "Mélangez les pommes de terre tièdes avec l'échalote et la vinaigrette."], ["viande"])
R("Rôti de porc, lentilles et carottes", PL, 50, [("porc", 130), ("lentille", 150), ("carotte", 100), ("huileolive", 4)],
  ["Rôtissez le porc 30 minutes à 190 °C.", "Servez avec les lentilles et les carottes."], ["viande", "four"])
R("Escalope de poulet à la tomate et pâtes complètes", PL, 25, [("poulet", 130), ("coulis", 120), ("patescompl", 130), ("basilic", 3)],
  ["Poêlez le poulet, ajoutez le coulis.", "Servez sur les pâtes avec le basilic."], ["viande"])
R("Sauté de bœuf aux poivrons", PL, 25, [("rumsteck", 120), ("poivron", 150), ("oignon", 30), ("riz", 120), ("huileolive", 5)],
  ["Saisissez le bœuf en lanières.", "Ajoutez poivrons et oignon, cuisez 8 minutes.", "Servez avec le riz."], ["viande", "rapide"])
R("Salade de poulet, quinoa et avocat", PL, 20, [("poulet", 120), ("quinoa", 130), ("avocat", 50), ("tomate", 100), ("citron", 10)],
  ["Mélangez le quinoa avec la tomate et l'avocat.", "Ajoutez le poulet en lamelles et le citron."], ["viande", "rapide"])
R("Jambon, haricots blancs et tomate", PL, 20, [("jambon", 100), ("haricotblanc", 180), ("coulis", 100), ("oignon", 30)],
  ["Faites revenir l'oignon, ajoutez coulis et haricots.", "Terminez avec le jambon en dés."], ["viande", "rapide"])
R("Lapin aux herbes et pommes de terre", PL, 45, [("lapin", 150), ("herbes", 2), ("pdt", 200), ("harivert", 100), ("huileolive", 5)],
  ["Badigeonnez le lapin d'huile et d'herbes.", "Rôtissez-le 30 minutes à 190 °C avec les pommes de terre.", "Servez avec les haricots verts."], ["viande", "four"])
R("Poulet et riz à la tomate", PL, 30, [("poulet", 140), ("riz", 120), ("coulis", 100), ("poivron", 60), ("oignon", 30)],
  ["Faites revenir poulet, oignon et poivron.", "Ajoutez le coulis et le riz cuit, chauffez 5 minutes."], ["viande"])
R("Dinde, brocoli et pommes de terre vapeur", PL, 25, [("dinde", 140), ("brocoli", 200), ("pdt", 200), ("huileolive", 5)],
  ["Poêlez la dinde dans l'huile.", "Servez avec le brocoli et les pommes de terre vapeur."], ["viande"])
R("Bœuf haché, courgettes farcies", PL, 45, [("hache5", 130), ("courgette", 250), ("coulis", 80), ("riz", 60), ("emmental", 15)],
  ["Évidez les courgettes et remplissez-les de viande, de riz et de coulis.", "Parsemez d'emmental, enfournez 30 minutes à 190 °C."], ["viande", "four"])
R("Poulet à la crème de poireaux", PL, 30, [("poulet", 140), ("poireau", 150), ("cremelegere", 40), ("pates", 120)],
  ["Poêlez le poulet puis les poireaux.", "Ajoutez la crème, servez avec les pâtes."], ["viande"])

# ---------------------------------------------------------------- plats : poissons (17)
R("Cabillaud sauce tomate-basilic et riz", PL, 25, [("cabillaud", 170), ("coulis", 100), ("basilic", 3), ("riz", 120), ("huileolive", 4)],
  ["Pochez le cabillaud dans le coulis 10 minutes.", "Servez avec le basilic et le riz."], ["poisson"])
R("Saumon sauce citron et pommes de terre vapeur", PL, 25, [("saumon", 120), ("fb0", 60), ("citron", 10), ("pdt", 200), ("harivert", 150)],
  ["Cuisez le saumon à la vapeur ou au four.", "Mélangez le fromage blanc et le citron en sauce.", "Servez avec les légumes."], ["poisson"])
R("Thon grillé, ratatouille", PL, 30, [("thon", 130), ("courgette", 120), ("aubergine", 80), ("tomate", 100), ("huileolive", 6), ("pdt", 120)],
  ["Faites mijoter les légumes dans l'huile.", "Grillez le thon cuit 2 minutes par face.", "Servez ensemble."], ["poisson"])
R("Dos de merlu au beurre blanc léger", PL, 25, [("merlu", 170), ("echalote", 20), ("vinblanc", 30), ("beurre", 8), ("pdt", 200)],
  ["Pochez le merlu.", "Réduisez l'échalote et le vin, montez au beurre.", "Servez avec les pommes de terre."], ["poisson"])
R("Sardines, tomates et pommes de terre", PL, 25, [("sardine", 130), ("tomate", 150), ("pdt", 200), ("persil", 3), ("huileolive", 5)],
  ["Grillez les sardines.", "Servez avec tomates, pommes de terre et persil."], ["poisson"])
R("Poisson blanc au four, fenouil et citron", PL, 30, [("lieu", 170), ("fenouil", 150), ("citron", 15), ("huileolive", 6), ("riz", 120)],
  ["Disposez le poisson et le fenouil émincé dans un plat.", "Arrosez de citron et d'huile, enfournez 20 minutes à 190 °C.", "Servez avec le riz."], ["poisson", "four"])
R("Crevettes, pois chiches et épinards", PL, 20, [("crevette", 130), ("poischiche", 120), ("epinard", 100), ("ail", 3), ("huileolive", 6)],
  ["Faites revenir l'ail et les épinards dans l'huile.", "Ajoutez les pois chiches et les crevettes 3 minutes."], ["poisson", "rapide"])
R("Truite, riz et brocoli", PL, 25, [("truite", 140), ("riz", 120), ("brocoli", 200), ("citron", 10)],
  ["Cuisez la truite au four 15 minutes.", "Servez avec le riz, le brocoli et le citron."], ["poisson", "four"])
R("Moules à la crème et frites au four", PL, 35, [("moule", 250), ("cremelegere", 40), ("echalote", 20), ("pdtfour", 200), ("persil", 3)],
  ["Faites ouvrir les moules avec l'échalote.", "Ajoutez la crème et le persil.", "Servez avec les pommes de terre au four."], ["poisson"])
R("Salade de thon, haricots verts et œuf", PL, 20, [("thon", 110), ("harivert", 150), ("oeufdur", 55), ("pdt", 150), ("tomate", 100), ("huileolive", 6)],
  ["Composez la salade avec haricots, pommes de terre et tomate.", "Ajoutez le thon, l'œuf dur et l'huile."], ["poisson", "rapide"])
R("Églefin gratiné aux épinards", PL, 35, [("eglefin", 170), ("epinard", 150), ("fb0", 80), ("emmental", 15), ("pdt", 150)],
  ["Posez poisson et épinards dans un plat.", "Nappez de fromage blanc et d'emmental.", "Gratinez 20 minutes."], ["poisson", "four"])
R("Saumon, quinoa et courgettes", PL, 25, [("saumon", 110), ("quinoa", 130), ("courgette", 150), ("huileolive", 4), ("citron", 10)],
  ["Poêlez les courgettes.", "Cuisez le saumon.", "Servez avec le quinoa et le citron."], ["poisson"])
R("Maquereau grillé et lentilles", PL, 25, [("maquereau", 110), ("lentille", 170), ("echalote", 20), ("vinaigre", 5), ("huileolive", 4)],
  ["Grillez le maquereau.", "Mélangez les lentilles à l'échalote et au vinaigre."], ["poisson"])
R("Cabillaud en croûte d'herbes", PL, 30, [("cabillaud", 170), ("biscotte", 15), ("persil", 5), ("citron", 10), ("pdt", 200), ("harivert", 100)],
  ["Mélangez biscotte écrasée et herbes, déposez sur le poisson.", "Enfournez 15 minutes à 200 °C.", "Servez avec les légumes."], ["poisson", "four"])
R("Wok de crevettes et légumes", PL, 20, [("crevette", 130), ("brocoli", 150), ("carotte", 80), ("riz", 120), ("huileolive", 5)],
  ["Saisissez les crevettes 2 minutes.", "Ajoutez les légumes 6 minutes.", "Servez avec le riz."], ["poisson", "rapide"])
R("Lieu, pommes de terre et poireaux", PL, 30, [("lieu", 170), ("poireau", 150), ("pdt", 200), ("cremelegere", 30)],
  ["Cuisez poireaux et pommes de terre.", "Pochez le poisson, nappez de crème."], ["poisson"])
R("Haddock et haricots verts", PL, 20, [("haddock", 160), ("harivert", 200), ("pdt", 200), ("fb0", 60)],
  ["Pochez le haddock 8 minutes.", "Servez avec haricots, pommes de terre et fromage blanc."], ["poisson", "rapide"])

# ---------------------------------------------------------------- plats : œufs et végétariens (12)
R("Omelette aux tomates et au basilic", PL, 15, [("oeuf", 200), ("tomate", 150), ("basilic", 3), ("pdt", 150), ("huileolive", 5)],
  ["Faites revenir les tomates dans l'huile.", "Versez les œufs, ajoutez le basilic.", "Servez avec les pommes de terre."], ["vegetarien", "oeufs"])
R("Lentilles, œuf et épinards", PL, 20, [("lentille", 180), ("oeuf", 120), ("epinard", 100), ("fb0", 80)],
  ["Réchauffez les lentilles avec les épinards.", "Servez avec les œufs au plat et le fromage blanc."], ["vegetarien", "oeufs"])
R("Poêlée de tofu, légumes et riz", PL, 20, [("tofu", 200), ("courgette", 120), ("poivron", 80), ("riz", 120), ("huileolive", 5)],
  ["Poêlez le tofu en cubes.", "Ajoutez les légumes en dés 8 minutes.", "Servez avec le riz."], ["vegetarien", "rapide"])
R("Gratin de chou-fleur au fromage blanc", PL, 40, [("chouxfleur", 250), ("fb0", 150), ("emmental", 30), ("oeuf", 60), ("pdt", 120)],
  ["Cuisez le chou-fleur 10 minutes.", "Mélangez fromage blanc, œuf et emmental, nappez.", "Gratinez 20 minutes."], ["vegetarien", "four"])
R("Houmous maison, crudités et œufs durs", PL, 20, [("poischiche", 120), ("fb0", 60), ("citron", 10), ("oeufdur", 110), ("carotte", 100), ("paincompl", 40)],
  ["Mixez pois chiches, fromage blanc et citron.", "Servez avec les œufs durs, les crudités et le pain."], ["vegetarien", "oeufs"])
R("Salade de haricots rouges et de mozzarella", PL, 15, [("haricotrouge", 150), ("mozzarella", 70), ("tomate", 100), ("mais", 40), ("huileolive", 6), ("fb0", 60)],
  ["Mélangez tous les ingrédients.", "Assaisonnez d'huile et de poivre."], ["vegetarien", "rapide"])
R("Poêlée de champignons et d'œufs", PL, 18, [("champignon", 200), ("oeuf", 180), ("ail", 3), ("persil", 3), ("pdt", 150), ("huileolive", 5)],
  ["Poêlez champignons et ail.", "Ajoutez les œufs battus et le persil.", "Servez avec les pommes de terre."], ["vegetarien", "oeufs"])
R("Pâtes complètes aux légumes grillés et au chèvre", PL, 25, [("patescompl", 140), ("courgette", 100), ("aubergine", 80), ("chevre", 60), ("fb0", 120), ("huileolive", 4)],
  ["Grillez les légumes.", "Mêlez-les aux pâtes avec le chèvre et le fromage blanc."], ["vegetarien"])
R("Curry de légumes et de pois chiches", PL, 30, [("poischiche", 150), ("courgette", 120), ("carotte", 80), ("curry", 3), ("fb0", 200), ("riz", 80)],
  ["Faites mijoter les légumes avec le curry.", "Ajoutez les pois chiches, servez avec le riz et le fromage blanc."], ["vegetarien"])
R("Tortilla de légumes", PL, 30, [("oeuf", 200), ("pdt", 150), ("courgette", 100), ("oignon", 30), ("huileolive", 6)],
  ["Faites revenir les légumes en dés.", "Versez les œufs battus et cuisez à feu doux des deux côtés."], ["vegetarien", "oeufs"])
R("Soupe de légumes, œuf et fromage", PL, 25, [("carotte", 100), ("poireau", 100), ("pdt", 150), ("oeufdur", 110), ("emmental", 25), ("paincompl", 40)],
  ["Cuisez les légumes dans l'eau 20 minutes et mixez.", "Servez avec l'œuf dur, l'emmental et le pain."], ["vegetarien", "oeufs"])
R("Dal de pois chiches à la tomate", PL, 25, [("poischiche", 200), ("coulis", 100), ("curry", 3), ("oignon", 30), ("fb0", 120), ("riz", 60)],
  ["Faites revenir l'oignon avec le curry.", "Ajoutez coulis et pois chiches, mijotez 10 minutes.", "Servez avec le riz et le fromage blanc."], ["vegetarien"])

# ---------------------------------------------------------------- plats : classiques d'Europe (12)
R("Pizza fine aux légumes et à la mozzarella", PL, 40, [("painblanc", 80), ("coulis", 60), ("mozzarella", 60), ("poivron", 60), ("champignon", 60), ("thon", 50)],
  ["Étalez le coulis sur la pâte fine.", "Garnissez de légumes, de thon et de mozzarella.", "Enfournez 15 minutes à 220 °C."], ["poisson", "four"])
R("Spaghettis aux boulettes", PL, 35, [("pates", 140), ("hache5", 110), ("coulis", 120), ("parmesan", 10), ("oignon", 30)],
  ["Formez de petites boulettes avec la viande et l'oignon.", "Faites-les mijoter dans le coulis.", "Servez sur les pâtes avec le parmesan."], ["viande"])
R("Gratin d'endives et de jambon", PL, 45, [("endive", 300), ("jambon", 120), ("lait", 100), ("emmental", 25), ("farine", 8), ("pdt", 150)],
  ["Faites braiser les endives, enroulez-les dans le jambon.", "Nappez d'une béchamel légère.", "Gratinez et servez avec les pommes de terre."], ["viande", "four"])
R("Risotto de riz aux courgettes et aux crevettes", PL, 30, [("riz", 120), ("crevette", 110), ("courgette", 150), ("parmesan", 12), ("bouillon", 150), ("huileolive", 5)],
  ["Faites revenir les courgettes dans l'huile.", "Ajoutez le riz cuit et le bouillon, réduisez.", "Ajoutez les crevettes et le parmesan."], ["poisson"])
R("Lasagnes de courgettes à la bolognaise", PL, 50, [("courgette", 250), ("hache5", 110), ("coulis", 100), ("fb0", 100), ("emmental", 20)],
  ["Tranchez les courgettes en lamelles.", "Superposez avec la viande à la tomate.", "Nappez de fromage blanc et d'emmental, enfournez 30 minutes."], ["viande", "four"])
R("Cassoulet de dinde et haricots blancs", PL, 45, [("dinde", 120), ("haricotblanc", 200), ("lardons", 20), ("coulis", 100), ("carotte", 60)],
  ["Faites revenir lardons et dinde en dés.", "Ajoutez coulis, carotte et haricots, mijotez 25 minutes."], ["viande"])
R("Soupe au pistou et jambon", PL, 35, [("haricotblanc", 120), ("courgette", 100), ("carotte", 80), ("basilic", 6), ("jambon", 100), ("pates", 60)],
  ["Cuisez les légumes et les haricots dans l'eau.", "Ajoutez les pâtes, puis le basilic haché et le jambon."], ["viande"])
R("Blanc de poulet à l'italienne", PL, 30, [("poulet", 130), ("tomate", 150), ("mozzarella", 40), ("basilic", 3), ("patescompl", 110)],
  ["Poêlez le poulet, posez tomate et mozzarella.", "Couvrez 5 minutes pour faire fondre.", "Servez avec les pâtes."], ["viande"])
R("Gratin de macaronis au jambon", PL, 40, [("pates", 130), ("jambon", 90), ("fb0", 120), ("emmental", 25), ("epinard", 80)],
  ["Mélangez pâtes, jambon et épinards.", "Nappez de fromage blanc et d'emmental, gratinez 20 minutes."], ["viande", "four"])
R("Poulet façon cacciatore", PL, 40, [("poulet", 140), ("tomate", 150), ("olive", 15), ("poivron", 80), ("pdt", 200), ("huileolive", 4)],
  ["Faites revenir le poulet.", "Ajoutez tomate, poivron et olives, mijotez 25 minutes.", "Servez avec les pommes de terre."], ["viande"])
R("Salade périgourdine légère", PL, 20, [("poulet", 110), ("laitue", 80), ("tomate", 100), ("noix", 10), ("pdt", 150), ("vinaigre", 5), ("huileolive", 5)],
  ["Composez la salade avec laitue, tomate et pommes de terre tièdes.", "Ajoutez le poulet émincé et les noix."], ["viande", "rapide"])
R("Boeuf bourguignon allégé", PL, 70, [("rumsteck", 130), ("carotte", 120), ("champignon", 100), ("oignon", 40), ("vinblanc", 40), ("pdt", 180)],
  ["Faites dorer la viande avec l'oignon.", "Ajoutez vin, carottes et champignons, mijotez 50 minutes.", "Servez avec les pommes de terre."], ["viande"])

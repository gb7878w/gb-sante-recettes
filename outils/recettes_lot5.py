"""Cinquième lot : spécialités européennes pauvres en glucides et riches en protéines (France, Italie, Espagne, Portugal, Grèce, Allemagne)."""
from recettes_src import R, PD, PL, CO

LC = "lowcarb"

# ---------------------------------------------------------------- petits-déjeuners (15)
R("Omelette aux cèpes et au comté (France)", PD, 12, [("oeuf", 130), ("cepe", 80), ("comte", 20), ("beurre", 5)],
  ["Poêlez les cèpes dans le beurre.", "Versez les œufs battus, ajoutez le comté et repliez."], [LC, "France", "oeufs", "rapide"])
R("Œufs cocotte à la crème et au jambon (France)", PD, 20, [("oeuf", 120), ("jambon", 40), ("cremelegere", 25), ("ciboulette", 3)],
  ["Préchauffez le four à 180 °C.", "Répartissez jambon et crème dans des ramequins, cassez les œufs dessus.", "Enfournez 12 minutes, parsemez de ciboulette."], [LC, "France", "oeufs", "four"])
R("Fromage blanc, saumon fumé et ciboulette (France)", PD, 5, [("fb0", 200), ("saumonfume", 60), ("ciboulette", 3), ("citron", 5)],
  ["Mélangez le fromage blanc, le citron et la ciboulette.", "Servez avec le saumon fumé."], [LC, "France", "poisson", "rapide"])
R("Frittata aux courgettes et au parmesan (Italie)", PD, 15, [("oeuf", 130), ("courgette", 100), ("parmesan", 15), ("huileolive", 4)],
  ["Poêlez les courgettes en rondelles dans l'huile.", "Ajoutez les œufs battus et le parmesan, cuisez à feu doux."], [LC, "Italie", "oeufs", "rapide"])
R("Œufs au plat, jambon de Parme et salade (Italie)", PD, 10, [("oeuf", 120), ("parme", 40), ("laitue", 40), ("huileolive", 4)],
  ["Faites cuire les œufs au plat.", "Servez avec le jambon de Parme et la salade."], [LC, "Italie", "oeufs", "rapide"])
R("Ricotta, tomates et basilic (Italie)", PD, 5, [("ricotta", 120), ("tomatecerise", 100), ("basilic", 3), ("oeufdur", 55)],
  ["Disposez la ricotta dans une assiette.", "Ajoutez tomates, basilic et œuf dur coupé."], [LC, "Italie", "oeufs", "rapide"])
R("Tortilla fine aux poivrons et au jambon sec (Espagne)", PD, 15, [("oeuf", 130), ("poivron", 60), ("jambonsec", 30), ("huileolive", 5)],
  ["Poêlez les poivrons dans l'huile.", "Ajoutez les œufs battus et le jambon sec, cuisez des deux côtés."], [LC, "Espagne", "oeufs", "rapide"])
R("Œufs brouillés au chorizo (Espagne)", PD, 10, [("oeuf", 120), ("chorizo", 25), ("tomate", 80)],
  ["Faites revenir le chorizo en rondelles.", "Ajoutez la tomate et les œufs, brouillez doucement."], [LC, "Espagne", "oeufs", "rapide"])
R("Œufs aux asperges (Espagne)", PD, 12, [("oeuf", 130), ("asperge", 100), ("jambonsec", 25), ("huileolive", 4)],
  ["Poêlez les asperges avec le jambon sec.", "Ajoutez les œufs battus et remuez."], [LC, "Espagne", "oeufs", "rapide"])
R("Œufs mollets et sardines (Portugal)", PD, 12, [("oeufdur", 110), ("sardinehuile", 50), ("tomate", 80), ("persil", 3)],
  ["Coupez les œufs en deux.", "Servez avec les sardines égouttées, la tomate et le persil."], [LC, "Portugal", "poisson", "oeufs", "rapide"])
R("Omelette portugaise au chorizo et aux olives (Portugal)", PD, 12, [("oeuf", 130), ("chorizo", 20), ("olive", 15), ("persil", 3)],
  ["Faites revenir le chorizo.", "Ajoutez olives, persil et œufs battus, repliez."], [LC, "Portugal", "oeufs", "rapide"])
R("Yaourt grec, concombre et feta (Grèce)", PD, 5, [("fb0", 150), ("yaourt", 100), ("concombre", 60), ("feta", 30), ("menthe", 2)],
  ["Mélangez fromage blanc et yaourt.", "Ajoutez concombre en dés, feta et menthe."], [LC, "Grèce", "vegetarien", "rapide"])
R("Omelette grecque aux tomates et à la feta (Grèce)", PD, 12, [("oeuf", 130), ("tomate", 100), ("feta", 30), ("origan", 1), ("huileolive", 4)],
  ["Faites revenir les tomates dans l'huile.", "Ajoutez les œufs battus, la feta et l'origan."], [LC, "Grèce", "vegetarien", "oeufs", "rapide"])
R("Œufs durs et saucisse de Francfort (Allemagne)", PD, 12, [("oeufdur", 110), ("francfort", 60), ("moutarde", 8), ("cornichon", 30)],
  ["Réchauffez la saucisse.", "Servez avec les œufs durs, la moutarde et les cornichons."], [LC, "Allemagne", "oeufs", "rapide"])
R("Quark aux herbes et jambon cuit (Allemagne)", PD, 6, [("fb0", 200), ("jambon", 60), ("oeufdur", 55), ("noix", 10), ("ciboulette", 3), ("radis", 40)],
  ["Mélangez le fromage blanc et la ciboulette.", "Servez avec le jambon et les radis."], [LC, "Allemagne", "rapide"])

# ---------------------------------------------------------------- collations (22)
R("Rillettes de saumon au fromage blanc (France)", CO, 8, [("saumon", 50), ("fb0", 60), ("citron", 5), ("ciboulette", 2), ("concombre", 50)],
  ["Émiettez le saumon cuit avec le fromage blanc, le citron et la ciboulette.", "Servez avec des rondelles de concombre."], [LC, "France", "poisson", "rapide"])
R("Camembert rôti et radis (France)", CO, 12, [("camembert", 40), ("radis", 60), ("fb0", 60)],
  ["Réchauffez le camembert au four 8 minutes à 180 °C.", "Servez avec les radis et le fromage blanc."], [LC, "France", "four"])
R("Œuf mimosa au thon (France)", CO, 12, [("oeufdur", 110), ("thon", 30), ("fb0", 30)],
  ["Écrasez les jaunes avec le thon et le fromage blanc.", "Garnissez les blancs."], [LC, "France", "poisson", "oeufs"])
R("Jambon de Parme et mozzarella (Italie)", CO, 4, [("parme", 30), ("mozzarella", 50), ("basilic", 2)],
  ["Enroulez la mozzarella dans le jambon.", "Ajoutez le basilic."], [LC, "Italie", "rapide"])
R("Ricotta au citron et aux herbes (Italie)", CO, 5, [("ricotta", 100), ("citron", 5), ("basilic", 3), ("tomatecerise", 60)],
  ["Mélangez la ricotta avec le citron et le basilic.", "Servez avec les tomates."], [LC, "Italie", "vegetarien", "rapide"])
R("Antipasti de légumes grillés et mozzarella (Italie)", CO, 15, [("courgette", 80), ("aubergine", 60), ("mozzarella", 40), ("huileolive", 3)],
  ["Grillez les légumes en tranches avec l'huile.", "Ajoutez la mozzarella."], [LC, "Italie", "vegetarien"])
R("Anchois et œuf dur à la catalane (Espagne)", CO, 12, [("oeufdur", 110), ("anchois", 25), ("tomatecerise", 60)],
  ["Disposez œuf, anchois et tomates dans une assiette."], [LC, "Espagne", "poisson", "oeufs"])
R("Jambon sec et fromage de brebis (Espagne)", CO, 4, [("jambonsec", 30), ("brebis", 30), ("tomatecerise", 60)],
  ["Disposez jambon, fromage de brebis et tomates cerises."], [LC, "Espagne", "rapide"])
R("Tapas de poivrons grillés et d'anchois (Espagne)", CO, 8, [("poivronrouge", 80), ("anchois", 20), ("oliveverte", 10), ("fb0", 50)],
  ["Disposez les poivrons grillés avec les anchois et les olives.", "Servez avec le fromage blanc."], [LC, "Espagne", "poisson", "rapide"])
R("Sardines à l'huile, citron et persil (Portugal)", CO, 4, [("sardinehuile", 60), ("citron", 8), ("persil", 3), ("tomate", 60)],
  ["Servez les sardines égouttées avec le citron, le persil et la tomate."], [LC, "Portugal", "poisson", "rapide"])
R("Salade de morue, œuf dur et persil (Portugal)", CO, 15, [("morue", 70), ("oeufdur", 55), ("persil", 4), ("huileolive", 3)],
  ["Émiettez la morue dessalée cuite.", "Mélangez avec l'œuf dur, le persil et l'huile."], [LC, "Portugal", "poisson", "oeufs"])
R("Fromage de chèvre et olives (Portugal)", CO, 4, [("chevre", 40), ("oliveverte", 15), ("tomatecerise", 60)],
  ["Disposez chèvre, olives et tomates."], [LC, "Portugal", "vegetarien", "rapide"])
R("Tzatziki et bâtonnets de concombre (Grèce)", CO, 6, [("tzatziki", 100), ("concombre", 100), ("feta", 20)],
  ["Servez le tzatziki avec les bâtonnets de concombre et la feta émiettée."], [LC, "Grèce", "vegetarien", "rapide"])
R("Feta, tomates et origan (Grèce)", CO, 4, [("feta", 50), ("tomatecerise", 100), ("origan", 1), ("fb0", 50)],
  ["Disposez feta et tomates, parsemez d'origan.", "Ajoutez le fromage blanc."], [LC, "Grèce", "vegetarien", "rapide"])
R("Œuf dur et olives vertes (Grèce)", CO, 12, [("oeufdur", 110), ("oliveverte", 20), ("concombre", 60)],
  ["Servez l'œuf dur avec les olives et le concombre."], [LC, "Grèce", "vegetarien", "oeufs"])
R("Radis, fromage blanc et jambon (Allemagne)", CO, 5, [("radis", 80), ("jambon", 40), ("fb0", 80), ("ciboulette", 2)],
  ["Mélangez le fromage blanc et la ciboulette.", "Servez avec les radis et le jambon."], [LC, "Allemagne", "rapide"])
R("Quark et saumon fumé (Allemagne)", CO, 4, [("fb0", 100), ("saumonfume", 40), ("aneth", 2)],
  ["Mélangez le fromage blanc et l'aneth.", "Servez avec le saumon fumé."], [LC, "Allemagne", "poisson", "rapide"])
R("Saucisse de Francfort et moutarde (Allemagne)", CO, 5, [("francfort", 50), ("moutarde", 8), ("cornichon", 30)],
  ["Réchauffez la saucisse.", "Servez avec la moutarde et les cornichons."], [LC, "Allemagne", "rapide"])
R("Œuf dur, anchois et câpres (France)", CO, 10, [("oeufdur", 110), ("anchois", 15), ("capres", 5)],
  ["Coupez l'œuf en deux.", "Garnissez d'anchois et de câpres."], [LC, "France", "poisson", "oeufs"])
R("Brie et noix (France)", CO, 3, [("brie", 40), ("noix", 8), ("fb0", 60)],
  ["Servez le brie avec les noix et le fromage blanc."], [LC, "France", "vegetarien", "rapide"])
R("Salami, mozzarella et cornichons (Italie)", CO, 3, [("salami", 30), ("cornichon", 30), ("mozzarella", 30)],
  ["Disposez salami, mozzarella et cornichons."], [LC, "Italie", "rapide"])
R("Chorizo et fromage de brebis (Espagne)", CO, 3, [("chorizo", 20), ("brebis", 25), ("oliveverte", 10), ("concombre", 50)],
  ["Disposez le tout dans une assiette."], [LC, "Espagne", "rapide"])

# ---------------------------------------------------------------- plats (63)
R("Poulet aux herbes et courgettes à la crème (France)", PL, 30, [("poulet", 150), ("courgette", 200), ("cremelegere", 40), ("herbes", 2), ("beurre", 5)],
  ["Dorez le poulet dans le beurre.", "Ajoutez courgettes, crème et herbes, mijotez 10 minutes."], [LC, "France", "viande"])
R("Entrecôte, beurre persillé et haricots verts (France)", PL, 20, [("entrecote", 150), ("beurre", 10), ("persil", 4), ("harivert", 200)],
  ["Grillez l'entrecôte.", "Servez avec les haricots verts et le beurre persillé."], [LC, "France", "viande", "rapide"])
R("Cuisse de canard aux champignons (France)", PL, 35, [("canard", 220), ("champignon", 150), ("echalote", 20), ("vinblanc", 30), ("beurre", 8)],
  ["Dorez le canard.", "Ajoutez champignons, échalote et vin, mijotez 15 minutes."], [LC, "France", "viande"])
R("Poisson meunière, beurre et citron (France)", PL, 20, [("merlu", 180), ("beurre", 10), ("citron", 15), ("persil", 4), ("harivert", 150)],
  ["Poêlez le poisson au beurre.", "Ajoutez citron et persil, servez avec les haricots verts."], [LC, "France", "poisson"])
R("Salade de chèvre chaud (France)", PL, 15, [("chevre", 80), ("laitue", 100), ("noix", 12), ("jambon", 50), ("tomate", 80), ("vinaigre", 5)],
  ["Passez le chèvre au four 6 minutes.", "Servez sur la salade avec jambon, noix et vinaigrette."], [LC, "France", "four"])
R("Endives au jambon et à la crème (France)", PL, 35, [("endive", 250), ("jambon", 130), ("cremelegere", 40), ("emmental", 25)],
  ["Enroulez les endives dans le jambon.", "Nappez de crème et d'emmental, gratinez 20 minutes."], [LC, "France", "four"])
R("Lapin à la moutarde sans pommes de terre (France)", PL, 45, [("lapin", 160), ("moutarde", 12), ("cremelegere", 30), ("harivert", 200)],
  ["Dorez le lapin, nappez de moutarde et de crème.", "Mijotez 30 minutes, servez avec les haricots verts."], [LC, "France", "viande"])
R("Filet de bar rôti et fenouil (France)", PL, 30, [("bar", 170), ("fenouil", 200), ("citron", 10), ("huileolive", 5)],
  ["Rôtissez le bar et le fenouil en lamelles à 190 °C.", "Arrosez de citron."], [LC, "France", "poisson", "four"])
R("Poulet basquaise sans riz (France)", PL, 40, [("poulet", 150), ("poivron", 200), ("tomate", 100), ("oignon", 30), ("huileolive", 5)],
  ["Dorez le poulet avec l'oignon.", "Ajoutez poivrons et tomates, mijotez 25 minutes."], [LC, "France", "viande"])
R("Œufs aux lardons et aux champignons au vin blanc (France)", PL, 25, [("oeuf", 180), ("lardons", 40), ("champignon", 100), ("vinblanc", 30)],
  ["Faites revenir lardons et champignons, ajoutez le vin.", "Pochez les œufs dans la sauce 3 minutes."], [LC, "France", "oeufs"])
R("Saltimbocca de veau (Italie)", PL, 20, [("veau", 150), ("parme", 40), ("beurre", 8), ("harivert", 200)],
  ["Posez le jambon de Parme sur l'escalope.", "Poêlez au beurre, servez avec les haricots verts."], [LC, "Italie", "viande", "rapide"])
R("Poulet à la parmesane (Italie)", PL, 30, [("poulet", 150), ("coulis", 80), ("mozzarella", 50), ("parmesan", 10), ("basilic", 3)],
  ["Poêlez le poulet, nappez de coulis.", "Ajoutez la mozzarella et le parmesan, gratinez 8 minutes."], [LC, "Italie", "viande", "four"])
R("Carpaccio de bœuf, salade et parmesan (Italie)", PL, 15, [("entrecote", 130), ("laitue", 80), ("parmesan", 25), ("citron", 10), ("huileolive", 8)],
  ["Tranchez finement le bœuf grillé froid.", "Servez sur la salade avec le parmesan, le citron et l'huile."], [LC, "Italie", "viande", "rapide"])
R("Escalope de dinde au citron (Italie)", PL, 20, [("dinde", 160), ("citron", 15), ("beurre", 8), ("epinard", 150)],
  ["Poêlez la dinde au beurre avec le citron.", "Servez avec les épinards."], [LC, "Italie", "viande", "rapide"])
R("Poisson à l'acqua pazza (Italie)", PL, 30, [("cabillaud", 180), ("tomatecerise", 150), ("ail", 3), ("olive", 15), ("huileolive", 6)],
  ["Faites revenir l'ail et les tomates cerises dans l'huile.", "Pochez le cabillaud avec les olives 10 minutes."], [LC, "Italie", "poisson"])
R("Courgettes farcies à la viande (Italie)", PL, 40, [("hache5", 140), ("courgette", 250), ("coulis", 80), ("parmesan", 15)],
  ["Évidez les courgettes et garnissez-les de viande à la tomate.", "Parsemez de parmesan, enfournez 30 minutes à 190 °C."], [LC, "Italie", "viande", "four"])
R("Aubergines à la parmesane (Italie)", PL, 45, [("aubergine", 250), ("mozzarella", 90), ("coulis", 100), ("parmesan", 20), ("oeuf", 60)],
  ["Superposez aubergines grillées, coulis et mozzarella.", "Ajoutez le parmesan et l'œuf battu, enfournez 25 minutes."], [LC, "Italie", "vegetarien", "four"])
R("Frittata aux épinards et à la ricotta (Italie)", PL, 25, [("oeuf", 180), ("epinard", 150), ("ricotta", 80), ("parmesan", 10)],
  ["Mêlez œufs, épinards et ricotta.", "Cuisez à feu doux, parsemez de parmesan."], [LC, "Italie", "vegetarien", "oeufs"])
R("Thon, tomates et mozzarella (Italie)", PL, 15, [("thon", 130), ("mozzarella", 70), ("tomate", 150), ("basilic", 3), ("huileolive", 5)],
  ["Disposez tomates, mozzarella et thon.", "Assaisonnez de basilic et d'huile."], [LC, "Italie", "poisson", "rapide"])
R("Veau mijoté façon osso buco (Italie)", PL, 60, [("veau", 160), ("carotte", 60), ("celeri", 40), ("coulis", 100), ("oignon", 30)],
  ["Dorez le veau, ajoutez légumes et coulis.", "Mijotez 45 minutes."], [LC, "Italie", "viande"])
R("Pollo alla cacciatora sans féculent (Italie)", PL, 40, [("poulet", 150), ("tomate", 150), ("olive", 15), ("champignon", 100), ("romarin", 2), ("huileolive", 8)],
  ["Dorez le poulet.", "Ajoutez tomates, champignons, olives et romarin, mijotez 25 minutes."], [LC, "Italie", "viande"])
R("Gambas à l'ail (Espagne)", PL, 15, [("crevette", 200), ("ail", 5), ("huileolive", 15), ("paprika", 2), ("persil", 4)],
  ["Faites revenir l'ail dans l'huile avec le paprika.", "Ajoutez les crevettes 3 minutes, parsemez de persil."], [LC, "Espagne", "poisson", "rapide"])
R("Calamars à la plancha et salade (Espagne)", PL, 20, [("calmar", 180), ("citron", 15), ("huileolive", 8), ("laitue", 80), ("tomate", 100)],
  ["Saisissez les calamars à feu vif 3 minutes.", "Servez avec citron, salade et tomate."], [LC, "Espagne", "poisson", "rapide"])
R("Poulet au chorizo et aux poivrons (Espagne)", PL, 35, [("poulet", 150), ("chorizo", 30), ("poivron", 150), ("tomate", 100)],
  ["Dorez poulet et chorizo.", "Ajoutez poivrons et tomate, mijotez 20 minutes."], [LC, "Espagne", "viande"])
R("Pulpo à la galicienne sans pommes de terre (Espagne)", PL, 15, [("poulpe", 180), ("paprika", 2), ("huileolive", 10), ("concombre", 100)],
  ["Tranchez le poulpe cuit.", "Assaisonnez d'huile et de paprika, servez avec le concombre."], [LC, "Espagne", "poisson", "rapide"])
R("Gazpacho et œufs durs au jambon sec (Espagne)", PL, 15, [("tomate", 250), ("concombre", 100), ("poivron", 60), ("oeufdur", 110), ("jambonsec", 40)],
  ["Mixez tomate, concombre et poivron en gazpacho.", "Servez avec les œufs durs et le jambon sec en dés."], [LC, "Espagne", "oeufs"])
R("Merlu à la sauce verte (Espagne)", PL, 25, [("merlu", 180), ("persil", 10), ("ail", 4), ("huileolive", 8), ("petitspois", 60)],
  ["Pochez le merlu avec l'ail.", "Ajoutez persil, petits pois et huile, mixez à moitié la sauce."], [LC, "Espagne", "poisson"])
R("Tortilla de courgettes (Espagne)", PL, 25, [("oeuf", 200), ("courgette", 150), ("oignon", 30), ("jambonsec", 30), ("huileolive", 6)],
  ["Faites revenir courgette et oignon.", "Ajoutez œufs battus et jambon sec, cuisez des deux côtés."], [LC, "Espagne", "oeufs"])
R("Agneau rôti au romarin et haricots verts (Espagne)", PL, 30, [("agneau", 150), ("romarin", 2), ("ail", 4), ("harivert", 200)],
  ["Rôtissez l'agneau à l'ail et au romarin 20 minutes à 200 °C.", "Servez avec les haricots verts."], [LC, "Espagne", "viande", "four"])
R("Cabillaud à la portugaise (Portugal)", PL, 30, [("cabillaud", 180), ("tomate", 150), ("poivron", 80), ("oliveverte", 15), ("huileolive", 6)],
  ["Posez le cabillaud sur un lit de tomates et poivrons.", "Ajoutez les olives, enfournez 20 minutes à 190 °C."], [LC, "Portugal", "poisson", "four"])
R("Sardines grillées à la portugaise (Portugal)", PL, 20, [("sardine", 180), ("poivron", 100), ("tomate", 100), ("citron", 10)],
  ["Grillez les sardines.", "Servez avec poivrons rôtis, tomate et citron."], [LC, "Portugal", "poisson", "rapide"])
R("Poulet piri-piri (Portugal)", PL, 35, [("poulet", 160), ("paprika", 3), ("citron", 15), ("ail", 4), ("laitue", 80), ("huileolive", 6)],
  ["Marinez le poulet avec piment, citron, ail et huile.", "Rôtissez 25 minutes à 200 °C, servez avec la salade."], [LC, "Portugal", "viande", "four"])
R("Morue aux œufs et aux olives façon Brás (Portugal)", PL, 25, [("morue", 150), ("oeuf", 120), ("oignon", 30), ("olive", 15), ("persil", 4)],
  ["Faites revenir l'oignon et la morue émiettée.", "Ajoutez les œufs battus, olives et persil."], [LC, "Portugal", "poisson", "oeufs"])
R("Caldo verde sans pommes de terre au chorizo (Portugal)", PL, 30, [("chou", 200), ("chorizo", 30), ("poulet", 120), ("oignon", 30)],
  ["Cuisez le chou émincé et l'oignon dans l'eau 15 minutes.", "Ajoutez le poulet cuit et le chorizo."], [LC, "Portugal", "viande"])
R("Porc aux moules à la portugaise (Portugal)", PL, 35, [("porc", 150), ("moule", 150), ("ail", 4), ("persil", 4), ("citron", 10)],
  ["Dorez le porc en dés avec l'ail.", "Ajoutez les moules cuites, citron et persil."], [LC, "Portugal", "viande", "poisson"])
R("Daurade grillée aux herbes (Portugal)", PL, 25, [("dorade", 180), ("citron", 15), ("thym", 2), ("harivert", 200), ("huileolive", 6)],
  ["Grillez la dorade avec les herbes.", "Servez avec les haricots verts et le citron."], [LC, "Portugal", "poisson"])
R("Salade grecque au poulet et à la feta (Grèce)", PL, 20, [("poulet", 150), ("feta", 50), ("concombre", 100), ("tomate", 150), ("olive", 15), ("huileolive", 6)],
  ["Mélangez concombre, tomate et olives.", "Ajoutez le poulet grillé, la feta et l'huile."], [LC, "Grèce", "viande", "rapide"])
R("Souvlaki de poulet, tzatziki et salade (Grèce)", PL, 25, [("poulet", 160), ("tzatziki", 80), ("tomate", 100), ("concombre", 80), ("origan", 1)],
  ["Grillez le poulet en brochettes à l'origan.", "Servez avec le tzatziki et les crudités."], [LC, "Grèce", "viande"])
R("Moussaka sans pommes de terre (Grèce)", PL, 55, [("aubergine", 250), ("agneau", 110), ("coulis", 80), ("fb0", 100), ("oeuf", 30)],
  ["Grillez les aubergines, poêlez l'agneau au coulis.", "Superposez, nappez de fromage blanc et d'œuf.", "Enfournez 25 minutes à 190 °C."], [LC, "Grèce", "viande", "four"])
R("Poisson grillé à la grecque (Grèce)", PL, 25, [("bar", 180), ("citron", 15), ("origan", 1), ("huileolive", 8), ("tomate", 120)],
  ["Grillez le bar à l'origan.", "Servez avec tomates, citron et huile."], [LC, "Grèce", "poisson"])
R("Calamars farcis à la feta (Grèce)", PL, 35, [("calmar", 170), ("feta", 50), ("tomate", 120), ("persil", 4)],
  ["Farcissez les calamars de feta et de persil.", "Mijotez-les dans la tomate 20 minutes."], [LC, "Grèce", "poisson"])
R("Agneau rôti à l'origan (Grèce)", PL, 40, [("agneau", 150), ("origan", 2), ("citron", 15), ("courgette", 200), ("huileolive", 6)],
  ["Rôtissez l'agneau à l'origan et au citron 25 minutes.", "Servez avec les courgettes grillées."], [LC, "Grèce", "viande", "four"])
R("Boulettes d'agneau et tzatziki (Grèce)", PL, 25, [("hache5", 100), ("agneau", 60), ("menthe", 3), ("tzatziki", 80), ("concombre", 100)],
  ["Mélangez les viandes hachées et la menthe, formez des boulettes.", "Poêlez-les, servez avec tzatziki et concombre."], [LC, "Grèce", "viande"])
R("Horiatiki aux œufs durs et au thon (Grèce)", PL, 15, [("thon", 120), ("oeufdur", 110), ("tomate", 150), ("concombre", 100), ("feta", 40), ("oliveverte", 15)],
  ["Composez la salade de tomate et concombre.", "Ajoutez thon, œufs, feta et olives."], [LC, "Grèce", "poisson", "oeufs", "rapide"])
R("Gratin d'épinards et de feta (Grèce)", PL, 35, [("epinard", 200), ("feta", 60), ("oeuf", 120), ("fb0", 100)],
  ["Mêlez épinards, feta, œufs et fromage blanc.", "Enfournez 25 minutes à 180 °C."], [LC, "Grèce", "vegetarien", "oeufs", "four"])
R("Choucroute allégée au jambon et à la saucisse (Allemagne)", PL, 25, [("choucroute", 250), ("jambon", 100), ("francfort", 70), ("moutarde", 8)],
  ["Réchauffez la choucroute rincée.", "Ajoutez jambon et saucisse, servez avec la moutarde."], [LC, "Allemagne", "viande", "rapide"])
R("Schnitzel de dinde sans chapelure (Allemagne)", PL, 20, [("dinde", 160), ("oeuf", 30), ("parmesan", 15), ("citron", 10), ("harivert", 200)],
  ["Trempez l'escalope dans l'œuf et le parmesan râpé.", "Poêlez 3 minutes par face, servez avec citron et haricots verts."], [LC, "Allemagne", "viande"])
R("Rôti de porc et chou rouge (Allemagne)", PL, 50, [("porc", 150), ("chourouge", 200), ("moutarde", 8), ("thym", 2)],
  ["Rôtissez le porc au thym 30 minutes à 190 °C.", "Servez avec le chou rouge braisé et la moutarde."], [LC, "Allemagne", "viande", "four"])
R("Saucisses de Francfort et chou braisé (Allemagne)", PL, 30, [("francfort", 140), ("jambon", 70), ("chou", 250), ("moutarde", 10), ("oignon", 30)],
  ["Braisez le chou et l'oignon 15 minutes.", "Poêlez les saucisses, servez avec la moutarde."], [LC, "Allemagne", "viande"])
R("Salade de chou et de poulet au yaourt (Allemagne)", PL, 15, [("poulet", 150), ("chou", 150), ("yaourt", 100), ("moutarde", 8), ("carotte", 40)],
  ["Mélangez chou émincé, carotte râpée, yaourt et moutarde.", "Ajoutez le poulet effiloché."], [LC, "Allemagne", "viande", "rapide"])
R("Hareng aux oignons et au yaourt (Allemagne)", PL, 15, [("harengfume", 150), ("oignon", 30), ("yaourt", 125), ("aneth", 3), ("oeufdur", 55)],
  ["Mélangez yaourt, oignon et aneth.", "Servez avec le hareng et l'œuf dur."], [LC, "Allemagne", "poisson", "oeufs", "rapide"])
R("Boulettes de viande allemandes (Frikadellen) et salade (Allemagne)", PL, 25, [("hache5", 150), ("oeuf", 30), ("oignon", 30), ("laitue", 80), ("moutarde", 8)],
  ["Mélangez viande, œuf et oignon, formez des galettes.", "Poêlez-les 4 minutes par face.", "Servez avec la salade et la moutarde."], [LC, "Allemagne", "viande"])
R("Fricassée de champignons, jambon et œufs à la crème (Allemagne)", PL, 25, [("champignon", 250), ("oeuf", 120), ("cremelegere", 40), ("jambon", 60), ("persil", 4)],
  ["Poêlez les champignons et le jambon.", "Ajoutez la crème et les œufs brouillés."], [LC, "Allemagne", "oeufs"])
R("Poulet rôti aux herbes et brocoli (Allemagne)", PL, 40, [("poulet", 160), ("brocoli", 200), ("thym", 2), ("beurre", 8)],
  ["Rôtissez le poulet au thym 25 minutes à 200 °C.", "Servez avec le brocoli au beurre."], [LC, "Allemagne", "viande", "four"])
R("Gratin de chou-fleur au jambon et au gruyère (Allemagne)", PL, 35, [("chouxfleur", 250), ("jambon", 120), ("gruyere", 30), ("cremelegere", 30)],
  ["Cuisez le chou-fleur 8 minutes.", "Nappez de crème, ajoutez jambon et gruyère, gratinez 15 minutes."], [LC, "Allemagne", "viande", "four"])
R("Fondue de poireaux et saucisses (Allemagne)", PL, 30, [("poireau", 250), ("francfort", 100), ("jambon", 100), ("cremelegere", 30), ("moutarde", 8)],
  ["Faites fondre les poireaux 15 minutes.", "Ajoutez saucisses, crème et moutarde."], [LC, "Allemagne", "viande"])
R("Truite pochée, beurre citronné et haricots verts (Allemagne)", PL, 25, [("truite", 170), ("beurre", 10), ("citron", 10), ("harivert", 200)],
  ["Pochez la truite 10 minutes.", "Servez avec le beurre fondu citronné et les haricots."], [LC, "Allemagne", "poisson"])
R("Thon, œufs et salade verte (France)", PL, 15, [("thon", 130), ("oeufdur", 110), ("laitue", 100), ("tomate", 100), ("huileolive", 6)],
  ["Composez la salade.", "Ajoutez thon, œufs et huile."], [LC, "France", "poisson", "oeufs", "rapide"])
R("Raclette de légumes et de jambon (France)", PL, 30, [("raclette", 80), ("jambonsec", 40), ("chouxfleur", 150), ("champignon", 100), ("cornichon", 30)],
  ["Cuisez chou-fleur et champignons.", "Faites fondre la raclette dessus au four 8 minutes.", "Servez avec le jambon et les cornichons."], [LC, "France", "four"])
R("Tartiflette sans pommes de terre au chou-fleur (France)", PL, 40, [("chouxfleur", 250), ("reblochon", 70), ("lardons", 40), ("oignon", 30)],
  ["Cuisez le chou-fleur.", "Mêlez lardons et oignon, couvrez de reblochon.", "Gratinez 15 minutes."], [LC, "France", "viande", "four"])
R("Cassolette de fruits de mer à la crème (France)", PL, 25, [("crevette", 120), ("moule", 120), ("stjacques", 80), ("cremelegere", 40), ("persil", 3)],
  ["Pochez les fruits de mer.", "Ajoutez la crème et le persil, chauffez 3 minutes."], [LC, "France", "poisson"])
R("Pintade aux champignons (France)", PL, 40, [("pintade", 170), ("champignon", 150), ("cremelegere", 30), ("harivert", 150)],
  ["Dorez la pintade.", "Ajoutez champignons et crème, mijotez 20 minutes.", "Servez avec les haricots verts."], [LC, "France", "viande"])
R("Chou farci à la dinde (France)", PL, 50, [("dinde", 140), ("chou", 250), ("coulis", 80), ("oeuf", 30)],
  ["Blanchissez les feuilles de chou.", "Garnissez de dinde hachée et d'œuf, roulez.", "Mijotez dans le coulis 30 minutes."], [LC, "France", "viande"])

# Comparaison du modèle manuel et du modèle AutoML — TP05

| Critère | Manuel — Random Forest | AutoML — XGBoost |
|---|---|---|
| Famille de modèle | Forêt aléatoire, 500 arbres, profondeur maximale 16 | XGBoost, 322 arbres, 4 feuilles maximum par arbre |
| F1 sur le jeu de test | 0,8669 | 0,8561 |
| Temps de recherche machine | Recherche TP2 à renseigner si mesurée. Réentraînement au TP05 de 1,5 s. | 90 s |
| Temps humain (estimation) | À estimer pour les réglages du TP2 | À estimer pour la configuration et le lancement de FLAML |
| Latence médiane — essais 1 et 2 | 85,2 / 110,7 ms | 13,0 / 16,5 ms |
| Latence p95 — essais 1 et 2 | 136,0 / 147,8 ms | 13,9 / 26,2 ms |
| Taille du fichier | 13,37 Mo | 0,28 Mo |
| Explicabilité | Importance des variables, nombre d’arbres et profondeur maximale | Importance des variables, nombre d’arbres et nombre maximal de feuilles |

## Décision

Je choisis XGBoost pour la mise en production dans le cadre de ce TP.  
Son F1 de 0,8561 est inférieur de 0,0108 à celui du Random Forest.  
Sur les deux essais locaux, sa latence médiane est de 13,0 à 16,5 ms, contre 85,2 à 110,7 ms pour le Random Forest.  
Son p95 est inférieur aux deux essais et son fichier de 0,28 Mo représente environ 2 % de la taille du modèle manuel.  
J’accepte le léger écart de F1 en échange d’un service plus rapide et d’un modèle plus compact.
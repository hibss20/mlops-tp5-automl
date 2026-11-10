# Comparaison du modèle manuel et du modèle AutoML — TP05

| Critère | Manuel — Random Forest (500 arbres, profondeur 16) | AutoML — XGBoost |
|---|---|---|
| F1 sur le jeu de test | À relever dans MLflow | 0,8561 |
| Temps de recherche machine | À compléter avec les mesures du TP2 | 90 s |
| Temps humain (estimation) | À compléter | À compléter |
| Latence médiane — essai 1 | 85,2 ms | 13,0 ms |
| Latence médiane — essai 2 | 110,7 ms | 16,5 ms |
| Latence p95 — essai 1 | 136,0 ms | 13,9 ms |
| Latence p95 — essai 2 | 147,8 ms | 26,2 ms |
| Taille du fichier | 13,37 Mo | 0,28 Mo |
| Explicabilité | Importance des variables, nombre d’arbres et profondeur maximale | Importance des variables, nombre d’arbres et nombre maximal de feuilles |

## Décision

Je privilégie XGBoost pour la mise en production.
Il obtient un F1 de 0,8561 sur le jeu de test.
Sa latence médiane est de 13,0 à 16,5 ms, contre 85,2 à 110,7 ms pour le Random Forest.
Son fichier de 0,28 Mo est environ 48 fois plus léger que celui du Random Forest.
Je confirmerai ce choix après avoir comparé les F1 des deux modèles.
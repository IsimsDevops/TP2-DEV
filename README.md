# TP2-DEV
## Première application FastAPI

### Lancement de l'application

Installer FastAPI et ses dépendances :

```bash
python -m pip install "fastapi[standard]"
```

Lancer l'application depuis le dossier contenant `main.py` :

```bash
python -m uvicorn main:app --reload
```

Le serveur démarre à l'adresse http://127.0.0.1:8000.

### Test de l'application

Pour tester la route principale, ouvrir http://127.0.0.1:8000/ dans un navigateur.

Résultat attendu :

```json
{
  "message": "it works !"
}
```

Pour tester l'application avec l'interface interactive de FastAPI, ouvrir http://127.0.0.1:8000/docs, sélectionner `GET /`, cliquer sur `Try it out`, puis sur `Execute`.

Le résultat attendu est un code HTTP `200 OK` avec le message `{"message": "it works !"}`.
# Heroku Django Project (HDP)

<br/>
<br/>

## Installation

### Installation de python3
```
sudo apt install python3
sudo apt install python3-pip
```
Il faut s'assurer de la version de python qui est installée. La version de python
utilisée est `python 3.9.7`. Vous pouvez aussi utiliser version version `3.8`.

<br/>

### Installation de venv
```
sudo apt install python3-venv
```
OU
```
sudo pip3 install virtualenv
```
<br/>

### Créer un environnement virtuel
```
python3 -m venv env
```
OU
```
virtualenv env -p python3
```
<br/>

### Démarrage de l'environnement
```
source env/bin/activate
```
<br/>

### Installation des dépendances
```
pip install -r requirements.txt
```
<br/>
<br/>

## Configuration du projet

### Configuration de la base de données
Le système de gestion de base de données utilisé est `PostgreSQL`. Pour l'installer,
tapez la commande suivante :
```
sudo apt install postgresql
```

Démarrez ensuite le service du SGBDR avec la commande suivante:
```
sudo service postgresql start
```
Connectez vous en mode `root` avec les deux commandes suivantes :
```
sudo su - postgres
```
```
psql
```
<br/>

### Création de la base de données
La création de la base de données se fera en deux parties:
<br/>

- Première partie
Exécutez les trois commandes SQL suivantes :
1. Création d'un utilisateur :
```sql
CREATE USER user_name WITH ENCRYPTED PASSWORD 'secretpassword' LOGIN NOCREATEDB;
```

2. Création de la base de données pour l'utilisateur précédement créé :
```sql
CREATE DATABASE db_name OWNER user_name;
```

3. Attribution du droit de connexion à la base de données à l'utilisateur :
```sql
GRANT CONNECT ON DATABASE db_name TO user_name;
```
Déconnectez vous enfin du SGBDR en faisant deux fois `CTRL + D`.
<br/>

- Seconde partie
1. Il faut créer un fichier `.env` à la racine du dossier du projet.
```
touch .env
```

2. Insérer les informations suivantes dans le fichier `.env` :
```
USERDB=user_name
PASSWORDDB=secretpassword
DB=db_name
HOST=127.0.0.1
PORT=5432
```
`PS` : Si le port `5432` ne marche pas, alors essayez avec le port `5433`.

3. Exécutez les commandes suivantes pour faire la migration 
des modèles de base de données
```
./manage.py makemigrations
```
```
./manage.py migrate
```
<br/>

### Création d'un super utilisateur pour l'espace admin
```
./manage.py createsuperuser
```

Vous pouvez renseigner juste le `username` et le `password`.
<br/>

### Démarrage du serveur de django
```
./manage.py runserver
```
Résultats dans le terminal, qui indique que tout va bien est :
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 21, 2022 - 07:53:49
Django version 3.2.6, using settings 'docs.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

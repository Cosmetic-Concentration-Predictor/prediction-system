# README - prediction-system

Bienvenue sur la branche du projet ! Cette branche contient un fichier `docker-compose.yml` qui facilite l'exécution du projet à l'aide de Docker Compose.

## Docker Compose

Le fichier `docker-compose.yml` définit deux services :

### vue-app

Ce service construit et exécute l'application Vue.js. Il est basé sur un Dockerfile (`Dockerfile-vue`) situé dans le dossier `frontend`.

#### Dockerfile-vue :
```Dockerfile
FROM node:20.10.0

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

CMD ["npm", "run", "serve"]
```

### flask-app

Ce service construit et exécute l'application Flask. Il est basé sur un Dockerfile (`Dockerfile-flask`) situé dans le dossier `api`.

#### Dockerfile-flask :
```Dockerfile
FROM python:3.12.1-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
```

## Comment utiliser

Assurez-vous d'avoir Docker et Docker Compose installés sur votre système.

1. Ouvrez un terminal et naviguez jusqu'au répertoire racine du projet où se trouve le fichier `docker-compose.yml`.

2. Exécutez la commande suivante pour démarrer les services :
   ```bash
   docker-compose up -d
   ```

Cela construira les images Docker et lancera les conteneurs pour chaque service.

3. Une fois que les conteneurs sont en cours d'exécution, vous pouvez accéder à l'application Vue.js sur `http://localhost:8080` et à l'application Flask sur `http://localhost:5000`.

4. Pour arrêter les services, appuyez sur `Ctrl + C` dans le terminal où `docker-compose` est en cours d'exécution.

C'est tout ! Vous pouvez maintenant exécuter le projet à l'aide de Docker Compose. Explorez les services et apportez les modifications nécessaires.

Merci d'utiliser Docker Compose pour exécuter le projet !

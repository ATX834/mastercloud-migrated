# MasterCloud Remaster

Application MasterCloud Remaster, une plateforme de streaming musicale.

## Technologies utilisées

- Python
- FastAPI
- Nuxt 3
- Vue 3
- TypeScript
- Tailwind CSS

## Prérequis

- Node.js (version 16 ou supérieure)
- npm ou yarn

## Installation

1. Cloner le repository :
```bash
git clone [URL_DU_REPO]
cd mastercloud-frontend
```

2. Installer les dépendances :
```bash
npm install
# ou
yarn install
```

3. Créer un fichier `.env` à la racine du projet (optionnel) :
```env
NUXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## Développement

Pour lancer le serveur de développement :

```bash
npm run dev
# ou
yarn dev
```

L'application sera accessible à l'adresse `http://localhost:3000`

## Build

Pour construire l'application pour la production :

```bash
npm run build
# ou
yarn build
```

Pour prévisualiser la version de production :

```bash
npm run preview
# ou
yarn preview
```

## Structure du projet

```
mastercloud-frontend/
├── assets/          # Ressources statiques (CSS, images, etc.)
├── components/      # Composants Vue réutilisables
├── layouts/         # Layouts de l'application
├── pages/          # Pages de l'application
├── public/         # Fichiers publics
└── server/         # API et logique serveur
```

## Fonctionnalités

- Authentification
- Gestion des playlists
- Profil utilisateur
- Paramètres personnalisés
- Interface responsive

## Contribution

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

# DiscoBot - La Star des Salons Vocaux 🎶

Bienvenue dans l'univers étincelant de DiscoBot, le bot Discord qui transformera vos salons vocaux en une piste de danse virtuelle ! 🕺💃

## 🌟 Présentation 

DiscoBot est bien plus qu'un simple bot de musique pour Discord. C'est votre partenaire de fête ultime, prêt à faire vibrer vos serveurs avec les meilleurs sons et les rythmes les plus envoûtants. Mettez-vous en mode disco avec DiscoBot et préparez-vous à une expérience musicale épique !

## 🎵 Fonctionnalités

- Recherche de Musique 🔍 : DiscoBot vous permet de rechercher votre musique préférée par titre, garantissant que vous puissiez toujours écouter exactement ce que vous avez en tête.
- Commandes Intuitives 🎛️ : Contrôlez DiscoBot facilement avec des commandes simples et intuitives, même si vous avez deux pieds gauches !
- Lecture de Playlist 📜 : Créez une atmosphère continue en permettant à DiscoBot de gérer vos playlists. 
- Affichage Élégant 🌈 : Transformez votre expérience musicale avec un affichage visuel élégant. Les informations sur la chanson en cours, les pochettes d'album et plus encore sont présentées de manière attrayante pour une immersion totale dans la musique.



## 🚀 Comment l'installer ?

Vous déployer DiscoBot en utilisant Docker pour une installation rapide et efficace ! 🐳
### Prérequis

    Assurez-vous que Docker est installé sur votre machine.

### Étapes d'Installation

1. **Clonez le Repo :**
```bash
git clone https://github.com/AlexandreFigard/discobot.git
cd DiscoBot
```


2. **Configurez le Token Discord :**

- Obtenez votre token Discord en créant une nouvelle application sur le [Portail des développeurs Discord.](https://discord.com/developers)
- Créez un fichier .env à la racine du projet et ajoutez votre token :
```env
 DISCOBOT_TOKEN=VotreTokenDiscord
 ```
   

3. Build de l'Image Docker :

```bash
docker build -t discobot:latest .
```

4. Lancez le Conteneur :
```bash
docker run -d discobot:latest
```
Et voilà ! DiscoBot est maintenant prêt à faire vibrer vos salons vocaux.

## 🕺 Prêt à Danser ?

Mettez vos chaussures de danse, montez le volume et laissez DiscoBot transformer votre serveur en la boîte de nuit ultime ! Préparez-vous à une expérience musicale comme aucune autre.

Let's dance with DiscoBot! 🌟🎉

## Credits

- Mathéo Boulogne
- Alexandre Figard
- Mathieu Bedez
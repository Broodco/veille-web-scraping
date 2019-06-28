# Veille/Challenge **Web Scraping**

## Qu'est-ce que le **Web Scraping**?

Le **Web Scraping** est une technique permettant l'extraction de données d'un site via un programme. l'objectif est d'extraire le contenu de manière structurée en vue de réutiliser les données.

## Pourquoi le **Web Scraping**?

Plein d'utilisations :
- Une entreprise d'e-commerce peut tracker les prix de ses compétiteurs de manière automatique et, sur base de ces données, définir une stratégie de pricing.
- Un manufacteur peut garder un oeil sur les vendeurs de son produit.
- On peut récupérer des données de manière automatique afin de les réutiliser dans notre application, de la même manière qu'avec une API par exemple.
- Enormément d'applications en Data Science ==> car on récupère des données, tout simplement.
- Industrie de l'information. Pour se tenir au courant de certaines personnes, produits, entreprises, etc.

## Légalité et éthique

Cependant, attention. Le **Web Scraping** a des implications légales, morales et éthiques. Récupérer des données ne nous appartenant pas, sous Copyright ou protégées par les termes et conditions d'un site web est illégal. De plus, le **Web Scraping**, bien qu'énormément utilisé, est parfois apparenté à de la concurrence déloyale. Je vous invite à suivre les règles de bonnes pratiques du Web Scraping, que vous pouvez retrouver dans les sources (1).

## Comment on en fait?

On peut résumer le **Web Scraping** en deux étapes :
1. Récupérer le contenu d'un site web
2. Convertir ces données dans un format propice à une analyse

### Quel langage pour faire du **Web Scraping**?

**Tous**, à priori. Mais certains sont plus adaptés/populaires que d'autres. Premièrement, et surtout dans le cadre de petits projets ou exercices, il n'est pas nécessaire d'apprendre *LE* langage le plus efficace. Vous pouvez bien entendu utiliser un langage dans lequel vous vous sentez à votre aise. La plupart des langages possèdent des *librairies* qui vous faciliteront grandement le travail, à l'instar de *Scrapy* et *Beautiful Soup* pour Python, *CheerioJS* et *Puppeteer* pour Node.js.

Selon mes sources, on conseille principalement Python et Node.js pour le Web Scraping. 

Pour en savoir plus sur le sujet, je vous invite à vous rendre sur le site cité dans les sources (2), ou faire vos propres recherches (à l'aide de Web Scraping, qui sait !).

### Concrètement?

Voici quelques ressources que je mets à votre disposition si vous ne savez pas par où commencer :

- **Node.js** : [https://www.freecodecamp.org/news/the-ultimate-guide-to-web-scraping-with-node-js-daa2027dcd3/]
- **Node.js** (n°2) : [https://stackabuse.com/web-scraping-with-node-js/]
- **Python** : [https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722] 

## Exemples

### Exemple simple

Voici un petit programme écrit en Python, qui télécharge et affiche le contenu du fichier *robots.txt* du site *Wikipedia*.

    import requests
    response = requests.get("https://fr.wikipedia.org/robots.txt)
    robots = response.text
    print (robots)

Pas très compliqué en effet?

### Exemple moins simple

Merci Matthieu pour le coup de main ! : [https://github.com/MazzinWX/web_scraping_node]

## Le Challenge du jour

Votre challenge, si vous l'acceptez, est de récupérer une liste des repos de Bertrand depuis [sa page GitHub](https://github.com/BertrandMarlair?tab=repositories). Vous devrez récupérer, pour chaque repo, son _nom_ et sa _description_ (si il en a une), et créer un tableau qui sera converti en JSON par la suite. Le résultat final devrait ressembler à ça :

    [
        {
            'nom':'SuperRepo',
            'description':'Un repo super cool'
        },
        {
            'nom':'azerty',
            'description':'Pas de description'
        },
        ...
    ]

N'hésitez pas à me demander un coup de main :) Pour ma part, je l'ai fait en Python !

## Sources

- (1) [https://www.promptcloud.com/blog/web-scraping-best-practices/]
- (2) [https://www.promptcloud.com/blog/best-programming-language-for-web-scraping/]. 

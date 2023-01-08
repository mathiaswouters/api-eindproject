# Eindproject - API Development

Voor dit project moesten we een API maken rond een zelf te kiezen thema. We konden zelf kiezen of we hetzelfde thema gebruikten als dat van het basisproject of genoow een nieuw gebruikten, ik heb gekozen om een nieuwe te gebruiken. De API moest ook via GitHub Actions automatisch op docker hub gepost worden na een push naar de GitHub repo, deze moest dan ook op okteto gedeployed worden. We moesten tenslotte ook nog hashing en OAuth toepassen.

# Thema

Het thema dat ik voor dit project heb gekozen zijn Off-Road Cars, omdat ik zelf wel veel interesse heb in auto's. En dan zeker van die grote SUV's of pick-up's met een zware moter die over met gemak doorheen kunnen rijden.

Deze API is dus gemaakt voor als je bijvoorbeeld een grote off-road auto dealer hebt, dan kun je in deze API al de auto's toevoegen en raadplegen die dat je verkoopt.

# API

De API is opgedeeld in 3 onderdelen: brands, models, owners. Voor elk onderdeel is er ook een tabel aangemaakt in de database.
Dit zijn alle requests die er zijn:

- GET Brand: Geeft alle brands in de database
- GET Brand ID: Geeft de brand die bij een bepaalde ID hoort
- GET Brand Name: Geeft de brand per name
- GET Model: Geeft alle models
- GET Model ID: Geeft het model die bij een bepaalde ID hoort
- GET Model Name: Geeft het model per name
- GET Model Year: Geeft het model per year
- GET Model Body Type: Geeft het model per body type
- GET Model Power: Geeft het model per power
- GET Model Brand ID: Geeft het model per ID van een merk

- POST Model: maakt een nieuw model aan
- POST Brand: maakt een nieuwe brand aan
- POST Owner: maakt een nieuwe owner aan
- POST Token: maakt een nieuw token aan

- DELETE Model: Verwijdert een model uit de database

# database.py

Hier wordt de database aangemaakt en wordt er ook een URL voor gemaakt zodat je met de database kunt verbinden. Er worden ook de bijhorende classes aangemaakt zoals de SessionLocal class en de Base class en er wordt ook een engine aangemaakt.

# models.py

Hier maak je de nodige classes, dit worden de SQLAlchemy models.
Dit zijn de classes die dat ik gebruik:
![classes](./img/classes.png)

Zoals je ziet heb ik ook relaties toegevoegd:
Een brand kan meerdere models hebben, maar een model kan maar één brand hebben.
Een owner kan meerdere brands hebben, maar een brand kan maar één owner hebben.

# schemas.py

Hier maak ik de schemas aan voor de classes, dus ik zet hier eigenlijk hoe dat een nieuwe brand, model of owner aangemaakt moet worden door voor elk attribuut een base class, een create class en een class voor het attribuut zelf. Zoals je kan zien gebruik ik eigenlijk de create class alleen maar bij owner, dat doe ik omdat ja anders bij het oproepen van de owner class je ook gewoon z'n password kan zien. Dat vermijd ik door het password in de create class te zetten want dan komt deze alleen maar bij het maken van een nieuwe owner.

# crud.py

In de crud file maak ik alle nodige functies. Deze functies interageren met de gegevens in de database. Elke functie voegt oftewel nieuwe data toe, vraagt data aan in de db of verwijdert data van de database. Voor elke interactie met de database moet er een nieuwe session aangemaakt worden, omdat bij SQLlite elke session wordt afgesloten als de interactie gedaan is. Je maakt gebruik van de models gemaakt in de model.py file om de juiste gegevens mee te geven naar de database.

# main.py

In de main.py file komen alle requests te staan die je nodig hebt. Als eerste wordt er nagekeken of dat de database file te vinden is, daarna worden alle models (tabels in de database) aangemaakt. Vervolgens wordt de bearer token aangemaakt (zie bij "auth.py"),

# auth.py

# Aanvullingen

## Front-end

In mijn front-end roep ik de 2 get functies op die dat dan de landen/steden in mijn database laten zien. Ik heb de front-end wat bewerkt met bootstrap zodat deze niet de lelijke default html style heeft.

![front-end](./img/)

## Test

### test_main.py

...

# Postman screenshots

## GET Requests

### GET Brands

![GET Brands](./img/)

### GET Brand by ID

![GET Brand ID](./img/)

### GET Brand by Name

![GET Brand Name](./img/)

### GET Models

![GET Models](./img/)

### GET Model by ID

![GET Model ID](./img/)

### GET Model by Name

![GET Model Name](./img/)

### GET Model by Year

![GET Model Year](./img/)

### GET Model by Body Type

![GET Model Body Type](./img/)

### GET Model by Power

![GET Model Power](./img/)

### GET Model by Brand ID

![GET Model Brand ID](./img/)

## POST Requests

### POST Model

![POST Model](./img/)

### POST Brand

![POST Brand](./img/)

### POST Owner

![POST Owner](./img/)

### POST Token

![POST Token](./img/)

## DELETE Requests

### DELETE Model

![DELETE Model](./img/)

# OpenAPI docs screenshots

![OpenAPI docs](./img/)

# Links

- Hosted API: [Hosted API link](https://world-ranking-service-mathiaswouters.cloud.okteto.net)
- Front-end repo: [Front-end repo link](https://github.com/mathiaswouters/mathiaswouters.github.io)
- Hosted front-end: [Hosted front-end link](https://mathiaswouters.github.io/)

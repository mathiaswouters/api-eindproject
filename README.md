# Eindproject - API Development

Voor dit project moesten een API maken rond en zelf te kiezen thema. Deze API moest via docker gehost worden en er moest ook een front-end aangekoppeld zijn.

# Thema

Ik heb gekozen voor het thema reizen omdat ik zelf heel graag reis en hier kon ik al een begin maken voor een mogelijk programma dat mijn ranglijst van mijn top landen en steden kon bijhouden. Ik heb het zo gemaakt dat je op de front end 2 deeltjes ziet, één voor de landen en één voor de steden. Bij de 2 categoriën staat ook een knop om de landen/steden die dan al in de database staan te laten zien. Ik geef dan ook meteen wat informatie mee over die bestemming en er staat ook de rang bij.

De landen/steden staan opgeslagen in de API zelf in een JSON structuur.

# API

In de API maak ik gebruik van 3 GET requests die dat elk een andere functie heeft:

- GET Brand:
- GET Brand ID:
- GET Brand Name:
- GET Model:
- GET Model ID:
- GET Model Name:
- GET Model Year:
- GET Model Body Type:
- GET Model Power:
- GET Model Brand ID:

- POST Model:
- POST Brand:
- POST Owner:
- POST Token:

- DELETE Model:

# database.py

# models.py

# schemas.py

# crud.py

# main.py

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

### GET

![GET request 1](./img/)

### GET

![GET request 2](./img/)

### GET

![GET request 3](./img/)

### GET

![GET request 3 error](./img/)

## POST Requests

### POST

![POST request 1](./img/)

### POST

### POST

### POST

## DELETE Requests

### DELETE

# OpenAPI docs screenshots

![OpenAPI docs](./img/)

# Links

- Hosted API: [Hosted API link](https://world-ranking-service-mathiaswouters.cloud.okteto.net)
- Front-end repo: [Front-end repo link](https://github.com/mathiaswouters/mathiaswouters.github.io)
- Hosted front-end: [Hosted front-end link](https://mathiaswouters.github.io/)

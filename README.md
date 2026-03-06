# Tausta-ajoprosessi

Asynkroninen URL-osoitteiden käsittelyputki. API ottaa vastaan listan URL-osoitteita ja siirtää ne viestijonoon. 
Taustatyöprosessit noutavat jokaisen URL-osoitteen HTTP-tilatiedon ja tallentavat tulokset PostgreSQL-tietokantaan. 
Arkkitehtuuri hyödyntää FastAPI-kehystä rajapintakerroksessa, RabbitMQ:ta viestinvälittäjänä, Celeryä taustatehtävien 
hallinnassa ja PostgreSQL tietovarastona.

## Käyttöönotto

Varmista, että koneellasi on Docker ja Docker Compose asennettuna.

1. Kloonaa repositorio.
2. Käynnistä palvelu komennolla:
   ```
   docker-compose up --build
   ```

   API löytyy:
   ```
   http://localhost:8000
   ```
   ja sitä voi helposti käyttää Swagger-dokumentaation kautta:
   ```
   http://localhost:8000/docs
   ```

   Post-kutsussa voi käyttää seuraavaa request bodya eri tilanteiden havainnollistamiseksi:

   ```json
   {
   "urls": [
   "https://abc.vr",
   "https://httpbin.org/status/404",
   "https://google.fi"
   ]
   }
   ```

   Lisäksi palvelussa on käytössä RabbitMQ management -sivu, joka löytyy
   ```
   http://localhost:15672
   ```

## Riippuvuudet
Riippuvuudet löytyvät projektin juuresta 'requirements.txt' tiedostosta

```text
fastapi
uvicorn
celery
redis
psycopg2-binary
sqlalchemy
requests
pydantic
```

## Mitä voisi lisätä
Mikäli palvelua pitäisi parannella voisi lisätä tai muuttaa seuraavia asioita:
- Testikattavuutta ominaisuuksille, vaikkakin tässä työssä on vain niukasti niitä
- Requests-kirjaston tialle voisi vaihtaa jonkin asynkronisen kirjaston hakujen tehostamiseksi
- Autentikointi ainakin analyze-endpoint POST-kutsuun

## Tekoäly
Tekoälyä käytettiin pohjasovelluksen tekemiseen sekä hyvien docker-compose konfiguraatioiden luomiseen.
Tämän päälle luotiin turvallisempi palvelu try/except -rakenteilla, retry-logiikalla, virheviestien lisäämisellä
tietokantarakenteeseen, tietokantayhteyksien turvallisella sulkemisella sekä yksinkertaisella rate-limiting -ratkaisulla.

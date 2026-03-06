# Tausta-ajoprosessi

Asynkroninen URL-osoitteiden käsittelyputki. API ottaa vastaan listan URL-osoitteita ja siirtää ne viestijonoon. 
Taustatyöprosessit noutavat jokaisen URL-osoitteen HTTP-tilatiedon ja tallentavat tulokset PostgreSQL-tietokantaan. 
Arkkitehtuuri hyödyntää FastAPI-kehystä rajapintakerroksessa, RabbitMQ:ta viestinvälittäjänä, Celeryä taustatehtävien 
hallinnassa ja PostgreSQL:ää pysyvänä tietovarastona.

## Käyttöönotto

Varmista, että koneellasi on Docker ja Docker Compose asennettuna.

1. Kloonaa repositorio.
2. Käynnistä palvelu komennolla:
   ```bash
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

   ```
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

# MassMailer-sovellus
Sovelluksen avulla on mahdollista kirjoittaa muuttujia sisältäviä sähköposteja, määrittää muuttujille vastaanottajakohtaisia arvoja, sekä lähettää määritellyt arvot omaavia sähköposteja.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/nualn/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/nualn/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/nualn/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Ohjelman asennus ja käynnistys
1. Asenna riippuvuudet:
```bash
poetry install
```
2. Käynnistä sovellus:
```bash
poetry run invoke start
```
Tällä hetkellä sovelluksellaa ei ole vielä käyttöliittymää ja start komennto ajaa parserin ennalta annetuilla arvoilla.

## Testaus
1. Suorita testit
```bash
poetry run invoke test
```

2. Testikattavuusraportti
```bash
poetry run invoke coverage-report
```

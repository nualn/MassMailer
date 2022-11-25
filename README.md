# MassMailer-sovellus
Sovelluksen avulla on mahdollista kirjoittaa muuttujia sisältäviä sähköposteja, määrittää muuttujille vastaanottajakohtaisia arvoja, sekä lähettää määritellyt arvot omaavia sähköposteja.

## Dokumentaatio
[Vaatimusmäärittely](https://github.com/nualn/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/nualn/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/nualn/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Sovelluksen tila
Tällä hetkellä sovelluksella on vain yksinkertainnen tekstikäyttöliittymä parsimisominaisuudelle. Sillä pystyy sijoittamaan merkkijonoon vain yhden muuttujan.

## Ohjelman asennus ja käynnistys
1. Asenna riippuvuudet:
```bash
poetry install
```
2. Käynnistä sovellus:
```bash
poetry run invoke start
```

## Testaus
1. Aja testit
```bash
poetry run invoke test
```

2. Generoi testikattavuusraportti
```bash
poetry run invoke coverage-report
```

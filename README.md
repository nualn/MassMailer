# MassMailer-sovellus
Sovelluksen avulla on mahdollista kirjoittaa muuttujia sisältäviä sähköposteja, määrittää muuttujille vastaanottajakohtaisia arvoja, sekä lähettää määritellyt arvot omaavia sähköposteja.

## Dokumentaatio
[Käyttöohje](./dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)

[Changelog](./dokumentaatio/changelog.md)

[Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](./dokumentaatio/testaus.md)

## Github release

[Viikko 5 release](https://github.com/nualn/ot-harjoitustyo/releases/tag/viikko5)

[Viikko 6 release](https://github.com/nualn/ot-harjoitustyo/releases/tag/viikko6)

## Sovelluksen tila

Käyttäjä pystyy määrittämään muuttujia sovelluksen taulukkokenttään. Ne voi sijoittaa "To"-, "Subject" ja viestikentiin valitsemalla halutun rivin taulukosta ja painamalla Preview-nappia. Sijoitus kohdat määritellään lisäämällä tekstiin sarakkeen nimi hakasulkujen sisällä, esim *[muuttuja]*. Painamalla "Send all"-nappia kaikki viestit lähetetään GmailAPI:n kautta. Viestien lähettäminen vaatii sisäänkirjautumista. Sisäänkirjautumista varten tarvitset projektin juureen Google Cloud -projektin clientID:n sisältävän tiedoston nimellä *credentials.json*. Oman projektin voit luoda [näillä ohjeilla](https://developers.google.com/workspace/guides/create-project) ja clientID:n generointiin apua saa [täältä](https://developers.google.com/gmail/api/quickstart/python#set_up_your_environment). Voidaan myös puhua itse käyttämäni clientId:n jakamisesta sähköpostilla nuutti.nikkola@helsinki.fi tai Telegramilla @nuuttin.

## Ohjelman asennus ja käynnistys
1. Asenna riippuvuudet:
```bash
poetry install
```

2. Suorita alustustoimenpiteet:

```bash
poetry run invoke build
```

3. Käynnistä sovellus:
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
## Muut komennot
1. Aja lintteri
```bash
poetry run invoke lint
```
2. Autoformatoi koodi
```bash
poetry run invoke format
```

# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella käyttäjä pystyy lähettämään vastaanottajakohtaisin tiedoin kustomoituja massasähköposteja omilla Gmail-tunnuksillaan. Tämä sisältää sähköpostiviestien kirjoittamisen, vastaanottajakohtaisten muuttujien sekä niiden arvojen määrittämisen ja sähköpostien lähettämisen.

## Käyttäjät

Sovelluksessa on vain yksi käyttäjärooli.

## Perusversion tarjoama toiminnallisuus

- [x] Käyttäjä pystyy luomaan sähköpostipohjia.
  - [x] Pohjiin voi määritellä muuttujia.
- [x] Käyttäjä pystyy lisäämään vastaanottajia
- [x] Käyttäjä pystyy määrittelemään vastaanottajakohtaisia arvoja muuttujille.
- [x] Käyttäjä pystyy esikatselemaan personoitua viestiä valitsemalleen vastaanottajalle.
- [x] Ohjelma tuottaa käyttäjäkohtaisia sähköposteja korvaamalla muuttujat vastaanottajakohtaisilla arvoilla.
- [x] Käyttäjä pystyy lähettämään sähköpostit vastaanottajille Gmail API:n kautta.
  - [x] Käyttäjä voi antaa sovellukselle oikeuden lähettää sähköposteja OAuth2 protokollalla.

## Jatkokehitysideoita

- [x] Käyttäjä pystyy lataamaan vastaanottaja-muuttuja-listoja .table-tiedostoina.
- [x] Käyttäjä pystyy tallentamaan vastaanottaja-muuttuja-listoja .table-tiedostoina.
- [x] Käyttäjä pystyy tallentamaan ja lataamaan viestipohjia tietokannasta.
- [ ] Käyttäjä voi lisätä viesteihin liitteitä.

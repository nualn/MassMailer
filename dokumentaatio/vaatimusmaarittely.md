# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella käyttäjä pystyy lähettämään vastaanottajakohtaisin tiedoin kustomoituja massasähköposteja omilla Gmail-tunnuksillaan. Tämä sisältää sähköpostiviestien kirjoittamisen, vastaanottajakohtaisten muuttujien sekä niiden arvojen määrittämisen ja sähköpostien lähettämisen.

## Käyttäjät

Sovelluksessa on vain yksi käyttäjärooli.

## Nykyisen version tarjoama toiminnallisuus

- Käyttäjä pystyy luomaan sähköpostipohjia.
  - Pohjiin voi määritellä muuttujia.
- Käyttäjä pystyy lisäämään vastaanottajia
- Käyttäjä pystyy määrittelemään vastaanottajakohtaisia arvoja muuttujille.
- Käyttäjä pystyy esikatselemaan personoitua viestiä valitsemalleen vastaanottajalle.
- Ohjelma tuottaa käyttäjäkohtaisia sähköposteja korvaamalla muuttujat vastaanottajakohtaisilla arvoilla.
- Käyttäjä pystyy lähettämään sähköpostit vastaanottajille Gmail API:n kautta.
  - Käyttäjä voi antaa sovellukselle oikeuden lähettää sähköposteja OAuth2 protokollalla.
- Käyttäjä pystyy lataamaan muuttuja-taulukoita .table-tiedostoina.
- Käyttäjä pystyy tallentamaan muuttuja-taulukoita .table-tiedostoina.
- Käyttäjä pystyy tallentamaan ja lataamaan viestipohjia tietokannasta.

## Jatkokehitysideoita
- Käyttäjä voi lisätä viesteihin liitteitä.

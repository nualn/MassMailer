# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksella käyttäjä pystyy lähettämään vastaanottajakohtaisin tiedoin kustomoituja massasähköposteja omilla Gmail-tunnuksillaan. Tämä sisältää sähköpostiviestien kirjoittamisen, vastaanottajakohtaisten muuttujien sekä niiden arvojen määrittämisen ja sähköpostien lähettämisen.

## Käyttäjät

Sovelluksessa on vain yksi käyttäjärooli.

## Perusversion tarjoama toiminnallisuus

- Käyttäjä pystyy luomaan sähköpostipohjia.
  - Pohjiin voi määritellä muuttujia.
- Käyttäjä pystyy lisäämään vastaanottajia ja määrittelemään vastaanottajakohtaisia arvoja muuttujille.
- Ohjelma tuottaa käyttäjäkohtaisia sähköposteja korvaamalla muuttujat vastaanottajakohtaisilla arvoilla.
- Käyttäjä pystyy lähettämään sähköpostit vastaanottajille Gmail API:n kautta.
  - Käyttäjä voi antaa sovellukselle oikeuden lähettää sähköposteja OAuth2 protokollalla.

## Jatkokehitysideoita

- Käyttäjä pystyy esikatselemaan personoitua viestiä valitsemalleen vastaanottajalle.
- Käyttäjä voi lisätä viesteihin liitteitä.
- Käyttäjä pystyy lataamaan ja tallentamaan vastaanottaja-muuttuja-listoja CSV-tiedostoina.
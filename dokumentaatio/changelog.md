## Viikko 3
- Lisätty Parser-luokka joka vastaa muuttujien sijoittamisesta merkkijonoon.
- Lisätty testit Parser-luokalle
- Lisätty yksinkertainen tekstikäyttöliittymä parsimisominaisuudelle

## Viikko 4
- Muokattu Parser-luokan toimintaa
- Lisätty State-luokka, jossa pidetään kirjaa sovelluksen tilasta
- Lisätty GUI:n ensimmäinen versio
  - Lisätty luokka Tbl, joka pitää kirjaa käyttäjän lisäämistä muuttujariveisä
  - Lisätty luokka UI, jolla käyttäjä voi luoda viestin, luoda muuttujia ja esikatsella parsittua viestiä.
  - Refaktoroitu UI luokiksi Message_field ja Preview

## Viikko 5
- Käyttäjä voi kirjautua oauth2-protokollalla gmail-tililleen.
- Käyttäjä voi lähettää massasähköposteja.
- Lisätty luokat Authorizer, GmailService, App sekä Loginout.
- Luokka Tbl:in toteutus vaihdettu käyttämään tkintertable-kirjastoa 

## Viikko 6
- Käyttäjä voi tallentaa ja ladata viestejä tietokannasta
  - Lisätty luokka MessageRepository
  - Lisätty UI luokka Selector, joka toteuttaa dropdown menun
  - UI:hin lisätty valitsin sekä save- ja load-napit viestine tietokantaan talentamiseen ja sieltä lataamiseen.

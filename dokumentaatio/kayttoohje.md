# Käyttöohje

TODO: Lisää kuvankaappauksia

Lataa projektin viimeisimmän [releasen](https://github.com/nualn/ot-harjoitustyo/releases) lähdekoodi.

## Konfigurointi
Jos haluaa lähettää sovelluksella sähköpostia, tulee siihen kirjautua Google-käyttäjällä. Sisäänkirjautumista varten tarvitset projektin juureen Google Cloud -projektin clientID:n sisältävän tiedoston nimellä *credentials.json*. Oman projektin voit luoda [näillä ohjeilla](https://developers.google.com/workspace/guides/create-project) ja clientID:n generointiin apua saa [täältä](https://developers.google.com/identity/protocols/oauth2/native-app#creatingcred). Voidaan myös puhua itse käyttämäni clientId:n jakamisesta sähköpostilla nuutti.nikkola@helsinki.fi tai Telegramilla @nuuttin.

Viestipohjien tallennukseen käytettävän tietokannan nimeä voi halutessaan muuttaa tiedostossa src/config.py muokkaamalla muuttujaa DB_FILE_NAME.

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

## Sisäänkirjautuminen

Sovelluksen käyttöliitymässä on Login-nappi, jota painamalla käyttäjä voi autentikoitua Gmail-tililleen. Riippuen siitä, onko sovelluksessa tallessa voimassaoleva Oauth-token, avataan selainikkuna, jossa käyttäjä voi kirjautua Gmail-tililleen tai sitten käyttäjä kirjataan suoraan sisään. Tämä toiminnallisuus vaatii sekä Googlen sovellus-id:n sisältävän 'credentials.json' tiedoston että sen, että käyttäjän sähköposti on lisätty Googlen Cloud Consoleen testaajien listalle.


## Sähköpostien lähetys

Painamalla ikkunan alareunassa olevaa "Send all"-nappia voi lähettää massasähköposteja. Tämä toiminnallisuus vaatii, että käyttäjä on kirjautunut sisään.


## Viestipohjien tallentaminen tietokantaan

Viestipohja tallennetaan tietokantaan UI:n Save-nappulaa painamalla. Viereisestä valikosta voi myös valita tallennetaanko uusi viesti vai päivitetäänkö jo olemassa olevaa viestiä.


## Viestipohjien lataaminen tietokannasta

Viestipohja ladataan tietokannasta UI:n Load-nappulaa painamalla. Viereisestä valikosta voi valita, mikä viesti halutaan ladata.


## Viestin esikatselu

Muuttujataulukosta tällä hetkellä valittuna olevan rivin muuttujat sisältävää viestiä voi esikatsella UI:n Preview-nappulaa painamalla.


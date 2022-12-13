## Class diagram
```mermaid
classDiagram

GUI "1"--"1" Parser
GUI "1"--"1" App
App "1"--"1" Parser
App "1"--"1" Authorizer
App "1"--"1" GmailService
App "1"--"1" MessageRepository

```
## Folder diagram
```mermaid
graph TD

A[app.py] --> B[ui]
A --> C[parser]

B --> D[message_field.py]
B --> E[preview.py]
B --> F[selector.py]

C --> G[parser.py]

``` 

## Päätoiminnallisuudet

Tässä osiossa kuvataan sovelluksen päätoiminnallisuudet sekvenssikaavioiden avulla.

### Sisäänkirjautuminen

Sovelluksen käyttöliitymässä on Login-nappi, jota painamalla käyttäjä voi autentikoitua Gmail-tililleen. Riippuen siitä, onko sovelluksessa tallessa voimassaoleva Oauth-token, avataan selainikkuna, jossa käyttäjä voi kirjautua Gmail-tililleen tai sitten käyttäjä kirjataan suoraan sisään. Tämä toiminnallisuus vaatii sekä Googlen sovellus-id:n sisältävän 'credentials.json' tiedoston että sen, että käyttäjän sähköposti on lisätty Googlen Cloud Consoleen testaajien listalle.

```mermaid  
sequenceDiagram

actor User

User ->> UI: click "Login" button
UI ->> App: login()
App ->> Authorizer: login()
App ->> Authorizer: get_credentials()
Authorizer -->> App: credentials
App ->> GmailService: build(credentials)
App ->> GmailService: get_email()
GmailService -->> App: email
App ->> UI: email

``` 
### Sähköpostien lähetys

Käyttäjä voi lähettää massasähköposteja. Tämä toiminnallisuus vaatii, että käyttäjä on kirjautunut sisään.

```mermaid
sequenceDiagram

actor User

User ->> UI: click "Send all" button
UI ->> App: send_all(message, rows)
loop For every row
  App ->> Parser: parse(email, row)
  Parser -->> App: parsed_email
  App ->> Parser: parse(subject, row)
  Parser -->> App: parsed_subject
  App ->> Parser: parse(body, row)
  Parser -->> App: parsed_body
  App ->> GmailService: send(parsed_email, parsed_subject, parsed_body)
end

```

### Viestien tallentaminen tietokantaan

Käyttäjä voi tallentaa viestin tietokantaan UI:n Save-nappulaa painamalla. Viereisestä valikosta voi myös valita tallennetaanko uusi viesti vai päivitetäänkö jo olemassa olevaa viestiä.

```mermaid
sequenceDiagram

actor User

User ->> UI: click "Save" button
UI ->> App: save_message(message)
App ->> MessageRepository: create(to, subject, body)
```
### Viestien lataaminen tietokannasta

Käyttäjä voi ladata viestin tietokannasta UI:n Load-nappulaa painamalla. Viereisestä valikosta voi valita, mikä viesti halutaan ladata.

```mermaid
sequenceDiagram

actor User

User ->> UI: click "Load" button
UI ->> App: load_message(id)
App ->> MessageRepository: get_by_id(id)
MessageRepository -->> App: loaded_message
App -->> UI: loaded_message
UI ->> UI: set_message(loaded_message)

```

### Viestin esikatselu

Käyttäjä voi esikatsella valitsemansa rivin muuttujat sisältävää viestiä UI:n Preview-nappulaa painamalla.

```mermaid
sequenceDiagram

actor User

User ->> UI: click "Preview" button
UI ->> Parser: parse(message, rows)
Parser -->> UI: parsed_message
UI ->> UI: set_preview(parsed_message)

```
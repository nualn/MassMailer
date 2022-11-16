
```mermaid
 classDiagram
      Peli "1"--"2..8" Pelaaja
      Peli "1"--"2" Noppa
      Peli "1"--"1" Pelilauta
      Ruutu "40" -- "1" Pelilauta
      Ruutu "1"--"1" Ruutu
      Pelaaja "1"--"1" Pelinappula
      Pelinappula "0..1"--"1" Ruutu

      Class Peli
      Class Noppa
      class Pelaaja
      class Pelilauta
      class Ruutu
      Class Pelinappula
```

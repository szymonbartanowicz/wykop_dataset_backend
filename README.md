## Info
Backend wyszukiwarki napisany w FastAPI, korzystający z silnika wyszukiwań Solr. Aplikacja operuje na zbiorze danych zawierającym ponad 100 tysięcy dokumentów będącym reprezentacją postów w serwisie wykop.pl.
## Funkcjonalności

- Wyszukiwanie rozmyte
- Różne wagi dla pól tekstowych
- Obsługa filtrów (contains, equals, greater than, less than)
- Paginacja
- Sortowanie
- Możliwość dostosowania zwracanych kolumn
- Snippety z pogrubionymi fragmentami tekstu pasującymi do frazy szukającej
- Filtrowanie fasetowe
## Instalacja
1. **Sklonowanie projektu**:
   ```
   git clone https://github.com/szymonbartanowicz/wykop_dataset_backend.git
2. Wejście do projektu:
   ``` 
   cd wykop_dataset_backend 
   ```
3. **Ustawienie zmiennych środowiskowych**:
   ```
   cp .env.example .env
   ```
   Możliwość ustawienia portów dla backendu oraz Solr oraz ustawienia nazwy kolekcji Solr. Domyślnie plik **.env.example** uzupełniony.


4. **Uruchomienie aplikacji**:
   ```
   docker compose up
   ```
   Ta komenda uruchomi kontenery dla FastApi oraz Solr. Z pliku **wykop_dataset.csv** zostanie utworzona kolekcja Solr. Włączone zostanie też odświeżanie w tle.
## Dokumentacja
http://localhost:8000/docs \
Powyższy link może się różnić w zależności od ustawionego portu dla backendu.
## Testy
    docker-compose exec backend pytest

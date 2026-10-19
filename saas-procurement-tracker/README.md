# SaaS Procurement Tracker

## Starten

1. Pak de ZIP uit.
2. Open de uitgepakte map in Opdrachtprompt of PowerShell.
3. Voer uit: `python app.py`
4. De tracker opent automatisch in de browser.

De applicatie gebruikt alleen de Python-standaardbibliotheek. Er zijn geen externe packages nodig.
Gegevens worden automatisch in de lokale browseropslag bewaard. Via de knoppen bovenaan kunnen gegevens als JSON worden geëxporteerd en opnieuw geïmporteerd.

## Mappen

- `app.py`: lokale Python-webserver
- `templates/index.html`: pagina-opbouw
- `static/css/style.css`: vormgeving en responsive ontwerp
- `static/js/app.js`: trackerlogica, autosave en JSON-import/export
- `static/icons/`: losse fase-iconen
- `data/projects.json`: voorbeeld/seed voor toekomstige serveropslag
- `exports/`: map voor handmatig opgeslagen exports

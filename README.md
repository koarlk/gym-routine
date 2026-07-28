# Gym Tracker

Kleine Web-App zum Mitschreiben von Krafttraining: Maschine, Gewicht, Wiederholungen.
Optimiert fuer das iPhone, laeuft nach dem ersten Aufruf offline.

## Funktionen

- Saetze erfassen mit +/- Tasten (±2,5 kg / ±1 Wdh.)
- Vorbelegung mit den letzten Werten der jeweiligen Uebung, Anzeige der Bestleistung
- Verlauf nach Trainingstagen, gruppiert nach Uebung
- Statistik je Uebung inkl. persoenlicher Bestleistung
- Export/Import der Daten als JSON

## Datenhaltung

Alle Trainingsdaten liegen ausschliesslich im `localStorage` des jeweiligen Browsers.
Es gibt keinen Server, kein Konto und keine Synchronisierung zwischen Geraeten.
Zum Umzug auf ein anderes Geraet dient der Export unter *Statistik → Daten exportieren*.

## Auf dem iPhone installieren

Seite in Safari oeffnen, dann *Teilen → Zum Home-Bildschirm*.
Danach startet sie im Vollbild und funktioniert ohne Netz.

## Lokal starten

```bash
python3 serve.py
```

Zeigt eine Adresse an, die im selben WLAN auch vom Handy erreichbar ist.

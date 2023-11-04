# Pythonunterlagen für EMS - Gruppe Energiesysteme und Netzsimulation

Dieses Repository sammelt einige Notebooks und Python Files. Diese Behandeln
unterschiedliche Bereiche der Datenakquisition und Modellierung von Energiesystemen
sowie Energienetzen. Die Notebooks beinhalten Erklärungen und Best Practices und 
werden während des Semesters nach Bedarf ergänzt und erweitert.

Das Repository kann nach Installation von git mit dem Befehl

```bash
git clone https://github.com/skloibhofer/fh-pandapower-cosimulation.git
```

heruntergeladen werden. Im Notebook *00_prerequisites.ipynb* wird noch detaillierter
auf die Verwendung von Versionskontrolle, die Installation von Python und einer
Programmieroberfläche und das allgemeine Setup eingegangen. Die weiteren Notebooks
beinhalten Python Code und Erklärungen.

## LV-Überblick

Geplanter Inhalt der Übung zur Simulation von Strom-Netzen, -Erzeugung oder -Verbrauch mit Python.

* Setup
    * Versionskontrolle
    * Pythoninstallation und Packages
    * Programmieroberfläche

* Entwickeln einzelner Komponenten, Auffrischen Python Basics
    * Standardlastprofile: Arbeiten mit Zeitreihen und Funktionen
    * Batterie: Aufbau einer Klasse
    * PV: Verwenden einer externen Library 

* Stromnetzsimulation mit pandapower
    * Aufbau eines Netzes aus Grundkomponenten
    * Power Flow Berechnung und Resultate
    * Verwenden von Beispielnetzen
    * Kombination mit eigenen Profilen und zeitliche Entwicklung des Power Flows

Weitere Themen sind PowerFactory (wird nicht in diesem Repository behandelt), danach
die Projektfindung und Durchführung in Kleingruppen. Je nach Bedarf behandeln wir
dann auch noch weitere Themen gemeinsam, diese werden dann auch hier hinzugefügt.
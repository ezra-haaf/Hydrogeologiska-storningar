Stödverktyg & rutiner
=====================

Denna sida samlar de viktigaste verktygen och arbetsstegen för att förberade data och
komma igång med analyser av hydrogeologiska störningar i undermarksbebeyggelse. 
Fokus på denna sida ligger på stödverktyg: förberedning av grundvattennivådata, 
kompensation med barodata, import av klimatdata från SMHIs öppna data, modllering
av avdunstning, introduktion till Impuls-Respons modellering i Pastas, 
som är viktigt verktyget för tidsserieanalys i projektet, samt kalibreringsrutiner.

Databeredning av vanlig input data
-------------------------------------------

Här finns notebooks som visar hur data kan förberedas för användning i tidsserieanalys.

.. nbgallery::
   :caption: Databehandling 

   examples/kompensation
   examples/nederbord
   examples/missforest-gapfilling


Pastas basics
---------------
Pastas är ett bibliotek för tidsserieanalys av hydrogeologiska data, och är huvudverktyget som användes i projektet.

Sidorna är kopierade från Pastas officiella dokumentation, och är avsedda att ge en praktisk introduktion till de metoder som rekommenderas baserat på projektet för identifikation av orsaker till hydrogeologiska störningar i undermarksbebeyggelse.
Fler exempel kan hittas här: https://pastas.readthedocs.io/en/latest/examples/index.html

.. nbgallery::
   :caption: Dessa workbooks ger en praktisk introduktion till Python biblioteket *Pastas*. 

   examples/preprocessing
   examples/model_primer



Kommentar
---------

Om du vill ha en mer generell översikt över externa paket, datakällor och andra
resurser som kan användas tillsammans med handledningen, se
`Resurskatalog <resurskatalog.html>`_.
Resurskatalog
=============

Här samlas relevanta kodpaket, verktyg och datakällor som kan användas som stöd i
handledningens arbetsflöden. Katalogen är tänkt som en praktisk startpunkt för
den som vill hitta befintliga resurser för tidsserieanalys, referensjämförelser,
gapfyllning och grundvattenrelaterade observationsdata.

Kodpaket och verktyg
--------------------

`ARCHI <https://code.usgs.gov/water/ARCHI>`_
   Ett paket för automatiserad regional korrelationsanalys och imputering av
   hydrologiska tidsserier. Det är särskilt relevant när grundvattendata har
   luckor eller oregelbunden provtagningsfrekvens och man vill använda
   referensstationer för att fylla eller komplettera serier.

   **Typ:** Paket/verktyg

   **Programspråk:** R

   **Praktisk användning:** Kan fungera som referens för arbetsflöden kring
   gapfyllning, stationsurval och regional jämförelse av tidsserier.

`gwrefpy <https://github.com/sgfsweden/gwrefpy>`_
   Ett Python-paket för att koppla observationsbrunnar till referensbrunnar och
   analysera avvikelser i grundvattentidsserier. Paketet är användbart för
   övervakning, kvalitetskontroll och för att identifiera när en observerad serie
   börjar avvika från ett förväntat regionalt beteende.

   **Typ:** Paket

   **Programspråk:** Python

   **Praktisk användning:** Passar väl i arbetsflöden där man vill jämföra
   observationsserier mot referensserier som stöd för tolkning av störningar.

Datakällor
----------


`SGU: Grundvattennivåer, mätstationer <https://www.sgu.se/grundvatten/grundvattennivaer/matstationer/>`_
   SGU:s tjänst för uppmätta grundvattennivåer från mätstationer som myndigheten
   ansvarar för eller använder inom miljöövervakningen. Tjänsten ger tillgång
   till stationsinformation, interaktiva diagram och nedladdningsbara mätdata.

   **Typ:** Datatjänst

   **Geografisk täckning:** Sverige

   **Praktisk användning:** Bra som nationell referenskälla för observationer,
   bakgrundsdata och jämförelser mot lokala mätserier.

`EDGE-1 på OSF <https://osf.io/skxg5/overview>`_
   Ett harmoniserat dataset med kvalitetssäkrade tidsserier av
   grundvattennivåer från flera europeiska länder, bland annat Sverige. Resursen
   är framtagen för hydrologiska analyser och studier av grundvattentorka och kan
   också vara relevant som jämförelsematerial i metodutveckling och testning.

   **Typ:** Dataset

   **Geografisk täckning:** Sverige, flera europeiska länder

   **Praktisk användning:** Lämpligt som referenskälla för grundvattentidsserier. Observera 
   att det inte är en komplett nationell databas, utan ett urval av kvalitetsgranskade serier
   som är interpolerade till dygnsdata från 1990 - 2023.

Litteratur
-----------
Referensgranskade artiklar och publikationer som är relevanta för metoderna och arbetsflödena
^^^^^^^^^^^

`2022 - Data-Driven Estimation of Groundwater Level Time-Series at Unmonitored Sites Using Comparative Regional Analysis <https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022WR033470>`_
   Artikeln presenterar en data-driven metod för att uppskatta dagliga
   grundvattennivaserier vid prognosbrunnar genom komparativ regional analys och
   referensbrunnar. Metoden kombinerar kummulativa nivåer med regionala
   hydrogeologiska och klimatiska platsegenskaper och visar hur modellval samt urval av
   referensbrunnar påverkar prediktionskvaliteten.

`2023 - Assessing automated gap imputation of regional scale groundwater level data sets with typical gap patterns <https://www.sciencedirect.com/science/article/pii/S0022169423003669>`_
   Studien introducerar ett realistiskt upplägg for utvärdering av luckfyllning i
   grundvattentidsserier genom vanliga mönster av luckor i tidsserier i stället for enbart
   slumpade luckor. Resultaten visar att MissForest presterar battre an linjär
   interpolation och imputePCA for längre sammanhangande luckor, men att extrema
   händelser och mänsklig aktivitet fortsatt ar svara att fylla i på ett robust sätt.

`2024 - Data-driven modelling of hydraulic-head time series: results and lessons learned from the 2022 Groundwater Time Series Modelling Challenge <https://hess.copernicus.org/articles/28/5193/2024/hess-28-5193-2024.html>`_
   Artikeln sammanfattar resultat fran en internationell modelleringsutmaning dar
   flera team jamforde lumped-parameter-modeller, maskininlarning och djupinlarning
   for grundvattennivåmätserier. En central slutsats ar att ingen enskild
   modelltyp ar bäst i alla fall, och att modellörens metodval, feature engineering
   och osakerhetsuppskattning har stor inverkan pa slutprestandan.

`2025 - Quantification and Analysis of Hydrograph Behavior Using Groundwater Signatures <https://ngwa.onlinelibrary.wiley.com/doi/full/10.1111/gwat.13486>`_
   Artikeln introducerar en signatures-modul i Pastas for att kvantifiera
   grundvattendynamik med standardiserade nyckeltal for exempelvis klustring,
   forändringsdetektion och modellutvärdering. Genom praktiska exempel visas hur
   signaturer kan anvandas till exempel for att att välja
   modellstruktur utifran observerad grundvattendynamik.

Övriga relevanta publikationer
^^^^^^^^^^^

`2024 - SGF Rapport 2024:2 Akvifärs referensmetod <https://svenskageotekniskaforeningen.se/wp-content/uploads/Publikationer/SGF_Rapporter/2024_2_Akvifars_refmetod.pdf>`_
   Metodrapport som beskriver en referensmetod för regressionsbaserad beskrivning av ostörda 
   grundvattenförhållanden i ett prognosrör. Metoden är avsedd att användas som stöd i 
   bedömning av påverkan grundvattenförhållanden i samband med byggprojekt. 
   Metoden är implementerat i :ref:`verktyget gwrefpy <gwrefpy>
   



Avgränsning
-----------

Katalogen är avsiktligt kort och fokuserar på resurser som är direkt relevanta
för att genomföra analys av störningar i grundvattentidsserier, referensjämförelser 
och hydrogeologisk analys. 
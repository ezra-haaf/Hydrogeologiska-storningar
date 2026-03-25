Förbättra underlag för Larmnivåer och Extremvärdesanalys
========================================================

För att undvika beroende av uppmätt data från enskilda mätpunkter, eller referensstationer
med låg tillförlitlighet, föreslås att använda modellerade grundvattennivåer som underlag för larmnivåer och extremvärdesanalys.

Nedan hittas stegen för att åstadkomma detta, inklusive datakällor och modelleringsverktyg.

.. mermaid::

   flowchart TD
   GWOBS["Bearbetning av Grundvattennivå observationer"]
   KLIMAT["Hämta klimatdata"]
   AVD["Avdunstningsmodellering"]
   GWMOD["Grundvattenmodellering"]
   HIST["Historisk rekonstruktion"]
   NED["Nederbörd"]
   TEMP["Temperatur"]

   KLIMAT --> AVD
   GWOBS --> GWMOD
   AVD --> GWMOD
   GWMOD --> HIST

   KLIMAT -.-> NED
   KLIMAT -.-> TEMP

   click GWOBS "../examples/kompensation.nblink" "Öppna kompensation"
   click KLIMAT "../examples/klimatdata.nblink" "Öppna klimatdata"
   click NED "../examples/nederbord.nblink" "Öppna nederbörd"
   click TEMP "../examples/temperatur.nblink" "Öppna temperatur"
   click AVD "../examples/avdunstning.nblink" "Öppna avdunstning"
   click GWMOD "../examples/kalibrering.nblink" "Öppna kalibrering"
   click HIST "../examples/hindcasting.nblink" "Öppna hindcasting"
       
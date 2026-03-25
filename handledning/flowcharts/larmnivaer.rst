Förbättra underlag för Larmnivåer och Extremvärdesanalys
========================================================

För att undvika beroende av uppmätt data från enskilda mätpunkter, eller referensstationer
med låg tillförlitlighet, föreslås att använda modellerade grundvattennivåer som underlag för larmnivåer och extremvärdesanalys.

Nedan hittas stegen för att åstadkomma detta, inklusive datakällor och modelleringsverktyg.

.. mermaid::
   %%{init: {'theme':'forest'}}%% 
   flowchart TD
   GWOBS["Bearbetning av Grundvattennivå observationer"]
   KLIMAT["Hämta klimatdata"]
   AVD["Avdunstningsmodellering"]
   GWMOD["Grundvattenmodellering"]
   PL[""]
   HIST["Historisk rekonstruktion"]
   NED["Nederbörd"]
   TEMP["Temperatur"]

   KLIMAT --> AVD
   GWOBS -- PL
   PL --> GWMOD
   AVD --> GWMOD
   GWMOD --> HIST

   KLIMAT -.-> NED
   KLIMAT -.-> TEMP

   click GWOBS "../examples/kompensation.html" "Öppna kompensation"
   click KLIMAT "../examples/klimatdata.html" "Öppna klimatdata"
   click NED "../examples/nederbord.html" "Öppna nederbörd"
   click TEMP "../examples/temperatur.html" "Öppna temperatur"
   click AVD "../examples/avdunstning.html" "Öppna avdunstning"
   click GWMOD "../examples/kalibrering.html" "Öppna kalibrering"
   click HIST "../examples/hindcasting.html" "Öppna hindcasting"
       
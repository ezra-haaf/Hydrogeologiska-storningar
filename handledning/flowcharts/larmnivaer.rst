Förbättra underlag för Larmnivåer och Extremvärdesanalys
========================================================

För att undvika beroende av uppmätt data från enskilda mätpunkter, eller referensstationer
med låg tillförlitlighet, föreslås att använda modellerade grundvattennivåer. Modellen kan sedan 
användas för att rekonstruera historiska nivåer baserat på historisk klimatdata, och därmed ge 
ett mer robust underlag för larmnivåer och extremvärdesanalys.

Nedan hittas stegen för att åstadkomma detta, inklusive datakällor och modelleringsverktyg. 

*(Klicka på lådorna för att komma till relevanta skripter.)*



.. graphviz::

   digraph G {
     rankdir=LR;
     splines=ortho;
     node [shape=box, style="rounded,filled", fillcolor="#e8f3e8", penwidth=0];

     GWMAT [label="Mätning av\nGrundvattennivåer"]; 
     GWOBS [label="Bearbetning av\nGrundvattennivå observationer", URL="../examples/kompensation.html", target="_top"];
     KLIMAT [label="Hämta klimatdata", URL="../examples/klimatdata.html", target="_top"];
     AVD    [label="Avdunstningsmodellering", URL="../examples/avdunstning.html", target="_top"];
     GWMOD  [label="Grundvattenmodellering", URL="../examples/kalibrering.html", target="_top"];
     HIST   [label="Historisk rekonstruktion", URL="../examples/hindcasting.html", target="_top"];
     NED    [label="Nederbörd", URL="../examples/nederbord.html", target="_top"];
     TEMP   [label="Temperatur", URL="../examples/temperatur.html", target="_top"];


     KLIMAT -> AVD;
     GWMAT -> GWOBS;
     GWOBS -> GWMOD;
     AVD -> GWMOD;
     GWMOD -> HIST;
     KLIMAT -> NED;
     NED -> GWMOD;
     KLIMAT -> TEMP;
     TEMP -> GWMOD;
   }
       
Identifiera och spåra störningar 
================================

Nedan hittas ett beslutsträd som guidar användaren genom processen att bygga en modell för  att 
1) identifiera om en tidsserie är störd.  
2) testa olika störningskällor och identifiera den mest sannolika orsaken till störningen.

*(Klicka på lådorna för att komma till relevanta skripter.)*






.. graphviz::

   digraph G {
     rankdir=TD;
     splines=ortho;
     node [shape=box, style="rounded,filled", fillcolor="#e8f3e8", penwidth=0];

     GWMAT [label="Mätning av\nGrundvattennivåer"]; 
     GWOBS [label="Bearbetning av\nGrundvattennivå observationer"];
     KLIMAT [label="Hämta klimatdata", URL="../examples/klimatdata.html", target="_top"];
     AVD    [label="Avdunstningsmodellering", URL="../examples/avdunstning.html", target="_top"];
     GWMOD  [label="Grundvattenmodellering", URL="../examples/tunnel1_gbg.html", target="_top"];
     ADD1   [label="Tillägg av störningsserier", URL="../examples/tunnel2_gbg.html", target="_top"];
     NED    [label="Nederbörd", URL="../examples/nederbord.html", target="_top"];
     TEMP   [label="Temperatur", URL="../examples/temperatur.html", target="_top"];


     KLIMAT -> AVD;
     GWMAT -> GWOBS;
     GWOBS -> GWMOD;
     AVD -> GWMOD;
     GWMOD -> ADD1;
     KLIMAT -> NED;
     NED -> GWMOD;
     KLIMAT -> TEMP;
     TEMP -> GWMOD;
   }
       
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
     node [shape=box, style="rounded,filled", fillcolor="#e8f3e8", penwidth=0, fontname="Helvetica"];

     GWMAT [label="Insamling av\nGrundvattennivåer"]; 
      
     KLIMAT [label="Insamling av klimatdata", URL="../examples/klimatdata.html", target="_top", width=4];
     STOR [label="Insamling av störningsdata"];
     #STOBS [label="Bearbetning av\nstörningsdata"];
     #AVD    [label="Avdunstningsmodellering", URL="../examples/avdunstning.html", target="_top"];
     GWMOD  [label="Grundvattenmodellering", URL="../examples/tunnel1_gbg.html", target="_top",width=5.5];
     DECIDE1 [label="Residualer \nnormalföredelade", shape=diamond, fill="#fff4cc"];
     DECIDE2 [label="Residualer \nnormalföredelade", shape=diamond, fill="#fff4cc", URL="../examples/tunnel3_gbg.html"];
     ADD1   [label="Grundvattenmodellering med störningsserier", URL="../examples/tunnel2_gbg.html", target="_top", width=4];
     NED    [label="Nederbörd", URL="../examples/nederbord.html", target="_top"];
     TEMP   [label="Temperatur", URL="../examples/temperatur.html", target="_top"];
     FIN [label="Slutgiltig modell", shape=ellipse, fillcolor="#d1e7dd", width=3];
     { rank=same; GWMAT; KLIMAT; STOR; }
      

     subgraph cluster_processing {
         label="Bearbetning/förädling";
         style="filled,rounded";
         color="grey95";
         fontname="Helvetica-Bold"

         GWOBS [label="Bearbetning av\nGrundvattennivå observationer", fillcolor="white", URL="../examples/kompensation.html"];
         STOBS [label="Bearbetning av\nstörningsdata", fillcolor="white", URL="../examples/prepare_leakage.html", target="_top"];
         AVD [label="Avdunstningsmodellering", fillcolor="white", URL="../examples/avdunstning.html", target="_top"];
         { rank=same; GWOBS; STOBS; AVD}
     }

     KLIMAT -> AVD;
     GWMAT -> GWOBS [lhead=cluster_processing];
     GWOBS -> GWMOD;
     NED -> AVD;
     TEMP -> AVD;
     AVD -> GWMOD;
     GWMOD -> DECIDE1;
     DECIDE1 -> ADD1 [label="Nej", labelfloat=true, fontname="Helvetica-Oblique"];
     DECIDE1 -> FIN [label="Ja", fontname="Helvetica-Oblique"];
     KLIMAT -> NED;
     NED -> GWMOD;
     KLIMAT -> TEMP;
     TEMP -> GWMOD;
     STOR -> STOBS;
     STOBS -> ADD1;
     ADD1 -> DECIDE2; 
     DECIDE2 -> FIN [label="Ja", fontname="Helvetica-Oblique"];  
     DECIDE2 -> STOR [label="Nej", fontname="Helvetica-Oblique"];
   }
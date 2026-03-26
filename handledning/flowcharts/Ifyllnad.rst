Fylla i luckor i tidsserier
===========================

I många undermarksprojekt finns utmaningar med ofullständiga tidsserier, där det kan finnas luckor 
i data på grund av mätfel, underhåll eller andra störningar. Att fylla i dessa luckor på ett robust 
sätt är avgörande för att kunna genomföra meningsfulla analyser. Genom att modellera grundvattennivå-
tidsserier med Pastas kan enstaka tidsserier fyllas i och förlängas, se tex :doc:`Larmnivåer <larmnivaer>`. 
Att modellera många tidsserier med Pastas kan dock vara tidskrävande, och i vissa fall kan det vara mer 
effektivt att använda maskininlärning för att fylla i luckor på många tidsserier samtidigt. 

Nedan hittas ett beslutsträd som guidar användaren genom processen att välja lämpliga metoder för 
ifyllnad av data, baserat på datamängd, mönster i data och analysmål.  

*(Klicka på lådorna för att komma till relevanta skripter.)*



.. graphviz::

   digraph G {
     rankdir=TB;
     splines=ortho;
     nodesep=0.4;
     ranksep=0.5;

     node [fontname="Helvetica", fillcolor="#f3f1e8", fontsize=11, penwidth=0];
     edge [fontname="Helvetica", fontsize=10, color="#555555"];

     // Shapes/styles
     Start [label="Data set", shape=box, style="rounded,filled", fillcolor="#f3f1e8"];
     D1 [label="Referensdata tillgänglig?", shape=diamond, style="filled", fillcolor="#fff4cc"];
     D2 [label="Referenstidsserier har data\ndär luckor finns?", shape=diamond, style="filled", fillcolor="#fff4cc"];
     D3 [label="God passning\n(per rör)?", shape=diamond, style="filled", fillcolor="#fff4cc"];

     Mass [label="Kör masshantering", shape=box, style="rounded,filled", fillcolor="#e8f3e8",
           URL="../examples/ifyllnad_mf_cv.html", target="_top"];

     Pastas [label="Kalibrering med\nPastas per rör", shape=box, style="rounded,filled", fillcolor="#e8f3e8",
             URL="../examples/kalibrering.html", target="_top"];

     End [label="Klart", shape=box, style="rounded,filled", fillcolor="#d9ead3"];

     // Flow
     Start -> D1;

     D1 -> D2 [label="Ja"];
     D1 -> Pastas [label="Nej"];

     D2 -> Mass [label="Ja"];
     D2 -> Pastas [label="Nej"];

     Mass -> D3;

     D3 -> End [label="Ja"];
     D3 -> Pastas [label="Nej"];

     Pastas -> End;
   }
       
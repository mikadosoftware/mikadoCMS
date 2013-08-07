

Experience at BUPA
------------------

A hypothetical company

105M dollars to produce 6M lines of Java code for a huge ERP-style backend
doing websites, customer service etc.  It has taken years, been through 2 CEOs 4 CIOs 7 major consultancies.  Its not uncommon, but it is a mess.

So, we review the code - and we find a lot of duplication.

Because no unit testing, and the horrors of bad releases, testing is really stringertn, really manual and really long

So refactoring some code in the core is almost impossible - so the core code is copioed and put into new features - a lot.

We run some software metrics - and here is an easy one. Code similarity.
http://www.ics.heacademy.ac.uk/resources/assessment/plagiarism/detectiontools_sourcecode.html or maybe somehting like http://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm

Anyway we discover that 25 % (yes, this is not that unusual, especially in a big enterprisey shop with lots of boilerplate code and tools - hello eclipse)
of the code is "similar" - that is if you handed both pieces of code to the Professor in class, one of you would be in trouble for plagarism.

OK, what that means is roughly we could have lopped off 1/4 of the Lines Of Code and made the code smaller.  So we could have saved ourselves 25m dollars - right?

Well, no - lines of code is a linear measure - but complexity is exponential - the more code, the more connections, the more pathways to test, the more bugs to fix and so on, the more to hold in ones head.

So ...

::

    C = Cost
    L = linesOfcode

    L ^ n = C

    6m ^ n = 100m

    n = 2.6 (isn't it nice how my hypothetical company's figures work out)

    L^2.6 = C

    If there are L/1.35 lines, how much would it have cost?

    C' = (L/1.35)^n
    C' = L^n / 1.35^n
    C' = C / 1.35^n   (C=L^n remember?)

    So if we had just allowed ourselves refactoring instead of copy paste...

    C' = 105 / 1.35^2.6
    C' = 48M

    So by simply introducing refactoring (the most basic quality improvement)
    how hypothetical but not unusual company would have saved 50M dollars.

    And can you swear to me that everyone of those 4.5M remaining lines of 
    code need to be there? If you take an extreme view of piss poor code bases 
    (I could replace this with 10 perl scripts and 100 lines of Prolog) we could assume a 6M line code base could drop to 1.5M lines - still huge but if someone said you were running a 5 year project to write a major corps core services in 1.5M lines no onw would blink.


    C' = (L/4)^n
    C' = L^n / 4^n
    C' = C / 4^n   (C=L^n remember?)


    C' = 105 / 4^2.6
    C' = 2.85M
        
    Holy crap!  A 100M dollar project that produces 6M lines of interacting code now should cost 2.8M!!!


    There is a big big assumption in here - that every line of code is like 
    an atom in a radioactive lump of plutonium.  

    It may not be a safe assumption - but by god it rocks some serious concerning figures.

    It really is down to number of interacting pieces - if every ten lines 
    is a decayable lump we really only have 10M lines of code.
    Everything else stays the same

    You can measure average function length - then ability to RPC.  


    
How do you spend 100M dollars?
------------------------------

A consultant on 1000 USD a day => 200,000 pa
ten consultants => 2M pa
for five years. 10M

Now thats just ten guys.  What about a project manager, a couple of testers, office space, and the cost of brining in the deputy head of sales to make sure the damn thing does what we want...

Now bring in 100 consultants for a major project - yeah baby lets ramp it up a bit.  Ooops 100M spent - but hey this is core to our business.  


You see, I am lucky - I get paid to write open source software.  For a
university, in Texas.

.. figure:: https://mw2.google.com/mw-panoramio/photos/medium/12149191.jpg
     :width: 250 px
     :height: 140 px

     This one.

Which is actually a great job, but that's not the point.  The point is I
realised that people thousands of miles away were savvy enough to want Open
Source Software built for them, but my local council *on the same road as my
office* was not.

.. figure:: /assets/images/gibsondrive.jpg

       This road. The rainy one.

Do you know there is a list describing everything government is supposed to do?
Its called the `Local Government Service Listing
<http://standards.esd.org.uk>`_, and its got everything in it, from Fire Brigade
Training to Council Tax Collection and Planning Applications.

In all, over 2100 services, and every single one is going to become digital, and
rely on someone to write their software.

And how many of those will use Open Source software?  Good Question.


Ok, so what is this Open Source Software?
-----------------------------------------

Its pretty simple, honest. You write a book for your little boy about pirates
and otters. You just print it on your inkjet and then you put it in a
library. Now anyone can come read it.  

Anyone does, and one of them thinks, I would rather it was about a girl, so my
daughter can relate to it better.  And she takes your book makes a copy and
changes the *he* to *she*, and has fairy pirates and she puts it back and later
someone else changes the pirate ships to space ships and so it goes.

Thats it really.  Anyone has permission to write software, just as anyone has
permission to write books.  There are only two questions - did they write *high
quality* software and does it *do what you want*?

High quality Open Source Software
---------------------------------

Now here is a fun statement - Open Source Software is higher quality than the proprietary equivalents.

`Coverity <http://www.coverity.com>`_ publish a annual comparison of major software
projects "out there".  For all their projects, Open Source has less bugs than
the proprietary equivalents till the size of project reaches a million lines of
code. 

Basically this is public evidence for one of the software industry's dirty
secrets - it turns out if you think someone is going to read your code 
you take more care because you want the respect of your peers.  I mean
if PG Wodehouse was writing books just for his landlord to read, and no-one else was
going to see them, would he put in *that* much extra effort?

Add to that the near pathological development cultures in many many big
companies and coverity's figures make a lot of sense.



Does it scratch your itch?
--------------------------

So I looked at the government tender sites.  I even wrote some scraping software to help me anlyse it. [#]_
Anyway of 70 tenders I could snaffle that day, 1, yes *one* mentioned using Open Source.

No-one is building Open Source for governments - at least they aren't asking for it.

How many ?
----------

There are over 2000 services that UK local authority bodies are funded in order to provide
Each of those 2000 services will soon be delivered, in part or wholly, through digital 
means, and thus be entirely dependant on software.

That means that if we are lucky, we taxpayers will be splodging out real cash to
(big, often American) companies for all but 28 of the 2000 services.

Why not write Open Source Software for all 2000 and then save some cash, get
better quality software, and stimulate the economy by having small businesses
write the software, run it in the cloud for everyone to access and get a regular
cheque for updating it and keeping it smooth.

Bingo ! That was it - all I had to do was run to the `LGA conference <http://www.local.gov.uk>`_, where pretty much
every council Chief Executive and elected Leader would be attending, shout out
the words and the scales would fall from their eyes.

**No-one had thought of this before**

oh, OK, I may not have been the first to think of this.  
-------------------------------------------------------

There is a bit of a sea change happening in Government IT now.  The GDS has
developed a central web portal called `GOV.UK <http://www.gov.uk>`_ and rather
casually done it transparently and openly [#]_ The whole government IT approach
is being re-thought - and re-thought with an eye on making it much easier for
small companies to get in and bring real change.

Professional UK Open Source developers I have talked to (Interviews coming here
I promise) tell me that government contracts are hard to crack.  The tender
process is long, weighted against "look we will develop it but you need to work
with us" versus "prebuilt, commerical packages"

It turns out that GDS and the like already know about this.  There is a new
tender process-y thing.  Called G-Cloud where commercial companies can get
"approved" for government IT work *before* a tender and then all a public body
need do is say "yes, that one".

In theory all we would need to do is find a couple of councils who needed, say,
a new plugin for a planning application system, put it on G-Cloud, and the
councils could pay for development of their needs, openly, deliverd through
G-Cloud and at a marginal cost.  And the other 431 councils could come along and
get a copy.

For free.  (or if they wanted it hosted, for the price of hosting)

Its almost as if someone had planned it that way.


What are we going to do about it?
---------------------------------

::

   - WHAT DO WE *WANT*?!

   - Digital services delivered though software that is seen as a public good,
     developed openly and transparently at the most efficient, marginal cost
     in partnership with government domain experts and run on cloud services 
     under the auspices of best practises in Open Source development.

   - ... Errr, When do we want it?

   - Now !


I am going to the `LGA's conference
<http://sites.idea.gov.uk/annual-conference/>`_ and will be hosting a Fringe
Breakfast on July 3rd at 8am in Manchester.  Some people more intelligent and
entertaining than me will be speaking, so don't worry.

The goal - to find 4 services that at least 4 council leaders want and will need
to replace this year.  

Then get them to fund 1/4 of their budget into a G-Cloud
based Open Development pilot project.  

We (hopefully pretty soon I will be we) shall setup a committee of Open Source
Worthies, who will take on project oversight, to guide and mentor projects to
find their own ways within the best practises of Open Source development.

And then arrange commercial cloud companies to host and support the projects.  

This way, real people in government will be able to help real users with Open
Source tools that cost us the taxpayer only what they cost to build.

As it *should* be.

Please sign up at the top of the page.


Updates
-------

I will post links here - and mail out to the list, so make sure you sign up :-)



     


.. [#] For those of you not techies "I wrote some software to analyse all
       government tenders in the south east of england" sounds impressive.
       Maybe.  It kind of is, but it also is the point I am making - all the
       software to run this site, to analyse the data I am using to make point,
       all of it is open source and free to download.  It can be reused by
       anyone.  I don't charge for it.  Because for me, the effort to write a
       piece of software that analyses tenders in SE is trivial, but the effort
       needed to convert it to, say, www.analyseTenders.com is well, thats
       running a busiines, and I have one of those.

.. [#] They have released (most) of it as open source on github.  I am intending to 
       steal the great named "unicorn-herder" to run this site on Real Soon Now.


..     There is a whole mess of research to be done on how the labour market fluidity in OSS
       impacts the quality, and how remote working will have similar impact on real labout makret fluidity.


Interview with a Local Government Development Manager
=====================================================

Dave Partridge is IT Development Manager at Tonbridge & Malling Borough
Council. Over coffee and a light smattering of rain, we chatted about the
council, the needs and positions of local government for new and old software.

.. image:: /assets/images/headshot_dave_partridge.jpg

I bought the lattes, and whilst queuing we made polite chitchat.  Dave's two
daughter's are both at university, his eldest has graduated last year, and we
commiserated on the state of the employment market for new graduates.  He
apologised for being a little distracted - he was waiting for her call, she had
applied for a graduate position in London.

Open Directions
---------------

"Central government has made it quite clear the direction they want us to go.
More Open Source.  There is no doubt about that.  The difficulty is finding
products that fit the bill.  Or to be more specific, finding business models
that local government can trust will be there after the initial rush."

We dive right in, Dave admires the way Squiz manages the business model
tightrope - bolting on consultancy, but he reserves his praise for a company I
have not heard of - eBase.  "Dave Rawlings there, is always searching for new
ways to bring products to market."

To play Dave's long game you must supply three things Dave thinks vital for
local government.  He looks for people playing a long game, which with capital
funding cycles of upto three years (!) really counts, he looks for ways to avoid
being trapped - both by vanishing of support for a purchased product, and for
the more obvious proprietary lock-in.

These three areas make people like Dave think twice about leaping into the OSS
market, because without building local partnerships, and having in-house
expertise, *OSS is just another supplier*.  It is, for me, a cat flap moment.
Obvious when someone points it out, but not something I would ever come up with
for myself.


"The corporate systems market is cornered"
------------------------------------------


These corporate systems, with names like `UNIFORM <http://software.idoxgroup.com/products/uni-form.cfm>`_ and suppliers like `Northgate <http://www.northgate-is.com/>`_ seem to dominate the local government landscape, and yet they are 
effectively unknown outside the government bubble.  I cannot see myself committing to become an expert in any of their systems - it hardly looks like transferrable skillsets.  Is that a difficulty in keeping in-house teams?

"Getting skills back in-house is a problem.  We are still heavily focused on
supporting desktops and a few proprietary corporate systems and we no longer
have skills outside those areas.  If it is not vital to keeping today's services
running, we lost it over years of cuts."

Dave has managed to acquire the kernel of a new development team, and explained
how he has cut their teeth on a project eerily familiar to my ears.

Abandoned vehicles. 
-------------------

"What we do is pretty simple.  It's either People or Locations.  Put that at the
heart of your systems, and make sure you can integrate, and the rest will
follow."

The abandonded vehicles project was abandoned itself.  It had started in the
Thatcher years (yes, folks, you heard it right) but died numerous deaths since
then.  It was however a perfect example - simple to understand, yet touching on
multiple agencies.  A vehicle could need Police, Fire, co-ordination with 
County Council, independant contractors all to move a car no-one wanted.  Even the starting point could be complicated.

.. pull-quote:: "What we do is pretty simple.  It's either People or Locations."

"Imagine someone wanting to report a car, they log onto their local website, but it happens to be just over the boundary for the next district over.  It matters at the backend, because it could take a long time to get out of my service request queue and over into Swales.  That would slow response, but its none of the users business to know which web site to report on.  This is where the previous attempts got bogged down.  Analysts would go look at the process for handling abandoned vehicles in County, in Tunbridge Wells, in Swales or here and find slightly different approaches.  And try to consolidate them all, or as they say, take the wrong thing and automate it so you do the wrong thing, faster, cheaper."

Start with User Need
--------------------

Dave and others then sat down and looked at it from the front.  

"All you are doing is saying 'there is a car over there, please go deal with
it'.  It should not be rocket science".

This month sees the project meet for final approval from the different involved
agencies, but Dave's technical description tells me of the complexities and the
right way to route around them.  The web form is pretty simple, and is stored
centrally - it can get branded on the way out to any partners web site.  

Then it captures the request and depending, not on the originating site, but the
geo-location gathered, drops the service request into one of many different
CRMs.  We have reusable integration points for Northgate and others - so we can
just pass the request on, no fuss.

This is a theme repeated, the CRM systems for local government are their already existing message queue systems.  They are well used, and their foibles well understood, and not only that the reporting makes everyone happy.

Clearly CRM's are a vital part of the integration process - drop your workflow in there and *the job's a good 'un.*

Dave covers other issues such as managing partnerships, procurement processes ("not my area, just a frustration") before hitting an example dear to my dosmesticated heart - bin collections.

Refuse online
-------------

It's one of everybodies *top tasks* - simply because every week we come into
contact with every household in our area, and guess what, if we do it perfectly,
no-one notices, do it wrong and ...

It is a little unfair I admit, but they still did not collect my bins last
week.(Plastic in the recycling. I got a note).  Dave has seen one other council
take an innovative approach - GPS tracking of the refuse lorries, combined with
driver taking notes on which bins were available, and dumping the lot into a
CRM.  "Sorry Mrs Trumpington-smythe, your bin was not on the roadside when our
driver came past.  No.s 7, 9 and 11 had put theirs out as usual."

He cannot drum up enough interest to replicate it at his council.  I wonder what
the LGA will turn up?

Here I see the perfect dichotomy between "starting with the User need" and
"funding from the council's need".  Councils want to defend themselves from
calls like the above.  And thats fine and quite understandable.  However the
same process of data collection can feed into areas I see as user need (Which
lorry is coming to do my bins this morning? Where are they? How is that as a %
of usual schedule? Is it a green or black bin day? Can I book mark this page?"

Summary
-------

We desperately need to tip the playing field.  

People like Dave understand the benefits of Open Software in their work.  They
also know and feel the pressure to get there.  However they have legitimate
reasons to treat Open Source Software as just another, very big, disorganised
supplier, and equally good reasons to avoid getting trapped.  This is not a
problem with education of local councils.  It is not a problem of motivation.
It is a system, and the biases are against us. 

As we broke up, Dave's daughter called with great news - she got the job.
Perhaps he has it right - keep focused on the goal, remain optimistic, and play a long game.




=====
About
=====

Introduction to OdiEtAmo
========================

This is the Odi et Amo project, an open source community project aimed at::

  Making (commercial) team development with Oracle Data Integrator (and related
  tools) more in line with modern development processes.

In short, getting Oracle Data Integrator (ODI) to integrate with
source control, code review, build tools and better monitoring in the
wild.

We grew out of an internal project at a large well-known health
insurer, and have now released that code base to become fully managed
by the community.

A little bit of history
-----------------------

The three original developers of the code base worked at a large and
well known private medical insurance company in London. They were
involved in the Data Warehousing development teams and wanted to use
modern source control and review techniques with the Oracle Data
Integrator (ODI) and related code base.

Unfortunately the Oracle Data Integrator (as of time of writing) does
not support serialising code out to a repository. The "official"
approach is to use version labels, the equivalent of putting 01, 02,
03 on the end of each code file you write. To put it sarcastically,
this is a little bit behind the state of the art in distributed
version control.

So we had three choices. (Four, if you include giving up and going
down the pub.)

1. Keep going using manual tracking (this became quickly impractical)
2. Wait for Oracle to solve it. It is not currently on any published roadmap we can find.
3. Fix it ourselves

We choose 4. go down the pub. No, sorry. *3. Fix it ourselves.*

Surprisingly, it worked.

With late nights and weekends, a couple of people pulled together
enough fixes to prove this could really work.  The company then paid
for further development, and currently use it internally. In an
enlightened step, they then released the code base so that the
community can keep it alive.

So we now have the ability to serialise in and out from a ODI
repository all code at the granular level (tables, interfaces,
procedures, etc), store that in any suitable source reposistory
(currently targetted at TFS).  Other features include a real-time
comparison of running repositories, cryptographic "fingerprinting" of
repositories and more.  Please see the manual for details.  

What is the current involvement of this large insurer?
------------------------------------------------------

As you can probably tell from the coy references, officially
absolutely nothing. No funding, no warranty, no beer and pizza. This
really is a community project, licensed under an approved Open Source
license and totally steered by the community. Please join the mailing
list.

Where does that name come from ?
--------------------------------

`en.wikipedia.org/wiki/Catullus_85 <http://en.wikipedia.org/wiki/Catullus_85>`_

Catullus 85 is a poem by the Roman poet Catullus for his mistress
Lesbia. (Yes, really. His poetry has influenced everyone from
Shakespeare to Betjamin.  And he was very upset when she dumped
him. So don't snigger.).

The Latin odi et amo translates to I hate her and I love her

I studied Catullus as a kid and quite liked him ("He's like 2000 years
old and he swears, cool!"). But mostly I liked the ODI pun.

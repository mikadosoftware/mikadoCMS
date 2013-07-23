Source Control vs Version Control
=================================

What's the difference and why does it matter for my DataWarehouse?
------------------------------------------------------------------

This is a little parable about two hard working people and a Word Document.
It is unlikely to make a dent in the Grimm Brothers royalties packages but bear with me. No Magic involved at all.

Look, Version Control is simple. It's what you do with that annoying report 
your boss wants you to finish.  You save a copy to the desktop and 
call it `BigReport.doc` and an hour later you save `BigReport1.doc`,
then `BigReport2.doc` and so on.  You have different versions representing 
what you were writing at different points in time.

Its simple. And it works.  Right up till the moment your boss tells you the
report needs to be co-written with Judy from Marketing.  By 5pm tomorrow.  "Ok",
you say. Here is my latest copy - please add your changes in.  So you go off and
continue adding your graphs and what not.  Save - `BigReport3.doc`.

And Judy adds the competitor analysis. Save - `BigReportJudy1.doc`.

Aha. And then the penny drops.

When we introduce parallel edits to a single document in a version control
system, Bad Things can and do Happen.

But all is not lost.  We can co-ordinate.  But conversations tend to end up like
this "Err, why don't *you* stop working on your document and I will finish my
part first.  That way at 4:59 I am not the one getting the blame".

Ok, maybe co-ordination is not the way to go.  How about sitting at the same
desk.  Yeah, right.

Ok if only there was some way to merge the two different documents together.
And now, welcome to the world of *source control*.


If there was a way to automatically find the changes Judy had made, then add
them back into the latest copy of your document, and only let you know if you
had both changed, say, the same word, then you could both work in parallel, swap
your changes easily and get it all done by 5pm.

Luckily over the past thirty years, just such diff and merge tools have been
developed to a truly impressive degree.  As long as you are just using plain
text.

You are just using plain text to write this all down, aren't you? 

Now, Word does have another similarity to modern ETL tools - they do not store
things in plain text.  ODI for example keeps all its routines in a seperate
database, the actual source code to be executed is stored in a database, not in
a text file.

So if we want to work in parallel teams, and to use Word or ODI, we need to have
a way of faithfully extracting the plain text versions of each part, then
allowing modern source control, diff and merge to help us keep control, and then
with equal fidelity put the now merged plain text versions back into the ETL
tool (or Word, in our slightly redundant fable).

And that is precisely what the Open Source tool ODI-SCM does.  It enables
multipole data warehousing teams to work together on the same ODI repo, in an
Agile manner, and still use modern source control to keep their development on
track.

Now go live happily ever after :-)

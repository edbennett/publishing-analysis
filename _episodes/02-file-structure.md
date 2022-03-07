---
title: "Structuring your repository"
teaching: 10
exercises: 10
questions:
- "How should files be organised in a repository?"
- "What metadata should be included, and how?"
- "How do I adjust the structure of a repository once it is created?"
objectives:
- "Be able to organise code, documentation, and metadata into an easy-to-user directory layout."
- "Understand the importance of a README, license, and citation file."
- "Be able to restructure an existing repository."
keypoints:
- "Put code into a specific subdirectory (or several, if there is lots of code)."
- "Keep important metadata, such as a license, citation information, and README in the root of the repository."
- "Keep other ancillary data, documentation, etc. in separate subdirectories."
- "Use `git mv` to move files and let Git know that they have moved."
---

Now that we have a repository to work with, and that has all of our code in, we can start
tidying it up so that it is easier for others to understand.

## README

A README is the first thing you should add to your repository, if it doesn't already have
one. The file name convention is old&mdash;it dates to before you could have lower case
letters and spaces in a file name&mdash;and is intended as an instruction to anyone who
happens upon it to read it before looking anywhere else. READMEs were originally (and
frequently still are) plain text files, although other formats are also popular now.

> ## Markdown
>
> A popular format for READMEs on GitHub is Markdown, which looks like plain text
> but specific characters will let you indicate headings, bold, italic, etc.
>
> For more information about Markdown, you might check out the Carpentries Incubator's
> [Introduction to MarkDown][markdown-intro].
{: .callout}

Conversely, when you start using a new piece of software (or investigate someone else's
analysis code), it's a good idea to start by looking for a README to see what the author
thought was important you understand first.

There are many things that you can include in a README. Exactly what should and shouldn't
go there will depend on your project, and don't forget that starting with something short
is still better than having no README at all. (On the other hand, a README that is incorrect
can be _less_ helpful than no README at all, so be sure to keep yours updated if your
code changes.) Some things to consider

* The name of the code, or project; this typically goes at the top
* A short description of what the code does
* A link or citation to the paper (or a preprint) the work supports, if it is available
* Instructions on how to install and use the software (which we'll discuss in more detail
  in a later episode)

Let's write a short README for the `zipf` repository now.

~~~
$ cd ~/Desktop/zipf
$ nano README.txt
~~~
{: .language-bash}

~~~
zipf analysis
=============

This repository contains code to observe whether books adhere to Zipf's law, as 
done in support of the paper "Zipf analysis of 19th-century English-language books",
V. Dracula, to appear in Annals of Computational Linguistics, 2022.

To run the code, you will need the Pandas package installed.
~~~
{: .output}

This is a little brief, but is some progress, and we'll revisit tightening up some of
the details in later episodes.

Let's commit this to the repository now.

~~~
$ git add README
$ git commit -m 'add a README'
$ git push origin main
~~~
{: .language-bash}

We'll be keeping up this habit of regularly committing and pushing, so that our fallback
version on GitHub stays up to date. (The benefits of storing a copy remotely are lost if
when your laptop is stolen you have to fall back on a version from years ago!)

## LICENSE

The next thing to do is to let people know what they're allowed to do with your code.
(Or, conversely, what they're not allowed to do!) By default, copyright law is a huge
barrier to doing anything productive with code that is not explicitly licensed.

Since we are researchers, not copyright lawyers, writing our own license from scratch
is not a good idea. It's more likely that we will either not give away the permissions
we need for someone to be able to use the code, or give away rights that we do not
intend to. (Or both.) It's much safer to pick a license that someone else has designed,
and that has been written and vetted by teams of copyright lawyers. This has the added
bonus of being more widely understood; someone reading a set of rights you're giving
explicitly will be more confused than if they saw the name of a familiar license, and
if they have a particularly careful legal department, then they'll be much happier to
see a familiar name.

A good place to start when deciding what license to give to your research code is
[Choose a license][choosealicense], which has a comparison table of some of the
more common licenses used for software. Some questions to ask yourself:

* Do you want others to have to share their changes to your source code under the same
  terms if they share the software?
* Do you want others to be able to distribute your code under the same name
  (trademark rights)?
* If your code makes use of patents you own, are you giving users of the code rights
  to use them?
* Do others need to explicitly state what changes they've made to your version?
* Can others run your software as a service without sharing changes?

Let's place Zipf under the MIT License.

~~~
$ nano LICENSE
~~~
{: .language-bash}

~~~
MIT License

Copyright (c) 2020 Amira Khan, Ed Bennett

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
~~~
{: .output}

> ## Names
>
> You might have spotted that the name in the README doesn't match the name in the license
> here. This is because the paper referred to in the README is imaginary, while the code
> is actually written by real people and licensed by them, so we need to acknowledge them
> appropriately, even on a toy example project like this.
{: .callout}

Again, let's commit and push:

~~~
$ git add README
$ git commit -m 'add a LICENSE'
$ git push origin main
~~~
{: .language-bash}


## CITATION

The idea of a CITATION file is much newer than the README and LICENSE, and the uppercase
is a convention carried over from the latter two rather than ever having been technically
necessary. It is rather more specific to software used in an academic context.

In its simplest form, the CITATION file should describe how someone who finds your code
useful in their own research (in particular, but not only, if they use/modify it themselves
to generate their own results) should cite it. Sometimes this will be a citation to the
paper that the code supports, but we'll discuss later how the repository itself can be
cited in the final episode.

In the absence of a CITATION file, many researchers using your work may instead use a
footnote with a URL, or text in the acknowledgement, or some other way that makes it
much harder to track how much impact your work is having. While assessing work on the
basis of citation counts is fundamentally flawed, citation is still a vital part of
good scholarship, and having clear and consistent data on what work is being referred
is both invaluable in itself and also a vital part of intellectual honesty&mdash;as
Newton said, we are only able to research by standing on the shoulders of giants.

For now, we can add a brief text description of how to cite the work.

~~~
$ nano CITATION
~~~
{: .language-bash}

~~~
If you use this code in your own work or research presented in a publication, we ask
that you please cite:

"Zipf analysis of 19th-century English-language books",
V. Dracula, to appear in Annals of Computational Linguistics, 2022
~~~
{: .output}

Again, we should now commit and push this:

~~~
$ git add README
$ git commit -m 'give information on how to cite'
$ git push origin main
~~~
{: .language-bash}

> ## Citation file formats
>
> If you are in a field that makes use of LaTeX, you may consider including a
> BibTeX version of your citation so that others can copy it directly into their
> work.
>
> There is also a [Citation File Format][cff], which lets you specify citation
> information in a more structured format.
{: .callout}


## Directory structure

Now that we've started adding metadata to the repository, the root directory is starting
to get a little cluttered. For someone arriving at the repository for the first time, it
might be hard to tell what is important information they need to look at, what is the
code that they need to run first, and what is ancillary supporting code that they can
dig into at a later date.

To make this easier, you should use directories (folders) to separate out related elements.
Things like the README, LICENSE, and CITATION, that apply to the whole repository (and that
users will need to see first) should be at the root of the repository. Code should go in
its own subdirectory&mdash;in principle this could be called something like `code`, but it
is conventionally named for the name of the repository.

If you have a lot of code, then it might be a good idea to split it up. A directory with
dozens or hundreds of files in is not conducive to easy reading! Again, grouping related
files together is the target&mdash;for example, you could group all of your figure files
in one directory, files with common functionality that are never called directly from the
command line in another.

Let's rearrange the files in the `zipf` repository now. We can do this using the `git mv`
command. This moves a file in the same way that `mv` does, but also alerts Git about the
change so that it can be committed more easily.

~~~
$ mkdir zipf
$ git mv zipf.py zipf
~~~
{: .language-bash}

The `frankenstein.txt` looks to be data that the code operates on. This doesn't belong in
the same directory as the code, and neither does it belong in the root of the repository.
Let's give it its own `data` directory for now.

~~~
$ mkdir data
$ git mv frankenstein.txt data
$ git commit -m 'reorganise directory structure'
$ git push
~~~
{: .language-bash}

As our repository is small we've done this reorganisation in a single step, but of course
if there were more to do we could do things in stages, working incrementally.


> ## Python packaging
>
> You can take this structure to the next level with the concept of a Python _package_.
> This is a specific structure designed so that others can install your repository and
> have it accessible via `import` like other packages you might install with `pip`.
>
> For just publishing your analysis this can be overkill, but if you think any of the
> code you have written could be useful more generally, then packaging it is a very good
> idea. While it's too much for the time we have this week, the (free, online) book
> [Research Software Engineering with Python][py-rse] has a section on
> [Creating Packages with Python][py-rse-packaging].

> ## Tidying up
>
> Kazu has committed his analysis directory into a Git repository. While he is happy that
> he now can keep track of versions and share with colleagues, he realises that to allow
> others to easily make use of the workflows he's prepared, he will need to make some
> improvements to the structure of the repository.
>
> Given the structure below, what changes would you suggest Kazu make?
>
> ~~~
> analyze.py
> draw_fig3.py
> fig1.py
> figure_2.py
> notes/
>   notes_for_julia.eml
> tables_code.zip
> test.py
> ~~~
> {:.output}
>
>> ## Solution
>>
>> Some things that Kazu might want to consider (there may be others!):
>>
>>  * `fig1.py`, `figure_2.py`, and `draw_fig3.py` could be renamed consistently
>>  * The `.py` files could be placed in a `code` subdirectory
>>  * Code isn't very useful in a ZIP file; it would be better if the programs
>>    in this file were committed directly to the repository instead
>>  * The `notes_for_julia.eml` looks like it might be the only documentation
>>    Kazu has written for this code. Perhaps it could form the basis of a README.
>>    This should be in the root of the repository, and probably shouldn't be in
>>    the form of an email.
>>  * `analyze.py` could also be in the `code` directory. Kazu might also want
>>    to have subdirectories of `code` specifically for analysis, plots, and tables.
>>  * Kazu should specify licensing and citation information.
> {: .solution}
{: .challenge}


> ## Choosing a license
>
> Kai has written some engineering analysis code that could be very useful in
> the private sector. They don't like the idea of their hard work being used
> as the basis for a commercial product that they won't see any income from
> (especially if they start to receive requests for support), so they would
> like a license that makes sure that any changes to the software are made
> freely available, and with the same rights to those who receive the modified
> version.
>
> Sameth has prepared some code for genetic analysis that solves a very specific
> problem, but that others with more financial resources may also be able to adapt
> to do some very impactful research that could form the basis of an Impact Case
> Study. Due to the way the field works, these others would need to be able to
> distribute the software, but would want to keep the source code changes thay have
> made proprietary.
>
> What licenses would you suggest that Kai and Sameth choose for their software?
>
>> ## Solution
>>
>> Kai is most likely looking for the Affero GNU Public License, although
>> they may instead opt for the GNU Public License.
>>
>> Sameth could use the MIT or BSD license, among others.
>>
>> If no-one else contributes changes back to their code, then nothing is stopping
>> them negotiating a separate licensing agreement&mdash;for example, if a major
>> engineering firm wanted to pay Kai for the rights to distribute modified versions
>> without sharing the code. However, Kai would need to be careful about who owns
>> the code&mdash;if they are a postdoc, then it may be their university who has
>> the rights to this.
>>
>> If others have also made contributions, then whether you can re-license the code
>> will depend on getting the agreement of all authors. A Contributor Agreement
>> makes this easier, by granting certain rights up-front rather than needing
>> to track down a lot of authors later.
> {: .solution}
{: .challenge}


> ## Tidy up for yourself
>
> In the previous episode's challenges, you created a repository for the example
> code downloaded. Use `git mv` now to start tidying up this repository.
{: .challenge}

{% include links.md %}

[cff]: https://citation-file-format.github.io
[choosealicense]: https://choosealicense.com
[markdown-intro]: https://carpentries-incubator.github.io/markdown-intro/
[py-rse]: https://merely-useful.tech/py-rse/
[py-rse-packaging]: https://merely-useful.tech/py-rse/packaging.html

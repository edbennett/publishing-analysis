---
title: "Get it in Git"
teaching: 45
exercises: 25
questions:
- "Why should I make my code public?"
- "How do I get files into a GitHub repository?"
- "What should I include in a repository?"
objectives:
- "Understand the many reasons for publishing analysis"
- "Be able to add files to a Git repository and push it to GitHub"
- "Be able to categorise files into those to commit, and those to omit"
keypoints:
- "Publishing analysis code allows others to better understand what you have done, to verify that your analysis does what you claim, and to build on your work.e"
- "Use `git init`, `git add`, `git commit`, `git remote add`, and `git push`, as discussed in the [Software Carpentry Git lesson](https://swcarpentry.github.com/git-novice)"
- "Include all the code that you have written to use in this analysis."
- "Leave out e.g. temporary copies, old backup versions, files containing secret or confidential information, and supporting files generated automatically."
---

Once upon a time, research was published entirely in the form of papers. If you
performed a piece of analysis, it would be done by hand in your research notebook
or lab diary, and carefully written up, so that anyone with a little time could
easily reproduce it. All relevant data were published as tables, either in the
main text, or in appendices, or as supplementary material.

Then, computers were invented, and gradually researchers realised that they could
get analyses done much more quickly (and with much larger data sets) if they got
the computer to do the analysis instead. As time has gone on, computers have got
more powerful, and researchers have got more experience of software, the complexity
of such analyses has increased, as has the volume of data they can deal with.

Now, since computers are deterministic machines, that (should) always give the
same output given the same input, then one might expect that as this occurred,
then the ability of other researchers to reproduce exactly the computations that
were done to produce a paper has increased. Unfortunately, the opposite has
happened! As the complexity of the analysis has increased, the detail in which
it is described has not done the same (possibly even gone down), and in most
fields it did not immediately become common to publish the code used to produce
a result along with the paper showing the result.

This is now starting to change. There has been increasing pressure for some
time to publish datasets along with papers, so that the data that were
collected (in many cases at significant investment of researcher time or
money) are not lost, but can be studied by others to learn more from them.
More recently, the same pressure has turned its focus on the software used.

In this lesson, we are going to learn how we can take code that we have written
to perform the data analysis (or simulation, or anything else) for a paper, and
publish it so that others are able to reproduce our work. We will focus on Python,
since that is a popular programming language in research computing, but many of
the topics we cover will be more broadly applicable.

> ## Reproduce?
>
> The word "reproduce" here is being used with a specific meaning: another researcher
> should be able to take the same data, and apply the same analysis, and get the same
> result. This is distinct from: "replicability", where another researcher should be
> able to apply the same analytical techniques to a fresh, different data set, and
> still get the same results; "robustness", where applying different analytical
> techniques to the same data give the same result; and "generalisability", where
> applying different analytical techniques to freshly-collected data give the same
> result.
>
> Reproducibility is in principle the simplest of these to achieve&mdash;since we are
> using deterministic machines, it should be achievable to repeat the same analysis on
> the same data. However, there are still challenges that need to be overcome to get
> there.
>
> [The Turing Way][turing-way] has more detail on these definitions.
{: .callout}

> ## Alternatives
>
> The workflow we will talk about in this lesson is one way to publish code for
> data analysis&mdash;and in many cases is the shortest path we can take to get
> to a publishable results. In some cases there are other alternative technologies
> or ways of doing things, that would take a bit longer to learn but could also
> be very useful. In the interests of keeping this lesson a reasonable length,
> and because entire lessons already exist about many of these topics,
> these will be signposted in callouts to where you can learn more.
{: .callout}


## A first step

In general, we want to do the best job we can; in the context of publishing a
piece of data analysis code this means having it run automatically, always give
fully reproducible output, be extensively tested and robust, follow good coding
standards, etc. However, it is important to not let the perfect be the enemy of
the good! Even if we could devote all our time
to polishing it, there would always be some area that could be improved, or
tidied, or otherwise made slightly better before we called the code "ready" to
be published. Add on the fact that we need to keep doing research, and teaching,
and in fact can't devote all our time to polishing one piece of analysis code,
and it becomes clear that if we wait until we have all our software in a perfect
state before sharing it, then it will never be shared.

Instead, we can take a more pragmatic approach. If the alternative is publishing
nothing, then any step we can take towards our goals will be progress! We can
start with the absolute minimum step, and work incrementally towards where
we'd ideally like to be.

Remember
that you were going to publish results based on the code anyway, then the code
must already be good enough to trust the output of, so there should be no barrier
to making it available.


> ## Difficulties in reproduction
>
> Have you ever tried to reproduce someone's published work but not been able to,
> as their publication didn't give sufficient detail? Would this have been helped
> if they had published the software they used?
>
> Are there any other situations where your research would have benefited from
> access to someone else's analysis code?
>
> Discuss with a neighbour, or in breakout rooms.
{: .challenge}

> ## Why not publish?
>
> What reasons might there be to be reluctant to publish your data analysis code?
>
> What counterarguments might one have to these reasons?
>
> Discuss with a neighbour, or in breakout rooms.
{: .challenge}


The first step we will take today is to get your code into version control,
and uploaded to GitHub. This will be useful in many ways:

* We can track the history of our analysis as it has developed
* We can share the repository with collaborators and get their input
* We will have a backup version in case we make unwanted changes, or lose
  data (e.g. a broken or stolen laptop)
* We will be able to connect it to Zenodo later in the lesson to turn the
  code into a citable object with a DOI
  
(If you're already using version control for your analysis code, then you're
already in a strong starting position!)

Let's start off by opening a Unix shell, and navigating to the example code we
will be working on for this lesson.

~~~
$ cd ~/Desktop/zipf
~~~
{: .language-bash}

Next, we turn this directory into a Git repository:

~~~
$ git init
~~~
{: .language-bash}

Before we start adding files to the repository, we need to check a couple of things.
While most problems we can come back to and fix later (in the spirit of working
incrementally), there are a couple of things that are easier to avoid than they
are to repair later:

* We do not want to put private or secret data into our repository. Remember that
  Git stores the complete version history, so even if you remove the secrets in a
  later commit, they will still be visible to anyone who has access to the full
  repository. A common problem here is people posting their private tokens for
  cloud services; there are robots that watch every new upload to GitHub to take
  any such tokens that get accidentally included, so that they can take over the
  account and use it for their own nefarious purposes.
* It's a good idea to avoid putting any large data files into the repository. This
  means that it's possible for others to take a local copy of the repository to
  look at the code without needing to download a large volume of data that they
  don't need. Again, even if you later added a commit removing the data, it would
  still be there in the commit history, so would need to be downloaded every time
  someone took a fresh copy of the repository.

Let's see what we currently have:

~~~
$ ls
~~~
{: .language-bash}

~~~
book_summary.sh    dracula.txt        id_rsa             script_template.py
collate.py         frankenstein.txt   id_rsa.pub         utilities.py
countwords.py      full_data.npy      plotcounts.py
~~~
{: .output}

Of these, `full_data.npy` is a few megabytes in size, much larger than any of
the code we are working with, so we will omit that. `id_rsa` is a private SSH
key, so that definitely doesn't want to be committed&mdash;it probably ended
up in this directory by accident. `frankenstein.txt` is a piece of data we would
like to operate on&mdash;since it is small, there are arguments both ways as to
whether to keep it in the repository or to publish it separately as data.
For now, let's keep it in; we can always remove it later.
(We'll talk a little more about data later in the lesson.)

Since we don't want to move or remove files from our existing analysis (which
assumes files are where they are currently are placed), we can use a `.gitignore`
file to specify to Git what we don't want to include.

~~~
$ nano .gitignore
~~~
{: .language-bash}

~~~
*.npy
id_rsa
id_rsa.pub
~~~
{: .output}

> ## More to ignore
> 
> While we're creating a `.gitignore` anyway, you could also add some other
> common things to make sure not to include in a repository, for example:
> 
> * Temporary files, which were used as part of the analysis but are not needed
> * Cache files, like `__pycache__`, that Python sometimes generates, since
>   these are useless on anyone else's computer
> * Duplicate or old copies of code, since we'll be using Git to manage the
>   history of the code from now on.
>
> GitHub has
> [a repository of common `.gitignore` files for various languages][github-gitignore]
> and technologies that you may want to borrow from.
{: .callout}

Now, a check of `git status` will show us what Git would like to commit:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.gitignore
	book_summary.sh
	collate.py
	countwords.py
	dracula.txt
	frankenstein.txt
	plotcounts.py
	script_template.py
	utilities.py

nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

To get all of these files into an initial Git commit, we can add them to the
staging area and then commit the resulting data:

~~~
$ git add .
$ git commit -m 'initial commit of analysis code'
~~~
{: .language-bash}

Finally, we need to push this to GitHub. Visit [GitHub][github] and create a new,
empty repository. In this case, let's call the repository `zipf-analysis`. Add
this repository as a remote to your local copy, and push:

~~~
$ git remote add origin git@github.com:USERNAME/zipf-analysis
$ git push origin main
~~~
{: .language-bash}

> ## SSH keys
>
> If you find that GitHub doesn't let you do this, then you will need to set up
> key authentication with GitHub. To do this, follow the instructions in the
> [Software Carpentry Git lesson][git-novice].
{: .callout}

We now have the code that we used for our research stored online, and available.
If we had no more time, we could put a footnote pointing to this repository,
and call it done. However, with a little extra effort, there are many ways we
can improve on this, and as we go through the remainder of the episode we will
see how.

> ## What to include
>
> Anneka has a folder containing the analysis that she has performed,
> and that she is preparing to publish as a journal article. It contains
> the following files and subfolders:
>
> * `fig5.py`, which plots a graph used in the paper draft
> * A folder called `__pycache__`; Anneka isn't sure what this is
> * `analyse_slides.py`, which doesn't generate anything included in the
>   paper directly, but generates numbers needed by `fig5.py`
> * `table3.tex`, an output file used in the publication
> * A folder called `tensorflow` containing the source code for the TensorFlow library, which Anneka needed to manually install
> * `participants.csv`, a listing of the people that Anneka took samples from, and which images are from which person.
> * `Makefile`, which Anneka got from a collaborator; she isn't sure what it does
> * `test.py`, which doesn't generate any outputs used in the publication, but does illustrate a simple example of how to use the code
> * `.DS_Store` and `thumbs.db`, which keep showing up on Anneka's disk
> * `fig5_tmp.py`, which was used by Anneka to test some modifications to one of the graphs in the paper but was ultimately not used for the final analysis
>
> Which of these (if any) should Anneka include in her repository? In each case, why, or why not?
>
>> ## Solution
>>
>> * `fig5.py`: This is needed to reproduce Anneka's work, so should be included.
>> * `__pycache__`: This is a folder you will frequently see when working with Python; it contains temporary files generated from your Python code by the Python interpreter. It is useless on anyone else's computer, so should be excluded.
>> * `analyse_slides.py`: Even though no outputs are used directly in the publication, this file is needed to reproduce Anneka's work, so should be included.
>> * `table3.tex`: This should be generated as an output of the code, and is included as part of the publication, so doesn't need to be included in the repository.
>> * `tensorflow`: The source code to Tensorflow is available elsewhere, so should not be included in the repository. We'll discuss later how to specify what packages need to be installed for your analysis to work. Note that if Anneka has made changes to Tensorflow, then these should be in _a_ repository, but probably not _this_ one&mdash;Tensorflow is much larger than the analysis for one paper, and has its own repository. Look up the idea of "forking on GitHub" for more information about one way this could be done.
>> * `participants.csv`: This is data, not code, so we would need to decide whether we are mixing data and code, or keeping this repository to be code-only. Since it is also personal, private data, special care would need to be taken before this is committed to any public repository, either for data or code.
>> * `Makefile`: Anneka should understand what this does before committing it. It's possible that she is using it without realising it (e.g. if she runs `Make`), in which case it is needed to reproduce her work. Perhaps she could check with her collaborator what the `Makefile` does.
>> * `test.py`: While not strictly necessary to reproduce Anneka's work, this file could help someone else looking to do so to better understand how Anneka's code works. It's not essential to include, but committing it is probably a good idea.
>> * `.DS_Store` and `thumbs.db`: These are metadata files made by macOS and Windows; they're useless on anyone else's computer, and should not be committed.
>> * `fig5_tmp.py`: Since there is already a canonical version of `fig5.py` above, this alternative version should not be committed.
> {: .solution}
{: .challenge}



> ## Creating another repository
>
> Download [this example archive of code](../files/challenge.zip) and extract it to
> a convenient location on your computer. This will give you a directory
> containing a small piece of research software, and the data it was last used
> to analyse.
>
> Turn this directory into a repository and push it to GitHub.
>
> Remember to exclude any files that shouldn't be in the code repository.
{: .challenge}


## FAIR's fair

You might have heard of the concept of "FAIR data", and more recently "FAIR
software". The acronym FAIR stands for:

* Findable
* Accessible
* Interoperable
* Reusable

The standards for data are well-developed; the situation for software (i.e. code)
is more fluid, and still continuing to develop. For this lesson, we will address
the first two points; the latter two points are a step further&mdash;the aim for
now is to let us document what we have done in our own work, rather than provide
tools for others to use.

In the spirit of not letting the perfect be the enemy of the good, this lesson is
doing what it can for now; as standards develop, it may be updated.

{% include links.md %}

[github]: https://github.com
[github-gitignore]: https://github.com/github/gitignore
[git-novice]: https://softwarecarpentry.github.io/git-novice
[turing-way]: https://the-turing-way.netlify.app/reproducible-research/overview/overview-definitions.html

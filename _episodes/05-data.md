---
title: "Data"
teaching: 10
exercises: 5
questions:
- "How do I get data for my code to work on?"
- "Where should I store data?"
- "Should data be published?"
objectives:
- "Be able to pull data from data repositories to operate on."
- "Understand options around keeping data with or separate from code."
- "Be aware of options around data publication."
keypoints:
- "Use `curl` to download data automatically."
- "For small amounts of data, and code that is specifically to analyse only those data, data and code can be stored and published together."
- "For large datasets, or where code is used for multiple different datasets, keep the two separate."
- "Data can be frequently be published, if there are no constraints preventing it. If data are not published, then publishing analysis code becomes less valuable."
---

As this lesson focuses on code, we haven't talked a huge amount about data. However, data
analysis code can't do very much without some data to analyse, so in this episode we'll
discuss some of the aspects of open data that overlap with publishing data analysis code.
Open data is a huge area, much larger than the scope of this lesson, so we will only
touch on some of the outskirts of this; there are many resources available that you can
(and should) check out when you get the chance to get a fuller picture.

A first consideration is to decide whether or not the data you are analysing can, or should,
be published (by you). For publicly-funded research there is now a general expectation that
data should be made public unless there is a compelling reason not to, but there are a
variety of reasons that could justify (or even demand) not publishing data. Some examples:

* If the data you are working with is confidential, and you don't have permission from
  each person represented in it, then laws in most of the world prevent you from publishing.
* If you have not generated or collected any of your own data, but instead only analysed
  data from public datasets, then there may be no need to re-publish the data, as it is
  already available. In this case, a citation is sufficient.
* If you are working with data that is commercially sensitive and have a confidentiality
  agreement with the company in question, then you may not be able to publish the data,
  at least without the approval of the commercial partner organisation. Of course, this
  is likely to also apply to other aspects of your research, even papers or conference
  talks.
* If your project deals with matters that could affect national security, then there may
  be even more stringent checks on publishing data or papers.
* If you are part of a collaboration that has not agreed to publish data, then you should
  not unilaterally publish data, especially if it has been generated collaboratively and
  not by you personally. You can of course advocate to the collaboration that they should
  move in this direction. In some cases, collaborations will also have embargo policies
  that keep data private for a finite period of time to allow collabration members to get
  as much science as they plan to out of the data, and avoid being "scooped" by another
  team able to move more rapidly.
* If the data are so large that it is not practical to store or host for extended periods
  of time, then opening the data may not be possible. This generally only applies to very
  large experiments or supercomputing facilities, however.


## Together or separate?

Assuming that you have decided that your data are publishable, the next question is whether
they should be published in the same release as your analysis code, or as a separate
package. Once again, there are a number of factors that affect this, but the top two
are:

* Is the volume of data significantly larger than the volume of code? If so, then it is
  likely to be better to keep the two separate, so that those who want to check out and
  study or re-use your code won't have to download a large volume of data that they don't
  need.
* Is the code likely to be useful in its own right, outside of the specific analysis you
  have done for the particular publication you're working on? If so, then again it is
  likely to be a good idea to keep the code separate, and you may then want to look more
  closely at packaging your code to make it easier for others to install and run.

If neither of these is true&mdash;i.e., the volume of data is pretty small, and the code
you have is quite tightly coupled to it, then it may be better to publish the code and
data together in a single package. This has the advantage that the two are
self-reinforcing; reading the code helps to understand the data, and having the data
allows the reader to run the code and see how it works on the data.


## Working with open data

As mentioned already, if the data you are working with have already been published, then
it is not necessary (or appropriate) to re-publish it. So, what should we do instead?

As in the previous episode about documentation, there are two options: either we describe
(in the README or elsewhere) how to get the data to operate on, or we automate the process.

Revisiting our `zipf` repository, we can see that we have the complete text of two books
in our `data` subdirectory. The books are in the public domain and fully attributed to
their authors, and the volume of data is hardly huge, so in principle there is not an
urgent reason to omit the data, but conversely its easy availability means that including
it isn't essential either. Let's see how we could go about removing it.

To create a Git commit that removes files, we can use the `git rm` command. Similarly to
`git mv`, this combines the `rm` command with making Git aware of what we have done.
Remember that this will only remove the file from the most recent commit; it will still
be present in the history for anyone who checks out an earlier commit. (So don't use this
method to remove sensitive data you've accidentally committed!)

~~~
$ cd ~/Desktop/zipf
$ git rm data/frankenstein.txt data/dracula.txt
~~~
{: .language-bash}

Let's not commit this until we've also documented what the user should do instead to
get the data that the code expects to operate on. One option would be to place links to
the text of the two books in the README, and give instructions to download them and place
them in the `data` directory (after creating it, if we don't decide to do that).

However, we'll choose to automate this. To download data from the Internet, we'll use the
`curl` tool, which is installed as part of most Unix-like systems.

> ## `wget`
>
> `wget` is an alternative to `curl` that is more specifically designed for downloading
> files rather than interacting with web servers in general; unfortunately it is not
> installed by default on some operating systems, so to avoid complexity&mdash;both for
> us and for the users of our published code who would also need to install it&mdash;we
> will stick with `curl`.
{: .callout}

To take a file from the web and place it onto the disk in the file `data/frankenstein.txt`,
we can use the command:

~~~
$ curl -L -o data/frankenstein.txt https://www.gutenberg.org/files/84/84-0.txt
~~~
{: .language-bash}

The `-L` flag tells `curl` to follow any redirects it encounters; the `-o` tells it to put
the data into a specified file on disk (otherwise it would output to standard output).
The URL (starting `https://`...) is something you need to find for your particular
data&mdash;in this case, it can be found by searching the 
[Project Gutenberg website][gutenberg].

Now that we can download files without needing to click in a web browser, we have all
the tools we need to automate getting the data for this paper.

~~~
$ nano bin/run_analysis.sh
~~~
{: .language-bash}

~~~
mkdir data
curl -L -o data/frankenstein.txt https://www.gutenberg.org/files/84/84-0.txt
curl -L -o data/dracula.txt https://www.gutenberg.org/files/345/345-0.txt
~~~
{: .language-bash}

We should also add a sentence to the README detailing what data the code will work on.

~~~
$ nano README.txt
~~~
{: .language-bash}

~~~
This script will automatically pull the full text of the two books to
process (Frankenstein and Dracula) from Project Gutenberg (gutenberg.org) and place
them into the `data` directory. Internet access is required for this to work.
~~~
{: .output}

Now that this is done, we mustn't forget to commit it back to the Git repository.

~~~
$ git add README.txt bin/run_analysis.sh
$ git commit -m 'remove data; retrieve automatically from Gutenberg instead'
$ git push origin main
~~~
{: .language-bash}


> ## Getting more data off the web
>
> The procedure above assumes that the data you want to work with is hosted as a simple
> file that you can download. There is a wealth of data available online in more complex
> arrangements; for more detail on how this can be accessed programmatically, see
> the [Introduction to the Web and Online APIs][web-novice].
{: .callout}


## Dummy data

If commercial, privacy, or other constraints prevent you releasing data for your code
to operate on, it is frequently useful to publish dummy data that have the same format
as the actual data your code is designed to work with. This will allow readers to
check how the program behaves in a trial run, even if the data it returns are meaningless.
How to construct dummy data will depend heavily on exactly what kind of analysis you are
performing, so we won't go into more detail about how to create this.

> ## Automated tests
>
> Dummy data is an important part of an automated test system; if you have one, then
> having the other makes more sense. For more information on automated testing, see
> for example,
> [Introduction to automated testing and continuous integration in Python][python-testing-ci]
{: .callout}

> ## To publish or not to publish
>
> Navia is working on some research that compares two open data sets. She would like to
> publish her work in an open, reproducible way. In addition to a typical journal output,
> what else should she publish?
>
> 1. Nothing. Her paper should include all the code needed to reproduce the results.
> 2. A package containing both datasets and the code she used to analyse it. Since the datasets
>    were not originally packaged together and were both used in preparing the work, it is
>    important to include them.
> 3. A package containing the code for the analysis, and a separate package containing the two
>    datasets used in the analysis.
> 4. A package containing just the code used for the analysis, which downloads the open
>    datasets.
> 5. A package containing just the code used for the analysis. The data will be cited in the
>    paper, so is not needed.
>
>> ## Solution
>>
>> Since the data are already openly available, there is no need for Navia to re-publish them.
>> (Indeed, if she did, it would be misrepresenting others' work as her own.)
>> The code is likely to be too detailed to be of interest to many readers of the publication,
>> who will instead be interested in the results of the analysis.
>>
>> So, the answer is either 4 or 5. The exact answer will depend on how the code is written.
>> If it is a general tool for comparing two datasets, then specifying the datasets in the
>> paper may be appropriate. If the code is specific to this publication, then it is more
>> likely to be appropriate to include a tool to fetch the data automatically, since anyone
>> wanting to use the tool will need to use it.
> {: .solution}
>
> Which of the following should Navia cite in her paper?
>
> 1. The datasets used
> 2. The publications where the datasets were first presented
> 3. Whatever is specified in the CITATION file for the datasets
> 4. Any repositories where Navia has published code or data that were used
>    for this paper.
> 5. Any repositories where Navia has published code or data, regardless of
>    whether they were used for this paper.
>
>> ## Solution
>>
>> 1. Yes, these definitely need to be cited
>> 2. If the original publications helps to understand the provenance or
>>    context of the data, or is necessary to support the narrative of this paper,
>>    then yes this could be cited. Otherwise, it would depend on the CITATION file
>>    of the dataset.
>> 3. Yes, it is usually a good idea to cite work in the form requested by the
>>    originators of the data.
>> 4. Yes, publishing your code but not citing it makes it hard to find, so many readers
>>    may not realise it is available. Adding a citation in the paper flags the existence
>>    of the published analysis code, so that the interested reader can see it, while
>>    others do not need to dwell on it.
>> 5. No, only tooling that is specifically relevant to the work in this paper should
>>    be cited.
> {: .solution}
{: .challenge}

> ## Get some data
>
> Use `curl` to download the [Pakistan biomass field survey][biomass-field] from the
> World Bank. Adjust the script in the `challenge` repository so that this
> is done automatically as part of the analysis.
{: .challenge}

{% include links.md %}

[biomass-field]: https://energydata.info/dataset/a27a9b60-706b-4c81-8608-c913d2ed998f/resource/fdef4f22-fe57-49b1-9c42-e5dac79cc90c/download/pakistanbiomassfieldsurvey.csv
[gutenberg]: https://gutenberg.org
[python-testing-ci]: https://edbennett.github.io/python-testing-ci/
[web-novice]: https://edbennett.github.io/web-novice/

---
title: "Reproducible software environments"
teaching: 30
exercises: 20
questions:
- "Why do I need to document the software environment?"
- "How do I document what packages and versions are needed to reproduce my work?"
- "How can I use environment definitions to get started on a new machine?"
objectives:
- "Understand the difficulties of reproducing an undocumented environment."
- "Be able to create a `requirements.txt` and `environment.yml` file."
- "Be able to use `pip` and `conda` to create new environments from definition files."
keypoints:
- "Different versions of packages can give different numerical results. Documenting the environment ensures others can get the same results from your work as you do."
- "`pip freeze` and `conda env export` give plain text files defining the packages installed in an environment, and that can be used to recreate it."
- "Use `pip install -r` and `conda env create` to create a new environment from a definition."
---

So far, we have focused on getting the code that we have written in to a form where another
researcher can run it in the same way. Unfortunately, this isn't enough to ensure that the
analysis we have done is reproducible. Each of the libraries we rely on in our code is
constantly being developed and updated, as is the Python language, and the operating
system that it runs on. As this happens, the default version to be installed on request
will change. While minor version changes typically do not introduce any incompatibilities,
eventually almost all software needs to introduce changes that break backwards compatibility
in some way in order to develop and improve functionality available to new code.
In the best case this will cause cosmetic changes, and the next best the code will fail
to work at all because some function has been renamed, relocated, or removed. The worst
case is when the code still runs without error, but gives a very different answer to that
obtained with the old version of the library.

To make our analysis fully reproducible, we need to reproduce the entire computational
environment that was used to perform it. In principle, this includes not only the version
of Python and the packages that were installed, but also the operating system and the
underlying hardware! For now, we will focus on reproducing as much of the original
environment as we can.

## Exporting your environment

The `pip` package manager for Python gives us a way of defining the set of Python packages
currently installed, so that we can install the same set elsewhere. The command to do this
is `pip freeze`. By default it outputs to standard output; by convention, we place the
output into a file called `requirements.txt`.

~~~
$ pip freeze > requirements.txt
~~~
{: .language-bash}

Meanwhile, the Conda package manager also gives a way of exporting the current environment.
This includes more than just Python packages; it also includes the specific Python version,
as well as some dependency packages that would otherwise need to be installed separately.
We can export our Conda environment as:

~~~
$ conda env export -f environment.yml
$ cat environment.yml
~~~
{: .language-bash}

By convention the filename for conda environments is `environment.yml`; this file is in
YAML format, and as we can see includes some more information than the `requirements.txt`.
Note that in general we will prefer `conda env export` for Conda environments, as
`pip freeze` gets confused by the way that Conda installs packages. It is also possible to
construct a `requirements.txt` file by hand, but you must be careful to specify which
package versions you need, as just the package names will not fully define your environment.

## Trimming down an environment

We can see that both of these files are very long; this is because we have exported the
Anaconda base environment. This comes with a huge array of packages that could be useful
for doing scientific computation. However, it means that it will be a lot of data to
download for anyone who wants to recreate the environment, and a lot of that data will not
be needed as it is packages we haven't used. Instead, let's create a new, clean environment
to export, starting from Python 3.9

~~~
$ conda create -n zipf python=3.9
$ conda activate zipf
~~~
{: .language-bash}

Now, we can install into this environment only the packages that we refer to in our
Zipf code. If we haven't documented all the requirements in the README yet, we can work
out what these are by looking for any `import` statements in our code, and identifying
those that are not either provided by our own code or by the Python standard library.

~~~
$ grep -r --no-filename import bin | sort | uniq
~~~
{: .language-bash}

~~~
from collections import Counter
import argparse
import csv
import matplotlib.pyplot as plt
import pandas as pd
import string
import sys
import utilities as util
~~~
{: .output}

Of these, `collections`, `argparse`, `csv`, `string`, and `sys` are all part of the Python
standard library, and `utilities` is part of our own code. That leaves Matplotlib and Pandas.
Let's install these with Conda:

~~~
$ conda install pandas matplotlib
~~~
{: .language-bash}

It's a good idea to do a quick check now that this environment can indeed run our analysis,
in case we've forgotten anything:

~~~
$ bash ./bin/run_analysis.sh
~~~
{: .language-bash}

Let's export the environment again in both formats:

~~~
$ pip freeze > requirements.txt
$ conda env export -f environment.yml
$ cat requirements.txt
$ cat environment.yml
~~~
{: .language-bash}

These files are now much shorter, so will be much quicker to install.

## Creating an environment from a definition

Having exported our environment, it would be useful to check the reverse process. How do
we turn an environment definition into an environment we can use? We can use Conda to
achieve both of these.

> ## Other virtual environments
>
> For pip and  `requirements.txt`, strictly speaking Conda is not required; any number
> of solutions (e.g. `venv`, `pipenv`) could be used instead. However, since we are
> currently using Anaconda to provide Python to us, the Conda-based solution is likely
> to be a little cleaner.
{: .callout}

To test the pip-based solution, we first create a new environment with only Python, and
activate it. Then, we tell pip to install from our requirements file:

~~~
$ conda create -n pip-test python=3.9
$ conda activate pip-test
$ pip install -r requirements.txt
~~~
{: .language-bash}

We can do a similar thing for the Conda export:

~~~
$ conda env create -f=environment.yml -n conda-test
$ conda activate conda-test
~~~
{: .language-bash}

Finally, we can re-check that the created environment runs the analysis just as well as the
original:

~~~
$ bash ./bin/run_analysis.sh
~~~
{: .language-bash}

Now that we've tested that it works, we should add the environment to our repository.

~~~
$ git add environment.yml
$ git commit -m 'define software environment'
$ git push origin main
~~~


## Running on someone else's computer

We've now verified that we can recreate the computational environment we used for a piece
of work. However, we have only done this on our own computer. Since other researchers won't
have access to our computer, it would be good if we could test on neutral ground, to check
that the analysis isn't specific to our own machine, but will run elsewhere as well.
Even better would be if we could also run any researcher's (public) code there, to avoid
needing to download each and fill our disk with Conda environments as we explore what open
software is available.

There is a tool that will help with this called [Binder][binder]. This is a piece of
software that will identify the environment requirements (looking for files like
`requirements.txt` and `environment.yml`) and automatically build a "container" that
runs exactly the software requested. No matter where in the world you are, it will
end up with the same operating system and package versions. Once it has built the
environment, it will then launch a Jupyter Notebook environment for you to run the
code from the repository. The primary design of Binder is to enable exploring others'
data, but it also works for testing environments and running code outside of notebooks.

There is a public Binder instance available at [MyBinder][mybinder], which we can use for
testing. (This is run on a relatively small budget, so sometimes it is short on resources;
you shouldn't treat it as a free resource to run long-running computations on! If you need
to run Binders regularly, or need compute resources bigger than what you have on your own
machine, then talk to the research computing group at your institution, who are likely to
have suggestions on where to turn.)

To test our `zipf` repository and its environment, we can enter the URL to the repository
into the [MyBinder home page][mybinder]. In principle we could test the repository state
at any point in its history, and launch a specific notebook if we wanted. For now, we will
test the most recent commit, and launch the Binder without targeting any one notebook.

If you want to encourage others to explore your data with Binder, the home page also gives
you the option to add a badge to your README that will take users directly to a new Binder
for the repository without needing to type the details in by hand.



> ## Spot the difference
>
> Take a look at the following plot of cattle populations by country, which was generated
> by [a Python program using Matplotlib](../files/cattlepopulations.py).
>
> ![A bar chart for cattle population by country or region, showing bars for India, Brazil, USA, China, EU, and Argentina. The country labels are offset to the left of the bars, which are royal blue.](../fig/cattle.png)
>
> Try and run the `cattlepopulations.py` file yourself. Does the output you see look the same
> as the one above? If not, why not?
>
>> ## Solution
>>
>> Matplotlib changed its default style set with version 2.0, so the colours of plots made
>> with the default styles changes between the old and new versions. Also, the default
>> behaviour of bar charts is to centre the labels, where to achieve this before you needed
>> to do extra work.
>>
>> This is why we must specify our environment when we share our code&mdash;otherwise,
>> other people will get different results to us. In this case it was just the formatting
>> of a plot, but in some cases it will be the actual numerical results that will differ!
>>
>> As an aside,
>> in fact there have been other changes to bar charts so that they are easier to make.
>> Specifically, the `positions` variable is no longer necessary at all, you can use:
>>
>> ~~~
>> plt.bar(countries, cattle_numbers)
>> ~~~
>> {: .language-python}
>>
>> and achieve the same results as the file above did.
> {: .solution}
{: .challenge}

> ## Containers
>
> A popular, but somewhat more involved, alternative to using these kinds of environment
> is to use _containerisation_, with products such as Docker and Apptainer (previously
> Singularity). This is beyond the scope of what we're covering in this lesson, but
> the Carpentries Incubator provides an excellent
> [lesson on getting started with Docker][incubator-docker] that is worth looking at
> if you are interested.
>
> In fact, Docker is what powers Binder&mdash;Binder is a web wrapper around a tool that
> takes a Git repository, identifies the requirements, and builds a Docker container
> that meets them. If your requirements are too complex to be contained in a Conda
> environment definition, then you may want to explore defining the container directly
> instead.
{: .callout}

> ## Define some environments
>
> Use `pip freeze` and `conda env export` to define `requirements.txt` and
> `environment.yml` files for your base Anaconda environment. How long are they?
>
> Create a new Conda environment with just the packages you need for the `challenge`
> repository, and export `requirements.txt` and `environment.yml` files. How long
> are these files compared to the ones for the base Anaconda environment?
>
>> ## Solution
>>
>> TODO
> {: .solution}
{: .challenge}


{% include links.md %}

[binder]: https://mybinder.readthedocs.io/en/latest/
[incubator-docker]: http://carpentries-incubator.github.io/docker-introduction
[mybinder]: https://mybinder.org

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

> ## Spot the difference
>
> Take a look at the following plot of cattle populations by country, which was generated
> by [a Python program using Matplotlib](files/cattlepopulations.py).
>
> ![A bar chart for cattle population by country or ergion, showing bars for India, Brazil, USA, China, EU, and Argentina. The country labels are offset to the left of the bars, which are royal blue.](fig/cattle.png)
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


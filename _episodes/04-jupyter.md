---
title: "Jupyter Notebooks and automation"
teaching: 15
exercises: 10
questions:
- "How does using Jupyter Notebooks affect automation and reproducibility?"
- "How do I put a Jupyter Notebook into a repository?"
- "What changes can I make to a Jupyter Notebook to improve automation?"
objectives:
- "Understand what data are included in a Jupyter Notebook, and how to remove it"
- "Be able to adjust notebooks to reduce manual intervention"
keypoints:
- "Jupyter Notebook can be run in a non-linear order, and store their output as well as their input"
- "Remove all output from notebooks before committing to a pure code repository."
- "Test notebooks from a fresh kernel, or run them from the command line with `runipy`."
---

> ## Bringing matters to order
>
> Sanjay is investigating some work by his colleage Prof. Nuss, whose conclusions
> he disagreed with. Prof. Nuss included the following figure in a publication
> draft, which Sanjay is suspicious of.
>
> ![A graph of Relative maize exports by country, showing bars for USA, Argentina, Brazil, Ukraine, France, Russia, Romania, and Hungary. Approximate numbers are 1.0, 0.45, 0.2, 0.2, 0.2, 0.1, 0.1, 0.05](../fig/maizeexports.png)
>
> In response to a query from Sanjay, Prof. Nuss provides [the Jupyter notebook that she used to perform the analysis](../files/maizeexports.ipynb).
>
> Sanjay finds that when he runs Prof. Nuss's code, it doesn't give the same plot As
> is included in the paper draft. What has happened to cause this?
>
>> ## Solution
>>
>> The cell to produce the bar plot was run after the cell defining the subsidy areas
>> had been run, without re-running the definition of the countries, meaning that the
>> variable `data` had the wrong contents.
> {: .solution}
>
> How could this error have been avoided?
>
>> ## Solution
>>
>> There's more than one way this could have been avoided:
>>
>> * Prof. Nuss could (and should) make sure to run the notebook end-to-end before
>>   using the output in a publication
>> * Avoiding using the same variable name to represent two different sets of data
>>   would have avoided the problem (as well as potentially making the code easier
>>   to read)
>> * Keeping related data together, for example in a Pandas DataFrame, would avoid
>>   the possibility of part of the data being replaced but the metadata not.
>>   Reading in the data from a file could help with this.
> {: .solution}
{: .challenge}

> ## Commit a notebook
>
> Add the notebook from the previous challenge to the `challenge` repository.
> Before you commit, do the following cleanup tasks:
>
> * Remove any output from the notebook
> * Adjust the notebook to output to files rather than the screen
> * Attribute authorship for code that you didn't write
> * Add documentation of what the notebook does
> * Adjust the run instructions to include the new tool
{: .challenge}


{% include links.md %}


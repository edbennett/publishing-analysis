---
title: "Documentation and automation"
teaching: 20
exercises: 10
questions:
- "How do I tell other researchers how to use my code?"
- "How can I make it easier for others (or me) to run my full analysis?"
objectives:
- "Be able to write a README documenting how to run a tool."
- "Be able to write a shell script to automate an analysis process."
- "Understand how to remove manual editing steps from processes."
keypoints:
- "Use a README or similar file to explain the essential steps of running your analysis."
- "Use shell script or similar to automate the steps you would take to perform your analysis."
- "Use command-line arguments or other parameters instead of having to manually edit lines of code."
---

> ## Truths about READMEs
>
> Take a look at the following statements. Which do you think are true?
>
>  1. If I write a good enough README, then I'll never need any other documentation
>  2. If I write a shell script that does my entire analysis, I don't need a README
>  3. If I don't have a README, my repository is useless.
>  4. A README should have instructions on using the software, and information on what
>     it does.
>  5. A README should be plain text only. Other documentation can have more formatting.
>
>> ## Solution
>>
>> 1. False. While a good README may be enough documentation for a very small project,
>>    more frequently you will benefit from other types of documentation; for example,
>>    comments in your code, and more detailed descriptions for more technical aspects.
>> 2. False. Even if a shell script completely reproduces your outputs, you should have
>>    a README to point the user at the right script to run, and to describe what to expect.
>> 3. False. Having your code in version control and shareable is a good step! But without
>>    a README, it's likely that others will find your code hard to use or understand.
>>    (As will you if you return to it after a few months or years!)
>> 4. True. Normally the ordering is reversed, though, with the description of the purpose
>>    of the code coming before the details on using it.
>> 5. False. Historically READMEs were plain text files, but now they take a variety of
>>    formats; many will use Markdown, which allows headings, bold, italic, images, etc.
> {: .solution}
{: .challenge}


> ## `make` it better
>
> A more powerful alternative to using shell scripts to document and automate your
> analysis process is to use a workflow management tool. A simple one of these that
> is frequently used in software development is called Make; Software Carpentry has
> [a lesson on getting started with Make][make-novice].
>
> More powerful again are tools like [Snakemake][snakemake] and [Nextflow][nextflow],
> which are used for very intricate scientific analyses with very many steps.
>
> We don't have time to look into these tools in more detail in this lesson, but
> if you find that your shell scripts are getting too long or intricate, then it
> it might be worth your time to look into using one of these tools.
{: .callout}


> ## Removing hardcoded data
>
> Take a look at the `calc_fractal.py` file in the repository we worked on in previous
> challenges. Currently this will generate the files needed for `fig3.py`, but must
> be edited to allow `fig1.py` and `fig2.py` to run correctly.
>
> Adapt `calc_fractal.py` to allow this parameter to instead by set by a command-line
> argument.
>
> Now, adapt the instructions in the README into a shell script to allow the analysis
> to be run automatically.
>
> What other change would be needed to allow this analysis to be run unattended?
>
>> ## Solution
>>
>> TODO: code solution
>>
>> Currently the images are shown on the screen; the user must save and close
>> each image. It would be better to use `savefig` to save the figure to disk,
>> instead.
{: .challenge}

{% include links.md %}

[make-novice]: https://swcarpentry.github.io/make-novice/

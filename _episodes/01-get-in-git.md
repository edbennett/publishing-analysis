---
title: "Get it in Git"
teaching: 20
exercises: 15
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
- "Use `git init`, `git add`, `git commit`, `git remote add`, and `git push`, as discussed in the [Software Carpentry Git lesson][git-novice]"
- "Include all the code that you have written to use in this analysis."
- "Leave out e.g. temporary copies, old backup versions, files containing secret or confidential information, and supporting files generated automatically."
---

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



> ## What to include
>
> Anneka has a folder containing the analysis that she has performed,
> and that she is preparing to publish as a journal article. It contains
> the following files and subfolders:
>
> * `fig5.py`, which plots a graph used in the paper draft
> * A folder called `__pycache__`; Anneka isn't sure what this is
> * `analyse_slides.py`, which doesn't generate anythin included in the
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
> Download [this example archive of code](files/challenge.zip) and extract it to
> a convenient location on your computer. This will give you a directory
> containing a small piece of research software, and the data it was last used
> to analyse.
>
> Turn this directory into a repository and push it to GitHub.
>
> Remember to exclude any files that shouldn't be in the code repository.
{: .challenge}

{% include links.md %}


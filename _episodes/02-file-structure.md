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


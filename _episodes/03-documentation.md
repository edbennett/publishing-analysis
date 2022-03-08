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

Sharing your code and giving it a comprehensible structure is a great first and second
step, but without some guidance on how to run your code, then others will find it very
difficult to reproduce your steps. To you it might be obvious that you first run
`incomprehensible_longname.py` and then `another_long_name.py`, but it likely won't be
to anyone else.

Thus, we need to make sure to explain to others how to make use of the code that you
have shared with them. There are two main ways to do this: descriptively, and
programmatically.

Describing in English (or your preferred human language) how to use the software has
the advantage that you can do it relatively quickly, from memory, and with little
testing, since the "code" you are writing runs on a human brain, which can figure
things out if they are unclear. The disadvantage is that you _can't_ do very much
testing; you don't know how someone else will interpret your instructions.
Conversely doing things programmatically so that the complete analysis is fully
automated takes more effort up front, but again makes it even easier to run your code.

To start with, let's see what a descriptive README of the current project might look
like.

~~~
To reproduce the figures in the publication, follow these steps:

1. Create a `results` directory

2. Use `countwords.py` to count the words in `frankenstein.txt`.

      python countwords.py > results/frankenstein.csv

3. Use `plotcounts.py` to plot the resulting file.

      python plotcounts.py

4. Save the plot as `frankenstein.pdf`.

5. Edit `countwords.py` and `plotcounts.py` to replace `frankenstein` with `dracula`.

6. Repeat the above instructions to generate `dracula.csv` and plot `dracula.pdf`.
~~~
{: .output}

Let's commit this:

~~~
# git add README
# git commit -m 'add run instructions to README'
# git push origin main
~~~
{: .language-bash}

Once again, these instructions are substantially better than what we had before. Then,
we would have had to pore over the code to work out what it did, and guess at what
exactly was done. If you have time to write this but not to do more work to automate
the analysis, then it is definitely work worth doing.


## Avoid manually editing parameters

While having instructions is good, it would be good if we could remove at least
some of the manual effort from this process.

The most obvious issue here is that it is rather laborious to have to edit a source
file in order to change which analysis is done. This is very error-prone, and risks
others getting different results to you and challenging your work (or worse, you
making an error in your own work and needing to revise your results after publication).
In this project you may end up with the wrong book name on a figure; in others
the parameters may be numbers, so the error may become even more difficult to spot.

To avoid this, we would like our programs to take command-line arguments rather than
having parameters hard-coded. We saw in Software Carpentry one way of doing this,
by using `sys.argv`. That works, but can be a little fragile. Instead, here we will
introduce the `argparse` module from the Python standard library; this gives a way
of defining in more depth what arguments you want your program to accept.

This is slightly more verbose than using `sys.argv` directly, but gives an improvement
in usability that makes it more than worthwhile.

Let's start with `countwords.py`. To begin, we add `argparse` to our imports at the top
of the file.

~~~
import argparse
~~~
{: .language-python}

Now, where we want to start doing work, we will create an `ArgumentParser`, specify
what arguments we want it to accept, and then parse them out from our input.

~~~
parser = argparse.ArgumentParser(description=(
    "Count the occurrences of all words in a text "
    "and write them to a CSV-file."
))
parser.add_argument('infile', type=argparse.FileType('r'),
                    nargs='?', default='-',
                    help='Input file name')
parser.add_argument('-n', '--num',
                    type=int, default=None,
                    help='Output only n most frequent words')
args = parser.parse_args()
~~~
{: .language-python}

Working through this line-by-line:

* We create an `ArgumentParser`, giving it a description of what our program does.
* We add the `infile` argument, which will give us a file. If no argument is specified,
  then the default value is used, which in this case means "read from standard input".
  We also give it a description.
* We add the `--num` optional argument, which can also be referred to more briefly as `-n`,
  will be interpreted as an integer, defaults to `None`, and has a help message.
* We use all of this to interpret the command line that the program was run with.

Finally, we can use `args.infile` instead of needing to use `open()`, since `argparse`
handles the file opening by itself. We then use `args.num` in place of the hard-coded 100.

~~~
word_counts = count_words(args.infile)
util.collection_to_csv(word_counts, num=args.num)
~~~
{: .language-python}

Currently the README is no longer correct, since the program doesn't automatically
look for `frankenstein.txt` any more. So, let's hold off committing it for now.

> ## Try it yourself
>
> Get the `plotcounts.py` program to also use `argparse`. Allow the user to specify
> the `xlim` argument to `scatter` in addition to the `infile`.
>
>> ## Solution
>>
>> ~~~
>> parser = argparse.ArgumentParser(description="Plot word counts")
>> parser.add_argument('infile', type=argparse.FileType('r'),
>>                     nargs='?', default='-',
>>                        help='Word count csv file name')
>> parser.add_argument('--xlim', type=float, nargs=2,
>>                     metavar=('XMIN', 'XMAX'),
>>                     default=None, help='X-axis limits')
>> args = parser.parse_args()
>> ~~~
>> {: .language-python}
> {: .solution}
{: .challenge}


## Avoid interactivity

The next biggest issue with this software is that you have to manually save the
plot output. This is common in tools used interactively for data exploration, but
once you're publishing your analysis then it makes more sense to save to a file
directly from the program.

This isn't a huge change. In most cases, we can replace `plt.show()` with 
`plt.savefig(filename)`. If we are generating multiple plots we will need to be more
careful, as `savefig` doesn't start a new plot in the way that `show()` does.

Looking at `plotcounts.py`, we can also avoid hardcoding the filename to write by
adding an extra argument to the `ArgumentParser`.

~~~
parser.add_argument('--outfile', type=str,
                    default='plotcounts.png',
                    help='Output image file name')
~~~
{: .language-python}

Note that now we don't use the `FileType`, since we don't want `argparse` to open
the file&mdash;Matplotlib does this for us, so we just need a filename.

Now, we replace the last line with

~~~
plt.savefig(args.outfile)
~~~
{: .language-python}

Since the program is ending anyway, we don't need a `plt.close()` here.

## Avoid bare code

Frequently we define functions in Python files. In order to import these into other
pieces of Python code, Python runs the entire file top-to-bottom.

The effect of this is that if there is any code not within a function (or other block
that would prevent it doing so), then it will automatically run when we import the
module. For example, in `countwords.py`, the word count would be run even if we didn't
want it to be.

As such, you will frequently see guards of the form `if __name__ == '__main__'` in
programs. This checks to see whether the Python file is being run directly as a program,
or imported into another file as a module. These aren't always needed&mdash;in larger
programs many programmers will try to keep "tools" that can be run by the user entirely
separate from shared libraries that get imported. But in the kinds of code written for
research they are frequently useful.

Let's update `countwords.py` now:

~~~
def main(args):
    """Run the command line program."""
    word_counts = count_words(args.infile)
    util.collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=(
        "Count the occurrences of all words in a text "
        "and write them to a CSV-file."
    ))
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output only n most frequent words')
    args = parser.parse_args()
    main(args)
~~~
{: .language-python}

> ## Try it yourself
>
> Adjust the `plotcounts.py` file to use `if __name__ == '__main__'` guards.
{: .challenge}


## Use a shell script

The final step (for this lesson at least) in documenting your analysis through automation
is to write a shell script that will run all the steps needed in turn.

Now that we have adjusted the tools to not need direct interaction, this becomes relatively
short:

~~~
$ nano bin/run_analysis.sh
~~~
{: .language-bash}

~~~
mkdir results
for book in dracula frankenstein
do
    python countwords.py ${book}.txt --num 100 > results/${book}.csv
    python plotcounts.py results/${book}.csv --outfile results/${book}.pdf
done
~~~
{: .language-bash}

Now we can edit the README again:

~~~
To reproduce the figures in the publication, run the command:

    bash bin/run_analysis.sh

Results will be placed in a `results/` directory.
~~~
{: .output}

Now that the README and the code are consistent, we can commit this:

~~~
$ git add countwords.py plotcounts.py README
$ git commit -m 'automate analysis'
$ git push origin main
~~~
{: .language-bash}

Note that for the sake of simplicity today we have done this as a single pass, but
we could just as well have done this in smaller steps. We could update one tool to be
easier to run automatically, adjust the README to match, commit, push. Then move on to
the next one, and so on, until we get to the point we have now reached.

> ## Empty directories
>
> We had a shell script here create the `results` directory. Sometimes it is convenient
> to provide an empty directory, rather than having to create it. Since Git only stores
> files, not directories, by convention this is done by placing a hidden file called
> `.git_keep` into the directory and adding it to the repository.
>
> ~~~
> $ mkdir results
> $ touch results/.git_keep
> $ git add results/.git_keep
> $ git commit -m 'add an empty results directory'
> $ git push origin main
> ~~~
> {: .language-bash}
{: .callout}



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

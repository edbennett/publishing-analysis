---
title: "Verifying your analysis"
teaching: 20
exercises: 20
questions:
- "How can I use environment definitions to get started on a new machine?"
- "How can I check that my analysis is working?"
- "How do I verify that the environment definition is correct?"
objectives:
- "Be able to use `pip` and `conda` to create new environments from definition files."
- "Be able to test that an analysis gives correct result."
- "Be able to use MyBinder to test code in a clean environment."
keypoints:
- "Use `pip install -r` and `conda env create` to create a new environment from a definition."
- "Running your full analysis end-to-end in a clean environment will highlight most problems."
- "Binder services (e.g. MyBinder) will create an environment in the cloud based on your definiiton."
---

## Creating an environment from a definition

Having exported our environment, it would be useful to check the reverse process. How do
we turn an environment definition into an environment we can use? Conda gives us the tools
to do this, too.

~~~
$ conda env create -f environment.yml -n conda-test
$ conda activate conda-test
~~~
{: .language-bash}

Then, we can re-check that the created environment runs the analysis just as well as the
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

> ## What about `requirements.txt`?
>
> If you have a `requirements.txt` instead of an `environment.yml`, then you can
> install the required packages with Pip using
>
> ~~~
> $ pip install -r requirements.txt
> ~~~
> {: .language-bash}
>
> This will work inside a Conda environment, but Conda is not required&mdash;any number
> of solutions (e.g. `venv`, `pipenv`) could be used instead. 
{: .callout}


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
The environment takes a while to build, as it has a number of setup steps.
(Unfortunately, the MyBinder service has limited resources, so sometimes will fail to
build or fail to load due to lack of capacity or other maintenance issues.)

If you want to encourage others to explore your data with Binder, the home page also gives
you the option to add a badge to your README that will take users directly to a new Binder
for the repository without needing to type the details in by hand.



> ## Testing, testing
>
> Create a clean Conda environment on your computer based on the specification,
> in the `challenge` repository, and use it to re-run the analysis. Does it work,
> and give the same results as when running it in the environment you were previously
> using?
>
> If not, try to work out (or ask a helper) why the results are different.
{: .challenge}

> ## Another Binder
>
> Start a MyBinder instance for your `challenge` repository. Try running the full workflow
> on MyBinder. Does it gives the same results as you see running on your own machine?
>
> If not, try to work out (or ask a helper) why the results are different.
{: .challenge}

{% include links.md %}

[binder]: https://mybinder.readthedocs.io/en/latest/
[mybinder]: https://mybinder.org

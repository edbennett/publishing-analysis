---
title: "Introduction"
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
>> Since the data are already openly available, there is no need for Quang to re-publish them.
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

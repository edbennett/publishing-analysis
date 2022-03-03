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
FIXME

{% include links.md %}


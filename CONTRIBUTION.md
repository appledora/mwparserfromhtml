# Contributing guidelines

## Before contributing

Welcome to [`mwparserfromhtml`](https://gitlab.wikimedia.org/repos/research/html-dumps)! Before sending your pull requests, make sure that you __read the whole guidelines__. If you have any doubt on the contributing guide, please feel free to [state it clearly in an issue](https://gitlab.wikimedia.org/repos/research/html-dumps/-/issues). The intent of this document is to help get you started. Don't be afraid to reach out with questions – no matter how "silly.” Just open a PR whether you have made any significant changes or not, and we'll try to help. You can also open an issue to discuss any changes you want to make before you start.

## Contributing

### Contributor

We are very happy that you considered contributing to this repo! This repository is referenced and will be used by learners from all over the globe. Being one of our contributors, you agree and confirm that:
- Your work will be distributed under [MIT License](LICENSE.md) once your pull request is merged
- Your submitted work fulfils or mostly fulfils our styles and standards

__New implementation__ is welcome! For example, new solutions for a problem, different representations for a data structure or algorithm designs with different complexity but __identical implementation__ of an existing implementation is not allowed. Please check whether the solution is already implemented or not before submitting your pull request.

__Improving comments__ and __writing proper tests__ are also highly welcome.

### Contribution

We appreciate any contribution, from fixing a grammar mistake in a comment to implementing complex algorithms. Please read this section if you are contributing your work.

Your contribution will be tested by our [automated testing on GitLab Flow](https://docs.gitlab.com/ee/topics/gitlab_flow.html) to save time and mental energy.  After you have submitted your pull request, you should see the Gitlab Flow pipeline start to run at the bottom of your submission page.  If those tests fail, then click on the ___details___ button try to read through the pipeline output to understand the failure.  If you do not understand, please leave a comment on your submission page and a community member will try to help.

Please help us keep our issue list small by adding fixes: #{$ISSUE_NO} to the commit message of pull requests that resolve open issues. Also, name your PR branch using #ISSUE_NO-YOUR-DESCRIPTION format to help gitlab auto close the corresponding issue.

### Basic Guidelines

- Contributions of any size are welcome! Fixed a typo?
  Changed a docstring? No contribution is too small.
- Try to limit each pull request to *one* change only.
- *Always* add tests and docs for your code.
- Make sure your proposed changes pass our CI_.
  Until it's green, you risk not getting any feedback on it.
- Once you've addressed review feedback, make sure to bump the pull request with a comment so we know you're done.


## Local Development

* Clone the project either with __SSH__

    ``` > git@gitlab.wikimedia.org:repos/research/html-dumps.git```

    or with __HTTPS__

    ``` > https://gitlab.wikimedia.org/repos/research/html-dumps.git ```

* Navigate inside the cloned repo folder. Make sure `python V3.8` and `pip3` is installed. To setup the package dependencies run :

    ``` > pip3 install -r reqirements.txt```

### Code style

We use `precommit` package to enforce our styleguides through several hooks. We use `flake8` hook to enforce `PEP 8` conventions, `isort` hook to sort our imports, and we use the `black` formatter hook with a line length of 112 characters. Static typing is enforced using the `mypy` hook.
Use of static __type hinting__ is heavily encouraged.

- If you want to run pre-commit on its own, you can do so by calling it directly:

```bash
  $ pre-commit run --all-files
```
Code that does not follow these conventions won't pass our CI.


### Tests

- We use pytest_ for testing. For the sake of consistency, write your asserts as ``actual == expected``:

```python

    def test_add_one():
       assert func(2) == 3
       assert func(4) == 5
```
- You can run the test suite with pytest:

```bash

   $ python -m pytest

```

> **_NOTE:_**  This guideline is heavily inspired by the amazing [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) repository and Slavina's fantastic [python-mwsql](https://github.com/mediawiki-utilities/python-mwsql)!!

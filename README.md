# learn-python-the-right-way
![MP1](https://github.com/sciencejiho/CS421/workflows/MP1/badge.svg)&nbsp;![MP2](https://github.com/sciencejiho/CS421/workflows/MP2/badge.svg)&nbsp;![MP3](https://github.com/sciencejiho/CS421/workflows/MP3/badge.svg)&nbsp;![MP4](https://github.com/sciencejiho/CS421/workflows/MP4/badge.svg)&nbsp;![MP5](https://github.com/sciencejiho/CS421/workflows/MP5/badge.svg)

Practice Problems and solutions of the the book "Learn Python the Right Way".

## Table of contents

* [What's included](#tree)
* [Contributing to learn-python-the-right-way](#contribute)
* [Git Workflow](#workflow)

## <a name="tree"></a> What's included

```text
Unit 01/
├── judge
└── practice
Unit 02/
├── judge
└── practice
Unit 03/
├── judge
└── practice
Unit 04/
├── judge
└── practice
...
```

## <a name="contribute"></a> Contributing to learn-python-the-right-way
Want to file a bug, contribute some code, or improve documentation? Excellent! Read up on our guidelines for [contributing][contributing].

## <a name="workflow"></a> Git Workflow
The core idea behind the Feature Branch Workflow is that all feature development should take place in a dedicated branch instead of the master branch. This encapsulation makes it easy for multiple developers to work on a particular feature without disturbing the main codebase. It also means the master branch will never contain broken code, which is a huge advantage for continuous integration environments.

#### release
This branch contains the machine problems from the semester, as well as any other code examples staff members want to send to the students.

### Main Branches
* master
* develop

#### master
This is the main branch where the source code of HEAD always reflects a production-ready state. I consider this branch to be the main branch where the source code of HEAD always reflects a state with the latest delivered development changes for the next release. Some would call this the “integration branch”.

#### develop
This branch is the branch where all the development takes place. When the source code in the develop branch reaches a stable point and is ready to be released, all of the changes should be merged back into master somehow and then tagged with a release number. How this is done in detail will be discussed further on.

### Feature Branches
* feature
* hotfix

#### feature
Feature branches (or sometimes called topic branches) are used to develop new features for the upcoming or a distant future release. When starting development of a feature, the target release in which this feature will be incorporated may well be unknown at that point. The essence of a feature branch is that it exists as long as the feature is in development, but will eventually be merged back into develop (to definitely add the new feature to the upcoming release) or discarded (in case of a disappointing experiment).

Feature branches typically exist in developer repos only, not in origin.

#### hotfix
Hotfix branches are very much like release branches in that they are also meant to prepare for a new production release, albeit unplanned. They arise from the necessity to act immediately upon an undesired state of a live production version. When a critical bug in a production version must be resolved immediately, a hotfix branch may be branched off from the corresponding tag on the master branch that marks the production version.

The essence is that work of team members (on the develop branch) can continue, while another person is preparing a quick production fix.

----------

[contributing]: https://github.com/sciencejiho/learn-python-the-right-way/blob/master/CONTRIBUTING.md

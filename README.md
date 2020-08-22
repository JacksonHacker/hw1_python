# Setup your environment

You will need to set up an appropriate coding environment on whatever computer
you expect to use for this assignment.
Minimally, you should install:
 
* [git](https://git-scm.com/downloads)
* [Python (3.8 or higher)](https://www.python.org/)
* [Pytest](https://docs.pytest.org/en/stable/)


# Check out a new branch

Before you start editing any code, you will need to create a new branch in your
GitHub repository to hold your work.

1. Go to the repository that GitHub Classroom created for you. You should have received an email/link and you are most probably reading this there. It should look like
`https://github.com/cs4583fall2020/python-hw3-<your-username>`, where
`<your-username>` is your GitHub username. 
[Create a branch through the GitHub interface](https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/).
2. Name your `<branch>` as `lastname_firstname_dev`
2. Clone the repository to your local machine and checkout the branch you
just created. Your command must be similar to :
   ```
   git clone -b <branch> https://github.com/cs4583fall2020/python-hw3-<your-username>.git
   ```

# Write your code

You will implement one function each for each of the sub questions of qns 5, Eg:` def q5_1(self,query):` inside 
the class `InvertedIndex`(src/main/python/edu/arizona/cs/invertedindex.py). These functions should return the documents in the right order , as asked in the question. 

Also, you **should not edit** these files:
- `runAllTests.sh`
- `.travis.yml`
- `src/main/resources/Docs.txt`
- `src/test/python/edu/arizona/cs/test_q5.py`

**Note: The file `src/main/resources/Docs.txt` is the input file you must use as per hw1 guidelines. Please don't edit it or move it.**




### TL;DR: If you have already started coding, your code should have ideally been returning document names as results. Now all you have to do is return your results as strings via the respective `q5_*` functions.

# Test your code

Tests have been provided for you in the `src/test/python/edu/arizona/cs/test_q5.py` file.
To run all the provided tests, run the ``pytest`` script from the parent directory containing `src/` or any of its subdirectories

If your code passes the test case, you will see output like:
```
============================= test session starts ==============================
platform darwin -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /Users/mordor/tawork/hw1/hw1_python
collected 3 items                                                              

src/test/python/edu/arizona/cs/test_q5.py ...                            [100%]

============================== 3 passed in 0.10s ===============================
```

# Submitting your code

As you are working on the code, you should regularly `git commit` to save your
current changes locally and `git push` to push all saved changes to the remote
repository on GitHub.    

To submit your assignment,
[create a pull request on GitHub](https://help.github.com/articles/creating-a-pull-request/#creating-the-pull-request).
where the "base" branch is "master", and the "compare" branch is the branch you
created at the beginning of this assignment.
Then go to the "Files changed" tab, and make sure that all your changes look as you would expect them
to.
There are test cases that will be run automatically (via., [travis](https://travis-ci.com/))
when a pull request is submitted. 
These are the same as `sbt test`. 
So if your code passed `sbt test` in your machine, 
it’s highly likely that it will pass in github. Nevertheless 
you should make sure that you see a green tick mark or a message 
saying “All Checks Have Passed”. Else close the pull request, fix the errors, and raise another pull request.
**Do not merge the pull request.**

Your instructor will grade the code of this pull request. 
Pull requests submitted after the deadline won’t be considered.

# Grading

Qn1 of this assignment will be graded primarily on their ability to pass the tests that
have been provided to you on github after the pull request.
Assignments that pass all, and with the corresponding code implementing the correct logic, will receive at least 90% of the
possible points.

To get the remaining of the points, the scores you return for all the documents will be checked.

# HelloActions-Arian

A simple "Hello World" project that runs on **GitHub Actions**. When code is
pushed to `main` (or the workflow is started manually), GitHub spins up a
virtual machine, installs Python, runs `hello.py`, and shows the output in the
Actions log.

## Program output

```text
Hello GitHub Actions Student!
This program is running inside GitHub Actions.
```

The program reads the name from the `WHO_TO_GREET` environment variable and
falls back to a default value when that variable is not set.

## Workflow explanation

**1. What is the purpose of the `on` section?**
It defines the events that trigger the workflow — the conditions under which
GitHub Actions decides to run it. Here it runs on a push to `main` and on manual
dispatch.

**2. What does `workflow_dispatch` do?**
It lets the workflow be started manually from the Actions tab with the "Run
workflow" button, instead of waiting for a push.

**3. What does `runs-on` specify?**
The type of virtual machine (the "runner") the job runs on. Here it is
`ubuntu-latest`, a Linux machine provided by GitHub.

**4. Why is `actions/checkout` needed?**
The runner starts empty. `actions/checkout` downloads the repository's files
onto the runner so the following steps can actually see and run `hello.py`.

**5. What does the language setup action do?**
`actions/setup-python` installs the requested version of Python on the runner
and puts it on the PATH, so the `python` command is available in later steps.

**6. What is the difference between compiling and running the program?**
Compiling translates source code into an executable form before it runs. Running
is executing the program to produce output. Python is interpreted, so this
project has no separate compile step — it goes straight to running. (A language
like Java would need a compile step first, e.g. `javac Hello.java`.)

**7. Where can you see the program output?**
In the Actions tab: open the workflow run, open the job, and expand the "Run the
Python program" step. The greeting appears in that step's log.

**8. What is the difference between a workflow, a job, and a step?**
A **workflow** is the whole automated process defined by the `.yml` file. A
**job** is a unit of work inside the workflow that runs on one runner. A **step**
is a single action or command inside a job, and steps run in order.

## AI assistance

AI (Claude) was used to help draft the program and the workflow file, explain
GitHub Actions concepts, and structure this README. I reviewed everything,
created the repository, committed the files, and ran the workflow (both the
automatic push-triggered run and the manual `workflow_dispatch` run) myself, and
I confirmed the output in the Actions logs.

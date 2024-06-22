# Setup the development environment

We don't want that libraries used for this project will pollute the global 
Python installation.

Usually this is solved creating a so-called "virtual environment" which act as
a local installation of Python.

The simplest way to create a new virtual environment (in Python 3.x) is 
launching the following command: 

```bash
$ python -v venv .venv 
```

After that command a .venv directory will be created. 

Other alternatives are virtualenv which works with Python 2.x, and poetry that
does also some other things.

The .venv directory should be not tracked by the version control system because
their content may work only on the current machine.

```bash
$ cat .gitignore
/.venv/
```

The environment can be used only if it is activated.
```bash
$ source .venv/bin/activate
```

After sourcing this script the shell will load some environment variables that
permit to use the Python executable in this environment. For the PATH variable
is updated in order to find the python executable in the .venv/bin directory.

# libraries

With the virtual environment activated we can install some libraries in it, 
just using the `pip` command.

For example if we want need a yaml library we can install

```bash
pip install PyYAML
```

Unfortunately this is operation will be not saved automatically in any 
configuration file tracked by the version control.

But pip provides a method for listing all the libraries currently installed 
comprising the exact version used. The output of this command if saved  can be 
used to reproduce a similar environment in another machine.

To see the output of the command we need just to call it:

```bash
$ pip freeze
PyYAML==6.0.1
```

It's common to save the output of the command in a file called requirements.txt
in order to be used later for reinstalling all the dependencies.

```bash
$ pip freeze > requirements.txt
```

Usually this file is tracked using version control.
```bash
$ git add requirements.txt
$ git commit -m "Adding requirements.txt"
```









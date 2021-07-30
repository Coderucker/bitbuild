# bitbuild [![Build application](Bit-Build)](https://github.com/Bit-Build/bitbuild/actions/workflows/build_app.yml) [![Python application](https://github.com/Bit-Build/bitbuild/actions/workflows/test-app.yml/badge.svg)](https://github.com/Bit-Build/bitbuild/actions/workflows/python-app.yml)
Automate your Build Tasks
> bitbuild automatically detects file changes inside your project and Build or Execute or Do whatever you want it to do

# Feature
- ⚙️Cross Platform, Works across any operating system.
- 🎇 Just run `bitbuild .` and it us gonna detect changes and run actions according to those changes.
- ⚙️ Automate your tasks.
- 💡 Avoid wasting time running build commands
- 🛠️ Run and test actions that you run inside your CI/CD Provider inside your machine itself.
- 📃 Add multiple Actions based on different files
- 🛠️ Limit the number of times the code should build
- 🔥 Control the workflow to run

# Installation
This will be available` after the release of verison 1.0.0

If you wanna test it out Just clone this repo.
```sh
git clone https://github.com/bitbuild/bitbuild.git
cd bitbuild
py -m pip install
python Test.py
```

# Contribution
`bitbuild` is build to make your code workflow easier.
If you have any ideas or problems related to this repo, open a issue about it.
If you have a idea and you can implement it by yourself, open a PR.

To contribute, clone this repo first :)
```sh
git clone https://github.com/bitbuild/bitbuild.git
cd bitbuild
py -m pip install
python Test.py
```

We recommend not to use any third party libraries, As we wanna build this using on our own Tech Stack.

# Building
Building this program is easy using `pyinstaller`.
First, you need to setup a Virtual Environment using python and install all required packages.
- Windows

    ```ps1
    py -m venv .
    py -m pip freeze > requirements.txt
    py -m pip install -r requirements.txt
    ```
- Linux or Unix
    ```sh
    python3 -m venv .
    python3 -m pip freeze > requirements.txt
    python3 -m pip install -r requirements.txt
    ```
Then, you need to install `pyinstaller` package from `PYPI`.
and Build it to a bundled executable file.
- Windows

    ```ps1
    .\Scripts\activate
    py -m pip install
    py -m pyinstaller --onefile main.py
    ```
- Linux or Unix
    ```sh
    source Scripts/activate
    python3 pip install pyinstaller
    python3 -m pyinstaller --onefile main.py
    ```

# License
**bitbuild** is Licensed Under `Apache License 2.0`
It is legit to use this software any where.
For Further details, read the [LICENSE](https://github.com/bitbuild/bitbuild/blob/LICENSE)

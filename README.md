
<div style="display: flex; justify-content: center; align-items: center;">
<img src="./Resources/bit-build-icon.png" height="40px" style="margin: 10px; border-radius: 40px;"/>
<header>
BitBuild
</header>
</div>

[![Build application](https://github.com/Bit-Build/bitbuild/actions/workflows/build_windows.yml/badge.svg)](https://github.com/Bit-Build/bitbuild/actions/workflows/build_windows.yml) [![Build application](https://github.com/Bit-Build/bitbuild/actions/workflows/build_linux.yml/badge.svg)](https://github.com/Bit-Build/bitbuild/actions/workflows/build_linux.yml) [![Build application](https://github.com/Bit-Build/bitbuild/actions/workflows/build_macos.yml/badge.svg)](https://github.com/Bit-Build/bitbuild/actions/workflows/build_macos.yml) [![Python application](https://github.com/Bit-Build/bitbuild/actions/workflows/test-app.yml/badge.svg)](https://github.com/Bit-Build/bitbuild/actions/workflows/python-app.yml) 
<br> <br>

**Automates your Build Tasks**
> BitBuild is an automation tool. It automatically detects file changes inside your project and Build or Execute or Do whatever you want it to do

# Feature
- ⚙️Cross Platform, Works across any operating system.
- 🎇 Just run `bitbuild` and it us gonna detect changes and run actions according to those changes.
- ⚙️ Automate your tasks.
- 💡 Avoid wasting time running build commands
- 🛠️ Run and test actions that you run inside your CI/CD Provider inside your machine itself.
- 📃 Add multiple Actions based on different files
- 🛠️ Limit the number of times the code should build
- 🔥 Control the workflow to run

# Installation
Try using the beta-version of the program in the releases.

If you wanna test it out Just clone this repo.
```sh
git clone https://github.com/Bit-Build/bitbuild.git
cd bitbuild
py -m pip install -r requirements.txt
python test.py
```

# Contribution
`BitBuild` is build to make your code workflow easier.
If you have any ideas or problems related to this repo, open a issue about it.
If you have a idea and you can implement it by yourself, open a PR.

To contribute, clone this repo first :)
```sh
git clone https://github.com/Bit-Build/bitbuild.git
cd bitbuild
py -m pip install -r requirements.txt
python Test.py
```

We recommend not to using any third party libraries, As we wanna build this using on our own Tech Stack.

# Building
Building this program is easy using `pyinstaller`.
First, you need to setup a Virtual Environment using python and install all required packages.
- Windows

    ```ps1
    py -m venv venv
    py -m pip freeze > requirements.txt
    py -m pip install -r requirements.txt
    ```
- Linux or Unix
    ```sh
    python3 -m venv venv
    python3 -m pip freeze > requirements.txt
    python3 -m pip install -r requirements.txt
    ```
Then, you need to install `pyinstaller` package from `PYPI`.
and Build it to a bundled executable file.
- Windows

    ```ps1
    .\venv\Scripts\activate
    py -m pip install
    py -m pyinstaller --onefile main.py
    ```
- Linux or Unix
    ```sh
    source venv/Scripts/activate
    python3 -m pip install pyinstaller
    python3 -m pyinstaller --onefile main.py
    ```

# License
**BitBuild** is Licensed Under `Apache License 2.0`
It is legit to use this software any where.
For Further details, read the [LICENSE](https://github.com/bitbuild/bitbuild/blob/LICENSE)

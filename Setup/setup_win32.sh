echo "Setting Up \n"

echo "Installing Packages"
py -m venv venv
py -m pip freeze > requirements.txt
py -m pip install -r requirements.txt

echo "Activating venv"
./venv/Scripts/activate

echo "Building main file using pyinstaller"
py -m pyinstaller --onefile main.py
echo "Setting Up \n"

echo "Installing Packages"
python3 -m venv venv
python3 -m pip freeze > requirements.txt
python3 -m pip install -r requirements.txt
python3 -m pip install pyinstaller

echo "Activating venv"
source venv/Scripts/activate

echo "Building main file using pyinstaller"
python3 -m pyinstaller --onefile main.py
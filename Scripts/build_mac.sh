echo "Installing Packages"
pip freeze > requirements.txt
pip install -r requirements.txt
pip install pyinstaller

echo "Building to executable"
pyinstaller --onefile main.py
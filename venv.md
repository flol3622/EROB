## Setup
```bash	
# controlled environment
conda create -n erob python=3.8
conda activate erob

# extremely fast package installer
pip install uv 
uv pip install pyqt6-tools PySide6 auto-py-to-exe
```

## Qt Designer
```bash
# open Qt Designer once in the environment
pyqt6-tools designer .\Corpus\GUI\layout.ui
```

## Compile
```bash
pyinstaller --noconfirm --onefile --console --icon "C:/Users/phili/Documents/scratch/EROB/Corpus/GUI/icon.ico" --name "EROB" --add-data "C:/Users/phili/Documents/scratch/EROB/Corpus/GUI;GUI/"  "C:/Users/phili/Documents/scratch/EROB/Corpus/_GUI.py"
```

## Setup copiler
```bash
auto-py-to-exe.exe
```

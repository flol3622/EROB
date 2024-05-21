## Setup
```bash	
# controlled environment
conda create -n erob python=3.8
conda activate erob

# extremely fast package installer
pip install uv 
uv pip install pyqt6-tools PySide6 auto-py-to-exe rich
```

## Qt Designer
```bash
# open Qt Designer once in the environment
pyqt6-tools designer .\Corpus\GUI\layout.ui
```

## Compile
```bash
pyinstaller --noconfirm --onefile --console --icon "./Corpus/GUI/icon.ico" --name "EROB" --add-data "./Corpus/GUI;GUI/"  "./Corpus/_GUI.py"
```

## Setup copiler
```bash
auto-py-to-exe.exe
```

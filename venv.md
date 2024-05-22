## Setup
```bash	
# controlled environment
conda create -n erob python=3.8
conda activate erob

# extremely fast package installer
pip install uv 
uv pip install pyqt6-tools PySide6 auto-py-to-exe rich numpy scipy
```

## Qt Designer
```bash
# open Qt Designer once in the environment
pyqt6-tools designer .\GUI\layout.ui
```

## Compile
```bash
pyinstaller --noconfirm --onefile --console --icon "./GUI/icon.ico" --name "EROB" --add-data "./GUI;GUI/" --add-data "./Data;Data/"  "./_GUI.py"
```

## Setup compiler
```bash
auto-py-to-exe.exe
```

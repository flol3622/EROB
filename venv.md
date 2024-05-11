## Setup
```bash	
# controlled environment
conda create -n erob python=3.8
conda activate erob

# extremely fast package installer
pip install uv 
uv pip install pyqt6-tools PySide6
```

## Qt Designer
```bash
# open Qt Designer once in the environment
pyqt6-tools designer .\Corpus\GUI\layout.ui
```
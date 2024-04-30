## Setup
```bash	
# controlled environment in folder
conda create -p .venv python=3.8
conda activate < path to \.venv>

# extremely fast package installer
pip install uv
uv pip install PySide6

# unresolved packages
pip install pyqt6-tools
```

## Qt Designer
```bash
# open Qt Designer once in the environment
pyqt6-tools designer  
```

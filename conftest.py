import sys
from pathlib import Path

# Добавляем папку src в sys.path
project_root = Path(__file__).parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

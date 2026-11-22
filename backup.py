from pathlib import Path
from datetime import datetime
import zipfile

# Get the project directory
ROOT = Path(__file__).resolve().parent

# Create backup folder
BACKUP_DIR = ROOT / "backups"
BACKUP_DIR.mkdir(exist_ok=True)

# Generate date and time
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# ZIP backup file
backup_file = BACKUP_DIR / f"backup_{timestamp}.zip"

# Folders to exclude
excluded = {
    ".git",
    "backups",
    "__pycache__",
    ".venv",
    "venv"
}

# Create backup
with zipfile.ZipFile(
    backup_file,
    "w",
    zipfile.ZIP_DEFLATED
) as zip_file:

    for file in ROOT.rglob("*"):

        if not file.is_file():
            continue

        relative_path = file.relative_to(ROOT)

        # Skip excluded folders
        if any(part in excluded for part in relative_path.parts):
            continue

        zip_file.write(file, relative_path)

print("================================")
print(" BACKUP CREATED SUCCESSFULLY!")
print("================================")
print("Backup location:", backup_file)

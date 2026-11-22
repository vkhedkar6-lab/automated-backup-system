from pathlib import Path
from datetime import datetime
import zipfile
import sys

def create_backup():

    try:
        # Project directory
        project_dir = Path(".")

        # Backup directory
        backup_dir = Path("backups")
        backup_dir.mkdir(exist_ok=True)

        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Backup filename
        backup_file = backup_dir / f"backup_{timestamp}.zip"

        # Excluded folders
        exclude = {
            ".git",
            "backups",
            "__pycache__",
            ".venv",
            "venv"
        }

        # Create ZIP backup
        with zipfile.ZipFile(
            backup_file, "w", zipfile.ZIP_DEFLATED
        ) as zipf:

            for file in project_dir.rglob("*"):

                if file.is_file():
                    if not any(part in exclude for part in file.parts):
                        zipf.write(
                            file,
                            file.relative_to(project_dir)
                        )

        print("BACKUP CREATED SUCCESSFULLY!")
        print(f"Backup location: {backup_file}")

    except (OSError, zipfile.BadZipFile) as error:
        print(f"BACKUP FAILED: {error}")
        sys.exit(1)

    except Exception as error:
        print(f"UNEXPECTED ERROR: {error}")
        sys.exit(1)


if __name__ == "__main__":
    create_backup()

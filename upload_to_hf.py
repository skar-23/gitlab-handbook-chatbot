import os
from pathlib import Path
from huggingface_hub import HfApi
import time

# Wait for any active processes
time.sleep(5)

chroma_path = Path("chroma_db")
print(f"📁 chroma_db exists: {chroma_path.exists()}")

if chroma_path.exists():
    # Remove journal files before upload
    for journal in chroma_path.rglob("*.sqlite3-journal"):
        print(f"🗑️  Removing journal file: {journal}")
        journal.unlink()
    
    size_mb = sum(f.stat().st_size for f in chroma_path.rglob('*') if f.is_file()) / (1024**2)
    print(f"📊 chroma_db size: {size_mb:.1f} MB")
    
    print("\n🚀 Uploading chroma_db to HuggingFace...")
    api = HfApi()
    api.upload_folder(
        repo_id="skar-23/gitlab-chatbot-db",
        folder_path=str(chroma_path),
        repo_type="dataset",
        token=os.getenv("HF_TOKEN")
    )
    print("✅ Upload complete!")
else:
    print("❌ chroma_db not found")

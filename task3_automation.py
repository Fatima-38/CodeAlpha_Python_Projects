import re
import os

# ─────────────────────────────────────────────
#  TASK 3 — Three automation mini-tools in one
# ─────────────────────────────────────────────

def move_jpg_files():
    """Move all .jpg files from current folder to a 'jpg_images' subfolder."""
    source = os.getcwd()
    destination = os.path.join(source, "jpg_images")
    os.makedirs(destination, exist_ok=True)

    moved = 0
    for file in os.listdir(source):
        if file.lower().endswith(".jpg"):
            src_path = os.path.join(source, file)
            dst_path = os.path.join(destination, file)
            os.rename(src_path, dst_path)
            print(f"  Moved: {file} → jpg_images/")
            moved += 1

    print(f"\n✅ Done! {moved} .jpg file(s) moved to 'jpg_images/'.")


def extract_emails():
    """Extract all email addresses from a .txt file."""
    filename = input("Enter the source .txt filename: ").strip()

    if not os.path.exists(filename):
        print(f"⚠ File '{filename}' not found.")
        return

    with open(filename, "r") as f:
        content = f.read()

    # Regex to match standard email addresses
    emails = re.findall(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", content)
    unique_emails = sorted(set(emails))

    if not unique_emails:
        print("⚠ No email addresses found in the file.")
        return

    output_file = "extracted_emails.txt"
    with open(output_file, "w") as f:
        f.write(f"Extracted Emails ({len(unique_emails)} found)\n")
        f.write("=" * 35 + "\n")
        for email in unique_emails:
            f.write(email + "\n")

    print(f"\n✅ Found {len(unique_emails)} unique email(s):")
    for e in unique_emails:
        print(f"  📧 {e}")
    print(f"\nSaved to '{output_file}'.")


def show_menu():
    print("=" * 45)
    print("    🤖 Task Automation Menu")
    print("=" * 45)
    print("  1. Move all .jpg files to 'jpg_images/'")
    print("  2. Extract emails from a .txt file")
    print("  0. Exit")
    print("=" * 45)


def run():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please try again.")

        print()

run()
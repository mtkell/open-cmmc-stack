import os
from pathlib import Path

EXPECTED_ROLE_FILES = [
    "tasks/main.yml",
    "defaults/main.yml",
    "meta/main.yml",
]

OPTIONAL_FILES = [
    "handlers/main.yml",
    "templates/",
    "files/",
    "vars/main.yml",
    "molecule/default/converge.yml",
    "molecule/default/verify.yml",
]

PLACEHOLDER_TERMS = ["TODO", "FILL_ME_IN", "REPLACE_ME"]

def is_placeholder(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            return any(term in content for term in PLACEHOLDER_TERMS)
    except Exception:
        return False

def is_non_empty(file_path):
    try:
        return os.path.getsize(file_path) > 0
    except Exception:
        return False

def audit_role(role_path):
    role_name = os.path.basename(role_path)
    issues = []

    for rel_path in EXPECTED_ROLE_FILES:
        full_path = os.path.join(role_path, rel_path)
        if not os.path.isfile(full_path):
            issues.append(f"❌ MISSING: {rel_path}")
        elif not is_non_empty(full_path):
            issues.append(f"⚠️ EMPTY: {rel_path}")
        elif is_placeholder(full_path):
            issues.append(f"⚠️ PLACEHOLDER: {rel_path}")

    for rel_path in OPTIONAL_FILES:
        full_path = os.path.join(role_path, rel_path)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            if not is_non_empty(full_path):
                issues.append(f"⚠️ OPTIONAL EMPTY: {rel_path}")
            elif is_placeholder(full_path):
                issues.append(f"⚠️ OPTIONAL PLACEHOLDER: {rel_path}")

    return role_name, issues

def main():
    base_path = Path("ansible/roles/")
    if not base_path.exists():
        print("❗ 'ansible/roles/' directory not found.")
        return

    print("🔍 Auditing roles in:", base_path)
    for role_dir in base_path.iterdir():
        if role_dir.is_dir():
            role_name, issues = audit_role(role_dir)
            if issues:
                print(f"\n🔎 Role: {role_name}")
                for issue in issues:
                    print("   ", issue)
            else:
                print(f"✅ Role: {role_name} — All checks passed.")

if __name__ == "__main__":
    main()

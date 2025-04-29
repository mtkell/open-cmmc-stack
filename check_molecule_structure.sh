#!/bin/bash

echo "🔍 Checking Molecule structure under ansible/roles/..."

# Define your role list
roles=( secure_ubuntu podman_services identity file_storage monitoring preflight )

exit_code=0

for role in "${roles[@]}"
do
  echo "-------------------------------------------------"
  echo "🔎 Checking role: $role"

  role_path="ansible/roles/$role/molecule/default"

  # Check if molecule/default/ exists
  if [ ! -d "$role_path" ]; then
    echo "❌ ERROR: Missing $role_path directory"
    exit_code=1
    continue
  fi

  # Check if molecule.yml exists
  if [ ! -f "$role_path/molecule.yml" ]; then
    echo "❌ ERROR: Missing molecule.yml in $role_path"
    exit_code=1
  else
    echo "✅ molecule.yml found."
  fi

  # Check if scenario.yml exists
  if [ ! -f "$role_path/scenario.yml" ]; then
    echo "❌ ERROR: Missing scenario.yml in $role_path"
    exit_code=1
  else
    echo "✅ scenario.yml found."
  fi

  # Optional: check create/converge/destroy/verify
  for file in create.yml converge.yml destroy.yml verify.yml
  do
    if [ ! -f "$role_path/$file" ]; then
      echo "⚠️  WARNING: Missing $file in $role_path (not critical but needed)"
    else
      echo "✅ $file present."
    fi
  done

  # Check if molecule.yml has valid YAML header
  if ! grep -qE '^---' "$role_path/molecule.yml"; then
    echo "❌ ERROR: molecule.yml does not start with valid YAML (---)"
    exit_code=1
  else
    echo "✅ molecule.yml starts with valid YAML header."
  fi

done

echo "-------------------------------------------------"

if [ "$exit_code" -eq 0 ]; then
  echo "🎉 All Molecule role structures look good!"
else
  echo "⚠️  There are some problems. Please fix them."
fi

exit $exit_code

input_file = "requirements.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

with open(input_file, "w") as file:
    for line in lines:
        # Strip whitespace to process each line
        line = line.strip()
        # Skip empty lines or comments
        if not line or line.startswith("#"):
            file.write(line + "\n")
            continue
        # Keep only the text before the first '='
        package_name = line.split("=")[0].strip()
        file.write(package_name + "\n")

print(f"Updated {input_file} successfully.")

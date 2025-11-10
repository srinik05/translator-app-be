import argostranslate.package
import argostranslate.translate

# Update package index
argostranslate.package.update_package_index()

# List available packages (optional)
available_packages = argostranslate.package.get_available_packages()
for pkg in available_packages:
    print(f"{pkg.from_code} -> {pkg.to_code}")

# Function to install a package by source->target code
def install_lang_package(from_code, to_code):
    pkg = [p for p in available_packages if p.from_code == from_code and p.to_code == to_code]
    if pkg:
        download_path = pkg[0].download()
        argostranslate.package.install_from_path(download_path)
        print(f"Installed package {from_code} -> {to_code}")
    else:
        print(f"No package found for {from_code} -> {to_code}")

# Install English -> Hindi
install_lang_package("en", "hi")

# Install English -> Telugu
install_lang_package("en", "te")

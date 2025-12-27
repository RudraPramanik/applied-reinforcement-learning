import nbformat
import sys

if len(sys.argv) < 2:
    raise ValueError("Usage: python clean_metadata.py <notebook.ipynb>")

nb_path = sys.argv[1]
nb = nbformat.read(nb_path, as_version=4)

# Remove problematic metadata only
nb.metadata.pop("widgets", None)
nb.metadata.pop("colab", None)
nb.metadata.pop("kernelspec", None)
nb.metadata.pop("language_info", None)

nbformat.write(nb, nb_path)
print(f"✓ Metadata cleaned (outputs preserved): {nb_path}")

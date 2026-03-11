# Sphinx notebook gallery boilerplate

This folder contains a minimal Sphinx setup for rendering JupyterLab notebooks as a gallery.

## Install docs dependencies

```powershell
python -m pip install -r requirements.txt
```

## Build the HTML docs

```powershell
.\make.bat html
```

The notebook sources stay in the top-level `../notebooks/` folder. The files inside `examples/` are lightweight `.nblink` references that let Sphinx include those notebooks without copying them.

from setuptools import setup, find_packages

setup(
    name="pecubegui",
    version="0.1.0",
    description="A GUI-based tool for the Pecube thermochronology software.",
    author="Maxime Bernard",
    url="https://github.com/OpenThermochronology/PecubeGUI",
    # This identifies the sub-directories containing __init__.py (Utils, Topography, etc.)
    packages=find_packages(),
    py_modules=["main"],
    include_package_data=True,
    install_requires=[
        "PyQt5",
        "numpy",
        "pandas",
        "scipy",
        "matplotlib",
        "pyvista",
        "pyvistaqt",
        "folium",
        "xarray",
        "bmi-topography",
        "cmcrameri",
    ],
    entry_points={
        "console_scripts": [
            "pecubegui = PecubeGUI.main:main",
        ],
    },
)

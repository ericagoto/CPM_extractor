from setuptools import setup

__version__ = (0, 0, 0)

setup(
    name="CPM_extractor",
    description="Pyhton package to modify the CPM column in a kml file",
    url="https://github.com/sum1lim/CPM_extractor",
    version=".".join(str(d) for d in __version__),
    author="Sangwon Lim",
    author_email="sangwon3@ualberta.ca",
    include_package_data=True,
    scripts="""
        ./scripts/CPM_extractor
        ./scripts/gui
    """.split(),
)

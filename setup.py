import setuptools
# with open('README.md','r',encoding='utf-8') as f:
#     long_description=f.read()


# [build-system]
requires = ["setuptools >= 61.0"]
build_backend = "setuptools.build_meta"

__version__='0.0.0'
REPO_NAME='wine-quality-ml-project-Implement'
AUTHOR_USER_NAME='zain-khan'
SRC_REPO='wine-quality-ml-project'
AUTHOR_EMAIL='za870411@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for ml project',
    # long_description=long_description,
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')

)
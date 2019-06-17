from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name="{{ cookiecutter.repo_name }}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="{{ cookiecutter.project_short_description }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email="{{ cookiecutter.email }}",
    url="{{ cookiecutter.host }}/{{ cookiecutter.host_username }}/{{ cookiecutter.repo_name }}",
    packages=["{{ cookiecutter.package_name }}"],
    entry_points={"console_scripts": ["{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:cli"]},
    install_requires=requirements,
    keywords="{{ cookiecutter.repo_name }}",
    license="Apache License 2.0",
    classifiers=["Programming Language :: Python :: 3.7"],
)

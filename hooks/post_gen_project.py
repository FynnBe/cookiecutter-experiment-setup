import os


try:
    import sh
except ImportError:
    # fallback: emulate the sh API with pbs
    import pbs

    class Sh(object):
        def __getattr__(self, attr):
            return pbs.Command(attr)

    sh = Sh()

sh.git.init()
sh.git.add("*")
sh.git.commit("-m", '"initial commit without submodules"')

host = "{{ cookiecutter.host }}"
if host.startswith("/"):
    host = os.path.abspath(host)

sh.git.submodule.add(
    "--name",
    "{{ cookiecutter.model_repo_name }}",
    f"{host}/{{ cookiecutter.host_username }}/{{ cookiecutter.model_repo_name }}",
    "{{ cookiecutter.package_name }}/{{ cookiecutter.model_repo_name }}",
)
sh.git.submodule.add(
    "--name",
    "{{ cookiecutter.utils_repo_name }}",
    f"{host}/{{ cookiecutter.host_username }}/{{ cookiecutter.utils_repo_name }}",
    "{{ cookiecutter.package_name }}/{{ cookiecutter.utils_repo_name }}",
)

sh.git.add("*")
sh.git.commit("-m", '"add submodules"')

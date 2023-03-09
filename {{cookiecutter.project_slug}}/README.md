<div align="center">
<h1> {{cookiecutter.project_name}} </h1>

<p> {{ cookiecutter.project_short_description }} </p>

<p>
    <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/build_and_test.yml">
        <img src="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/actions/workflows/build_and_test.yml/badge.svg" alt="Build Status">
    </a>
    <a href="https://app.codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}">
        <img src="https://codecov.io/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg" alt="codecov">
    </a>
{%- if cookiecutter.need_docs == "yes" %}
    <a href="https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/">
    	<img src="https://readthedocs.org/projects/{{cookiecutter.project_slug}}/badge/?version=latest" alt="Documentation">
    </a>
{%- endif %}
  <a href="https://pypi.org/project/{{cookiecutter.project_slug}}/">
    <img src="https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg" alt="Install with PyPi" />
  </a>
  <a href="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}" alt="{{cookiecutter.open_source_license}}" />
  </a>
</p>
</div>

**Work In Progress**


## Features

* TODO

## Credits

This package was created with Cookiecutter and the `Nanguage/cookiecutter-pypackage` project template.

+ Cookiecutter: https://github.com/audreyr/cookiecutter
+ `Nanguage/cookiecutter-pypackage`: https://github.com/Nanguage/cookiecutter-pypackage

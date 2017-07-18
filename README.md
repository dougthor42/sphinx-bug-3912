# SphinxBug3912

This repo demonstrates [sphinx-doc/sphinx#9312](https://github.com/sphinx-doc/sphinx/issues/3912).

## Steps to Reproduce:
```cmd
C:\temp>python -c "import sys;print(sys.version)"
3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)]
C:\temp>git clone https://github.com/dougthor42/sphinx-bug-3912.git
C:\temp>cd sphinx-bug-3912
C:\temp\sphinx-bug-3912>python -m venv .venv
C:\temp\sphinx-bug-3912>.venv\Scripts\activate.bat
(.venv) C:\temp\sphinx-bug-3912>python -m pip install --upgrade pip wheel
...
(.venv) C:\temp\sphinx-bug-3912>python -m pip install -r requirements.txt
...
(.venv) C:\temp\sphinx-bug-3912>python -m pip install -r requirements-dev.txt
...
(.venv) C:\temp\sphinx-bug-3912>cd docs
(.venv) C:\temp\sphinx-bug-3912>make.bat html
Running Sphinx v1.5.5
making output directory...
loading pickled environment... not yet created
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 5 source files that are out of date
updating environment: 5 added, 0 changed, 0 removed
reading sources... [100%] module_w
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] module_w
generating indices... genindex py-modindex
writing additional pages... search
copying static files... WARNING: html_static_path entry 'C:\\temp\\sphinx-bug-3912\\docs\\_static' does not exist
done
copying extra files... done
dumping search index in English (code: en) ... done
dumping object inventory... done
build succeeded, 1 warning.

Build finished. The HTML pages are in _build\html.

(.venv) C:\temp\sphinx-bug-3912>python -m pip install --upgrade sphinx==1.6.1
...
(.venv) C:\temp\sphinx-bug-3912>make.bat html
Running Sphinx v1.6.1

Build finished. The HTML pages are in _build\html.

(.venv) C:\temp\sphinx-bug-3912>
```
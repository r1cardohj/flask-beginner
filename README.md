# flask-beginner

a quick project directory maker for flask.^_^

**Quick Start**

create a new dir such as `yourproject`

``` bash
cd yourproject
python -m venv env
env\Scripts\activate 
```

then

``` bash
(env):pip install flask-beginner
(env):beginner -n myapp
```

your project will like this
``` bash
yourproject
│  .gitignore
│  README.md
│  requirements.txt
│  test.py
│  wsgi.py
│
└─myapp
    │  __init__.py
    │  extensions.py
    │  forms.py
    │  models.py
    │  settings.py
    │
    ├─blueprints
    │      __init__.py
    │
    ├─static
    └─templates
```

**Version**

v 0.0.1 2023.8.6 create
v 0.0.2 2023.8.6 add app file `__init__.py`

## zh-hans

憋死我了一直写英文。

flask-beginner是用于 ~~偷懒~~ 

是用于创建我自己用的比较顺手的一个flask项目结构，

这个包依赖于flask，

也就是说开启一个flask项目直接用这个包就行。

虽然说这个包诞生以后的下载量可能完全是我自己在贡献，

但是这种全世界都能下载的感觉

真好啊 ^_^
# flatlib

Flatlib is a python library for Traditional Astrology.

```python

>>> date = Datetime('2015/03/13', '17:00', '+00:00')
>>> pos = GeoPos('38n32', '8w54')
>>> chart = Chart(date, pos)

>>> sun = chart.get(const.SUN)
>>> print(sun)
<Sun Pisces +22:47:25 +00:59:51>

```

## Documentation

Flatlib's documentation is available at [http://flatlib.readthedocs.org/](http://flatlib.readthedocs.org/).


## Installation

Flatlib is a Python 3 package, make sure you have Python 3 installed on your system. 

You can install flatlib with `pip3 install flatlib` or download the latest stable version from [https://pypi.python.org/pypi/flatlib](https://pypi.python.org/pypi/flatlib) and install it with `python3 setup.py install`. 


## Development

You can clone this repository or download a zip file using the right side buttons. 

打包pypi
1.修改setup.py 版本号
2.python setup.py sdist bdist_wheel
3.twine upload dist/*
4.输入name: __token__
5.去pypi网站设置新的tokenAPI 粘贴。password:
pypi-AgEIcHlwaS5vcmcCJGJkOGU1YmVlLWI0MWYtNDNlZS1hYmIzLTZmNmU3Njc5MzcwYgACFVsxLFsiZmxhdGxpYi10ZXNsYSJdXQACLFsyLFsiNGU4NjU2MWEtMzg5OS00NDAwLTg3M2EtZGI1YzE0N2E2ZGIwIl1dAAAGIIigw5s6NIQx_TFKUK-sLvfNbmDiX56_j1VLBgji918X
pypi-AgEIcHlwaS5vcmcCJGYyYWJiMjJkLWUzNTctNGNmZC1hNjEwLThjOTIzNjg5MmVhYgACFVsxLFsiZmxhdGxpYi10ZXNsYSJdXQACLFsyLFsiNGU4NjU2MWEtMzg5OS00NDAwLTg3M2EtZGI1YzE0N2E2ZGIwIl1dAAAGINDrNsGYBwB-GboFink4JOZdznRzA1kgabmU6Bxpa-Se



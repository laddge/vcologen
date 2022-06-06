# vcologen - vim colorscheme generator

## Install

```
pip install vcologen
```

## Usage

```python
import vcologen

name = "mytheme"
vcg = vcologen.Generator(name)

vcg.theme = "dark"
vcg.bg = "#000000"  # background
vcg.fg = "#ffffff"  # foreground
vcg.c1 = "#ff0000"  # color 1
vcg.c2 = "#00ff00"  # color 2
vcg.c3 = "#ffff00"  # color 3
vcg.c4 = "#0000ff"  # color 4
vcg.c5 = "#ff00ff"  # color 5
vcg.c6 = "#00ffff"  # color 6
vcg.cm = "#797979"  # comment color
vcg.cl = "#333333"  # cursor line color

path = "colors/mytheme.vim"
vcg.generate(path)
```

## License
This project is under the MIT-License.  
See also [LICENSE](LICENSE).

## Author
Laddge

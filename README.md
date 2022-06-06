# vcologen - vim colorscheme generator

## Install

```
pip install vcologen
```

## Usage

```python
import vcologen

name = "mytheme"
colors = [
    "#000000",  # background
    "#ffffff",  # foreground
    "#000000",  # black
    "#800000",  # red
    "#008000",  # green
    "#808000",  # yellow
    "#000080",  # blue
    "#800080",  # magenta
    "#008080",  # cyan
    "#c0c0c0",  # white
    "#808080",  # gray
    "#ff0000",  # light red
    "#00ff00",  # light green
    "#ffff00",  # light yellow
    "#0000ff",  # light blue
    "#ff00ff",  # light magenta
    "#00ffff",  # light cyan
    "#ffffff",  # bright white
]

generated = vcologen.generate(name, colors)

with open("mytheme.vim", "w") as f:
    f.write(generated)
```

## License
This project is under the MIT-License.  
See also [LICENSE](LICENSE).

## Author
Laddge

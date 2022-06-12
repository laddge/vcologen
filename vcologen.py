import jinja2


class Generator:
    def __init__(self, name):
        self.name = name
        self.theme = "dark"
        self.bg = "#000000"
        self.fg = "#ffffff"
        self.c1 = "#ff0000"
        self.c2 = "#00ff00"
        self.c3 = "#ffff00"
        self.c4 = "#0000ff"
        self.c5 = "#ff00ff"
        self.c6 = "#00ffff"
        self.cm = "#797979"
        self.cl = "#333333"
        self.template = """
hi clear
if exists('syntax_on')
syntax reset
endif

let g:colors_name = '{{ name }}'
set background={{ theme }}

{{ highlights([
    ["Normal", fg, bg, "NONE"],
    ["DiffText", c1, "NONE", "NONE"],
    ["ErrorMsg", c1, "NONE", "NONE"],
    ["WarningMsg", c1, "NONE", "NONE"],
    ["PreProc", c1, "NONE", "NONE"],
    ["Exception", c1, "NONE", "NONE"],
    ["Error", c1, "NONE", "NONE"],
    ["DiffDelete", c1, "NONE", "NONE"],
    ["GitGutterDelete", c1, "NONE", "NONE"],
    ["GitGutterChangeDelete", c1, "NONE", "NONE"],
    ["cssIdentifier", c1, "NONE", "NONE"],
    ["cssImportant", c1, "NONE", "NONE"],
    ["Type", c1, "NONE", "NONE"],
    ["Identifier", c1, "NONE", "NONE"],
    ["PMenuSel", c2, "NONE", "NONE"],
    ["Constant", c2, "NONE", "NONE"],
    ["Repeat", c2, "NONE", "NONE"],
    ["DiffAdd", c2, "NONE", "NONE"],
    ["GitGutterAdd", c2, "NONE", "NONE"],
    ["cssIncludeKeyword", c2, "NONE", "NONE"],
    ["Keyword", c2, "NONE", "NONE"],
    ["IncSearch", c3, "NONE", "NONE"],
    ["Title", c3, "NONE", "NONE"],
    ["PreCondit", c3, "NONE", "NONE"],
    ["Debug", c3, "NONE", "NONE"],
    ["SpecialChar", c3, "NONE", "NONE"],
    ["Conditional", c3, "NONE", "NONE"],
    ["Todo", c3, "NONE", "NONE"],
    ["Special", c3, "NONE", "NONE"],
    ["Label", c3, "NONE", "NONE"],
    ["Delimiter", c3, "NONE", "NONE"],
    ["Number", c3, "NONE", "NONE"],
    ["CursorLineNR", c3, "NONE", "NONE"],
    ["Define", c3, "NONE", "NONE"],
    ["MoreMsg", c3, "NONE", "NONE"],
    ["Tag", c3, "NONE", "NONE"],
    ["String", c3, "NONE", "NONE"],
    ["MatchParen", c3, "NONE", "NONE"],
    ["Macro", c3, "NONE", "NONE"],
    ["DiffChange", c3, "NONE", "NONE"],
    ["GitGutterChange", c3, "NONE", "NONE"],
    ["cssColor", c3, "NONE", "NONE"],
    ["Function", c4, "NONE", "NONE"],
    ["Directory", c5, "NONE", "NONE"],
    ["markdownLinkText", c5, "NONE", "NONE"],
    ["javaScriptBoolean", c5, "NONE", "NONE"],
    ["Include", c5, "NONE", "NONE"],
    ["Storage", c5, "NONE", "NONE"],
    ["cssClassName", c5, "NONE", "NONE"],
    ["cssClassNameDot", c5, "NONE", "NONE"],
    ["Statement", c6, "NONE", "NONE"],
    ["Operator", c6, "NONE", "NONE"],
    ["cssAttr", c6, "NONE", "NONE"],
    ["Pmenu", fg, cl, "NONE"],
    ["SignColumn", fg, bg, "NONE"],
    ["Title", fg, bg, "NONE"],
    ["LineNr", cm, bg, "NONE"],
    ["NonText", cm, bg, "NONE"],
    ["Comment", cm, "NONE", "NONE"],
    ["SpecialComment", cm, "NONE", "NONE"],
    ["CursorLine", "NONE", cl, "NONE"],
    ["TabLineFill", "NONE", cl, "NONE"],
    ["TabLine", cm, cl, "NONE"],
    ["StatusLine", fg, cl, "bold"],
    ["StatusLineNC", fg, bg, "NONE"],
    ["Search", fg, cm, "NONE"],
    ["VertSplit", cl, "NONE", "NONE"],
    ["Visual", "NONE", cl, "NONE"],
]) }}
"""

    def cuicolor(self, hexcolor):
        if hexcolor[0] != "#":
            return hexcolor
        termcolors = [
            (0, 0, 0),
            (128, 0, 0),
            (0, 128, 0),
            (128, 128, 0),
            (0, 0, 128),
            (128, 0, 128),
            (0, 128, 128),
            (192, 192, 192),
            (128, 128, 128),
            (255, 0, 0),
            (0, 255, 0),
            (255, 255, 0),
            (0, 0, 255),
            (255, 0, 255),
            (0, 255, 255),
            (255, 255, 255),
            (0, 0, 0),
            (0, 0, 95),
            (0, 0, 135),
            (0, 0, 175),
            (0, 0, 215),
            (0, 0, 255),
            (0, 95, 0),
            (0, 95, 95),
            (0, 95, 135),
            (0, 95, 175),
            (0, 95, 215),
            (0, 95, 255),
            (0, 135, 0),
            (0, 135, 95),
            (0, 135, 135),
            (0, 135, 175),
            (0, 135, 215),
            (0, 135, 255),
            (0, 175, 0),
            (0, 175, 95),
            (0, 175, 135),
            (0, 175, 175),
            (0, 175, 215),
            (0, 175, 255),
            (0, 215, 0),
            (0, 215, 95),
            (0, 215, 135),
            (0, 215, 175),
            (0, 215, 215),
            (0, 215, 255),
            (0, 255, 0),
            (0, 255, 95),
            (0, 255, 135),
            (0, 255, 175),
            (0, 255, 215),
            (0, 255, 255),
            (95, 0, 0),
            (95, 0, 95),
            (95, 0, 135),
            (95, 0, 175),
            (95, 0, 215),
            (95, 0, 255),
            (95, 95, 0),
            (95, 95, 95),
            (95, 95, 135),
            (95, 95, 175),
            (95, 95, 215),
            (95, 95, 255),
            (95, 135, 0),
            (95, 135, 95),
            (95, 135, 135),
            (95, 135, 175),
            (95, 135, 215),
            (95, 135, 255),
            (95, 175, 0),
            (95, 175, 95),
            (95, 175, 135),
            (95, 175, 175),
            (95, 175, 215),
            (95, 175, 255),
            (95, 215, 0),
            (95, 215, 95),
            (95, 215, 135),
            (95, 215, 175),
            (95, 215, 215),
            (95, 215, 255),
            (95, 255, 0),
            (95, 255, 95),
            (95, 255, 135),
            (95, 255, 175),
            (95, 255, 215),
            (95, 255, 255),
            (135, 0, 0),
            (135, 0, 95),
            (135, 0, 135),
            (135, 0, 175),
            (135, 0, 215),
            (135, 0, 255),
            (135, 95, 0),
            (135, 95, 95),
            (135, 95, 135),
            (135, 95, 175),
            (135, 95, 215),
            (135, 95, 255),
            (135, 135, 0),
            (135, 135, 95),
            (135, 135, 135),
            (135, 135, 175),
            (135, 135, 215),
            (135, 135, 255),
            (135, 175, 0),
            (135, 175, 95),
            (135, 175, 135),
            (135, 175, 175),
            (135, 175, 215),
            (135, 175, 255),
            (135, 215, 0),
            (135, 215, 95),
            (135, 215, 135),
            (135, 215, 175),
            (135, 215, 215),
            (135, 215, 255),
            (135, 255, 0),
            (135, 255, 95),
            (135, 255, 135),
            (135, 255, 175),
            (135, 255, 215),
            (135, 255, 255),
            (175, 0, 0),
            (175, 0, 95),
            (175, 0, 135),
            (175, 0, 175),
            (175, 0, 215),
            (175, 0, 255),
            (175, 95, 0),
            (175, 95, 95),
            (175, 95, 135),
            (175, 95, 175),
            (175, 95, 215),
            (175, 95, 255),
            (175, 135, 0),
            (175, 135, 95),
            (175, 135, 135),
            (175, 135, 175),
            (175, 135, 215),
            (175, 135, 255),
            (175, 175, 0),
            (175, 175, 95),
            (175, 175, 135),
            (175, 175, 175),
            (175, 175, 215),
            (175, 175, 255),
            (175, 215, 0),
            (175, 215, 95),
            (175, 215, 135),
            (175, 215, 175),
            (175, 215, 215),
            (175, 215, 255),
            (175, 255, 0),
            (175, 255, 95),
            (175, 255, 135),
            (175, 255, 175),
            (175, 255, 215),
            (175, 255, 255),
            (215, 0, 0),
            (215, 0, 95),
            (215, 0, 135),
            (215, 0, 175),
            (215, 0, 215),
            (215, 0, 255),
            (215, 95, 0),
            (215, 95, 95),
            (215, 95, 135),
            (215, 95, 175),
            (215, 95, 215),
            (215, 95, 255),
            (215, 135, 0),
            (215, 135, 95),
            (215, 135, 135),
            (215, 135, 175),
            (215, 135, 215),
            (215, 135, 255),
            (215, 175, 0),
            (215, 175, 95),
            (215, 175, 135),
            (215, 175, 175),
            (215, 175, 215),
            (215, 175, 255),
            (215, 215, 0),
            (215, 215, 95),
            (215, 215, 135),
            (215, 215, 175),
            (215, 215, 215),
            (215, 215, 255),
            (215, 255, 0),
            (215, 255, 95),
            (215, 255, 135),
            (215, 255, 175),
            (215, 255, 215),
            (215, 255, 255),
            (255, 0, 0),
            (255, 0, 95),
            (255, 0, 135),
            (255, 0, 175),
            (255, 0, 215),
            (255, 0, 255),
            (255, 95, 0),
            (255, 95, 95),
            (255, 95, 135),
            (255, 95, 175),
            (255, 95, 215),
            (255, 95, 255),
            (255, 135, 0),
            (255, 135, 95),
            (255, 135, 135),
            (255, 135, 175),
            (255, 135, 215),
            (255, 135, 255),
            (255, 175, 0),
            (255, 175, 95),
            (255, 175, 135),
            (255, 175, 175),
            (255, 175, 215),
            (255, 175, 255),
            (255, 215, 0),
            (255, 215, 95),
            (255, 215, 135),
            (255, 215, 175),
            (255, 215, 215),
            (255, 215, 255),
            (255, 255, 0),
            (255, 255, 95),
            (255, 255, 135),
            (255, 255, 175),
            (255, 255, 215),
            (255, 255, 255),
            (8, 8, 8),
            (18, 18, 18),
            (28, 28, 28),
            (38, 38, 38),
            (48, 48, 48),
            (58, 58, 58),
            (68, 68, 68),
            (78, 78, 78),
            (88, 88, 88),
            (98, 98, 98),
            (108, 108, 108),
            (118, 118, 118),
            (128, 128, 128),
            (138, 138, 138),
            (148, 148, 148),
            (158, 158, 158),
            (168, 168, 168),
            (178, 178, 178),
            (188, 188, 188),
            (198, 198, 198),
            (208, 208, 208),
            (218, 218, 218),
            (228, 228, 228),
            (238, 238, 238),
        ]
        hexcolor = hexcolor.strip("#")
        rgb = (int(hexcolor[:2], 16), int(hexcolor[2:4], 16), int(hexcolor[4:], 16))
        color = 0
        min_dist = 195075
        for i in range(256):
            dist = 0
            for j in range(3):
                dist += (termcolors[i][j] - rgb[j]) ** 2
            if dist < min_dist:
                color = i
                min_dist = dist
        return color

    def highlights(self, his):
        histr = ""
        line = "hi {} ctermfg={} ctermbg={} cterm={} guifg={} guibg={} gui={}\n"
        for hi in his:
            histr += line.format(
                hi[0],
                self.cuicolor(hi[1]),
                self.cuicolor(hi[2]),
                hi[3],
                hi[1],
                hi[2],
                hi[3],
            )
        return histr.strip("\n")

    def generate(self, path):
        generated = jinja2.Template(self.template).render(
            name=self.name,
            theme=self.theme,
            highlights=self.highlights,
            bg=self.bg,
            fg=self.fg,
            c1=self.c1,
            c2=self.c2,
            c3=self.c3,
            c4=self.c4,
            c5=self.c5,
            c6=self.c6,
            cm=self.cm,
            cl=self.cl,
        )
        with open(path, "w") as f:
            f.write(generated.strip() + "\n")

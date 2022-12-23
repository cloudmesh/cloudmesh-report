import textwrap
import yaml
from cloudmesh.common.FlatDict import read_config_parameters
from cloudmesh.common.util import readfile
from pprint import pprint

testcase = """
title: My report
introduction:
  - this-is-a-good-filename1.pdf:
    caption: my fig 1
    label: "fig:1"
  - this-is-a-good-filename2.pdf:
    caption: my fig 2
    label: "fig:2"
  - this-is-a-good-filename3.pdf:
  - this-is-a-good-filename4.pdf:
"""


class Report:
    begin_document = \
        textwrap.dedent("""
        \\documentclass{article}
    
        \\usepackage{graphicx}
    
        \\begin{document}
        """)

    end_document = \
        textwrap.dedent("""
        \\end{document}
        """)

    def generate_image(self,
                       filename,
                       caption=None,
                       label=None,
                       ):
        if caption is None:
            caption = filename
        if label is None:
            label = f"fig:{self.counter}"
        image = \
            textwrap.dedent("""
              \\begin{{figure}}
              \\centering
              \\includegraphics{({filename)}}
              \\caption{{{caption}}}
              \\label{{fig:{filename}}}
              \\end{figure}
              """)
        self.counter = self.counter + 1
        return image

    def __init__(self, directory="./", config=None):
        self.counter = 0
        self.config = config
        self.directory = directory

    def generate(self):
        self.read_config()
        # mages = determin list of image of image files
        # for i in self.images:
        #   self.generate_image(images.)
        #   filename =  put value here and derive from images
        print(self.begin_document)

        pprint (self.content)

        for section in self.content:
            if section in "title":
                print (f"\\maketitle{{{section}}}")
            else:
                print(f"\\section{{{section}}}")

        print(self.end_document)

    def read_config(self):
        filename = self.config
        # TBD Vagul
        content = readfile(self.config)
        self.content = yaml.safe_load(content)



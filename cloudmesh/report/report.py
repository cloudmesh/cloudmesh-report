# tbd


a = """
\documentclass{article}

\usepackage{graphicx}


\begin{document}
"""


images = determin list of image of image files
for i in images:
  filename =  put value here and derive from images

  image = f"""
  \begin{{figure}}
  \centering
  \includegraphics{({filename)}}
  \caption{{{Histogram of {filename}}}}
  label{{fig:{filename}}}
  \end{figure}
  """

c =
"""
\ens{document}
"""
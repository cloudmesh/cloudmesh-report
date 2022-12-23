import matplotlib.pyplot as plt

from cloudmesh.common.Shell import Shell


def export_figure(
        basename="abc",
        directory="./images",
        kind="svg,pdf,png",
        title=None,
        x=None,
        y=None,
        axis_font=12,
        size=[8, 8],
        x_range=None,
        y_range=None,
        visible_xaxis=None,
        dpi=300):
    """

    :param basename: basename of the file
    :type basename: string
    :param directory: the directory where to stor the file
    :type directory: string
    :param kind: the kind of the putput
    :type kind: comma separated string
    :param title: title of the graph. In most cases no title should be provided
    :type title: string
    :param xlabel: The label on the x axis
    :type xlabel: string
    :param ylabel: The label on the y axis
    :type ylabel: string
    :param axis_font: The fontsize of the x and y axis
    :type axis_font: int
    :param size: The size of the image in inches
    :type size: list with two elements
    :param x_range: list with two elements to specify the minimum and maximum on the x axis
    :type x_range: list with two elements
    :param y_range: list with two elements to specify the minimum and maximum on the y axis
    :type y_range: list with two elements
    :param visible_xaxis: if False the x axis label and ticks will not be shown
    :type visible_xaxis: boolean
    :param dpi: The resolution of the image in png format
    :type dpi: int
    :return: plt, ax
    :rtype: list
    """
    fig, ax = plt.subplots()

    output_format = kind.split(",")

    frame1 = plt.gca()
    frame1.axes.get_xaxis().set_visible(visible_xaxis)
    fig.set_size_inches(size[0], size[1])
    if title is not None:
        fig.suptitle(title, fontsize=axis_font)

    if y is not None:
        plt.ylabel(y, fontsize=axis_font)
    if x is not None:
        plt.xlabel(x, fontsize=axis_font)
    if x_range is not None:
        plt.xlim(x_range)
    if y_range is not None:
        plt.ylim(y_range)

    # We change the fontsize of minor ticks label
    ax.tick_params(axis='both', which='major', labelsize=axis_font)
    ax.tick_params(axis='both', which='minor', labelsize=axis_font)

    if directory is None:
        directory = "./"
    Shell.mkdir(directory)

    for f in output_format:
        if f in output_format and f == "png":
            plt.savefig(f"{directory}/{basename}.{f}", dpi=dpi, bbox_inches="tight")
        else:
            plt.savefig(f"{directory}/{basename}.{f}", bbox_inches="tight")
    return plt, ax

from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.variables import Variables
from cloudmesh.common.util import banner

class ReportCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_report(self, args, arguments):
        """
        ::

          Usage:
                report FILE

          This command generates a report based on a yaml file that specifies images

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

          Description:

            > cms report config.yaml

        """


        # map_parameters(arguments, "FILE")

        VERBOSE(arguments)

        from cloudmesh.common.report.report import Report

        filename = arguments["FILE"]

        r = Report(filename=filename)
        r.generate(filename)

        return ""

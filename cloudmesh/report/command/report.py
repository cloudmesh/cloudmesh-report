from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command


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

        from cloudmesh.report.report import Report

        filename = arguments["FILE"]

        r = Report(config=filename)
        r.generate()

        return ""

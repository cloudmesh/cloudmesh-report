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


        map_parameters(arguments, "file", "parameter", "experiment")

        VERBOSE(arguments)

        banner("rewriting arguments so we convert to appropriate types for easier handeling", color="RED")

        arguments = Parameter.parse(arguments,
                                    parameter='expand',
                                    experiment='dict',
                                    COMMAND='str')


        VERBOSE(arguments)

        banner("showcasing tom simple if parsing based on teh dotdict", color="RED")


        #
        # It is important to keep the programming here to a minimum and any substantial programming ought
        # to be conducted in a separate class outside the command parameter manipulation. If between the
        # elif statement you have more than 10 lines, you may consider putting it in a class that you import
        # here and have propper methods in that class to handle the functionality. See the Manager class for
        # an example.
        #

        if arguments.file:
            print("option a")

        elif arguments.list:
            print("option b")


        Console.error("This is just a sample of an error")
        Console.warning("This is just a sample of a warning")
        Console.info("This is just a sample of an info")

        Console.info(" You can witch debugging on and off with 'cms debug on' or 'cms debug off'")

        return ""

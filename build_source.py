import json
import run_process

class BuildSource:
    def build(self, source_version):
        command = get_command(self, source_version)
        result = run_process.runProcess(command)
    
    def get_command(self, source_version):
        config = json.loads("antimage.config")
        command_prefix = config["command_prefix"]
        account = config["environment"]["dev"]["account"]
        aws_feature = "codebuild"
    
        command = command_prefix + " " + account + " aws " + aws_feature + " "
        subcommand = "start-build "
        project_name = "--project-name " + config["codebuild"]["source"]["buildname"] + " "
        source_version = "--source-version " + source_version + " "
        environment_variable = "--environment-variables-override" + self.get_environment_variables()
        
        return command + subcommand + project_name + source_version + environment_variable
    
    def get_environment_variables(self):
        result = ""
        for variable_name in config["codebuild"]["source"]["environment_variable"] {
            environment_variable_map = config["codebuild"]["source"]["environment_variable"]
            result += "name=" + variable_name + ",value=" + environment_variable_map[variable_name]["value"] \
                + ",type=" + environment_variable[variable_name]["type"] + " "
        }
    
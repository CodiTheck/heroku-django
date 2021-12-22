import os

def get_env_var(var_name, default_value=None):
    """ Program that is used to recovery the environment data """
    try:
        return os.environ[var_name];
    except KeyError:
        if default_value is None:
            error_msg = "Set the {} environment variable".format(var_name);
            raise ValueError("No key and no default value!");
        else:
            return default_value;


pass;

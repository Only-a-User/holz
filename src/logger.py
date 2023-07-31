from pathlib import Path


class Logger:
    __logging_types = ["printer", "logger", "both"]

    def __init__(self, log_path: str = "", logging_type: str = "printer", override: bool = False):
        # set logging_type
        if logging_type in self.__logging_types:
            self.__logging_type = logging_type
        else:
            raise ValueError(f"Value of attribute 'logging_type' needs to be one of: {self.__logging_types}.")

        # set log file path
        if not self.__logging_type == self.__logging_types[0]:
            __log_path = Path(log_path)
            # handle empty path
            if str(__log_path) == ".":
                __log_path = __log_path / "holz.log"
            # change file extension if not log
            if not __log_path.suffix == '.log':
                __log_path = __log_path.with_suffix('.log')
            # handle override settings
            if Path(log_path).is_file() and not override:
                raise FileExistsError("File already exists. To override the existing file, set: override=True")

            self.__log_path = __log_path
            
            self.__initialize_file()

    def __initialize_file(self):
        # create dir if it does not exist
        if not Path(self.__log_path.parent).is_dir():
            Path(self.__log_path.parent).mkdir(parents=True)
        # TODO

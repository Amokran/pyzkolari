import os
import datetime
import logging
import threading
import traceback

class LogManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *, default_log_level=None):
        """Singleton implementation to ensure only one instance of LogManager exists."""
        """So you can import LogManager from any module and use the same instance."""
        """If an instance already exists, return it. Otherwise, create a new one."""

        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._init__logger(default_log_level)
            return cls._instance

    def _init__logger(self, default_log_level= logging.DEBUG):
        """Initialize the logger with default settings."""
        """Creates a console handler by default if not already existing."""
        
        self._log_file          = None  # path to the log file
        self._file_handler      = None  # FileHandler instance
        self._console_handler   = None  # StreamHandler instance
        self._file_prepared     = False # True if the log file is prepared. If not, cannot enable file logging
        self._file_enabled      = False # True if file logging is enabled. If not, logs only to console
        self._logger            = logging.getLogger("Global_logger")

        # Prevent log messages from being propagated to the root logger and stablish default log level
        self._logger.propagate = False
        self.set_default_log_level(default_log_level)

        # Console handler setup. If already exists, do not create another one.
        if not self._handler_exists(logging.StreamHandler):
            print("Setting up console handler for logging.")
            # Create and configure console handler
            self._console_handler = logging.StreamHandler()
            self._console_handler.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
            self._console_handler.setLevel(logging.INFO)
            # Add the console handler to the logger
            self._logger.addHandler(self._console_handler)
            print("Console handler created and added to _logger.")
        else:
            print("Console handler already exists. Skipping creation.")

    def _handler_exists(self, handler_type):
        """Check if a handler of a given type (StreamHandler or FileHandler) is already attached."""
        """Returns True if a handler of the specified type exists, False otherwise."""

        for h in self._logger.handlers:
            if isinstance(h, handler_type):
                return True
        return False

    def prepare_logfile(self, brieffilename=None, logfolder=None, force_create_folder=False):
        """Prepare the log file for logging. Must be called before enabling file logging."""

        # If already prepared, do nothing and return True. Doing nothing is idempotent.
        if self._file_prepared:
            print("Log file already prepared. Skipping preparation.")
            raise Exception("Log file already prepared. Skipping preparation.")

        # Determine log file name.
        print("Preparing log file for logging...") 
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = None
        if brieffilename:
            log_filename = f"log_{brieffilename}_{timestamp}.log"
            print(f"Using tailored log filename: {log_filename}")
        else:
            log_filename = f"log_{timestamp}.log"
            print(f"Using default log filename: {log_filename}")

        # Determine log file path. Create log folder if it does not exist and force_create_folder is True.
        if logfolder:
            if os.path.isdir(logfolder):
                print(f"Log folder exists: {logfolder}")        
            else:
                if force_create_folder:
                    print(f"Creating log folder: {logfolder}")  
                    os.makedirs(logfolder, exist_ok=False)
                else:
                    print(f"⚠️ Warning. Log folder does not exist: {logfolder}. Log to file unprepared.")
                    raise Exception(f"Log folder does not exist: {logfolder}. Log to file unprepared.")
            self._log_file = os.path.abspath(os.path.join(logfolder, log_filename))
        else:
            self._log_file = os.path.abspath(log_filename)
        
        # Set the log file path in the environment variable and mark as prepared
        # os.environ["LOG_MANAGER_FILE"] = self._log_file
        self._file_prepared = True                   
        print(f"Log file prepared: {self._log_file}")

        # Create the file handler              
        self.create_file_handler()  
    
    def create_file_handler(self):
        if not self._file_prepared:
            raise RuntimeError("Log file not prepared. Call prepare_logfile() first.")
        if not self._handler_exists(logging.FileHandler):
            print("Creating file handler for logging.")
            self._file_handler = logging.FileHandler(self._log_file, encoding="utf-8")
            self._file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            self._file_handler.setLevel(logging.INFO)
            self._logger.addHandler(self._file_handler)
            print(f"File handler created for log file: {self._log_file}")
        else:
            raise RuntimeError("File handler already exists. Skipping creation.")    

    def remove_file_handler(self):
        if self._handler_exists(logging.FileHandler):
            print(f"Removing file handler for log file: {self._log_file}")
            self._logger.removeHandler(self._file_handler)
            self._file_handler.close()
            self._file_handler = None
            print("File handler removed.")
        else:
            print("No file handler to remove.")       

    def remove_console_handler(self):
        if self._handler_exists(logging.StreamHandler):
            print(f"Removing console handler")
            self._logger.removeHandler(self._console_handler)
            self._console_handler.close()
            self._console_handler = None
            print("Console handler removed.")
        else:
            print("No console handler to remove.")     

    def enable_file_logging(self,force_create_handler=False):
        if not self._file_prepared:
            raise RuntimeError("Log file not prepared. Call prepare_logfile() first.")
        
        if force_create_handler:
            print("Force creating file handler.")
            if self._file_handler:
                self.removeHandler(self._file_handler)
                create_success = self.create_file_handler()
                if not create_success:
                    raise RuntimeError("File handler not created. Log to file unprepared.")
                else:
                    print(f"File logging enabled. Log file: {self._log_file}")
            else:
                raise RuntimeError("File handler not initialized. Call prepare_logfile() first.")

        self._file_enabled = True
        print("File logging enabled.")

    def disable_file_logging(self,force_remove_handler=False):
        if force_remove_handler:
            print("Force removing file handler.")
            if self._file_handler:
                self._logger.removeHandler(self._file_handler)
                print(f"File handler removed for log file: {self._log_file}")
                self._file_handler.close()
            else:
                raise RuntimeError("File handler not initialized. Call prepare_logfile() first.")
        self._file_enabled = False
        print("File logging disabled.")

    def set_default_log_level(self, level):
        self._logger.setLevel(level)
        if self._console_handler:
            self._console_handler.setLevel(level)
        if self._file_handler:
            self._file_handler.setLevel(level)
    
    def set_console_level(self, level):
        if self._console_handler:
            self._console_handler.setLevel(level)

    def set_file_level(self, level):
        if self._file_handler:
            self._file_handler.setLevel(level)

    def get_filename(self):
        return self._log_file if self._file_enabled else None

    def log(self, message, level=logging.INFO):
        if isinstance(message, Exception):
            message = traceback.format_exc()
            level = logging.WARNING
        self._logger.log(level, message)

    def info(self, message):
        self.log(message, logging.INFO)

    def trace(self, message):
        self.log(message, logging.DEBUG)

    def warn(self, message):
        self.log(message, logging.WARNING)

    def error(self, message):
        self.log(message, logging.ERROR)
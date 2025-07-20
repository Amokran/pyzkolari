import os
import datetime
import logging
import threading
import traceback

class LogManager:
    _instance          = None
    _lock              = threading.Lock()
    _log_file          = None               # Unique log file for the current execution
    _log_level_console = logging.INFO       # Log level for console output
    _log_level_file    = logging.INFO       # Log level for file output

    def __new__(cls, brieffilename=None, logfolder=None):
        """ 
        Singleton pattern to ensure only one instance of LogManager exists.
        If an instance already exists, it returns the existing instance.
        Very useful for logging in different modules without creating multiple loggers.
        """
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize_logger(brieffilename, logfolder)
            return cls._instance

    def _initialize_logger(self, brieffilename, logfolder):
        """Initialize the logger with the specified brief filename and log folder."""
        if not brieffilename and not logfolder:
            log_path = os.getenv("LOG_MANAGER_FILE")
            if log_path:
                LogManager._log_file = log_path
            else:
                print("⚠️ Warning. A log file is not defined. Please initialize LogManager with LogManager(brieffilename, logfolder)")
                return

        if brieffilename and logfolder:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_filename = f"log_{brieffilename}_{timestamp}.log"

            logfolder = os.path.abspath(logfolder)
            os.makedirs(logfolder, exist_ok=True)

            LogManager._log_file = os.path.join(logfolder, log_filename)
            os.environ["LOG_MANAGER_FILE"] = LogManager._log_file  # Store the log file path in an environment variable for later use

        # Configure the logger
        if LogManager._log_file:
            self.logger = logging.getLogger("GlobalLogger")
            self.logger.setLevel(logging.INFO)
            self.logger.propagate = False 

            # Use this handler to avoid duplicate logs in the console
            file_handler = logging.FileHandler(LogManager._log_file, encoding="utf-8")
            file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(file_formatter)

            # Use this handler to print logs to the console
            console_handler = logging.StreamHandler()
            console_formatter = logging.Formatter('[%(levelname)s] %(message)s')
            console_handler.setFormatter(console_formatter)

            # Avoid adding handlers multiple times
            if not self.logger.handlers:
                self.logger.addHandler(file_handler)
                self.logger.addHandler(console_handler)

    def get_filename(self):
        return self._log_file

    def log(self, message, level=logging.INFO):
        """ Log a message at the specified logging level."""
        
        if not LogManager._log_file:
            raise RuntimeError("❌ Error: LogManager is not initialized with a log file. Please initialize it with LogManager(brieffilename, logfolder).")
        
        if isinstance(message, Exception):
            message = traceback.format_exc()  # Convierte la excepción en string con la traza completa
        
        self.logger.log(level, message)

    def info(self, message):
        self.log(message, logging.INFO)

    def trace(self, message):
        #Apparemtly, not working correctly, sometimes the trace is not shown
        self.log(message,logging.DEBUG)

    def warn(self, message):
        #Apparemtly, not working correctly, sometimes the trace is not shown
        self.log(message,logging.WARNING)

    def error(self, message):
        #Apparemtly, not working correctly, sometimes the trace is not shown
        self.log(message,logging.ERROR)
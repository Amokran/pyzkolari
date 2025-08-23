
import logging

def run_example():
    """
    Example function to demonstrate how to use the pyzkolari module.
    This function initializes the LogManager and ConfigManager, and logs a message.
    """
    from src.pyzkolari import LogManager

    # Initialize the log manager
    LOGGER = LogManager(default_log_level=logging.INFO)
    LOGGER.info("LogManager initialized successfully.")

    # Prepare and enable file logging
    try:
        LOGGER.info("Setting up file logging...")
        LOGGER.prepare_logfile(brieffilename="logfile", logfolder="./logs", force_create_folder=True)
        LOGGER.enable_file_logging()
        LOGGER.info("File logging setup successfully.")
    except Exception as e_file_logging:
        print(f"Exception during file loggin setup: {e_file_logging}")
     
    # If you want to use the LogManager inside any other module, you must import the other module right here, after initializing the LogManager.
    # For example:  
    #   from pyzkolari import SomeOtherModule

    # Log a message
    LOGGER.info("This is an example log message from the main.py script.")
    LOGGER.warn("This is a warning message.")
    LOGGER.error("This is an error message.")

    LOGGER.set_console_level(logging.WARNING)  # Set console log level to WARNING

    LOGGER.log("This is a debug message that will not be shown in the console due to the log level.")
    LOGGER.trace("This is a trace message that will not be shown in the console due to the log level.")
    LOGGER.info("Console log level set to WARNING. Debug and trace messages will not be shown in the console.")

    LOGGER.set_file_level(logging.ERROR)  # Set file log level to ERROR
    LOGGER.log("This is an info message that will not be logged neither to the console nor to the file due to the log level.")
    LOGGER.warn("This is a warning message that will be logged to the console, but not the file.")
    LOGGER.error("This is an error message that will be logged both to the console and to the file.")

    LOGGER.set_default_log_level(logging.DEBUG)  # Reset log level to DEBUG
    LOGGER.info("Log level reset to DEBUG. All messages will be logged in both console and file.")
    LOGGER.trace("This is a trace message that will be logged in both console and file.")
    LOGGER.disable_file_logging()  # Disable file logging
    LOGGER.info("File logging disabled. No messages will be logged to the file.")
    LOGGER.info("1")
    LOGGER.info("2")
    LOGGER.info("3")
    LOGGER.enable_file_logging()  # Re-enable file logging
    LOGGER.info("File logging re-enabled. Messages will be logged to the file again.")
    LOGGER.info("4")
    LOGGER.info("5")
    LOGGER.info("6")
    LOGGER.info("Example run completed successfully.")

if __name__ == "__main__":
    run_example()

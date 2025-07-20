

LOG_PATH = "./logs"  # Default log path

def run_example():
    """
    Example function to demonstrate how to use the pyzkolari module.
    This function initializes the LogManager and ConfigManager, and logs a message.
    """
    from src.pyzkolari import LogManager

    # Initialize the log manager
    LOGGER = LogManager.LogManager(brieffilename= "example", logfolder = LOG_PATH)
    LOGGER.info("LogManager initialized successfully.")

    # Initialize the config manager
    LOGGER.info("ConfigManager loaded configuration successfully.")

    # If you want to use the LogManager inside any other module, you must import the other module right here, after initializing the LogManager.
    # For example:  
    #   from pyzkolari import SomeOtherModule

    # Log a message
    LOGGER.info("This is an example log message from the main.py script.")
    LOGGER.warn("This is a warning message.")
    LOGGER.error("This is an error message.")

if __name__ == "__main__":
    run_example()

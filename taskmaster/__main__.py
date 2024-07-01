import logging
from taskmaster.cli.cli import main
from taskmaster.logging_config import logging

logging.debug("Starting __main__.py")

if __name__ == "__main__":
    main()

logging.debug("Finished running main in __main__.py")

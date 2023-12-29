import logging


"""
Much better option than print cos you can set them every where you need and based on a level print out 
only certain logs that are important
"""

def main() -> None:
    # set logging level you want to be printed = WARNING and above
    logging.basicConfig(level=logging.WARNING)

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")


if __name__ == "__main__":
    main()
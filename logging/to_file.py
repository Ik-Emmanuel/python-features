import logging
import os


pwd = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(pwd, "basic.log")

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename=file
    )

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")


if __name__ == "__main__":
    main()
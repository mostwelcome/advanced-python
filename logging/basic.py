import logging


def main():

    logging.basicConfig(level=logging.DEBUG,
                        filename='output.log', filemode='w')
    logging.debug("This is debug message")
    logging.info("Info")
    logging.warning("warning")
    logging.error("Error")
    logging.critical("Critical")
    name = 'swag'

    logging.info(f'Here is the name: {name}')


if __name__ == "__main__":
    main()

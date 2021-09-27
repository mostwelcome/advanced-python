import logging


def main():

    fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"

    logging.basicConfig(level=logging.DEBUG, filemode='w',
                        filename='output_custom.log', format=fmtstr)
    logging.info('This is in info level')
    logging.warning('This is in warning level')


if __name__ == "__main__":
    main()

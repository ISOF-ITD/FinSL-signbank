import platform


class Configuration():
    BEAR_DEVELOPMENT_COMPUTER_NAME = 'BearUbuntuTest'
    FRIGG_NAME = 'uuc-isof005.its.uu.se'
    FRIGG_TEST_NAME = 'uuc-isof004-t.its.uu.se'

    LOCALHOST_ADDRESS = 'localhost'
    ODEN_ADDRESS = 'oden.sprakochfolkminnen.se'
    ODEN_TEST_ADDRESS = 'oden-test.sprakochfolkminnen.se'

    computer = platform.node()
    debug = not (computer == FRIGG_NAME)
from wsceleryactivity.command import WsCeleryActivityCommand


def main():
    wsceleryactivity = WsCeleryActivityCommand()
    wsceleryactivity.execute_from_commandline()


if __name__ == '__main__':
    main()
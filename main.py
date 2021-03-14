from optparse import OptionParser
from pathlib import Path
from compression import compress, decompress


def _usage():
    print("usage: main.py compress <file>")
    print("usage: main.py compress <file>")


def main():
    parser = OptionParser(
        usage="usage: %prog [options] file",
        description="Compress and decompress Dockerfiles."
    )
    parser.add_option(
        "--compress",
        action="store_true",
        dest="compress",
        help="Compress a Dockerfile."
    )
    parser.add_option(
        "--decompress",
        action="store_true",
        dest="decompress",
        help="Decompress a previously compressed Dockerfile."
    )
    (options, args) = parser.parse_args()

    if not options.compress and not options.decompress:
        parser.error("must select either --compress or --decompress")
    if options.compress and options.decompress:
        parser.error("must select only one of --compress and --decompress")
    if len(args) != 1:
        parser.error("must specify exactly one file")
    file = Path(args[0])
    if not file.is_file():
        parser.error("path must be a file")

    if options.compress:
        compress(file)
        return
    else:
        decompress(file)
        return


if __name__ == "__main__":
    main()

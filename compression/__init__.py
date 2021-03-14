from pathlib import Path
from re import sub

# TODO Compress GZIP
# TODO Merge consecutive RUN commands.
# TODO Remove unused build stages.


def _can_merge(line: str) -> str:
    return line.strip().endswith("\\")


def _merge_lines(prev_line: str, line: str) -> str:
    if prev_line is not None and prev_line.strip().endswith("\\"):
        return prev_line.strip().strip("\\") + " " + line
    return line


def _compress_line(line: str) -> str:
    line = line.strip()

    # Remove comments.
    line = sub(r"^#.*", '', line)

    # Remove commands.
    line = sub(r"^MAINTAINER\s+.*", '', line)
    line = sub(r"^LABEL\s+.*", '', line)

    line = line.strip()
    if len(line) == 0:
        return None

    # Replace commands.
    line = sub(r"^FROM\s+", "F ", line)
    line = sub(r"^RUN\s+", "R ", line)
    line = sub(r"^CMD\s+", "M ", line)  # Only last takes effect.
    # line = sub(r"^LABEL\s+", "L ", line)
    # line = sub(r"^MAINTAINER\s+", "I ", line)
    line = sub(r"^EXPOSE\s+", "X ", line)
    line = sub(r"^ENV\s+", "E ", line)
    line = sub(r"^ADD\s+", "A ", line)
    line = sub(r"^COPY\s+", "C ", line)
    line = sub(r"^ENTRYPOINT\s+", "P ", line)  # Only last takes effect.
    line = sub(r"^VOLUME\s+", "V ", line)
    line = sub(r"^USER\s+", "U ", line)
    line = sub(r"^WORKDIR\s+", "W ", line)
    line = sub(r"^ARG\s+", "R ", line)
    line = sub(r"^ONBUILD\s+", "O ", line)
    line = sub(r"^STOPSIGNAL\s+", "T ", line)
    line = sub(r"^HEALTHCHECK\s+", "H ", line)  # Only last takes effect.
    line = sub(r"^SHELL\s+", "S ", line)

    # Remove useless RUN commands.
    # RUN cd
    # RUN ls
    # RUN echo

    # Remove unused quotes.
    # line = sub(r"\"([^\s,:\\]+)\"", r"\1", line)

    # Remove unused braces.
    # line = sub(r"\[([^\s,:\\]+)\]", r"\1", line)

    return line + "\n"


def compress(path: Path) -> Path:
    compressed = path.with_suffix(".compressed")

    prev_line: str = None
    with open(path, 'r') as in_file:
        with open(compressed, 'w') as out_file:
            for line in in_file:
                # If possible/needed merge with previous line.
                line = _merge_lines(prev_line, line)
                if _can_merge(line):
                    prev_line = line
                    continue
                else:
                    prev_line = None

                line = _compress_line(line)
                if line is None:
                    continue
                out_file.write(line)

    return compressed


def _decompress_line(line: str) -> str:
    # Replace commands.
    line = sub(r"^F\s+", "FROM ", line)
    line = sub(r"^R\s+", "RUN ", line)
    line = sub(r"^M\s+", "CMD ", line)
    # line = sub(r"^L\s+", "LABEL ", line)
    # line = sub(r"^I\s+", "MAINTAINER ", line)
    line = sub(r"^X\s+", "EXPOSE ", line)
    line = sub(r"^E\s+", "ENV ", line)
    line = sub(r"^A\s+", "ADD ", line)
    line = sub(r"^C\s+", "COPY ", line)
    line = sub(r"^P\s+", "ENTRYPOINT ", line)
    line = sub(r"^V\s+", "VOLUME ", line)
    line = sub(r"^U\s+", "USER ", line)
    line = sub(r"^W\s+", "WORKDIR ", line)
    line = sub(r"^R\s+", "ARG ", line)
    line = sub(r"^O\s+", "ONBUILD ", line)
    line = sub(r"^T\s+", "STOPSIGNAL ", line)
    line = sub(r"^H\s+", "HEALTHCHECK ", line)
    line = sub(r"^S\s+", "SHELL ", line)
    return line


def decompress(path: Path) -> Path:
    decompressed = path.with_suffix(".decompressed")

    with open(path, 'r') as in_file:
        with open(decompressed, 'w') as out_file:
            for line in in_file:
                line = _decompress_line(line)
                out_file.write(line)

    return decompressed

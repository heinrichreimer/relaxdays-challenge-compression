from pathlib import Path
from compression import compress, decompress
from os import system


def save_image(dockerfile: Path, image: Path):
    system("docker build -t tmp -f \"{file}\" \"{context}\"".format(
        file=dockerfile,
        context=dockerfile.parent
    ))
    system("docker save -o \"{image}\" tmp".format(
        image=image
    ))


def same(a: Path, b: Path):
    return system("diff \"{a}\" \"{b}\"".format(
        a=a,
        b=b
    )) == 0


original = Path(__file__).parent / "test" / "Dockerfile"
compressed = compress(original)
decompressed = decompress(compressed)

original_image = original.parent / "original.tar"
decompressed_image = original_image.parent / "decompressed.tar"

save_image(original, original_image)
save_image(decompressed, decompressed_image)
same = same(original_image,  decompressed_image)

if same:
    print("Good!")
else:
    print("Bad!")

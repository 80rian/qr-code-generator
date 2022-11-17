import argparse
import qrcode
from typing import Optional


def qr_generator(
    title: str,
    link: str,
    dir: Optional[str] = None,
) -> None:
    """
    creates a qr code with given link
    """

    title = title.split(".")[0]

    img = qrcode.make(link)

    dest = "." if dir is None else dir
    img.save(f"{dest}/{title}.jpg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--title",
        dest="title",
        type=str,
        required=True,
        help="name of the output file",
    )
    parser.add_argument(
        "--link",
        dest="link",
        type=str,
        required=True,
        help="qr code redirect link",
    )
    parser.add_argument(
        "--output-dir",
        dest="dir",
        type=str,
        required=False,
        help="output directory path",
    )

    args = vars(parser.parse_args())

    qr_generator(
        title=args["title"],
        link=args["link"],
        dir=args.get("dir"),
    )

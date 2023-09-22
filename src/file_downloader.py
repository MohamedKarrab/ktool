import urllib.request
import urllib.parse
import os


def file_downloader(args):
    try:
        print("Downloading..")
        url = args.url
        file_name = os.path.abspath(os.path.basename(urllib.parse.urlsplit(url).path))
        if args.output is not None:
            args.output = os.path.abspath(args.output)
            file_name = args.output
        urllib.request.urlretrieve(url, file_name)

    except Exception as e:
        print("An Error has occurred: ", e)
        return True
    download_directory = "/".join(file_name.split('/')[:-1])
    actual_file_name = file_name.split('/')[-1]
    print("File downloaded in ", download_directory, " as ", actual_file_name)
    return True

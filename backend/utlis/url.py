import json
import os


def get_url_list():
    urlpath = os.path.join(
        os.path.dirname(__file__),
        "../url"
    )
    urlfiles = os.listdir(urlpath)
    URLDict = {}

    for urlfile in urlfiles:
        with open(os.path.join(urlpath, urlfile), "r") as f:
            URLDict[urlfile.split(".")[0]] = json.load(f)
    return URLDict

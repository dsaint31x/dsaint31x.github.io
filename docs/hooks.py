import shutil


def copy_ads(*args, **kwargs):
    shutil.copy("ads.txt", "docs/ads.txt")
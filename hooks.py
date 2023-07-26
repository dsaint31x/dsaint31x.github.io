import shutil
import mkdocs.plugins

def on_pre_build(config):
    shutil.copy("mkdocs/ads.txt", "docs/ads.txt")


def copy_ads(*args, **kwargs):
    shutil.copy("ads.txt", "docs/ads.txt")

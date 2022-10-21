def remove_url_anchor(url: str):
    return url[:(url.find('#'))] if url.find('#') > 0 else url

def remove_url_anchor(url: str):
    return url.split('#')[0]
from flask import request, send_from_directory
from . import utility
from config import MEDIA_ROOT


def url_media(media_file_name: str) -> str:
    return request.host_url.rstrip("/") + f'/media/{media_file_name}'


@utility.route('/media/<path:filename>')
def media_files(filename):
    return send_from_directory(MEDIA_ROOT, filename)

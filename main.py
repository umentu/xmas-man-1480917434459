# -*- coding: utf-8 -*-

import os
import sys
import json
import re
import datetime
import calendar
import codecs
from operator import itemgetter

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import bottle
from bottle import route, run
from bottle import TEMPLATE_PATH, jinja2_template as template
from bottle import static_file
from bottle import request, response
from bottle import redirect
from bottle import default_app

from jinja2 import Environment, PackageLoader
from PIL import Image

bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024 * 1024

# sites.pyが設置されているディレクトリの絶対パスを取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# テンプレートファイルを設置するディレクトリのパスを指定
TEMPLATE_PATH.append(BASE_DIR + "/templates")

"""
static files
"""
@route('/css/<filename>')
def server_css(filename):
    """ setting for css file """
    return static_file(filename, root=BASE_DIR+"/static/css")


@route('/js/<filename>')
def server_js(filename):
    """ setting for js file """
    return static_file(filename, root=BASE_DIR+"/static/js")


@route('/images/<filename>')
def server_img(filename):
    """ setting for images file """
    return static_file(filename, root=BASE_DIR+"/static/images")


@route('/fonts/<filename>')
def server_font(filename):
    """ setting for font file """
    return static_file(filename, root=BASE_DIR+"/static/fonts")


@route('/images/<filename>')
def server_images(filename):
    """ setting for font file """
    return static_file(filename, root=BASE_DIR+"/images")


@route('/thumbnail/<filename>')
def server_thumbnail(filename):
    """ setting for font file """
    return static_file(filename, root=BASE_DIR+"/thumbnail")

@route('/timelapse/<filename>')
def server_timelapse(filename):
    """ setting for font file """
    return static_file(filename, root=BASE_DIR+"/timelapse")


@route('/', method='GET')
def index(title='トップページ'):
    """TOPPAGE """
    images = os.listdir(BASE_DIR+ "/thumbnail")
    images = sorted(images, reverse=True)[0:100]

    return template('index.html', {"images": images})

@route('/timelapse', method='GET')
def timelapse(title='トップページ'):
    """TOPPAGE """

    return template('timelapse.html')



@route('/upload', method="POST")
def upload():

    image_file = request.files.image

    if re.search("[0-9]+\.jpg", image_file.filename):

        file_name = image_file.filename
        image_file.save(IMAGE_DIR + file_name, overwrite=True)

        img = Image.open( IMAGE_DIR + file_name )
        img.thumbnail( (80, 60) )
        img.save( THUMB_DIR + file_name )

    return "ok"


if __name__ == '__main__':
    run(host='xmas-man.mybluemix.net', port=8000, debug=True, reloader=True)
else:
    application = default_app()

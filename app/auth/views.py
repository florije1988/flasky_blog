# -*- coding: utf-8 -*-
__author__ = 'florije'

from flask import render_template
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')

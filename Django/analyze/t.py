__author__ = 'Xc'
import os

static_dir = os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/')
print os.listdir(static_dir)
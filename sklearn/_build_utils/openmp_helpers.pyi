# This code is adapted for a large part from the astropy openmp helpers, which
# can be found at: https://github.com/astropy/extension-helpers/blob/master/extension_helpers/_openmp_helpers.py  # noqa

import os
import sys
import textwrap
import warnings
import subprocess

from distutils.errors import CompileError, LinkError

from .pre_build_helpers import compile_test_program

def get_openmp_flag(compiler): ...
def check_openmp_support(): ...

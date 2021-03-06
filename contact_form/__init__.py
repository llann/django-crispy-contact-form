VERSION = (0, 3, 3, 'stable')


def get_release():
    return '-'.join([get_version(), VERSION[-1]])


def get_version():
    """
    Returns only digit parts of version.
    """
    return '.'.join(str(i) for i in VERSION[:3])


__author__ = 'dlancer'
__docformat__ = 'restructuredtext en'
__copyright__ = 'Copyright 2014-2017, dlancer'
__license__ = 'BSD'
__version__ = get_version()
__maintainer__ = 'dlancer'
__email__ = 'dmdpost@gmail.com'
__status__ = 'Development'

# default the contact_form app config
default_app_config = 'contact_form.apps.AppConfig'

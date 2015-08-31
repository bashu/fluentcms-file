fluentcms-file
==============

A file plugin for django-fluent-contents_

Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: shell

    pip install fluentcms-file


Backend Configuration
---------------------

First make sure the project is configured for django-fluent-contents_.

Then add the following settings:

.. code-block:: python

    INSTALLED_APPS += (
        'fluentcms_file',
    )

    # The upload folder for all files.
    # Defaults to the root of the media folder.
    FLUENTCMS_FILE_UPLOAD_TO = 'uploads/'

The database tables can be created afterwards:

.. code-block:: shell

    python ./manage.py migrate

Now, the ``FilePlugin`` can be added to your ``PlaceholderField`` and
``PlaceholderEditorAdmin`` admin screens.

Frontend Configuration
----------------------

If needed, the HTML code can be overwritten by redefining ``fluentcms_file/file.html``.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/edoburu/django-fluent-contents

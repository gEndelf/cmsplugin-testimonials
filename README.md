cmsplugin-randomquote
=====================

Testimonials django-cms plugin based on [**random quote** plugin](https://github.com/dbrgn/cmsplugin-randomquote).

Setup / Configuration
---------------------

- Install this plugin (``pip install cmsplugin-testimonials``)
- Add ``cmsplugin-testimonials`` to your ``INSTALLED_APPS``
- Run the schema migrations:
  
```
    python manage.py syncdb
    python manage.py migrate cmsplugin-testimonials
```

- Add the plugin to a placeholder
- Create some ``Testimonial`` Objects in the admin panel

License
-------

[MIT](http://www.opensource.org/licenses/mit-license.html), see LICENSE

Changelog
---------

v1.0.0 (11.09.14)
~~~~~~~~~~~~~~~~~

- Separated from https://github.com/dbrgn/cmsplugin-randomquote django-cms plugin
- add carousel functionality

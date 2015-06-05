Installation
------------

Firstly, install postgreSQL and create a DB. Then, write in your terminal:

.. code-block :: pycon

    >>> pip install -r requirements.txt
    >>> export DATABASE_URL="postgresql:///[name]"
    >>> export APP_SETTINGS="config.Config"

To create the tables, enter python and type:

.. code-block :: pycon

    >>> from app import db
    >>> db.create_all()

Then run ``python app.py``. Voila!


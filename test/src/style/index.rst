Guidelines
**********

.. slideconf::
   :theme: boundless_single
   :autoslides: True

.. ifslides::
   
   Theme ``boundless_single``

Writing Style
=============

This section concerns the tone and voice used when writing text for workbooks.

These writing guidelines are compatible with the writing style of Boundless Server, which are extension of the GeoServer `Documentation Guide <http://docs.geoserver.org/latest/en/docguide/style.html>`__ instructions.

.. ifnotslides::

   Reference:

   * :server:`Boundless Server User Manual <index.html>`
   * `Style Guidelines <http://docs.geoserver.org/latest/en/docguide/style.html>`__ (GeoServer Documentation Guide)

Be concise
----------

Style guide: *Documentation should be concise and not just a brain dump. Reference material should contain short pages and be easy to refer to without having to scroll through a large volume of text.  Tutorials can be longer, depending on scope.  If the point of the document is to share your thoughts and insights, it belongs in a blog post.  This documentation is a manual, not a wiki.*

.. nextslide::
   :increment:

For training materials we fall under "tutorials". Concise writing, with the understanding that understand that repetition, and taking multiple perspectives on the same subject matter, is required to communicate key ideas.

* For key ideas we often looking to communicate through a) text b) diagram c) hands-on step-by-step instructions.

* Consider to how to communicate the idea using both GIS professional terms, and IT professional terms.

Avoid marketing
---------------

Style guide: *If the point of the document is to showcase a new feature it does not belong in the documentation. Write an article or a blog post about it. If it is necessary to point out a technical benefit of a feature then do so from a technical standpoint.*

Bad
   Super-overlays are a great way to publish super cool datasets awesomely in Google Earth!
Good
   Super-overlays allow you to efficiently publish data via Google Earth.

.. nextslide::
   :increment:

Training is in-between marketing and documentation and marketing.

Many attending our instruction are being introduced to the product for the first time and we have a goal to entertain and get attendees excited about the technology and how it can be applied in their organization.

Guidance: Please leave feature-promotion to the description of the technology, and instructor notes. Needless verbiage, however enthusiastic, should not distrupt from step by step instructions.

Be professional
---------------

Style Guide: *Avoid the use of slang or other "colorful" language. The point of a technical document is to be informative, not to keep the reader amused.  Avoiding slang helps keep the document accessible to as large an audience as possible.*

Bad
   Next, fire up whatever tool you use to browse the web and point it in the direction of ...
Good
   Next, start your web browser and navigate to ...

.. nextslide::
   :increment:

Guidance: This is a difficult a difficult balance for training material, when teaching internationally simple consistent professional langague works best. If you have a some a colorful story, or description, please add as an instructor notes.

Use direct commands
-------------------

Style Guide: *When providing step-by-step instructions, use direct commands or requests. Avoid the use of "we" and "let's".*

Bad
   Now let's add a shapefile by ...
Good
   Add a shapefile by ...

Naming conventions
------------------

.. ifslides::
   
   Follow the Wikipedia naming conventions for page names, section names, verb use, and avoiding plurals.
   
.. ifnotslides::

    Reference:

    * `Wikipedia naming conventions <http://en.wikipedia.org/wiki/Wikipedia:Naming_conventions>`_.

.. nextslide:: Naming: Capitalization of page names

Capitalization of page names: Each word in the page name should be capitalized except for articles (such as "the", "a", "an") and conjunctions (such as "and", "but", "or"). A page name should never start with an article.

Bad
   Adding a shapefile or postgis table
Good
   Adding a Shapefile or PostGIS Table

Bad
   The Shapefile Tutorial
Good
   Shapefile Tutorial

.. nextslide:: Naming: Capitalization of section names

Capitalization of section names: Do not capitalize second and subsequent words unless the title is almost always capitalized in English (like proper names). Thus, capitalize John Wayne and Art Nouveau, but not Video Games.

Bad
   Creating a New Datastore
Good
   Creating a new datastore

.. nextslide:: Naming: Verb usage

Verb usage: It is recommended that the gerund (the -ing form in English) be used unless there is a more common noun form. For example, an article on swimming is better than one on swim.

Bad
   Create a new datastore
Good
   Creating a new datastore

.. nextslide:: Naming: Avoid plurals

Avoid plurals: Create page titles that are in the singular.  Exceptions to this are nouns that are always plural (scissors, trousers), a small class that requires a plural (polar coordinates, Bantu languages, The Beatles).

Bad
   Templates tutorial
Good
   Template tutorial

Formatting
----------

Any code or command line snippets should be formatted as code:

.. code-block:: bash

   $ ls

.. code-block:: bat

   > dir

Code examples include line numbers:

.. code-block:: python
   :linenos:
   
   my_string = "Hello, World!"
   print(my_string)

.. nextslide::
   :increment:

.. ifnotslides:: When considering PDF output we have some hard limitations on lines are longer than 77 characters. 

Use multiple lines in a format appropriate for the language in use. If possible, snippets should be functional when pasted directly into the appropriate target.

.. ifnotslides:: 
   
   For example, Java and XML make no distinction between a single space and multiple spaces, so the following snippets are fine:

.. code-block:: Java
   :linenos:

   org.geoserver.package.Object someVeryLongIdentifier =
      org.geoserver.package.Object.factoryMethod();

.. code-block:: xml
   :linenos:

   <namespace:tagname attributename="attributevalue"
      attribute2="attributevalue" nextattribute="this is on another line"/>

.. nextslide::
   :increment:

For shell scripts, new lines can be escaped with a backslash character :kbd:`\\`. It is also recommended to use a simple ``$`` prompt to save space. For example:

.. code-block:: bash

   $ /org/jdk1.5.0*/bin/java \
      -cp /home/user/.m2/repository/org/geoserver/*/*.jar \
      org.geoserver.GeoServer \
      -DGEOSERVER_DATA_DIR=/var/lib/geoserver_data/release

For windows commands, characters can be escaped with a :kbd:`^` character, but it is so unusual that it is not recommended. The ``>`` prompt can be used to save space.

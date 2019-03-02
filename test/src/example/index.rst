Examples
********

.. slideconf::
   :theme: boundless_single
   :autoslides: True

.. ifslides::
   
   Slide theme ``boundless_single``

.. ifnotslides::
   
   Illustrative examples Boundless Learning, also used as a stress test of ``boundless_single`` slide theme.

Connecting with pgAdmin
=======================

Use :command:`pgAdmin` to administration applications to connect to the PostgresSQL server running on localhost.

Launch the :command:`pgAdmin` application and connect to :command:`PostgreSQL`.

.. rst-class:: break

.. nextslide::

.. admonition:: Exercise Connecting to PostgreSQL   

   .. ifnotslides::  

      .. include:: exercise_connecting_to_postgresql.txt

Creating a Database
===================

The PostgreSQL application is installed as a service on Windows or Linux, and is capable of running several databases at once (with their own distinct security policies, extensions and content).  In the next Exercise we will create the ``training`` database used for this module.

.. rst-class:: break

.. nextslide::

.. admonition:: Exercise Creating a Postgres Database

   .. ifnotslides::
   
      .. include:: exercise_create_database.txt

.. ifnotslides::

   .. admonition:: SQL Reference
      
      * :postgresql:`createdb <app-createdb.html>`

PostGIS Extension Installation
==============================

The PostGIS extension can be added to a database to enable the geometry datatypes, spatial indexing, and functions required for a spatial database.  In the next Exercise we will add the PostGIS extension to the `training` database.
      
.. rst-class:: break

.. nextslide::

.. admonition:: Exercise Enabling the PostGIS extension

   .. ifnotslides::

      .. include:: exercise_enable_postgis_extension.txt

.. ifnotslides::

   .. admonition:: SQL Reference

      * :postgis:`Creating a spatial database using EXTENSIONS <postgis_installation.html#create_new_db_extensions>`
      * :postgresql:`CREATE EXTENSION <sql-createextension.html>` - add an extension to the current database
      * :postgis:`postgis_full_version <PostGIS_Full_Version.html>` -  reports full PostGIS version and build configuration info.

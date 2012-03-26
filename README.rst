=============================
ScaCS (Scala Cluster Service)
=============================

ScaCS provides a Scala framework used to manage the nodes of a cluster, their
data and the computations applied to that data.

Build from source
=================

Get the source code
-------------------

::

   $ git clone git://github.com/gdiscry/scacs.git
   $ cd scacs

Dependencies
------------

ScaCS requires the following dependencies to build from source:

- sbt_ ≥ v0.10 (v0.11.2 recommended)
- Akka_ ≥ v2.0 (fetched by sbt_)

Compilation
-----------

.. note::

   sbt_ is used to manage the build process of the project. You can use it
   directly from the command line::

      $ sbt '<command1>' '<command2>'

   or from an interactive shell::

      $ sbt
      > <command1>
      > <command2>

To compile ScaCS, use the ``compile`` sbt command::

   $ sbt compile

.. _sbt: https://github.com/harrah/xsbt/wiki
.. _Akka: http://akka.io/

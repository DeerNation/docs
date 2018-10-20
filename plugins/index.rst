Plugins
=======

Activity payload plugins
~~~~~~~~~~~~~~~~~~~~~~~~

Payload plugins add new messages types to the system. The basic data type that is sent in the channels is
an `Activity`. Activities consist of some general data, like the channel they have been published in, the
publishing date, the actor that did publish the message an some others. The actual content of the message
is defined by payload plugins.

As default, two payload plugins are part of the system:

1. A simple message type:

.. code-block:: javascript

    Message {
        content: string
        link: string
    }


The content is a string in markdown syntax and the link is a simple URL. Usually a message contains
either a content or a link, but not both at the same time.

2. An event type:

.. code-block:: javascript

    Event {
        name: string
        start: dateTime
        end: dateTime
        description: string
        organizer: string
        location: string
        categories: string[]
    }

The event type can be used for time related events that can be used in a calendar.

A payload plugins provides different features that are necessary to handle their data in backend and frontend,
the necessary parts are:

.. toctree::
   :hidden:

   payload/manifest
   payload/create


Backend:
********

1. A ``proto``-file that defines the data structure
2. A ``JSON-Schema`` definition that is used to check if a provided data structure is a valid message
3. An optional ``NotificationHandler``, that converts a message into a push notification
4. An optional ``QueryHandler`` that defines filters and options to customize queries for this payload type
   (e.g. used by the event payload plugin to allow querying event of a certain date range)

.. toctree::
    :glob:
    :maxdepth: 1
    :hidden:

    payload/backend/*

Frontend:
*********

1. A ``View-Renderer`` to render a message in the GUI including themes for that
2. A ``Form`` that allows message to be created/edited
3. ``Translations`` for the frontend
4. An optional ``Channel-View`` that shows channels of only this payload type, e.g. a Calendar view provided
   by the event payload plugin that shows events in a calendar

.. toctree::
    :glob:
    :maxdepth: 1
    :hidden:

    payload/frontend/*

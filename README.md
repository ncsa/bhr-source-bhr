BHR source BHR
==============

BHR block source that uses another BHR installation as a data source.
This allows you to peer with another site at the BHR level, instead of requiring the use of BGP peering.
This allows you to filter the blocks before they are applied.

This code works works, but the use of the source mapping prevents the use of

    must_exist = True

and some sites may want that functionality.  It would not be impossible to add
that functionality, but some refactoring in bhr\_client would be needed.


Configuration
=============

As with the regular BHR Client the BHR\_HOST, BHR\_TOKEN variables need to be set.
Additionally BHR\_PEER\_HOST and BHR\_PEER\_TOKEN variables for the second site need to be set.
Finally, BHR\_PEER\_SOURCE\_MAPPING\_FILE should be set to the path of a csv file containg two columns.
The name of the remote source that you want to sync locally, and the name it should be renamed to.

environment variables
~~~~~~~~~~~~~~~~~~~~~

    export BHR_HOST=https://bhr.us.example.com/
    export BHR_TOKEN=xxx
    export BHR_PEER_HOST=https://bhr.eu.example.com/
    export BHR_PEER_TOKEN=xxx
    export BHR_PEER_SOURCE_MAPPING_FILE=mapping.csv


mapping.csv
~~~~~~~~~~~

    scanners,scanners_eu

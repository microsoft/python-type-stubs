from xml.sax import handler
from netaddr.core import Publisher, Subscriber

"""
Routines for accessing data published by IANA (Internet Assigned Numbers
Authority).

More details can be found at the following URLs :-

    - IANA Home Page - http://www.iana.org/
    - IEEE Protocols Information Home Page - http://www.iana.org/protocols/
"""
IANA_INFO = {"IPv4": {}, "IPv6": {}, "IPv6_unicast": {}, "multicast": {}}

class SaxRecordParser(handler.ContentHandler):
    def __init__(self, callback=...) -> None: ...
    def startElement(self, name, attrs): ...
    def endElement(self, name): ...
    def characters(self, content): ...

class XMLRecordParser(Publisher):
    """
    A configurable Parser that understands how to parse XML based records.
    """

    def __init__(self, fh, **kwargs) -> None:
        """
        Constructor.

        fh - a valid, open file handle to XML based record data.
        """
        ...
    def process_record(self, rec):
        """
        This is the callback method invoked for every record. It is usually
        over-ridden by base classes to provide specific record-based logic.

        Any record can be vetoed (not passed to registered Subscriber objects)
        by simply returning None.
        """
        ...
    def consume_record(self, rec): ...
    def parse(self):
        """
        Parse and normalises records, notifying registered subscribers with
        record data as it is encountered.
        """
        ...

class IPv4Parser(XMLRecordParser):
    """
    A XMLRecordParser that understands how to parse and retrieve data records
    from the IANA IPv4 address space file.

    It can be found online here :-

        - http://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xml
    """

    def __init__(self, fh, **kwargs) -> None:
        """
        Constructor.

        fh - a valid, open file handle to an IANA IPv4 address space file.

        kwargs - additional parser options.
        """
        ...
    def process_record(self, rec):
        """
        Callback method invoked for every record.

        See base class method for more details.
        """
        ...

class IPv6Parser(XMLRecordParser):
    """
    A XMLRecordParser that understands how to parse and retrieve data records
    from the IANA IPv6 address space file.

    It can be found online here :-

        - http://www.iana.org/assignments/ipv6-address-space/ipv6-address-space.xml
    """

    def __init__(self, fh, **kwargs) -> None:
        """
        Constructor.

        fh - a valid, open file handle to an IANA IPv6 address space file.

        kwargs - additional parser options.
        """
        ...
    def process_record(self, rec):
        """
        Callback method invoked for every record.

        See base class method for more details.
        """
        ...

class IPv6UnicastParser(XMLRecordParser):
    """
    A XMLRecordParser that understands how to parse and retrieve data records
    from the IANA IPv6 unicast address assignments file.

    It can be found online here :-

        - http://www.iana.org/assignments/ipv6-unicast-address-assignments/ipv6-unicast-address-assignments.xml
    """

    def __init__(self, fh, **kwargs) -> None:
        """
        Constructor.

        fh - a valid, open file handle to an IANA IPv6 address space file.

        kwargs - additional parser options.
        """
        ...
    def process_record(self, rec):
        """
        Callback method invoked for every record.

        See base class method for more details.
        """
        ...

class MulticastParser(XMLRecordParser):
    """
    A XMLRecordParser that knows how to process the IANA IPv4 multicast address
    allocation file.

    It can be found online here :-

        - http://www.iana.org/assignments/multicast-addresses/multicast-addresses.xml
    """

    def __init__(self, fh, **kwargs) -> None:
        """
        Constructor.

        fh - a valid, open file handle to an IANA IPv4 multicast address
             allocation file.

        kwargs - additional parser options.
        """
        ...
    def normalise_addr(self, addr):
        """
        Removes variations from address entries found in this particular file.
        """
        ...
    def process_record(self, rec):
        """
        Callback method invoked for every record.

        See base class method for more details.
        """
        ...

class DictUpdater(Subscriber):
    """
    Concrete Subscriber that inserts records received from a Publisher into a
    dictionary.
    """

    def __init__(self, dct, topic, unique_key) -> None:
        """
        Constructor.

        dct - lookup dict or dict like object to insert records into.

        topic - high-level category name of data to be processed.

        unique_key - key name in data dict that uniquely identifies it.
        """
        ...
    def update(self, data):
        """
        Callback function used by Publisher to notify this Subscriber about
        an update. Stores topic based information into dictionary passed to
        constructor.
        """
        ...

def load_info():
    """
    Parse and load internal IANA data lookups with the latest information from
    data files.
    """
    ...

def pprint_info(fh=...):
    """
    Pretty prints IANA information to filehandle.
    """
    ...

def query(ip_addr):
    """Returns informational data specific to this IP address."""
    ...


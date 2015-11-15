from xml.etree import ElementTree


def xml2dict(xml_data):
    '''convert xml to dict

    >>> xml2dict("""
    ... <?xml version="1.0" encoding="UTF-8"?>
    ... <spam ham="egg">
    ...     <foo>bar</foo>
    ... </spam>
    ... """)
    {'tag': 'spam',
     'attrib': {'ham': 'egg'},
     'children': [{'tag': 'foo', 'text': 'bar'}]}
    '''
    xml_data = xml_data.decode('utf-8')
    xml_data = u''.join([
        line.strip() for line in xml_data.splitlines()
        if line.strip()])
    # ElementTree can decode by xml encoding declaration
    xml_data = xml_data.encode('utf-8')

    return _xml2dict(ElementTree.fromstring(xml_data))


def _xml2dict(element):
    children = []
    for child in element:
        children.append(_xml2dict(child))

    result = {'tag': element.tag}
    if element.text:
        result['text'] = element.text
    if element.attrib:
        result['attrib'] = element.attrib
    if children:
        result['children'] = children
    return result

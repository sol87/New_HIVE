# coding=utf-8
#__author__ = "xuguoliang"
# description="""  """

from sub_importer import *
from xml.etree import ElementTree
from XmlDictObject import XmlDictObject


def dict_to_xml(dict,xmlfile):
    root = ConvertDictToXml(dict)
    tree = ElementTree.ElementTree(root)
    tree.write(xmlfile,encoding="UTF-8",xml_declaration=True)

def ConvertDictToXml(xmldict):
    """
    Converts a dictionary to an XML ElementTree Element 
    """

    roottag = xmldict.keys()[0]
    root = ElementTree.Element(roottag)
    _ConvertDictToXmlRecurse(root, xmldict[roottag])
    return root
    
    
def _ConvertDictToXmlRecurse(parent, dictitem):
    assert type(dictitem) is not type([])

    if isinstance(dictitem, dict):
        for (tag, child) in dictitem.iteritems():
            if str(tag) == '_text':
                parent.text = str(child)
            elif type(child) is type([]):
                # iterate through the array and convert
                for listchild in child:
                    elem = ElementTree.Element(tag)
                    parent.append(elem)
                    _ConvertDictToXmlRecurse(elem, listchild)
            else:                
                elem = ElementTree.Element(tag)
                parent.append(elem)
                _ConvertDictToXmlRecurse(elem, child)
    else:
        parent.text = unicode(dictitem)
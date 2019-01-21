import os
import uuid
import xml.etree.ElementTree as ET

def add_accessibility_if_needed(xml_path):
    views = []
    xml_file = ET.parse(xml_path)
    root = xml_file.getroot()
    # get all subviews
    for subview in root.iter('subviews'):
        # through by all childs
        for child in subview:
            # get child tags
            tags = list(map(lambda subchild: subchild.tag, child))
            # if child don't have 'accessibility' tag   
            if "accessibility" not in tags:   
                views.append(child) # add child

    # add "accessibility" tag to all views
    for view in views:
        accessibility = ET.Element("accessibility", key="accessibilityConfiguration", identifier=str(uuid.uuid1()))  
        view.insert(0,accessibility)
    # save changes    
    xml_file.write(xml_path)

    


    

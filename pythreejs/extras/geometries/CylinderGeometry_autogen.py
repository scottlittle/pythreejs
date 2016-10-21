from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry


class CylinderGeometry(Geometry):
    """CylinderGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:47:51 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/CylinderGeometry 
    """

    def __init__(self, radiusTop=20, radiusBottom=20, height=100, radiusSegments=8, heightSegments=1, openEnded=False, thetaStart=0, thetaLength=6.283185307179586, **kwargs):
        kwargs['radiusTop'] = radiusTop
        kwargs['radiusBottom'] = radiusBottom
        kwargs['height'] = height
        kwargs['radiusSegments'] = radiusSegments
        kwargs['heightSegments'] = heightSegments
        kwargs['openEnded'] = openEnded
        kwargs['thetaStart'] = thetaStart
        kwargs['thetaLength'] = thetaLength
        super(Geometry, self).__init__(**kwargs)

    _view_name = Unicode('CylinderGeometryView').tag(sync=True)
    _model_name = Unicode('CylinderGeometryModel').tag(sync=True)

    radiusTop = CFloat(20).tag(sync=True)
    radiusBottom = CFloat(20).tag(sync=True)
    height = CFloat(100).tag(sync=True)
    radiusSegments = CInt(8).tag(sync=True)
    heightSegments = CInt(1).tag(sync=True)
    openEnded = Bool(False).tag(sync=True)
    thetaStart = CFloat(0).tag(sync=True)
    thetaLength = CFloat(6.283185307179586).tag(sync=True)


from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ...enums import *
from ...traits import *

from ...core.Geometry_autogen import Geometry

from ..core.Shape_autogen import Shape

class ShapeGeometry(Geometry):
    """ShapeGeometry
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:47:51 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Extras.Geometries/ShapeGeometry 
    """

    def __init__(self, shapes=[], **kwargs):
        kwargs['shapes'] = shapes
        super(Geometry, self).__init__(**kwargs)

    _view_name = Unicode('ShapeGeometryView').tag(sync=True)
    _model_name = Unicode('ShapeGeometryModel').tag(sync=True)

    shapes = Tuple().tag(sync=True, **widget_serialization)
    curveSegments = CInt(12).tag(sync=True)
    material = CInt(0).tag(sync=True)


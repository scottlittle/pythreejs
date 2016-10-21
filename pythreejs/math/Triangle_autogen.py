from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Triangle(ThreeWidget):
    """Triangle
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:47:51 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Math/Triangle 
    """

    def __init__(self, a=[0,0,0], b=[0,0,0], c=[0,0,0], **kwargs):
        kwargs['a'] = a
        kwargs['b'] = b
        kwargs['c'] = c
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('TriangleView').tag(sync=True)
    _model_name = Unicode('TriangleModel').tag(sync=True)

    a = Vector3(default=[0,0,0]).tag(sync=True)
    b = Vector3(default=[0,0,0]).tag(sync=True)
    c = Vector3(default=[0,0,0]).tag(sync=True)


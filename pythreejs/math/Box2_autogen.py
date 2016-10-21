from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from .._base.Three import ThreeWidget


class Box2(ThreeWidget):
    """Box2
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:47:51 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Math/Box2 
    """

    def __init__(self, min=[0,0], max=[0,0], **kwargs):
        kwargs['min'] = min
        kwargs['max'] = max
        super(ThreeWidget, self).__init__(**kwargs)

    _view_name = Unicode('Box2View').tag(sync=True)
    _model_name = Unicode('Box2Model').tag(sync=True)

    min = Vector2(default=[0,0]).tag(sync=True)
    max = Vector2(default=[0,0]).tag(sync=True)


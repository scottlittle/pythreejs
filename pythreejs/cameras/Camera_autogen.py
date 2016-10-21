from ipywidgets import Widget, DOMWidget, widget_serialization, Color
from traitlets import Unicode, Int, CInt, Instance, This, Enum, Tuple, List, Dict, Float, CFloat, Bool, Union, Any

from ..enums import *
from ..traits import *

from ..core.Object3D import Object3D


class Camera(Object3D):
    """Camera
    
    Autogenerated by generate-wrappers.js 
    Date: Fri Oct 21 2016 15:47:51 GMT-0700 (PDT) 
    See http://threejs.org/docs/#Reference/Cameras/Camera 
    """

    def __init__(self, **kwargs):
        super(Object3D, self).__init__(**kwargs)

    _view_name = Unicode('CameraView').tag(sync=True)
    _model_name = Unicode('CameraModel').tag(sync=True)

    matrixWorldInverse = Matrix4(default=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]).tag(sync=True)
    projectionMatrix = Matrix4(default=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]).tag(sync=True)


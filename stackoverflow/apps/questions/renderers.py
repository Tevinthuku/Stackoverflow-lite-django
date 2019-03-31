import json
from rest_framework.renderers import JSONRenderer


class BaseRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, media_type=None, render_context=None):
        errors = data.get("error", None)
        if errors is not None:
            return super(BaseRenderer, self).render(data)
        return json.dumps({
            "status": "success",
            "data": data
        })

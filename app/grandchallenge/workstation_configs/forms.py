from django.forms import ModelForm

from grandchallenge.core.forms import SaveFormInitMixin
from grandchallenge.core.widgets import JSONEditorWidget
from grandchallenge.workstation_configs.models import (
    OVERLAY_SEGMENTS_SCHEMA,
    WorkstationConfig,
)


class WorkstationConfigForm(SaveFormInitMixin, ModelForm):
    class Meta:
        model = WorkstationConfig
        fields = (
            "title",
            "description",
            "window_presets",
            "default_window_preset",
            "default_slab_thickness_mm",
            "default_slab_render_method",
            "default_orientation",
            "default_overlay_alpha",
            "default_overlay_lut",
            "default_overlay_interpolation",
            "overlay_segments",
            "default_zoom_scale",
            "show_image_info_plugin",
            "show_display_plugin",
            "show_invert_tool",
            "show_flip_tool",
            "show_window_level_tool",
            "show_reset_tool",
        )
        widgets = {
            "overlay_segments": JSONEditorWidget(
                schema=OVERLAY_SEGMENTS_SCHEMA
            ),
        }
        help_texts = {
            "overlay_segments": (
                "If an categorical overlay is shown, it is possible to show toggles "
                "to change the visibility of the different overlay categories. To do "
                "so, configure the categories that should be displayed. Data from the"
                " algorithm's output.json can be added as an extra label to each "
                "toggle using jinja templating. "
                'For example: [{ "voxel_value": 0, "name": "Level 0", "visible": '
                'false, "metric_template": "{{metrics.volumes[0]}} mm³"},]'
            ),
        }

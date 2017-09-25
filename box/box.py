"""A simple XBlock for displaying content in coloured boxes"""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, String
from xblock.fragment import Fragment


class BoxXBlock(XBlock):
    display_name = String(display_name="Display name", default='Box', scope=Scope.settings)
    boxcolour = String(display_name="Box Colour", values=('Grey', 'Red', 'Green', 'Blue', 'Yellow'),
        default="Grey", scope=Scope.settings,
        help="Pick a colour for your box.")
    boxcontent = String(display_name="Contents", multiline_editor='html', resettable_editor=False,
        default="", scope=Scope.content,
        help="Enter content to be displayed within your box")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the BoxXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/box.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/box.css"))
        frag.add_javascript(self.resource_string("static/js/src/box.js"))
        frag.initialize_js('BoxXBlock')
        return frag
    # Make fields editable in studio
    editable_fields = ('display_name', 'boxcolour', 'boxcontent', )
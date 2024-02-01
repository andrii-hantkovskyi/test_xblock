"""TO-DO: Write a description of what this XBlock is."""
import datetime
import logging
from random import randint

import pkg_resources
from web_fragments.fragment import Fragment
from webob import Response
from xblock.core import XBlock
from xblock.fields import String, Scope

log = logging.getLogger(__name__)


class TestXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    has_score = False
    icon_class = 'other'

    questions = String(
        default='', scope=Scope.settings, help='Questions')
    suggestions = String(
        default='', scope=Scope.settings, help='Suggestions')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the TestXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/testxblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/testxblock.css"))
        frag.add_javascript(self.resource_string(
            "static/js/src/testxblock.js"))
        frag.initialize_js('TestXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def add_topic(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        if data['topic_type'] not in ('question', 'suggestion'):
            log.error('Wrong type!')
            return None

        topic_type = data["topic_type"]
        title, content = data['title'], data['content']

        topics = getattr(self, f'{topic_type}s')
        topics += f"\n<div class='{topic_type}s__item'><h2>{title}</h2><p>{content}</p></div><hr>"
        setattr(self, f'{topic_type}s', topics)

        return Response(topics.replace("\n", ""), content_type="text/html; charset=utf-8")

    @XBlock.json_handler
    def pop_topic(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        if data['topic_type'] not in ('question', 'suggestion'):
            log.error('Wrong type!')
            return None

        topic_type = data["topic_type"]

        topics = getattr(self, f'{topic_type}s')
        topics = '\n'.join(topics.split('\n')[:-1])

        setattr(self, f'{topic_type}s', topics)

        return Response(topics.replace("\n", ""), content_type="text/html; charset=utf-8")

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("TestXBlock",
             """<testxblock/>
             """),
            ("Multiple TestXBlock",
             """<vertical_demo>
                <testxblock/>
                <testxblock/>
                <testxblock/>
                </vertical_demo>
             """),
        ]

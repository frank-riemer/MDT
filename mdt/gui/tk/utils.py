from Tkconstants import END
import os
import ttk
from mdt.gui.tk.widgets import CompositeWidget
from mdt.log_handlers import LogListenerInterface

__author__ = 'Robbert Harms'
__date__ = "2015-08-26"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


class SubWindow(object):

    def __init__(self, window_title):
        self._window_title = window_title

    @property
    def window_title(self):
        return self._window_title

    def render(self, toplevel):
        """Render the items in the given frame"""


class TabContainer(object):

    last_used_dwi_image = None
    last_used_mask = None
    last_used_roi_mask = None
    last_used_protocol = None
    last_used_model_output_folder = None
    last_optimized_model = None
    last_used_image_dimension = None
    last_used_image_slice_ind = None

    def __init__(self, window, tab_name):
        self.window = window
        self.tab_name = tab_name
        self._tab = ttk.Frame()
        self._tab.config(padding=(10, 13, 10, 13))
        self._tab.grid_columnconfigure(3, weight=1)

    def get_tab(self):
        """Get the tab frame for this tab object"""

    def tab_selected(self):
        """Called by the Notebook on the moment this tab becomes active."""

    def _init_path_chooser(self, file_chooser, path):
        """Init one of the file/directory choosers with the given path.

        If path is None or does not exist, it is not set. This uses the property file_chooser.initial_file
        to set the path.

        Args:
            file_chooser: the file chooser to set the path of
            path (str): the path to set as initial file
        """
        if path and os.path.exists(path):
            file_chooser.initial_file = path

    def _update_global_initial_dir(self, calling_widget, keys_to_listen_to):
        id_key = calling_widget.id_key

        if id_key in keys_to_listen_to:
            value = calling_widget.get_value()
            if os.path.isdir(value):
                CompositeWidget.initial_dir = value
            else:
                CompositeWidget.initial_dir = os.path.dirname(value)


class TextboxLogListener(LogListenerInterface):

    def __init__(self, text_box):
        self.text_box = text_box

    def emit(self, record, formatted_message):
        self.write(formatted_message)
        self.write("\n")

    def write(self, string):
        self.text_box.configure(state='normal')
        self.text_box.insert(END, string)
        self.text_box.configure(state='disabled')
        self.text_box.see(END)

    def flush(self):
        pass
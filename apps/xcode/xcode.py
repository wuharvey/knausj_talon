from talon import Context, actions, ui, Module, app, clip
from typing import List, Union

is_mac = app.platform == "mac"

ctx = Context()
mod = Module()
mod.apps.vscode = "app.name: XCode"
mod.apps.xcode = "app.name: XCode"

ctx.matches = r"""
app: xcode
"""


@ctx.action_class("win")
class win_actions:
    def filename():
        result = actions.win.title()
        # this doesn't seem to be necessary on xcode for Mac
        # if title == "":
        #    title = ui.active_window().doc

        if "." in result:
            return result

        return ""

    def file_ext():
        return actions.win.filename().split(".")[-1]


@ctx.action_class("edit")
class edit_actions:
    def find(text: str):
        if is_mac:
            actions.key("cmd-f")
        else:
            actions.key("ctrl-f")

        actions.insert(text)

    def line_swap_up():
        actions.key("alt-up")

    def line_swap_down():
        actions.key("alt-down")

    def line_clone():
        actions.key("shift-alt-down")

    # def jump_line(n: int):
    #     actions.user.xcode("workbench.action.gotoLine")
    #     actions.insert(str(n))
    #     actions.key("enter")



@ctx.action_class("user")
class user_actions:
    # find_and_replace.py support begin

    def find(text: str):
        """Triggers find in current editor"""
        if is_mac:
            actions.key("cmd-f")
        else:
            actions.key("ctrl-f")

        if text:
            actions.insert(text)

    def find_next():
        actions.key("enter")

    def find_previous():
        actions.key("shift-enter")

    def find_everywhere(text: str):
        """Triggers find across project"""
        if is_mac:
            actions.key("cmd-shift-f")
        else:
            actions.key("ctrl-shift-f")

        if text:
            actions.insert(text)

    def find_toggle_match_by_case():
        """Toggles find match by case sensitivity"""
        if is_mac:
            actions.key("alt-cmd-c")
        else:
            actions.key("alt-c")

    def find_toggle_match_by_word():
        """Toggles find match by whole words"""
        if is_mac:
            actions.key("cmd-alt-w")
        else:
            actions.key("alt-w")

    def find_toggle_match_by_regex():
        """Toggles find match by regex"""
        if is_mac:
            actions.key("cmd-alt-r")
        else:
            actions.key("alt-r")

    def replace(text: str):
        """Search and replaces in the active editor"""
        if is_mac:
            actions.key("alt-cmd-f")
        else:
            actions.key("ctrl-h")

        if text:
            actions.insert(text)

    def replace_everywhere(text: str):
        """Search and replaces in the entire project"""
        if is_mac:
            actions.key("cmd-shift-h")
        else:
            actions.key("ctrl-shift-h")

        if text:
            actions.insert(text)

    def replace_confirm():
        """Confirm replace at current position"""
        if is_mac:
            actions.key("shift-cmd-1")
        else:
            actions.key("ctrl-shift-1")

    def replace_confirm_all():
        """Confirm replace all"""
        if is_mac:
            actions.key("cmd-enter")
        else:
            actions.key("ctrl-alt-enter")

    def select_previous_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        actions.key("shift-enter esc")

    def select_next_occurrence(text: str):
        actions.edit.find(text)
        actions.sleep("100ms")
        actions.key("esc")

    # find_and_replace.py support end

# # Talon voice commands for Xcode
# # John S. Cooper  jcooper@korgrd.com

# from talon.voice import Key, Context
# from ..misc.mouse import control_shift_click

# ctx = Context("xcode", bundle="com.apple.dt.Xcode")

# ctx.keymap(
#     {
#         "build it": Key("cmd-b"),
#         "stop it": Key("cmd-."),
#         "run it": Key("cmd-r"),
#         "go back": Key("cmd-ctrl-left"),
#         "go (fore | forward)": Key("cmd-ctrl-right"),
#         "find in (proj | project)": Key("cmd-shift-f"),
#         "(sell find in (proj | project) | find selection in project)": Key(
#             "cmd-e cmd-shift-f enter"
#         ),
#         "(sell find ace in (proj | project) | replace selection in project)": Key(
#             "cmd-e cmd-shift-alt-f"
#         ),
#         "next in (proj | project)": Key("cmd-ctrl-g"),
#         "prev in (proj | project)": Key("shift-cmd-ctrl-g"),
#         "split window": Key("cmd-alt-enter"),
#         "show editor": Key("cmd-enter"),
#         "(show | hide) debug": Key("cmd-shift-y"),
#         "(show | find) call hierarchy": Key("cmd-ctrl-shift-h"),
#         "show (recent | recent files)": [Key("ctrl-1"), "recent files\n"],
#         "show related": Key("ctrl-1"),
#         "show history": Key("ctrl-2"),
#         "show files": Key("ctrl-5"),
#         "show (methods | items)": Key("ctrl-6"),
#         "show navigator": Key("cmd-0"),
#         "hide (navigator | project | warnings | breakpoints | reports | build)": Key(
#             "cmd-0"
#         ),
#         "show project": Key("cmd-1"),
#         "show warnings": Key("cmd-5"),
#         "show breakpoints": Key("cmd-8"),
#         "show (reports | build)": Key("cmd-9"),
#         "show diffs": Key("cmd-alt-shift-enter"),
#         "(next counterpart | show header | switcher)": Key("cmd-ctrl-down"),
#         "prev counterpart": Key("cmd-ctrl-up"),
#         "toggle comment": Key("cmd-/"),
#         "toggle breakpoint": Key("cmd-\\"),
#         "toggle all breakpoints": Key("cmd-y"),
#         "move line up": Key("cmd-alt-["),
#         "move line down": Key("cmd-alt-]"),
#         "go (deafen | definition)": Key("cmd-ctrl-j"),
#         "edit scheme": Key("cmd-shift-,"),
#         "quick open": Key("cmd-shift-o"),
#         "comm skoosh": "// ",
#         "(comm | comment) line": [
#             "//------------------------------------------------------------------------------",
#             Key("enter"),
#         ],
#         "step in": Key("f7"),
#         "step over": Key("f6"),
#         "step out": Key("f8"),
#         "step (continue | go)": Key("ctrl-cmd-y"),
#         "show blame for line": Key("cmd-alt-ctrl-b"),
#         "(reveal file | show file in finder)": Key("cmd-alt-ctrl-shift-f"),
#         "(snipline | delete line)": Key("cmd-alt-ctrl-shift-backspace"),
#         "add cursor down": Key("ctrl-shift-down"),
#         "add cursor up": Key("ctrl-shift-up"),
#         "add cursor": control_shift_click,
#         "dub add cursor": lambda m: control_shift_click(m, 0, 2),
#         "((select | sell) (partial | sub) [word] left)": Key("shift-ctrl-left"),
#         "((select | sell) (partial | sub) [word] right)": Key("shift-ctrl-right"),
#         # the following require custom key bindings in xcode preferences
#         "((partial | sub) [word] left | wonkrim)": Key("alt-ctrl-left"),
#         "((partial | sub) [word] right | wonkrish)": Key("alt-ctrl-right"),
#     }
# )
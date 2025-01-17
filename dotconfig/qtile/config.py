# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#import os
#import subprocess
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
#from libqtile import hook
from libqtile import qtile

#@hook.subscribe.startup
#def autostart():
#	home = os.path.expanduser('~.config/qtile/autostart.sh'),
#	subprocess.run([home])
#	lazy.spawn("picom -b")

mod = "mod4"
terminal = "alacritty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "b", lazy.spawn("brave-browser")),
    Key([mod], "f", lazy.spawn("flatpak run io.freetubeapp.FreeTube &")),
    #Key([mod, "shift"], "s", lazy.spawn("flameshot gui &")),
    #sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),
    Key([mod], "p", lazy.spawn("rofi -show drun")),
    #brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-")),
    #Mouse clicks
    Key([mod, "shift"], "o", lazy.spawn("xdotool click 1")),
    Key([mod, "shift"], "p", lazy.spawn("xdotool click 3")),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
		border_focus='81A1C1',
		single_border_width=None,
		margin=15,
		border_normal='4c566a'
    ),
    layout.Floating(
		border_focus='81a1c1',
		border_normal='4c566a'
    )
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

colours=['3b4252','d9dee9','3b3959','434c5e','81a1c1','5e81ac']

#### --- Top Bar Widgets --- ###

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(
			foreground=colours[1],
			background=colours[5]
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator2reverse.png',
			background=colours[4]
		),
                #
		widget.GroupBox(
			foreground=colours[1],
			background=colours[4],
			highlight_method='line',
			active="d8dee9",
			block_highlight_text_color='eceff4',
			inactive='88c0d0',
			highlight_color=['81a1c1','5e81ac'],
			this_current_screen_border='4c566a'
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separatorreverse.png',
			background=colours[0]
		),
                #
		widget.WindowName(
			foreground=colours[1],
			background=colours[0],
			max_chars=50),
                #
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator.png',
			background=colours[0]
		),
		#
		widget.Clock(
			format="%d-%m-%Y %a %H:%M",
			foreground=colours[1],
			background=colours[4],
			fontsize=15,
			font='mono'
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separatorreverse.png',
			background=colours[0]
		),
		#
		widget.Spacer(
			background=colours[0],
			foreground=colours[0]
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator2.png',
			background=colours[0]
		),
		#
		widget.Systray(
			foreground=colours[1],
			background=colours[5],
			icon_size=16),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator.png',
			background=colours[5]
		),
		#
		widget.Image(
			filename='~/.config/qtile/bar_icons/cpu.png',
			background=colours[4],
			mouse_callbacks={'Button1':lambda:qtile.cmd_spawn('alacritty -e cmatrix -B -C cyan')}
		),
		#
		widget.CPU(
			background=colours[4],
			foreground=colours[1],
			format='{load_percent}%',
			mouse_callbacks={'Button1':lambda:qtile.cmd_spawn('alacritty -e cmatrix -B -C cyan')}
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator2.png',
			background=colours[4]
		),
		#
		widget.Image(
			filename='~/.config/qtile/bar_icons/ram2.png',
			background=colours[5],
			padding=0,
			mouse_callbacks={'Button1':lambda:qtile.cmd_spawn('alacritty -e htop')}
		),
		#
		widget.Memory(
			background=colours[5],
			foreground=colours[1],
			measure_mem='M',
			mouse_callbacks={'Button1':lambda:qtile.cmd_spawn('alacritty -e htop')}
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator.png',
			background=colours[5]
		),
		#
		widget.Image(
			filename='~/.config/qtile/bar_icons/thermometer.png',
			background=colours[4]
		),
		#
		widget.ThermalSensor(
			background=colours[4],
			foreground=colours[1],
			tag_sensor="Core 0"
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator2.png',
			background=colours[4]
		),
		#
		widget.Image(
			filename='~/.config/qtile/bar_icons/speaker.png',
			background=colours[5],
			padding=0
		),
		#
		widget.Volume(
			background=colours[5],
			foreground=colours[1],
			fmt='{}'
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator.png',
			background=colours[5]
		),
		#
		widget.BatteryIcon(
			background=colours[4],
			theme_path='~/.config/qtile/bar_icons/battery_icons',
			update_interval=10
		),
		#
		widget.Battery(
			format='{percent:2.0%} {hour:d}:{min:02d}', #  {watt:.1f}W',
			foreground=colours[1],
			background=colours[4]
		),
		#
                widget.Image(
			filename='~/.config/qtile/bar_icons/separator2.png',
			background=colours[4],
			padding=0
		),
		#
		widget.Image(
			background=colours[5],
			foreground=colours[1],
			padding_x=0,
			filename='~/.config/qtile/bar_icons/power.png',
			mouse_callbacks={
				'Button1':lazy.shutdown(),
				'Button3':lambda:qtile.cmd_spawn('alacritty -e shutdown now')
			}
		)
            ],
            24,
            border_width=[3, 2, 5, 2],  # Draw borders
            border_color=[colours[3], colours[2], colours[2], colours[3]]
        ),
	wallpaper='~/.config/qtile/zeldalinks2.png',
	wallpaper_mode='fill'
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"


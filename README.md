# notepad  
Notepad program with related notes and categories  
Done with python & kivy

# TODO:  
[X] TopBar in place  
[X] SideBar in place 
[X] Note editor in place
[X] EditMenu in place
[X] NextNote button in place
[X] PreviousNote button in place
[X] Settings menu in place
[x] .ini file for categories
[x] Create save functionality
[x] Note saved according to category
[ ] Move to next note
[ ] Move to previous note
[ ] on_config_change
[ ] Read settings from .ini file (when changing categories)
[ ] Save into new file if the note is new
[ ] Create delete note functionality
[ ] EditMenu re-opens if you click text editor
[ ] Add borders to elements
[ ] Menus and dialogs
[ ] Add icons in place
[ ] Borders in icons
[ ] Opacity on icons when clicked
[ ] NotePanel bottom pixels are off
[ ] NotePanel top pixels are off (bug in kivy?)
[ ] Sixth tab label pixels are off

NOTES:
Creating a scrollbar incredibly hard
Toggling the editmenu not possible if the toggle button is inside said menu
Menu can't access the parent's methods, 
so remove_widget or toggle_edit can't be called inside EditMenu
Also the original togglebutton can't be brought to front, since kivy doesn't support
"always on top" for anything.
Since there isn't "always on top" creating a settings menu was really hard. I thought I could do it as a popup, but building a toggleable popup proved out to be impossible.
Luckily, Kivy had convenient widget for settings that matched common mobile views, so instead of creating my own, I went with the prebuilt one.
Setting category to edit and doing changes afterwards was complicated to implement with this widget, so I set the categories to their own tab.
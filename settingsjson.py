import json

settings_json = json.dumps([
    {
        "type": "title",
        "title": "Category settings"
    },
    {
        "type": "options",
        "title": "Category",
        "desc": "Select the category to edit",
        "section": "category",
        "key": "categoryID",
        "options": ["1", "2", "3", "4", "5", "6", "7", "8"]
    },
    {
        "type": "string",
        "title": "Category name",
        "desc": "Type to rename the category",
        "section": "category",
        "key": "categoryName",
    },
    {
        "type": "options",
        "title": "Category color",
        "desc": "Select the color of category",
        "section": "category",
        "key": "categoryColor",
        "options": ["white", "red", "blue", "teal", "green", "purple", "orange", "brown", "yellow", "white", "gray", "black"]
    },
    {
        "type": "title",
        "title": "Application settings"
    },
    {
        "type": "options",
        "title": "Window size",
        "desc": "Select the notepad application window size",
        "section": "application",
        "key": "window",
        "options": ["360x640"]
    },
    {
        "type": "path",
        "title": "File path",
        "desc": "Set the file path for notes",
        "section": "application",
        "key": "filePath",
    },
    {
        "type": "options",
        "title": "Language",
        "desc": "Select the notepad application language",
        "section": "application",
        "key": "language",
        "options": ["English"]
    },
])

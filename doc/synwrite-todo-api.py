GROUPING_ONE    = 1
GROUPING_2HORZ  = 2
GROUPING_2VERT  = 3
GROUPING_3HORZ  = 4
GROUPING_3VERT  = 5
GROUPING_3AS1P2 = 6
GROUPING_4HORZ  = 7
GROUPING_4VERT  = 8
GROUPING_4GRID  = 9
GROUPING_6GRID  = 10

MENU_SIMPLE = 0
MENU_DOUBLE = 1
MENU_STD    = 2

ATTRIB_CLEAR_ALL       = -1
ATTRIB_CLEAR_SELECTION = -2
ATTRIB_COLOR_FONT      = 0
ATTRIB_COLOR_BG        = 1
ATTRIB_SET_BOLD        = 2
ATTRIB_SET_ITALIC      = 3
ATTRIB_SET_UNDERLINE   = 4
ATTRIB_SET_STRIKEOUT   = 5

LOG_CLEAR         = 0
LOG_ADD           = 1
LOG_SET_PANEL     = 2
LOG_SET_REGEX     = 3
LOG_SET_LINE_ID   = 4
LOG_SET_COL_ID    = 5
LOG_SET_NAME_ID   = 6
LOG_SET_FILENAME  = 7
LOG_SET_ZEROBASE  = 8
LOG_CONSOLE_CLEAR = 20
LOG_CONSOLE_ADD   = 21
LOG_CONSOLE_GET   = 22

LOG_PANEL_OUTPUT   = "0"
LOG_PANEL_VALIDATE = "1"

LEXER_GET_LIST    = 0
LEXER_GET_ENABLED = 1
LEXER_GET_EXT     = 2
LEXER_GET_MOD     = 3
LEXER_GET_LINKS   = 4
LEXER_GET_STYLES  = 5
LEXER_SET_NAME    = 10
LEXER_SET_ENABLED = 11
LEXER_SET_EXT     = 12
LEXER_SET_LINKS   = 13
LEXER_SAVE_LIB    = 20
LEXER_DELETE      = 21
LEXER_IMPORT      = 22
LEXER_EXPORT      = 23
LEXER_CONFIG      = 24
LEXER_CONFIG_ALT  = 25
LEXER_ACTIVATE    = 26

FILENAME_SESSION         = -3
FILENAME_PROJECT         = -10
FILENAME_PROJECT_MAIN    = -11
FILENAME_PROJECT_WORKDIR = -12
FILENAME_PROJECT_SESSION = -13
FILENAME_PROJECT_FILES   = -14
FILENAME_LEXLIB          = -20
FILENAME_PATHS           = -21
FILENAME_FAVS            = -22

PROC_GET_CLIP         = 1
PROC_SET_CLIP         = 2
PROC_LOCK_STATUS      = 3
PROC_UNLOCK_STATUS    = 4
PROC_SOUND            = 5
PROC_COLOR_PICKER     = 6
PROC_ADD_RECENT_COLOR = 7
PROC_GET_COMMAND      = 8

PROP_NUMS           = 1
PROP_EOL            = 2
PROP_WRAP           = 3
PROP_RO             = 4
PROP_MARGIN         = 5
PROP_FOLDING        = 6
#free               = 7
PROP_TAB_SPACES     = 8
PROP_TAB_SIZE       = 9
PROP_COL_MARKERS    = 10
PROP_TEXT_EXTENT    = 11
PROP_ZOOM           = 12
PROP_INSERT         = 13
PROP_MODIFIED       = 14
PROP_VIS_LINES      = 15
PROP_VIS_COLS       = 16
PROP_LEFT           = 17
PROP_TOP            = 18
PROP_BOTTOM         = 19
PROP_RULER          = 20
PROP_TOKEN_TYPE     = 21
PROP_LEXER_FILE     = 22
PROP_LEXER_CARET    = 23
PROP_LEXER_POS      = 24
PROP_COLOR          = 25
PROP_NON_PRINTED         = 26
PROP_NON_PRINTED_SPACES  = 27
PROP_NON_PRINTED_ENDS    = 28
PROP_NON_PRINTED_ENDS_EX = 29
PROP_TAG                 = 30
PROP_LINE_STATE          = 31
PROP_KEEP_TRAIL_BLANKS   = 32
PROP_KEEP_CARET_IN_TEXT  = 33
PROP_AUTO_INDENT         = 34
PROP_LAST_LINE_SHOW      = 35
PROP_TAB_FILL            = 36
PROP_WRAP_AT_MARGIN      = 37

PROP_COORD_WINDOW  = 100
PROP_COORD_TREE    = 101
PROP_COORD_CLIP    = 102
PROP_COORD_OUT     = 103
PROP_COORD_PRE     = 104
PROP_DOCK_TREE     = 105
PROP_DOCK_CLIP     = 106
PROP_DOCK_OUT      = 107
PROP_DOCK_PRE      = 108
PROP_COORD_DESKTOP  = 120
PROP_COORD_MONITOR  = 121
PROP_COORD_MONITOR0 = 122
PROP_COORD_MONITOR1 = 123
PROP_COORD_MONITOR2 = 124
PROP_COORD_MONITOR3 = 125
PROP_SPLIT_MAIN_POS = 129
PROP_GROUP_MODE     = 130
PROP_GROUP_INDEX    = 131
PROP_FILENAME_SESSION = 132
PROP_FILENAME_PROJECT = 133
PROP_RECENT_FILES    = 135
PROP_RECENT_SESSIONS = 136
PROP_RECENT_PROJECTS = 137
PROP_RECENT_NEWDOC   = 138
PROP_RECENT_COLORS   = 139
PROP_EVENTS          = 140
PROP_EDITOR_BY_INDEX = 141
PROP_GROUPS          = 142

FIND_ACTION_FIND_NEXT    = 0
FIND_ACTION_FIND_ALL     = 1
FIND_ACTION_COUNT        = 3
FIND_ACTION_REPLACE_NEXT = 5
FIND_ACTION_REPLACE_ALL  = 6

FIND_OP_CASE     = 1 << 0
FIND_OP_WORDS    = 1 << 1
FIND_OP_BACK     = 1 << 2
FIND_OP_SELONLY  = 1 << 3
FIND_OP_ENTIRE   = 1 << 4
FIND_OP_REGEX    = 1 << 5
FIND_OP_REGEX_S  = 1 << 6
FIND_OP_PROMPT   = 1 << 8
FIND_OP_WRAP     = 1 << 9
FIND_OP_SKIPCOL  = 1 << 10
FIND_OP_BOOKMARK = 1 << 14
FIND_OP_EXTSEL   = 1 << 15

TOKENS_ALL        = 0
TOKENS_CMT        = 1
TOKENS_STR        = 2
TOKENS_CMT_STR    = 3
TOKENS_NO_CMT_STR = 4

def dlg_menu(id, caption, text):
    return sw_api.dlg_menu(id, caption, text)
def dlg_snippet(name, alias, lexers, text):
    return sw_api.dlg_snippet(name, alias, lexers, text)
def dlg_checklist(caption, columns, items, size_x, size_y):
    items = sw_api.dlg_checklist(caption, columns, items, size_x, size_y)
    return [(s=='1') for s in items]

def app_log(id, text):
    return sw_api.app_log(id, text)
def app_lock(id):
    return sw_api.app_lock(id)

def get_app_prop(id, value=''):
    return sw_api.get_app_prop(id, value)
def set_app_prop(id, value):
    return sw_api.set_app_prop(id, value)

def lexer_proc(id, text):
    return sw_api.lexer_proc(id, text)
def app_proc(id, text=''):
    return sw_api.app_proc(id, text)

def ini_read(filename, section, key, value):
    return sw_api.ini_read(filename, section, key, value)
def ini_write(filename, section, key, value):
    return sw_api.ini_write(filename, section, key, value)

def file_get_name(id):
    return sw_api.file_get_name(id)
def text_local(id, filename):
    return sw_api.text_local(id, filename)
def regex_parse(regex, data):
    return sw_api.regex_parse(regex, data)

#----------------------------------
# Editor class

class Editor:
##far todo
    def complete(self, text, len, show_menu=True):
        return sw_api.ed_complete(self.h, text, len, show_menu)
    def get_prop(self, id, value=''):
        return sw_api.ed_get_prop(self.h, id, value)
    def set_prop(self, id, value):
        return sw_api.ed_set_prop(self.h, id, value)
    def set_attr(self, id, color):
        return sw_api.ed_set_attr(self.h, id, color)
    def get_attr(self):
        return sw_api.ed_get_attr(self.h)
    def find(self, action, opt, tokens, sfind, sreplace):
        return sw_api.ed_find(self.h, action, opt, tokens, sfind, sreplace)

#noneed
    def get_alerts(self):
    def set_alerts(self, value):
    def get_word(self, x, y):
    def get_left(self):
    def set_left(self, num):
    def get_indexes(self):
import obspython as obs
import requests

url = ""
api = ""
user = ""
rank = ""
avatar = ""
country = ""
path = ""


# ------------------------------------------------------------

def update():
    global url
    global api
    global user
    global name
    global rank
    global avatar
    global country

    # get user data
    header = {'u': user, 'k': api}
    response = (requests.get("https://osu.ppy.sh/api/get_user", params=header)).json()
    user_id = response[0]['user_id']
    username = response[0]['username']
    pp_rank = '#' + response[0]['pp_rank']
    country_id = response[0]['country']

    # get user avatar
    try:
        img_data = requests.get('https://a.ppy.sh/' + user_id).content
        with open(path + 'img/avatars/' + user_id + '.jpg', 'wb') as handler:
            handler.write(img_data)

    except Exception as err:
        print(err)

    try:
        update_str_source(name_source, username)
        update_str_source(rank, pp_rank)
        update_img_source(country, path + 'img/flags/' + country_id + ".png")
        update_img_source(avatar, path + 'img/avatars/' + user_id + ".jpg")
    except Exception as err:
        print(err)


def update_str_source(source_name, text):
    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "text", text)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)


def update_img_source(source_name, img):
    source = obs.obs_get_source_by_name(source_name)
    if source is not None:
        settings = obs.obs_data_create()
        obs.obs_data_set_string(settings, "file", img)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)


def refresh_pressed(props, prop):
    update()


# ------------------------------------------------------------

def script_description():
    return "osu! player info grabber"


def script_load(settings):
    global path
    path = script_path()


def script_update(settings):
    global url
    global api
    global user
    global name_source
    global rank
    global avatar
    global country

    url = obs.obs_data_get_string(settings, "url")
    api = obs.obs_data_get_string(settings, "api")
    user = obs.obs_data_get_string(settings, "user")
    name_source = obs.obs_data_get_string(settings, "name")
    rank = obs.obs_data_get_string(settings, "rank")
    avatar = obs.obs_data_get_string(settings, "avatar")
    country = obs.obs_data_get_string(settings, "country")


def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_text(props, "api", "osu! API key", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_text(props, "user", "User", obs.OBS_TEXT_DEFAULT)

    name_list = obs.obs_properties_add_list(props, "name", "Name Source", obs.OBS_COMBO_TYPE_EDITABLE,
                                    obs.OBS_COMBO_FORMAT_STRING)
    rank_list = obs.obs_properties_add_list(props, "rank", "Rank Source", obs.OBS_COMBO_TYPE_EDITABLE,
                                           obs.OBS_COMBO_FORMAT_STRING)
    avatar_list = obs.obs_properties_add_list(props, "avatar", "Avatar Source", obs.OBS_COMBO_TYPE_EDITABLE,
                                    obs.OBS_COMBO_FORMAT_STRING)
    country_list = obs.obs_properties_add_list(props, "country", "Country Source", obs.OBS_COMBO_TYPE_EDITABLE,
                                              obs.OBS_COMBO_FORMAT_STRING)

    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_id(source)
            # print(source_id)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(name_list, name, name)
                obs.obs_property_list_add_string(rank_list, name, name)
            elif source_id == "image_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(avatar_list, name, name)
                obs.obs_property_list_add_string(country_list, name, name)

        obs.source_list_release(sources)

    obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)
    return props


#   Copyright 2012 Justin Michael Weeks
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
   
   
import urllib
import urllib2
import urlparse


add_to_page_dialog_url_format = "https://www.facebook.com/dialog/pagetab?app_id=APP_ID&display=popup&next=REDIRECT_URI"
feed_dialog_url_format = "https://www.facebook.com/dialog/feed?app_id=APP_ID&redirect_uri=REDIRECT_URI&display=DISPLAY_MODE&from=POSTING_USER&to=RECEIVING_USER&message=DEFAULT_TEXT&link=ATTACHED_LINK_URI&picture=PICTURE_URL&source=MEDIA_URL&name=NAME_OF_LINK&caption=CAPTION_OF_LINK&description=LINK_DESCRIPTION&properties=JSON_PROPERTIES&actions=JSON_ACTIONS&ref=TEXT_REFERENCE"
friends_dialog_url_format = "https://www.facebook.com/dialog/friends/?id=TARGET_FRIEND&app_id=APP_ID&redirect_uri=REDIRECT_URI&display=DISPLAY_MODE"
oauth_dialog_url_format = "https://www.facebook.com/dialog/oauth/?scope=REQUESTED_PERMISSIONS&client_id=APP_ID&redirect_uri=REDIRECT_URI&response_type=RESPONSE_TYPE&state=BAGGAGE_DATA&display=DISPLAY_MODE"
pay_dialog_url_format = "https://www.facebook.com/dialog/pay?app_id=APP_ID&redirect_uri=http://example.com/response&credits_purchase=false&order_info=ORDER_ID&dev_purchase_params=ADDITIONAL_PARAMETERS"
requests_dialog_url_format = ""
send_dialog_url_format = "https://www.facebook.com/dialog/send?app_id=123050457758183&name=People%20Argue%20Just%20to%20Win&link=http://www.nytimes.com/2011/06/15/arts/people-argue-just-to-win-scholars-assert.html&redirect_uri=http://www.example.com/response&display=DISPLAY_MODE&to=TARGET_USER&picture=URL_PICTURE&description=TEXT_DESCRIPTION"
authenticate_format = "https://graph.facebook.com/oauth/access_token?client_id=YOUR_APP_ID&redirect_uri=YOUR_URL&client_secret=YOUR_APP_SECRET&code=THE_CODE_FROM_ABOVE"

def add_to_page_dialog_url(app_id, redirect_uri, display="page"):
    format_url = urlparse.urlparse(add_to_page_dialog_url_format)
    new_url = format_url.scheme + ":" + "//" + format_url.netloc + format_url.path
    query = urlparse.parse_qs(format_url.query)
    
    query['app_id'] = app_id
    query['next'] = redirect_uri
    query['display'] = display
    
    return new_url + "?" + urllib.urlencode(query)
    
def feed_dialog_url(app_id, redirect_uri, display="page", from_user="", to_user="", message="", link="", picture="", source="", name="", caption="", description="", properties="", actions="", ref=""):
    format_url = urlparse.urlparse(feed_dialog_url_format)
    new_url = format_url.scheme + ":" + "//" + format_url.netloc + format_url.path
    query = urlparse.parse_qs(format_url.query)
    
    query['app_id'] = app_id
    query['redirect_uri'] = redirect_uri
    query['display'] = display
    query['from'] = from_user
    query['to'] = to_user
    query['message'] = message
    query['link'] = link
    query['picture'] = picture
    query['source'] = source
    query['name'] = name
    query['caption'] = caption
    query['description'] = description
    query['properties'] = properties
    query['actions'] = actions
    query['ref'] = ref
    
    return new_url + "?" + urllib.urlencode(query)
    
def friends_dialog_url(app_id, redirect_uri, target_friend, display="page"):
    format_url = urlparse.urlparse(friends_dialog_url_format)
    new_url = format_url.scheme + ":" + "//" + format_url.netloc + format_url.path
    query = urlparse.parse_qs(format_url.query)
    
    query['app_id'] = app_id
    query['redirect_uri'] = redirect_uri
    query['display'] = display
    query['id'] = target_friend
    
    return new_url + "?" + urllib.urlencode(query)
    
def oauth_dialog_url(client_id, redirect_uri, scope="", state="", response_type="", display="page"):
    format_url = urlparse.urlparse(oauth_dialog_url_format)
    new_url = format_url.scheme + ":" + "//" + format_url.netloc + format_url.path
    query = urlparse.parse_qs(format_url.query)
    
    query['client_id'] = client_id
    query['redirect_uri'] = redirect_uri
    query['scope'] = scope
    query['state'] = state
    query['response_type'] = response_type
    query['display'] = display
    
    return new_url + "?" + urllib.urlencode(query)
    
def pay_dialog_url(app_id, redirect_uri, credits_purchase, order_info="default-key", dev_purchase_params=""):
    format_url = urlparse.urlparse(pay_dialog_url_format)
    new_url = format_url.scheme + ":" + "//" + format_url.netloc + format_url.path
    query = urlparse.parse_qs(format_url.query)
    
    query['app_id'] = app_id
    query['redirect_uri'] = redirect_uri
    query['scope'] = scope
    query['state'] = state
    query['response_type'] = response_type
    query['display'] = display

    return new_url + "?" + urllib.urlencode(query)
    
def requests_dialog():
    pass

def send_dialog_url(app_id, redirect_uri, display="page", to="", link="www.google.com", picture="", name="", description=""):
    format_url = urlparse.urlparse(send_dialog_url_format)
    new_url = format_url.scheme + ":" + "//" + format_url.netloc + format_url.path
    query = urlparse.parse_qs(format_url.query)
    
    query['app_id'] = app_id
    query['redirect_uri'] = redirect_uri
    query['display'] = display
    query['to'] = to
    query['link'] = link
    query['picture'] = picture
    query['name'] = name
    query['description'] = description
    
    return new_url + "?" + urllib.urlencode(query)
    
def authenticate(client_id, redirect_uri, client_secret, code):
    format_url = urlparse.urlparse(authenticate_format)
    new_url = format_url.scheme + ":" + "//" + format_url.netloc + format_url.path
    query = urlparse.parse_qs(format_url.query)
    
    query['client_id'] = client_id
    query['redirect_uri'] = redirect_uri
    query['client_secret'] = client_secret
    query['code'] = code
    
    result = urllib2.urlopen(new_url, urllib.urlencode(query)).read()

    return urlparse.parse_qs(result).get('access_token')
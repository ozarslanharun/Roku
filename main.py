########################################################################
# Copyright 2019 Roku, Inc.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
########################################################################

from webDriver import WebDriver
import time

def run(hub_url: str, caps: dict):
    try:
        web_driver = WebDriver(hub_url, caps)

        # launch youtube
        # web_driver.launch_the_channel("837")

        web_driver.apps()
        # launch custom app
        time.sleep(5)
        web_driver.launch_the_channel("dev")

        # web_driver.verify_is_screen_loaded({"elementData": [{
        #     "using": "text",
        #     "value": "ROW 1"
        # }]})

        for i in range(5):
            t = time.time()
            web_driver.press_btn("select")
            t2 = time.time()
            print("select time :",t2-t)
            time.sleep(2)

        # web_driver.verify_is_screen_loaded({"elementData": [{
        #     "using": "text",
        #     "value": "Barack Gates, Bill Obama"
        # }]})

        # res = web_driver.verify_is_screen_loaded({"elementData": [{
        #     "using": "text",
        #     "value": "Authenticate to watch"
        # }]}, False, 2)
        # if res == False:
        #     res = web_driver.verify_is_screen_loaded({"elementData": [{
        #         "using": "text",
        #         "value": "Play"
        #     }]})
        #     web_driver.press_btn("select")
        # else:
        #     web_driver.press_btn("select")
        #     web_driver.verify_is_screen_loaded({"elementData": [{
        #         "using": "text",
        #         "value": "Please enter your username"
        #     }]})
        #     web_driver.send_word("user")
        #     web_driver.send_button_sequence(["down", "down", "down", "down", "select"])
        #     web_driver.verify_is_screen_loaded({"elementData": [{
        #         "using": "text",
        #         "value": "Please enter your password"
        #     }]})
        #     web_driver.send_word("pass")
        #     web_driver.send_button_sequence(["down", "down", "down", "down", "select"])
        web_driver.quiet()
        print("Test passed")
    except  Exception as e:
        print(f"Error: {e}")
        print("Test failed")
    
if __name__ == "__main__":
    # user creds stage
    # username = "mobileQA"
    # accessToken = "rg0Rh8hx9uYCHrZEXtQ9XYf2eCIKfMbIO2VLO1gyaxTA659zGJ"

    # QA prod
    username = "qadevops"
    accessToken = "mRY8s8vTCdx7mgHEluW4xPI4AR7IPMv2PkUpu3nH5kT32UyCvi"

    # hub_url = "stage-mobile-hub-virginia.lambdatestinternal.com/v1/session"
#     hub_url = "mobile-hub-internal.lambdatest.com/v1/session"
    hub_url = "mobile-hub-internal.lambdatest.com/wd/hub/session"

    url = "http://"+username+":"+accessToken+"@"+hub_url
    
    caps = {
        "deviceName": "Roku Express",
        "platformVersion": "11",
        "fixedIP":"28000100-0000-1000-8000-84eaed3d0c8c",
        "isRealMobile": True,
        "platformName": "roku",
        "build": "Roku Sanity",
        "name":"roku",
        # "app": "lt://APP10160202521666133222945745", # ip app
        "app": "roku", # channel app
        "video": True,
        "visual": True,
#         "privateCloud": True,
        "devicelog": True
        
    }
    t1 = time.time()
    run(url, caps)
    t2 = time.time()
    print("sec:",t2-t1)

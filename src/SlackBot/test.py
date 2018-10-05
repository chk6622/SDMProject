#!/usr/bin/env python
#coding: utf-8
'''
Created on Oct 4, 2018

@author: xingtong
'''

import time
from slackclient import SlackClient

BOT_NAME = 'happinessrobotteam11'

r'''Bot ID for 'chk6622' is UCAJF6DT3
    Bot ID for 'happinessrobotteam11' is UD6NR8D28
'''

# starterbot 的 ID 作为一个环境变量
BOT_ID = 'UD6NR8D28'

# 常量
AT_BOT = "<@" + BOT_ID + ">:"
EXAMPLE_COMMAND = "do"


SLACK_BOT_TOKEN='xoxb-417145055956-448773285076-BxLeF7ydbEmFbFzQ1u5yCguS'

slack_client = SlackClient(SLACK_BOT_TOKEN)



def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + "* command with numbers, delimited by spaces."
               
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
        
    slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
#         print output_list
        for output in output_list:
#             if output and 'text' in output and AT_BOT in output['text']:
            if output and 'text' in output and len(output['text'])>0:
                # 返回 @ 之后的文本，删除空格
#                 return output['text'].split(AT_BOT)[1].strip().lower(), \
#                        output['channel']
                return output['text'], output['channel']
    return None, None

if __name__ == "__main__":
#     channel='UCAJF6DT3'
#     response='haha'
#     if slack_client.rtm_connect():
#         slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
#         slack_client.api_call("reactions.add", channel=channel,  NAME = 'thumbsup', as_user=True)

    READ_WEBSOCKET_DELAY = 1 # 1 从 firehose 读取延迟 1 秒
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command:
                print command, channel
#             if command and channel:
#                 handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")

#     api_call = slack_client.api_call("users.list")
#     if api_call.get('ok'):
#         # retrieve all users so we can find our bot
#         users = api_call.get('members')
#         for user in users:
#             print user['name'],user.get('id')
#             if 'name' in user and user.get('name') == BOT_NAME:
#                 print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
#     else:
#         print("could not find bot user with the name " + BOT_NAME)
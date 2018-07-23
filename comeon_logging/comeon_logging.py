# -*- coding: utf-8 -*-

"""Main module."""

from slackclient import SlackClient
import os


def send_slack_message (channel, text):
    """
    send a message by slack

    """
    slack_key = os.environ['SLACK_KEY']
    try :
        slack_client = SlackClient(slack_key)
        slack_client.api_call("chat.postMessage", channel=channel, text=text, as_user='haenec')
        return True
    except :
        return False

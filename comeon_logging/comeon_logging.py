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


def send_player_missing (text) :
    """
    send a message to slack to inform about unmatch player

    """
    slack_key = os.environ['SLACK_KEY']
    env = os.environ['ENVIRONMENT']
    if env == 'PROD':
        channel = 'missing_player'
    else :
        channel = env.lower() + '_missing_player'
    
    messages = env + ' : ' + text

    
    try :
        slack_client = SlackClient(slack_key)
        slack_client.api_call("chat.postMessage", channel=channel, text=messages, as_user='haenec')
        return True
    except :
        return False    